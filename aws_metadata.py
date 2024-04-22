import base64
import binascii
import json
import math
import struct
from datetime import datetime


# key used for encrypt/decrypt metadata1
METADATA_KEY: bytes = b"a\x03\x8fp4\x18\x97\x99:\xeb\xe7\x8b\x85\x97$4"


def raw_xxtea(v: list[int], n: int, k: list[int] | tuple[int, ...]) -> int:
    if not isinstance(v, list):
        raise ValueError("arg `v` is not of type list")
    if not isinstance(k, list | tuple):
        raise ValueError("arg `key` is not of type list or tuple")
    if not isinstance(n, int):
        raise ValueError("arg `n` is not of type int")

    def mx() -> int:
        return ((z >> 5) ^ (y << 2)) + ((y >> 3) ^ (z << 4)) ^ (sum_ ^ y) + (
            k[(p & 3) ^ e] ^ z
        )

    def u32(x: int) -> int:
        return x % 2**32

    y = v[0]
    sum_ = 0
    delta = 2654435769
    if n > 1:  # Encoding
        z = v[n - 1]
        q = math.floor(6 + (52 / n // 1))
        while q > 0:
            q -= 1
            sum_ = u32(sum_ + delta)
            e = u32(sum_ >> 2) & 3
            p = 0
            while p < n - 1:
                y = v[p + 1]
                z = v[p] = u32(v[p] + mx())
                p += 1
            y = v[0]
            z = v[n - 1] = u32(v[n - 1] + mx())
        return 0

    if n < -1:  # Decoding
        n = -n
        q = math.floor(6 + (52 / n // 1))
        sum_ = u32(q * delta)
        while sum_ != 0:
            e = u32(sum_ >> 2) & 3
            p = n - 1
            while p > 0:
                z = v[p - 1]
                y = v[p] = u32(v[p] - mx())
                p -= 1
            z = v[n - 1]
            y = v[0] = u32(v[0] - mx())
            sum_ = u32(sum_ - delta)
        return 0
    return 1


def _bytes_to_longs(data: str | bytes) -> list[int]:
    data_bytes = data.encode() if isinstance(data, str) else data

    return [
        int.from_bytes(data_bytes[i : i + 4], "little")
        for i in range(0, len(data_bytes), 4)
    ]


def _longs_to_bytes(data: list[int]) -> bytes:
    return b"".join([i.to_bytes(4, "little") for i in data])


def _generate_hex_checksum(data: str) -> str:
    crc_checksum = binascii.crc32(data.encode()) % 2**32
    hex_checksum = format(crc_checksum, "X")

    if len(hex_checksum) < 8:
        pad = (8 - len(hex_checksum)) * "0"
        hex_checksum = pad + hex_checksum

    return hex_checksum


class XXTEAException(Exception):
    pass


class XXTEA:
    """XXTEA wrapper class.

    Easy to use and compatible (by duck typing) with the Blowfish class.

    Note:
        Partial copied from https://github.com/andersekbom/prycut and ported
        from PY2 to PY3
    """

    def __init__(self, key: str | bytes) -> None:
        """Initializes the inner class data with the given key.

        Note:
            The key must be 128-bit (16 characters) in length.
        """
        key = key.encode() if isinstance(key, str) else key
        if len(key) != 16:
            raise XXTEAException("Invalid key")
        unpacked_key = struct.unpack("IIII", key)
        if len(unpacked_key) != 4:
            raise XXTEAException("Invalid key")
        self.key = unpacked_key

    def encrypt(self, data: str | bytes) -> bytes:
        """Encrypts and returns a block of data."""
        ldata = math.ceil(len(data) / 4)
        idata = _bytes_to_longs(data)
        if raw_xxtea(idata, ldata, self.key) != 0:
            raise XXTEAException("Cannot encrypt")
        return _longs_to_bytes(idata)

    def decrypt(self, data: str | bytes) -> bytes:
        """Decrypts and returns a block of data."""
        ldata = math.ceil(len(data) / 4)
        idata = _bytes_to_longs(data)
        if raw_xxtea(idata, -ldata, self.key) != 0:
            raise XXTEAException("Cannot decrypt")
        return _longs_to_bytes(idata).rstrip(b"\0")


metadata_crypter = XXTEA(METADATA_KEY)


def encrypt_metadata(metadata: str) -> str:
    """Encrypts metadata to be used to log in to Amazon."""
    checksum = _generate_hex_checksum(metadata)
    object_str = f"{checksum}#{metadata}"
    object_encrypted = metadata_crypter.encrypt(object_str)
    object_base64 = base64.b64encode(object_encrypted)
    object_base64_decoded = object_base64.decode("utf-8")
    encrypted_metadata = f"ECdITeCs:{object_base64_decoded}"

    return encrypted_metadata


def decrypt_metadata(encrypted_metadata: str) -> str:
    """Decrypts metadata for testing purposes only."""
    metadata_prefix_position = encrypted_metadata.find("ECdITeCs:")

    if metadata_prefix_position != 0:
        raise Exception("malformed encrypted metadata")

    object_base64_decoded = encrypted_metadata[9:]
    object_base64 = object_base64_decoded.encode("utf-8")
    object_encrypted = base64.b64decode(object_base64)
    object_str = metadata_crypter.decrypt(object_encrypted).decode("utf-8")
    checksum, metadata = object_str.split("#", 1)

    if _generate_hex_checksum(metadata) != checksum:
        raise XXTEAException("Checksum mismatch during decryption.")

    return metadata


def now_to_unix_ms() -> int:
    return math.floor(datetime.now().timestamp() * 1000)


def meta_audible_app(user_agent: str, oauth_url: str) -> str:
    """Returns json-formatted metadata to simulate sign-in from iOS audible app."""
    meta_dict = {
        "start": now_to_unix_ms(),
        "interaction": {
            "keys": 0,
            "keyPressTimeIntervals": [],
            "copies": 0,
            "cuts": 0,
            "pastes": 0,
            "clicks": 0,
            "touches": 0,
            "mouseClickPositions": [],
            "keyCycles": [],
            "mouseCycles": [],
            "touchCycles": [],
        },
        "version": "3.0.0",
        "lsUbid": "X39-6721012-8795219:1549849158",
        "timeZone": -6,
        "scripts": {
            "dynamicUrls": [
                (
                    "https://images-na.ssl-images-amazon.com/images/I/"
                    "61HHaoAEflL._RC|11-BZEJ8lnL.js,01qkmZhGmAL.js,71qOHv6nKaL."
                    "js_.js?AUIClients/AudibleiOSMobileWhiteAuthSkin#mobile"
                ),
                (
                    "https://images-na.ssl-images-amazon.com/images/I/"
                    "21T7I7qVEeL._RC|21T1XtqIBZL.js,21WEJWRAQlL.js,31DwnWh8lFL."
                    "js,21VKEfzET-L.js,01fHQhWQYWL.js,51TfwrUQAQL.js_.js?"
                    "AUIClients/AuthenticationPortalAssets#mobile"
                ),
                (
                    "https://images-na.ssl-images-amazon.com/images/I/"
                    "0173Lf6yxEL.js?AUIClients/AuthenticationPortalInlineAssets"
                ),
                (
                    "https://images-na.ssl-images-amazon.com/images/I/"
                    "211S6hvLW6L.js?AUIClients/CVFAssets"
                ),
                (
                    "https://images-na.ssl-images-amazon.com/images/G/"
                    "01/x-locale/common/login/fwcim._CB454428048_.js"
                ),
            ],
            "inlineHashes": [
                -1746719145,
                1334687281,
                -314038750,
                1184642547,
                -137736901,
                318224283,
                585973559,
                1103694443,
                11288800,
                -1611905557,
                1800521327,
                -1171760960,
                -898892073,
            ],
            "elapsed": 52,
            "dynamicUrlCount": 5,
            "inlineHashesCount": 13,
        },
        "plugins": "unknown||320-568-548-32-*-*-*",
        "dupedPlugins": "unknown||320-568-548-32-*-*-*",
        "screenInfo": "320-568-548-32-*-*-*",
        "capabilities": {
            "js": {
                "audio": True,
                "geolocation": True,
                "localStorage": "supported",
                "touch": True,
                "video": True,
                "webWorker": True,
            },
            "css": {
                "textShadow": True,
                "textStroke": True,
                "boxShadow": True,
                "borderRadius": True,
                "borderImage": True,
                "opacity": True,
                "transform": True,
                "transition": True,
            },
            "elapsed": 1,
        },
        "referrer": "",
        "userAgent": user_agent,
        "location": oauth_url,
        "webDriver": None,
        "history": {"length": 1},
        "gpu": {"vendor": "Apple Inc.", "model": "Apple A9 GPU", "extensions": []},
        "math": {
            "tan": "-1.4214488238747243",
            "sin": "0.8178819121159085",
            "cos": "-0.5753861119575491",
        },
        "performance": {
            "timing": {
                "navigationStart": now_to_unix_ms(),
                "unloadEventStart": 0,
                "unloadEventEnd": 0,
                "redirectStart": 0,
                "redirectEnd": 0,
                "fetchStart": now_to_unix_ms(),
                "domainLookupStart": now_to_unix_ms(),
                "domainLookupEnd": now_to_unix_ms(),
                "connectStart": now_to_unix_ms(),
                "connectEnd": now_to_unix_ms(),
                "secureConnectionStart": now_to_unix_ms(),
                "requestStart": now_to_unix_ms(),
                "responseStart": now_to_unix_ms(),
                "responseEnd": now_to_unix_ms(),
                "domLoading": now_to_unix_ms(),
                "domInteractive": now_to_unix_ms(),
                "domContentLoadedEventStart": now_to_unix_ms(),
                "domContentLoadedEventEnd": now_to_unix_ms(),
                "domComplete": now_to_unix_ms(),
                "loadEventStart": now_to_unix_ms(),
                "loadEventEnd": now_to_unix_ms(),
            }
        },
        "end": now_to_unix_ms(),
        "timeToSubmit": 108873,
        "form": {
            "email": {
                "keys": 0,
                "keyPressTimeIntervals": [],
                "copies": 0,
                "cuts": 0,
                "pastes": 0,
                "clicks": 0,
                "touches": 0,
                "mouseClickPositions": [],
                "keyCycles": [],
                "mouseCycles": [],
                "touchCycles": [],
                "width": 290,
                "height": 43,
                "checksum": "C860E86B",
                "time": 12773,
                "autocomplete": False,
                "prefilled": False,
            },
            "password": {
                "keys": 0,
                "keyPressTimeIntervals": [],
                "copies": 0,
                "cuts": 0,
                "pastes": 0,
                "clicks": 0,
                "touches": 0,
                "mouseClickPositions": [],
                "keyCycles": [],
                "mouseCycles": [],
                "touchCycles": [],
                "width": 290,
                "height": 43,
                "time": 10353,
                "autocomplete": False,
                "prefilled": False,
            },
        },
        "canvas": {"hash": -373378155, "emailHash": -1447130560, "histogramBins": []},
        "token": None,
        "errors": [],
        "metrics": [
            {"n": "fwcim-mercury-collector", "t": 0},
            {"n": "fwcim-instant-collector", "t": 0},
            {"n": "fwcim-element-telemetry-collector", "t": 2},
            {"n": "fwcim-script-version-collector", "t": 0},
            {"n": "fwcim-local-storage-identifier-collector", "t": 0},
            {"n": "fwcim-timezone-collector", "t": 0},
            {"n": "fwcim-script-collector", "t": 1},
            {"n": "fwcim-plugin-collector", "t": 0},
            {"n": "fwcim-capability-collector", "t": 1},
            {"n": "fwcim-browser-collector", "t": 0},
            {"n": "fwcim-history-collector", "t": 0},
            {"n": "fwcim-gpu-collector", "t": 1},
            {"n": "fwcim-battery-collector", "t": 0},
            {"n": "fwcim-dnt-collector", "t": 0},
            {"n": "fwcim-math-fingerprint-collector", "t": 0},
            {"n": "fwcim-performance-collector", "t": 0},
            {"n": "fwcim-timer-collector", "t": 0},
            {"n": "fwcim-time-to-submit-collector", "t": 0},
            {"n": "fwcim-form-input-telemetry-collector", "t": 4},
            {"n": "fwcim-canvas-collector", "t": 2},
            {"n": "fwcim-captcha-telemetry-collector", "t": 0},
            {"n": "fwcim-proof-of-work-collector", "t": 1},
            {"n": "fwcim-ubf-collector", "t": 0},
            {"n": "fwcim-timer-collector", "t": 0},
        ],
    }
    return json.dumps(meta_dict, separators=(",", ":"))


print(decrypt_metadata("ECdITeCs%3AOSwJm5JT5S5EJ5FgYESBRtihMeVzsSx6vWQFy8MslNLo2oBw%2Fi3Ms33o7IbN6hXGT8TAI5JTMsAi1HhqdrZFOTbvIjfx4JisriHAp3uaR8OvGlZopKmArLN7SCUd3eBNOZ2UC%2F%2FtkgDji3%2BG%2FCHdne6D7Ewv2HhY9THJcrLM%2FnfrU%2F8g4Kjf%2FPLbLGKlmOZC0yipfxaJPbEWI%2FfFXNlnyTJLMpbVA731RUaC5tI6F4GqfgvcyT2S0zI6%2B2tRPInUL0v9I4P7KEf6o0NtfWUoMoDHnNUQh%2BUKXWBHvwl768efYHNBNAlvfEp8DNQaJE64AZCYggk15Egyb5K2fTg4HiYiu7Kk2HH6f%2Fw70Q8%2FJuaGT3WSdukl6HKf2gtOo3R10mONxO8RJD6b8ai4iwf40K7Svs5DJUzHaGoI%2FazQNOkdZQSdxIAHcjvPlFlibcP%2BKNOf%2F0n%2FS9fqkDKt5MRCJXMDHnAN2aINEhpxhpm5YXMz4051R4N3a3FPwOLWnFR2nmjIu3PJ98DBPO%2BWMfy0kFOEcnrvVWh2SRdrnZ9n3Iec7UBczMCxV8th0vkeHHWG5VJsbDjGFTetHYSmp%2F%2F4u7QUzupvnF4DbD0HkPqhmoRVqdVI%2FL01O%2BT78792FftLdNLViFYLziCbWTqmofryIDJkPgcgEME3dC6n03G6iCYFYjsmGDEHsn66CEWvkIZfEDBcgG38Xl6zDEbActZxAllcNq4AeVmLYupck47QzsqDXm7Yf7QW4Gj5dLo%2FijBKgCgeT4EiWKkw10VxfAh4NOMVfg0GfZgA6QQAvHWj0eGF7I9iyQlHZ1if%2BbwxFAnXpvNfbfC7up0DTS7NuJ5w5q%2F9UDszNYZvGDthL9cT9SftV2uXZqQE9E34suRQCFU20P3qJIm6JikYS0m3D9ZGqrRKjwn0f9hkzJKZS0xUymuzNuCGIGZtVGUDFodqTZqb3ptuuFB8HDHJ4rlkaR%2BjzVyaddURDPJzCihvFnTKLLOJLz%2FD%2FnkEWazleupHOgFnN6SZ8keOh2k1M%2BeWlydmzVchDry9KP64JOtIWy45v0wVevRkZ%2BUvJ2%2BaUaHViYNHjWAeMfKki1FPL%2FfFiPjFjpTbGKsqomuLX5DED%2Br%2B%2B4LBOuER0QGpwAdG6icRvc%2FFMbSkfsatV3dEaAqEOvDvbPdiI2Cz50HMKJmPOZQHbbqTKwIqEJR4amFMkiV%2BHmn2Nxf7U5ScxKcfxC1jo%2BUaOk1gv6%2F61S99FQmJoWNZEQQ1AcLjyX6ovzJvp245w3UvkWKVtwZNNl4AO8QRIf10MwJxXFQpBWkTVaTGADefNhIjYVs3Ti%2B3lreJUNI50dcJzv4R%2Byqk2btTvrFK5bgdML4w2VYUV6pGdn9Yv7GiDrRSvLOBRH%2FU7AE%2FlpDi1SlvcqvYjmS5dca%2BNusa%2FogaE8FqUX7ouWgLOEx4bglk3LkB7ogsg9cYPMy4p1tx8hdzHh854njbfAsU02%2FV7uqTv%2By6VAtHqhVMre9phtB52byfzzXQj3HYcHKpWIWikAh8xryKEb2hbadQoW%2BJf4kw28es2JzPR7XL966LLOi2dCISflZM3KsotPrPyOoktTTtVUtlYlYCUdPAzVje8aMUUL%2BlREzt14BmHVXFYzx317b38%2FH6lgK36qwbh3bNUSnZeE%2FgSrPMGuN93WAdiB2STAXIcMwPMtxtfJdlvnejgVH4a2wG0aT2YIoKqtFqlAvnq10Kla1XAH%2F7J7qj0QUm7t4mcEhJHKwZc6FI2e2OGsqf4Gu5aY3a5Wl6WMG6BvwGCFjlTPb6PBBJjPFl69bOhZqVEyDYkoXFcuvXKYesRXlLRDuhE1JVLwtAuvu6LHpYmWc2vWESSY6gyYFVEfVlnEIsNtUsz3BZb5unWpRo3ATJK%2FYKJYc6K1YoDndqecX7TBencXkvOVdWCBMhprueWheqYzDQO0DzkthvF254F%2FGRhlnmphBFreAQmgN%2BQJy8%2FJxoLg4ZjmTYp8eEH5K%2FwVVBls%2BTEnvVmnvOGvtaVZ5%2BzsJprEa%2Bq89FVAHzIj2XNk2kqotI4N2KV2vDUCbFBOoVabUJjgNcAq6zA1W0Xeduq5mMnh750xd%2B5WUdBDlbiBzDJW0PgF5Xi0wQ4wheTA7XVtNfNLdGPB9xgjJk6z4IYGeBIF1u1LE4ya27U9hggKNxKNn19IjT9IpkJKJm2qa9ug%2FpezjDfTorNfhE80N1kB6aryzURGWn7dxhrJPJhcKOWsIxcWfWhTAagUIYy6wHcDQcwJTe2cuL14K7qQCxJ%2BZHfUhAwdDUCwC2ApPMippkkTpzAcZqdPedXEjlpZ%2F4qbAwYta3i%2Fu%2B%2FxMANcLBym0L77wKXvD9EtOZHmHzcuGn2qoXvT9X83qJoBYwPccVVkoC6Yk3ZfvlD%2BSL16NRk%2BFG1ag6WWLR%2F7pdjT0oqUdbSsVc5goYuwb6ikG1IOYsfvAZb%2B8jYVD9QovqmdFIPm0%2FftMOEMZdzln9NVmDls49VcS5lAN%2FdegKfmx7L25COpjseFprZbucdm5tNvRK8CK3QAOIrquMbXVwEZQAnb6%2BR20FWiddWHTMGhmT8S844rAnz2urRA%2FCbD8fwSgmnt%2FRvkbnfxpkFNRGH3VvsnOWenRsUKwC5RLzM9jSKIR03T5nEACQqhX0nUtL3u3ipgM3yYBRscs5hMiBYu2DmZTF447i28YLRXxOFE9O2q%2BlkFKfz5g722MqHXOt%2F8UZlVnacEq8i95%2Be%2Fjcof2jKdCSlQ9i0CpKSn939k3CMaNZaYClT1337ukkZ8aHGQ6p2Vd5yJFNbwArpvPjfiEEyB8yK04%2Bea3yqAHVSGqyzk5EOevp6iaT2CoaZIvxL3f%2FFijt8RBB7qo2iNFdoChEuMR7tMNcg%2BY58x%2Bb98aYWOeDSjejqKaoko%2B87hWziujQWwmp2luahLRGzdhxLx49SaUDAn886NKV9qqgxbYuI1FrqNPqfPIqLIgVfn7FISb%2F46oUqWKPlx1Dy3d0M5xOuvsQcSio8pC%2FW%2BLteoDq6qGvdJng9atzTmrNI14HFUdTM3aNSgYUw7zFQIE7zpgVhqyv6nnHnRJ%2FY4nmRsvoevFYcaMcL8XSsIjAHXHu%2BRvpPiui5qoFLXlmqXHLdw%2BBIKE3a5%2BfAMaKWwm2Qyhs4%2FN0AckYPLCwJoZ6pp6inPLwNDx%2FmzayUlwlcYsadr5MBph01YNZROQX1%2FnvVo%2FRgqT6%2BwC9YlwRzOG58ipG5iAppkjeM8tQPyaURDaS4jYii5CnFXU%2Bb4KnZUlqJa8XmlOl6CqC6zk6IzSqjb8Zmon%2BJVRVeQV1iZ9qlfIoC%2F5oQJzz%2B68E9%2F1mT9WXaKxKmKPXimrQFt5fBdkY3RMHXBwp2t9XcEP%2Fr7G42sF6Nz%2F29f86dvKXjv4Y8EBWOix%2BUGhesuV1imdzk%2FyIUwcoHa7Kn2jOuv1K9BiFKO6SzFii3hzuiVV7fjJ1fMwRnL4UWYRj3PHz3r4Jv4rhyxYEg5kj9IThVxXp4w%2F%2BG%2FkiDa9KG%2B%2FAWMzWGbEEt9nC1eqkd4WbUNxOt6MOlRMKu1IFq%2FTtLu%2F746aQxj6gRJIQHHW5RDLhyhugBxbtTd1CLXCb5BznkDFYcDZlTyXFwSohqLeBOUNu6qMNGrVrJNQdAbw3kE9YMVtabbRWEAEQ9p7k%2Ftg8zXrzvPdryiSDOVeic9QqaI75%2B03nbkhkPjyfPSZKF1LbOd6CPNB3LbZrYeQjG8%2B2Z7LrJym2RDAe%2Fe4tYJHXmjFirMX6o6PD7nSFRL3ErA50ZrpHvdtBf8uCYeL3v0mBSa8GtkGnvgE%2FQP3Z6xIXMXWf%2F1PPdFkkAhoo%2BfuuSZhrDVhTnUHnBZzZKbV2qIWO5OD0P%2Fld9eOLOs3VEhvLkYiv4gWB4bz0sEBNznU%2Bg5wiHCS1NPXfNtwrPQ42BFA9SFfBYzuFsmtIFPeQWN%2F95cB9gG1iaW70SrMkr156VZdxOugf3uHNcJLfORdLZM0hmqZWQYbnQoYJ3aoiZuYED7RGGuqDhY0tZApZGja%2B8SRudMxPyBXgQyGtCW%2B%2F3gg6zQmoCBBL1a5eAv2gwu9JDw%2FUd70aFMGDtwfV4IDktmRS0SJdudr2zP%2FCMDbi7D7hHLYKGMSUVYawDY%2F%2Fy0cI23NrOlk9afQvyGtRcMRWihOAL2nBoaNetpEXOgGIMuJALdrjmGzmPKsyqY%2Fx1W3Ri0x29lzXn9Umu6sVLngVJezPAvev9m8%2F0teD3Q7om9X%2FiIMKn%2FndjPIPI1aEuCfTh%2B7sFGFVPUPkP3Z7PiRQPp56qI%2B4k%2B3v0J%2FGnpr%2FY%2ByuTHskEjx3TMBSUfQD2igN1cSgakTeM0krEm1YNyerSk%2BYxgvZfUUmUTzl35sKkQ2%2BbrrhVNXucIPdt5RFm%2BRq7jCfFPOEg8VAr8TM6p6Jij1g8fc9J5K7kGKbQeniCjliWYwZx69HMUrBYuBJlyxFgtWlGTYiyohlFYNWap%2F8UMeTUsNypsppwjghFZCraFlwWMM5ahrt841f%2BlSPgJWTE5xaRXhRBKJ5HZjcM669QJlJ2mhcRFHUvAwDShRmqZY98rGNtPQy%2FlR3QTHhXSYJqQDi9AIvVKkG22zAu9J3mupX7S0d454NzYX7w%2BEc5EwiI8fRocnGeGFlTdEu4KwWSVescGYEDamq077kVyQzbAv9UWT6IdbE5LINdFujsuHBBOI%2BzJOub4DQPySETPx5oZxP1uj1furbKrCer63dbYCbHMRrWQulmkqkISjfx0LZlmw84C2vE8H4M08ybQpYTFQtL7ygGnVr%2FPncf6L64PSWg9VL%2FcYq4nOQtSWt7oKEO5%2BCvsf4rtckN2JklrXtDn65oTdQ86fwA9X1x2MmWSeHm3Dm%2FvohNIhi%2BWIF1rHp01fyGN2y8A5v%2BGX92BDd08v52g7e9yvjbzYh9DyEkUnAKDfQn%2BYgNkub%2BZ8S3Yy%2BBiMyppWGs6ayPA0WMX1Xt9e7StUIeMNv52YpMfm5ljPDCvNdrn7ZPjeZQYzCDSIxudT%2BJQIiyxo4aOqZuAo7Wd%2Bd5Id4%2FuSJOg%2FPkHDqcj9GwuDIZ1tIDrqtTGKI60mS4dCrUA8CgYywUxUvhjXMrYDofv3PgyY%2BBqdPWtQDPadSgKnAci4iwXkjwPuGu9Mt5orRWhtVj6cD4V%2FNe%2FZ6GRuDWIb%2B6FbA1T3xTyt8beLG%2FPgYSQkhILbd1RwwzUc2%2FFJOvpofDYqGoVsRm908coDwXL%2FgGTTSXdqtN160b26ZSjfmBnjehT1rBrceOjNQbsT7pUZ4xNWUWL3Ng0VvLl3%2B3%2B2REaKThCoU6Y1mh0yfNwS8ruMyzXYa4vrthWMvBZ7MbKBC1eBuPX2HcnFVIICsDehRUgVHrRz%2Fa2aZFKblp3hPa97ZnNMmmXHPrMtyAQ2CFVubO4rksUQrMKM4nS9yCTPcOCIpJP3K6OWmYK9I87LeX6%2F6MVvICRGI4b3%2BZUubd7ZuKZR9zEOJm%2B30r%2FUY%2F%2Fe7Y%2Bu%2BEPJGU%2BYxhAbY3iDz8XlICfcHFwB0ZIQ6OZcAEfnjoxubkqHa5jEN%2BwgKDpLLnuW8PRO2bBuPZLllPgKGE9nJLWXueZ6mqec%2FwuyzNnaCAMg5m9YMayULXSSSVAROu1MaVGyYwARO1%2BzM11tRcG04QytpUr4wUebxDquQ3xtbIcItfDdUP03bru75Bnew4uL1Qch1vwjMa34BxvcRzI96mTP4Kj4JnAKIemX608anRjwpsKgPfidNXKR5%2F7P9bX4U7ffO5YUzWUM72EmbqUNqFFbZ5%2BGptBghWk1zHDLnYQXqtoVdvXB8z3537ynq%2BToPXniaPOjPQrURyucsCs%2FsBRjs%2F%2BltfD4Pp7aEr6plDJddJ2t5zo3JbwzqwsnOatkauSMRxgyriBr%2BLfjFvri4jeS6dF48FNoJUSyfN0qP%2BRJZXJdyzqNbPNLCXaeVx3koDZvtkzwx43O0BTxrrClnWt5isJRxIyoPjlJh%2FYaSY20eH%2F6ZSrExRrumg7h0ZSl6MeevZEBXgtqsMd%2Fg%2BElnoILU39ZZ%2FNyyKoE9Bpg33puvAJMcBQUPSn5pfdMU2SgijHuqiFVbDGBrWANgOoagUJEYSJxzMhMiA4R8GU1a2n9abn%2BbdIB3Jvvr6Aq3mbDwHq200oIXn3W56xbYF2KxIaHpi%2FAtXdYyRJjai%2B7%2BxfmKptGysUBrg8VkD00sKJ9d9mwJIfi8%2F54aZNGvikm%2BkuGzkvf%2BDWiyW7uD7Y8dqNGK4qgNQBU0YpS2UwJ8IrLPupq9sEaihDvXwvU%2FCjfC9Y%2BDdm5zOaSSqD%2F712ZWkuc8CNcW4BlP5Ikv9ds%2B5idd9IHdDtgLPQSRi4ccpKh6puBREZZhnnOoHHPtk2F%2Bou5epZoejDEJzvnNXwr3ISZm5F9kr%2F1msoqjqBTj5BQm2ilMSLabQmACplyZiUNLEPlwb9QPUYHfTVV8nzRTEj4U0i7TeY4XGU44fkyCPPR%2BWByoX%2Fxa4zlo9IY2XGg%2BxGkQW1fT%2Bqj9oL7MR9vvQKsLtcW3wVuMuMXkNQmI7xJm2uKQ6%2FY1%2Borii0mE9zCXrn%2B0kljPdyt2S03CbZFRBCwpPJmOnMEEQKQsyNnUP0xS9VvE4iXlDjFM%2F3y46HxKMItzQFeUxKEYWeixMZMiz0Kod9itXtysWB89s8yiJX7NHQoYyPoQKFQG8zQedehfVRZie2XU4yHO2lmUm6nO0jo%2Bzv4%2FMP9RmjHVQjRng%2FBKkePtGM3i5y3Q4GlHxmqFECQMS8JjSV%2Bla2zEd8%2B2zUIi7oeX3GpNMNbup9WCu5H%2Bwf9MzB%2FiXgNpjCqoB5ywbjw2DHgBXJ0cABozL6kwCG1v6orLluX9NnVBik%2BOpZwEePJfVYKL9e8wG5ysgJJOxvNHVDxaE5lu%2FvpmvkSjKtJWlVt5j0rWVZs5z5L0khIXm1dFIOMS8cnh95rIzumd9cg8jPwUpvFX7Zgk%2BVTNGVNOrqgX4gMHvbwoKbSIKa41bxwannY7BD9sjLbqIIfbcL%2Fe386Mo%2B0oLySfRlGvI6EczARlefkqtUJbw%2FyEry4e8siFNfmgj7w7mC%2BQfIr1hY9GJbKY5GHvIVOiN8PFaIjY%2FI1D03euD5ajgqJS%2Fjns0yAtRSTZawmh0CQlHhmaxrD%2BQ4ZK8xeGkyP1FHVQCpqppu25ky1%2Ff2dXrUqcLt9eX777ENVdWnLd9FCleDWDp9%2BTDj62d%2BRUn3vduL5wjMjQHlXxyG%2F3fxHOLZLYG1ZKo0WbuXlPVcOteYazervLTEAc9QVO1wljmj2z57zhcKUwCh1MPtaGTNrUPKdlBhvNiSicottxEh3O0JxBFbNn"))