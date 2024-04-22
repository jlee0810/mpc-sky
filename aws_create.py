import requests
import json
import string
import random
import time

# Constants for the API endpoints
DOMAINS_URL = "https://api.mail.tm/domains"
ACCOUNTS_URL = "https://api.mail.tm/accounts"
TOKEN_URL = "https://api.mail.tm/token"
MESSAGE_URL = "https://api.mail.tm/messages"


def get_domains():
    """Retrieve the list of available domains."""
    response = requests.get(DOMAINS_URL)
    if response.status_code == 200:
        domains = response.json()["hydra:member"]
        print("Domains retrieved successfully.")
        return domains
    else:
        print("Failed to retrieve domains. Status code: ", response.status_code)
        return None


def create_account(email_address, password):
    """Create a new account with the specified domain, email address, and password."""
    data = {"address": email_address, "password": password}
    response = requests.post(ACCOUNTS_URL, json=data)
    if response.status_code == 201:
        account_info = response.json()
        print("Account created successfully. Account ID: %s", account_info["id"])
        return account_info
    else:
        print("Failed to create account. Status code: %s", response.status_code)
        return None


def get_token(email_address, password):
    """Retrieve a token for the given email address and password."""
    data = {"address": email_address, "password": password}
    response = requests.post(TOKEN_URL, json=data)
    if response.status_code == 200:
        token = response.json()["token"]
        print("Token retrieved successfully.")
        return token
    else:
        print("Failed to retrieve token. Status code: %s", response.status_code)
        return None


def delete_account(account_id, token):
    """Delete an account with the given ID and authorization token."""
    delete_url = f"{ACCOUNTS_URL}/{account_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(delete_url, headers=headers)
    if response.status_code == 204:
        print("Account deleted successfully.")
    else:
        print("Failed to delete account. Status code: %s", response.status_code)


def get_messages(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(MESSAGE_URL, headers=headers)
    if response.status_code == 200:
        messages = response.json()["hydra:member"]
        print("Messages retrieved successfully.")
        return messages
    else:
        print("Failed to retrieve messages. Status code: %s", response.status_code)
        return None


def get_body(token, message_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{MESSAGE_URL}/{message_id}", headers=headers)
    if response.status_code == 200:
        body = response.json()["text"]
        print("Messages retrieved successfully.")
        return body
    else:
        print("Failed to retrieve messages. Status code: %s", response.status_code)
        return None


def generate_random_first_name():
    with open("first-names.txt", "r") as file:
        first_names = file.read().splitlines()

    first_name_index = random.randint(0, len(first_names) - 1)
    first_name = first_names[first_name_index].lower()

    return first_name


def generate_random_last_name(min_length=8, max_length=15):
    if min_length > max_length:
        min_length, max_length = max_length, min_length

    length = random.randint(min_length, max_length)

    last_name = "".join(random.choices(string.ascii_lowercase, k=length))

    return last_name


def get_most_recent_message(token):
    url = "https://api.mail.tm/messages"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        messages = response.json()["hydra:member"]
        if messages:
            most_recent_message = messages[0]
            return most_recent_message
        else:
            print("No messages found.")
    else:
        print("Error fetching messages:", response.status_code)


def get_otp(token, id):
    url = f"https://api.mail.tm/messages/{id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        message_data = response.json()

        if "text" in message_data and message_data["text"]:
            lines = message_data["text"].split("\n")
            for line in lines:
                if "Verification code:" in line:
                    code_index = lines.index(line) + 1
                    return lines[code_index].strip()
        else:
            print("No text found in the message.")
    else:
        print("Error fetching the message:", response.status_code)


domains = get_domains()
if domains:
    selected_domain = domains[0]["domain"]
    secure_first_name = generate_random_first_name()
    secure_last_name = generate_random_last_name()
    secure_password = generate_random_last_name()
    email_address = f"{secure_first_name}{secure_last_name}@{selected_domain}"
    password = generate_random_last_name()

    account_info = create_account(email_address, password)
    token = get_token(email_address, password)
    print("Your email created is: ", email_address)
    print("Your password is: ", password)

##########################################################################################################################################################################################
# Create AWS Account
URL = "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct&src=header_signup"

session = requests.Session()

url_home_page = "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?nc2=h_ct&src=header_signup"
response_home_page = session.get(url_home_page)
xsrf_token = response_home_page.headers["x-awsbc-xsrf-token"]

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/steps/current?enforcePI=False&type"

payload = {}
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}

response = session.request("GET", url, headers=headers, data=payload)

url = "https://vs.aws.amazon.com/token"

payload = json.dumps({})
headers = {
    "authority": "vs.aws.amazon.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://aws.amazon.com",
    "referer": "https://aws.amazon.com/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

response = session.request("POST", url, headers=headers, data=payload)

url = "https://vs.aws.amazon.com/token"

payload = json.dumps({"mid": "32782845309316423803590184641997859993"})
headers = {
    "authority": "vs.aws.amazon.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://aws.amazon.com",
    "referer": "https://aws.amazon.com/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

response = session.request("POST", url, headers=headers, data=payload)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/steps/all"

payload = {}
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}

response = session.request("GET", url, headers=headers, data=payload)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/emailotp/send"
rand_int = random.randint(5000, 10000)

payload = json.dumps(
    {
        "email": email_address,
        "fullName": f"{secure_first_name} {secure_last_name}",
        "captchaShownOnPage": False,
        "timeSpentOnPage": rand_int,
        "browserFingerPrintMetadata": "ECdITeCs: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",
    }
)
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://portal.aws.amazon.com",
    "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_mobile&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "x-awsbc-xsrf-token": xsrf_token,
}

response = session.request("POST", url, headers=headers, data=payload)

recent_msg_id = None

while True:
    print("Checking for new messages...")
    time.sleep(3)  # Wait for 5 seconds before checking again
    recent_msg = get_most_recent_message(token)

    if recent_msg and recent_msg["id"] != recent_msg_id:
        recent_msg_id = recent_msg["id"]
        otp = get_otp(token, recent_msg_id)
        break

rand_int = random.randint(10000, 15000)
url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/emailotp/verify"

payload = json.dumps(
    {
        "otp": otp,
        "timeSpentOnPage": rand_int,
        "browserFingerPrintMetadata": "ECdITeCs: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",
    }
)
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://portal.aws.amazon.com",
    "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_mobile&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "x-awsbc-xsrf-token": xsrf_token,
}

response = session.request("POST", url, headers=headers, data=payload)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/steps/all"

payload = {}
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}

response = session.request("GET", url, headers=headers, data=payload)

encryptedPassword = input("Enter encrypted password (read the README for more info): ")

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/identity/create"
rand_int = random.randint(10000, 15000)

payload = json.dumps(
    {
        "showCaptcha": False,
        "encryptedPassword": encryptedPassword,
        "timeSpentOnPage": rand_int,
        "browserFingerPrintMetadata": "ECdITeCs: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",
    }
)
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://portal.aws.amazon.com",
    "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "x-awsbc-xsrf-token": xsrf_token,
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)

if response.status_code != 200:
    url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/captcha/refresh?"

    payload = {}
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_mobile&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
    }

    response = session.request("GET", url, headers=headers, data=payload)
    response = response.json()

    #write to repsonse.txt the response
    with open('response.txt', 'w') as f:
        f.write(json.dumps(response["url"]))

    ces = response["ces"]
    guess = input("Enter the captcha guess: ")

    url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/identity/create"
    rand_int = random.randint(60000, 120000)
    payload = json.dumps(
        {
            "showCaptcha": True,
            "captcha": {
                "ces": ces,
                "url": None,
                "type": "CLASSIC_IMAGE",
                "guess": guess,
            },
            "encryptedPassword": encryptedPassword,
            "timeSpentOnPage": rand_int,
            "browserFingerPrintMetadata": "ECdITeCs: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",
        }
    )
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://portal.aws.amazon.com",
        "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "x-awsbc-xsrf-token": xsrf_token,
    }

    response = session.request("POST", url, headers=headers, data=payload)

    print(response.text)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/account"

payload = json.dumps(
    {
        "address": {
            "addressLine1": "910 weyburn pl",
            "addressLine2": "",
            "city": "los angeles",
            "state": "CA",
            "countryCode": "US",
            "postalCode": "90024",
            "fullName": f"{secure_first_name} {secure_last_name}",
            "phoneNumberCountryCode": "US",
            "phoneNumber": "+1 4244244224",
        },
        "clientInfo": {"languageSettings": "en_US"},
        "customerAgreement": True,
        "browserFingerPrintMetadata": "ECdITeCs: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",
    }
)
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://portal.aws.amazon.com",
    "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "x-awsbc-xsrf-token": xsrf_token,
}

response = session.request("POST", url, headers=headers, data=payload)


url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/steps/current?"

payload = {}
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}

response = session.request("GET", url, headers=headers, data=payload)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/creditcards/prerequisites"

payload = f'addCreditCardNumber=4118102055126788&xsrfToken={xsrf_token}'
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Origin': 'https://portal.aws.amazon.com',
  'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_mobile&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'x-awsbc-xsrf-token': xsrf_token,
}

response = session.request("POST", url, headers=headers, data=payload)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/creditcards"

payload = f'address%5BaddressLine1%5D=910%20weyburn%20pl&address%5BaddressLine2%5D=&address%5BaddressLine3%5D=&address%5BdistrictOrCounty%5D=&address%5Bcity%5D=los%20angeles&address%5Bstate%5D=CA&address%5BcountryCode%5D=US&address%5BpostalCode%5D=90024&address%5Bcompany%5D=&address%5BfullName%5D=testawsconfirm&address%5BphoneNumberCountryCode%5D=US&address%5BphoneNumber%5D=%2B1%204244244224&accountHolderName=John%20Yuan&addCreditCardNumber=4118102055126788&expirationMonth=02&expirationYear=2034&enforcePI=False&sor=AWS&addCreditCardVerificationNumber=733&xsrfToken={xsrf_token}&browserFingerPrintMetadata=ECdITeCs%3AaPgi6sfVuc%2FNhEacpTi8%2B3WHL2U6rNRzMs6Vlad8c0B5XDzD5qQuWMU1CmtSyq1Z83RzRlyxgTVRsLhvlffDsvtik7%2BcqYma4FrnQiccOkCEV7ZeFATaaaGBuI8qcu0iGhEUOd7dATJlkxFg4HCH84RD9Jn62WIQlSCfbXMBkOhJbCebimvmhvCxb9AYwXylrOtQsVhfT%2BlbAeZqbbJH13RCq8E0ipbpQjbjHP7PC%2Bkuw4S8HKe0VYu3OfX8VDUap8uQXQnvAaNiHGwg4eZQuLdwOwfA9%2FPmZrbCRSfVBHPBtoasltr0nYKbZhrzjRzMbMfP%2FxB8zMq7Rths0d8hG9SPJuqZSeegfgHHkRLZNzgpRGPTpHLg1j8dbPgveU0vMkVJcwW9IFY3ud4x5Ze0MxowoD5m%2FAgDWDTdE7Lkoo4eGhKDpfES4NbGpGyEwfYU%2Bj%2B1aK7455EV%2F7Fr%2BNkVgjc2aNxCLCSGQAKSwXbODsk0A7%2FuLvX0JOw85FRa8nY6mNxYCyGGEnUz1LRhVC1Rh18QX97XvTi%2BumeyUTQi9EItbXSPLrvMPT4RwLLB1wxgze5%2FJlQRRWR6AZTVnCRnPKGuCur0CWDGgybXWEvbHVHdgLAdRrSonyBXFPpAMcCYAg2AGZrpXPEJ%2F0oxbRbN4vPTa3qd3AL70PSA74NPAUX1Yluo7SNrUNuduWPPkUoF5lde6QEwRArf6fRhNUCC3UjsFIHsQNqIkMYkuuFz8u0MTk0lR6mQ4v3xQlztge2AJ0i%2BPNpNKmNJgdUtJ6SUiFux9jaZiyolvVvdcA1KVtqRnxtzeUsvUh%2BCMqRKhg53iOGCtvgGwgfUigphqwlJhc9MqyfF8gMjMAnvSmo%2FNTEzJgsn%2BOAJNXSAgJtCJvY61RAMPW%2FsSrZ%2Bg7rVIpLiVVF%2FI2ED6vKiH36UkLt0dCEIbnMhlTunGR8TJh15gyRtGwY0fV9uHqthv%2FJSwmaPPZ9IeEac71mRNgdMzMGXOI%2Bi0RN9IIh1kpV1FJW3yfkSHlDf7F8of7yr9hdEfUIRBgBkPFSBooF2jksVyghVj7lKsRAe7Dq6Kz3TtkEPv%2FnT1o98wcrMJR%2BSLuWpD%2FXBKvCi8hqvlzkQ76lF5t2lDAwdDNS7YPuAnpL8GkrLcNukk1TbAh3TGyy4Bc5UUv0vbE3IIloT69aTMNwo9EL0VVciJ6bWDxq%2BF5DQ9fcVtOSDq3ebyR5WRdGKKi3YCRSKyZODYnyrsGcjUlapW4Ky6Hf2YLNoQLCDP1McZn%2FyfGHMefBeebKbKzPMPv%2BZLHxnbLD6AgFdvvijDf%2BHEDFktKQmnX4eC5A4t4QezyVLTeiqBDWruQ0b0TZGEfUfzqZazm9z8OJIkHnhbRWQLTDlTeKwEEqGtPlsemeRtHNFhcUzltfjqsZKxFiq3qc9heaB2mLBodX4UsLsH%2FwPW35m0v%2F%2B1smI212YDT3hAP6hGDB82OP%2Bk6Vogff6BxPf1gSpqun1pIDNR55Du9fOZiqLRx%2FFHsqqrAnE8A7AM%2BEFnVaTjBqGxsRDl5r4m4LOz2Cr0lh1qUPEwBtcNBCu2m44DBc4cj%2FDjRQ4HOhr%2BwYv66xjwVNhMI6XCPeMoeXYkdy82IZ85e5ujrZv1OVblpF%2B2SvICl1vN2Du40kAZfmYxElx4JdiApMbfz%2Fx8VgTXe%2F6ohPZCq60y648kxaBx01q9hQVg4YYd1DITx6lgnqFrda35v9deyXMrL3CNSEdwHUzLgEOmuY0gBeoox%2Fg4Ae%2FKrYsvO1%2FRIy%2Bl9TWH3102xwjhBfLbHYo%2F7yTsyByiEMscnxFM6VhxLWXf2MoTOa4x6WCDaulkaxXbZgSWAWO43ckSlp7oBE8kDNrBCKzIpfdwYIfNBN7siG%2BJm%2FLl9JUrvtEg%2FYhdS2Z0mdjy8OAhOLaqpbvd7gPEzuSGV77cLj1JbibnrQa1xMj%2FjoBsUxcFCScRV76eJ3wEuD1lPoJIm2CIvBqTN9pgqMK2jf%2Fua6pQ6cQyDBICdgygzKauveimeAPXbyxmY4J9h%2BApD0RXLJai9Nf60DOvCTPo834vfelDn1l0484uZGCOLaaePftFKWYFhx%2B9h0ws1ROW4su3s4oy6eivLSAuZeYai5fEYscVcMiMEaVsWMFBMagAFRj8xqwOVMVf626rA1pyaXNK9XF5C3Ua5SKqUKWAt9l3S%2Fo83gy4aKKEw0tJgql%2FekqplfRvKdSyURrDUFc78JjKvj1zseyqHIMaHXUzt8hSfEKGgpkCNoVRQbIeyhfCpPZMmxrQvjbFlUSJmJXXKtXFmecf6vVY2KlCYLTMVJtmXhZ%2FqnxWCTePf3UtsnEaQdtWy%2F9hN4SQq4uwPu6ptMfxYsuRNuzzKoUTSrgRUZ7BQ1F1bpAJeB3TwhUmT6fChrk2wMFqmUrFIG7juale83oXl%2BS8bPZDAVt3axXCcG7tLIDnZ1AmuCQn7y9smFpBJMlColgJhqPoliXQkD3mPv2g82sopL3EXOI81sXTLQUKzo4%2BSkjnIy6Utg9ExtIp2p54LNKnaLwdhjNRfuLHrG8AY1H4RJfP7VT%2F37LSK4bGHphc7w4LSS7AHESDhCJ1mrwjEW4BC0wTySx8KVTJJAibWSvAeQoq5Ih2A3yxMKof0gPnd2EsvlNz9qFo3Y8AbNhUV%2BucWjJEpprfwl6ZTRyf9GzipbKhFDSFkjMAHCQg5laIazYfQaL%2F%2BmZtE1UOy2AS3NRzcAuXvpLCLgtf17Z4xaigxh9jBJ70LP7m4M3Z99C3PZl%2BtwqOQH0S%2F42TbW7OGz8IxZv%2F2VMdOPH6DIvXiCXpdKX8Vvl1WZ%2FOEbC7lcvhxMm0lJf9oC2ntD0JX7xY9I9zjnQVLzsQLXfqKw%2BI051qWjyRDlaX3dNDwD1vw9LJ5HB%2FCcdsWfXwelHvk2kvOTHI5u8IDsD5SV1J9grb4TsNskdgW8cCgcSzqcvJ2ptBLW2hnW%2BU3rnQS0cE1uy9Upo7I48MWgvRIJtDdvW7HpiZ4mlU8SwIcACMiTJwzFlT8hyoM7y9nKJZL9Bf8jdCqhE9hqdKMbc509X3Xa5koJI3GpnE9hDYS%2FxHHTLKjnIN4RoTI8FN3XjBHJbb3yTE1BKTfLT8hG7avxdLF0l1yNQFfIrnTugiM0vaDpDiJ7c6tnuh4zEBTIsPT9QGPa%2F9PDqRmNpJpIZMeUzLYddazFygJTjAUBR1MtkIafGuyaTtIM2kkUdzcl0kJWx8vFqMxO1sl8Da8P%2B8D0OwQSIwUpbR7X1QcI5DtGperOXMZ%2F5KVRbCLmzAUIkYBMBIYlV4g0gkzHxy84SkIFCShBWawzDEoiht6RS652TJIyVtJSrMxKT2Kvy7KOVwQhvSOFoeVs3vo9rZnD7vRFHe3RfnKC%2FTqis%2FIhbJilJ742mYOJFDE249vsmCEMax8qAL3fCG%2B%2B6b%2B5vbULwdahj0GYzoLgrFjgcG%2BnlFdr30jPM5TkTJBMwuNztjYr4tyNE6mPq4eYgi7AvRgeM6EBQgzcsdr0OBiMD%2Fa8wnLMV%2Bu3aTByVxHWq8dCsyR3%2B%2BQpVW8akTYSN1ZrjdM9biRAyVBUKPC1GGPMZwAKFH0ZdzqfyVDGxjGUHOu50uakCSm%2B%2BBf1pvjNu4O3NgDjhhdVghTOxodif0XJIs%2FRtuf%2BecBlRr7Dvnwk2HgLcPmHBQhz1BExpXNYiSQNVdV4W4GSLEwJFQl6KJ5XjFndihNqSLWveOP%2BpCFiIWr2vaVPhl1kF94aJC4928D0dousJJFZBLUjws61Z7TgHA45KbLCydcEJuEiY4WpSo8z7YDFUXKx3pyS7UZGWTpctGRM23t7f8PSqCQHD4kdjcLKb8pJurYokliucXyrcmEMgyg66reds8g62TEhUWuiSNVn3vMHOOCeJOtZOc5oCGOsarG0prpji0XQbB1%2FmMzxNOgjAPbTXnVqJ5mOLMwQSQuaLjvgM9aVwuK3rJtcEwydEkBlRneCiH9woe0QdqeVl%2FGTa2%2FNz38lNLzyhQB5W85qu47LzEZlHHlWl6RvbX1rNiyNp6%2B4846ULwF7AQrXR6CuKAXmMDekQbnbNQ8CNSXbyvKnBoUzWdD%2BFSNI5x9P9jCFmcwdyI7dtlOXC%2FFY2B6wND5DJOr36VU4xtcQZq1KvzN3Axy03vUe28e37kA2F2WpjJTbzdgT%2BXhuTj4pGc73b%2Bqu%2B3esMRLml9BCOrWYC3OPS%2F57DDGzMOy78ObTe2lFwZ0OquQgCFc9J0PD%2FWoeVEyg9OUvWSCXD2gdM2QhDLPW%2BUTOHzkO7yOZdHevCRHPKlPceVdCvHXq4GWmoSwJWQKWcbkcnMhdHFBUJRDj%2F0S7bDU%2FvtkNyreBD28iLXX6DW3Zzd9d7X15FDcpAoQzdUYgri7nNLD413cCSz795Ed7qW8pxVQ20YJIT76kJ1DJr5X%2Bd1ktryvWGrTWyiPpYFCbs5L8x1nW6E9Kkap5SIVFKKr1Frn1bUC0rIRLJCng0UvNTA37U%2BDpWJfE2PDeweu6TDey96OGOMP6pi48taZOhJnGuu79Vs5CHr4gqm9PRZcJuIOfBs4cUUOUVl9j64z9TQGeXiZRz2ViNNY1rEsOq696pgy9MiGe5i%2F1fa%2Buer6H6aXdS0hQ6U%2BuqGLhEuz%2BMiYs3O7yaKigsD4mQYFn3hjZE13YRF9oI2QcLhhqq31cC335arOjOr5HUlbi1EoWP9o3up5OdNcDqGPmhkzyMWa5%2BD9zZk%2F1KkalOXTr4ejux8N%2FcSox%2BJ9WOel84w%2BbdsH5ak%2FM2Sfii%2FOnhya7lp8XvaqNGCIqlk1SvUOdt7wWcyUaxKgJEb8n%2FNyU3yu%2Bx0Lu4sCuH9P6SCkz1%2BADQ3Gy6s25g5vdwOa4Dkahw2ykF9F%2BnMN%2BGW0nIjUZE4qicv3jMZ75wkuJTYEaiKGlv%2BbNcFgMcuVw3fxxFgkbmKAh0oYTQ3Owgp%2FnJhognPYm%2FiyQZ2mluiuKR%2FQjltqIQMsTwElU8Zx%2BSZA0CNvkAcSar7mwQnWMwG1jgRXWbsMAYu4iaAZfzmnGScgisLnMGHfCswoUHqWzspBv7lSDbb%2FRa0sQxJsbwiyOeJSk3Cpu0DZSh3kxkk0D48IDsF%2BY8YZLSabWyUA%2B9qtQRs3E9InpsOnf5YRgujN6Y2LuS8vMsQFbFWMzRE4lrdCS%2BYlevLfntHrvE5lvnf3V1EVQWoHXKFE4VSIMaVDlV1RcH9ikeWmmThxlaax8ZltMAIS0UeK7cNCrSW5GnRRzLLUf30hWpxEztpX7YlVEvEogbFXFSEhtMWrXy0XIotZtSEEXcmKnuTFqbwnfHYEV9LboMT1ELAOsPhVdKjzOtcWs8LCP3lEy2W1SJcw4DbSMWWQxxmytJ4bH3vv%2FINygz9i94ELDfrW%2BVxIyLC2wWDfTNv3jhlK%2FRHctBjIGG%2Bj7U81BlcWcVAPGOMVks4XQaBJi0NSglcm2Lt0v3PuVdxjS1YrXT%2BtvoEJ98VBZ75XrhWIMT19Tkyav647S6ZFPj6Vxl%2FmnfjYv6FWVYt%2BQ5lHvlh85NjRu0Zd%2Bjcyzj01wwghHvPiLNOPoYdSX3%2FyE8z7ZfVC2Lga7GmQoyjou3%2BOmYJA8Qc1aYzoaOWrK4JxGeb2ZMbHGFi8p3mwn02yAC2l%2FydUHokasRzyT01X7ESse81lfVemBi21znsNS%2B6w8uZQgjoBC%2BoleosAgFYH1CcGSW4UqyQVGO76FoqVnSUJqV1EQzQU8TUT9GDW0hc%2Bn8tyC82RmuWZ5DKFdKyGIhcONBsDuYG9L2Gy3DbaoQvcbFt9r67dt03hUyeOA3kqOHegBny5SZjUi5IXqUVOrMFUOL81YrmwVfKOa0Fcym1RC1TXA52lhU9Gbozr3273z2NXOTSCahb8DnX4AfOgNfH98%2FTAiHDxB0NkjuqmbGG5nyGXUsgLvJhQ73QB1dxpgaaBhboFurVTADxcBmQqBGb5BogcRj1%2B%2Bs7aAUBEuZBzHc%2BA%2Bgo92Nt54DuhehsFlgNmkuR1PN0GUCc3MqgUpX6bB47AIPJffFBYFzO34caQZ%2BDaGxNq0otfSuR0iKds1YohDBz%2FgJfnK9BWMvHFB4LMx1vELydTO2Jnl5YCaGphzGHsA3Tmt4XiTNo8nDwTyC4sfNVVV1rEiQndcP8Oe%2BnTfbaZ65jmstCUOpZczPDfc2IMFU5IPINV3rEp6ZEBGoWzyMNW6jKGgjeWLDQk%2Fo%2BzDRbYzWc2wfsOMLl5fLJYyniql5qEy7%2Bvd5Id7EpPxVQWFIFZiFmbBVkit8vkMBflA%2FR8Ppu2zpz6ON452h2wwLdT92tzv12fiaj32H0LJwI25jLr8Zw%2Bh4EupStaCLYdRuN3mTSiylBNVzytZixD6M6Etlhss84Zxz59tRskRG3YfrHTElF6%2B%2FBl3Lf8bt3iGd2Wo7EDXkAXhacG9NKhL3NW0nXbIdld4iTm4G963molF9B6mAJl5DLMu3%2BDJ3gDDLNa2ppVMxizL8XfGqTv8pYubmZj90KIUmNlCs5ACrRPWOxA6kD2gVJbbdMiW0plxoSi7DTgp3xFh2Y7z94zZZrVnaHvHRLFdhSFsbPOu6JsxqmpHBUhCr1BUjNrE%2FR%2B5NQhKGpTPaUI2jRS04RUZ3uU%2BX7JOhQdTQKFYGkteFWIEM1oQ9hg3pBFxUB419Cw1TQPlKqPHj%2BdGUiCo4oXCqUaNwanRZ6r1qa4sxl4QvOgStsBqYD2mBSLeaAeQdBFyNdj7a'
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Origin': 'https://portal.aws.amazon.com',
  'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_mobile&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'x-awsbc-xsrf-token': xsrf_token
}

response = session.request("POST", url, headers=headers, data=payload)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/steps/current?enforcePI=False&type"

payload = {}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_mobile&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = session.request("GET", url, headers=headers, data=payload)

print(response.text)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/captcha/refresh?divaImgCaptchaLevel=ImgMediumCaptcha&page=diva"

payload = {}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = session.request("GET", url, headers=headers, data=payload)
response = response.json()
with open('response.txt', 'w') as f:
    f.write(json.dumps(response["url"]))
ces = response['ces']
guess = input("Enter Captcha Guess: ")

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/diva/startSMS"

payload = json.dumps({
  "phoneNumber": "+1 4244650821",
  "language": "en-us",
  "captchaCES": ces,
  "captchaType": "CLASSIC_IMAGE",
  "captchaGuess": guess,
  "countryCode": "+1",
  "checkCaptcha": "true",
  "enforcePI": "False",
  "divaImgCaptchaLevel": "ImgMediumCaptcha",
  "country": "US",
  "verificationType": True,
  "browserFingerPrintMetadata": "ECdITeCs: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"
})
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Origin': 'https://portal.aws.amazon.com',
  'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_mobile&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'x-awsbc-xsrf-token': xsrf_token
}

response = session.request("POST", url, headers=headers, data=payload)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/diva/verifySMS"

sms_pin = input("Enter SMS Pin: ")

payload = json.dumps({
  "country": "US",
  "phoneNumber": "+1 4244650821",
  "enforcePI": "False",
  "smsPin": sms_pin,
})
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Origin': 'https://portal.aws.amazon.com',
  'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_mobile&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'x-awsbc-xsrf-token': xsrf_token,
}

response = session.request("POST", url, headers=headers, data=payload)

url = "https://portal.aws.amazon.com/billing/signup/rest/v1.0/subscribe/support"

payload = json.dumps({
  "product": "AWSSupportBasic",
  "browserFingerPrintMetadata": "ECdITeCs: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"
})
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Origin': 'https://portal.aws.amazon.com',
  'Referer': 'https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'x-awsbc-xsrf-token': xsrf_token
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)
