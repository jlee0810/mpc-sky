# This is the content of generate_pkce.py
import base64
import hashlib
import sys

def generate_pkce_code_challenge_from_verifier(code_verifier):
    """Generate the PKCE code challenge from the provided code verifier using S256 method."""
    # Encode the code verifier using SHA-256
    sha256_digest = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    # Base64-url encode the SHA-256 digest and remove any padding '='
    code_challenge = base64.urlsafe_b64encode(sha256_digest).decode('utf-8').rstrip('=')
    return code_challenge

if __name__ == "__main__":
    # Provided code verifier
    code_verifier = sys.argv[1]

    # Generate the code challenge
    code_challenge = generate_pkce_code_challenge_from_verifier(code_verifier)
    print(code_challenge)
