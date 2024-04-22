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

#############################################################################################################################################################################################################################################
session = requests.session()

url = f"https://www.ibm.com/account/apis/v2.0/pws/v3.0/lookup?emailAddress={email_address}"

payload = {}
headers = {
  'authority': 'www.ibm.com',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-US,en;q=0.9',
  'origin': 'https://cloud.ibm.com',
  'referer': 'https://cloud.ibm.com/',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

response = session.request("GET", url, headers=headers, data=payload)

url = "https://cloud.ibm.com/registration/generateValidationCode"

payload = json.dumps({
  "email": email_address,
})
headers = {
  'authority': 'cloud.ibm.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'origin': 'https://cloud.ibm.com',
  'referer': 'https://cloud.ibm.com/registration',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = session.request("POST", url, headers=headers, data=payload)

code = input("Enter verification code: ")

url = f"https://cloud.ibm.com/registration/verifyValidationCode?email={email_address}&code={code}"

payload = {}
headers = {
  'authority': 'cloud.ibm.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'referer': 'https://cloud.ibm.com/registration',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = session.request("GET", url, headers=headers, data=payload)

url = "https://cloud.ibm.com/registration/register_unpaid_account?originatingPage=/registration"

payload = json.dumps({
  "contacts": [
    {
      "type": "PRIMARY",
      "profile": {
        "userId": email_address,
        "password": f"{password}123Ab!"
      },
      "firstName": secure_first_name,
      "lastName": secure_last_name,
      "emailAddress": email_address,
    }
  ],
  "csfingerprintId": "0bc02ddf0dccbaf9116aea30fc25bbc1d316854f60c1ef2c5f55fd496983cdf0",
  "bmKey": "9477o840572o0rsn27r544919n9p671q2s4q6n425po0qq8719sq151889n37s7p",
  "countryCode": "US",
  "portalSourceIndicator": "CONSOLE",
  "verificationCode": code,
  "loginUrl": f"/login?defaultId={email_address}&firstLoginPremium1=true&state=%2Fregistration%2Fpayment",
  "reqType": "STANDARD_CREATE",
  "flowType": None,
  "promoCode": "FREEMIUM_TO_PAYG_200_35",
  "anonymousId": "bd38ace8-04c6-445f-a2e8-47141d70065b",
  "uPageViewId": "8b1802c4-77b1-46d8-8fb4-5efacb2b103c",
  "pageViewId": "8b1802c4-77b1-46d8-8fb4-5efacb2b103c",
  "notice_by_choice": {
    "by_email": "S",
    "by_phone": "N"
  },
  "loginContext": f"defaultId={email_address}"
})
headers = {
  'authority': 'cloud.ibm.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'origin': 'https://cloud.ibm.com',
  'referer': 'https://cloud.ibm.com/registration',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'transaction-id': 'a20b2922-5b8c-4e72-8ec1-0eac4622424e',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = session.request("POST", url, headers=headers, data=payload)

data = response.json()

url = f"https://cloud.ibm.com/registration/register_progress?id={data['id']}&accountId={data['accountId']}&orderId={data['orderId']}&email={email_address}&pollCount=2&reqType=STANDARD_CREATE&originatingPage=/registration"

payload = {}
headers = {
  'authority': 'cloud.ibm.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'referer': 'https://cloud.ibm.com/registration',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'transaction-id': 'REG-STANDARD-CREATE-dd22e602-4284-408a-8add-8be899176ccc',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = session.request("GET", url, headers=headers, data=payload)

url = "https://cloud.ibm.com/login/realm/IBMid?iamEndpoint=https://iam.cloud.ibm.com&state=%2Fregistration%2Fpayment"

payload = json.dumps({
  "username": email_address,
})
headers = {
  'authority': 'cloud.ibm.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'csrf-token': 'gW3eR6wB-h0jmFulx4EeaofzF9kWlbj8CB0E',
  'origin': 'https://cloud.ibm.com',
  'referer': 'https://cloud.ibm.com/login?state=%2Fregistration%2Fpayment',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)



# url = "https://cloud.ibm.com/login/doLogin?state=%2Fregistration%2Fpayment"

# payload = json.dumps({
#   "username": email_address,
#   "password": f"{password}123Ab!",
#   "realm": "IBMid",
#   "iamEndpoint": "https://iam.cloud.ibm.com",
#   "postLoginConsolePage": ""
# })
# headers = {
#   'authority': 'cloud.ibm.com',
#   'accept': '*/*',
#   'accept-language': 'en-US,en;q=0.9',
#   'content-type': 'application/json',
#   'csrf-token': 'hqLwb99U-GhyhKOWwaqjPsHj9EkKFjGDvdps',
#   'origin': 'https://cloud.ibm.com',
#   'referer': f'https://cloud.ibm.com/login?defaultId={email_address}&firstLoginPremium1=true&state=%2Fregistration%2Fpayment',
#   'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"macOS"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# }

# response = session.request("POST", url, headers=headers, data=payload)

# print(response.text)


# url = "https://cloud.ibm.com/analytics/profile"

# payload = {}
# headers = {
#   'authority': 'cloud.ibm.com',
#   'accept': '*/*',
#   'accept-language': 'en-US,en;q=0.9',
#   'referer': 'https://cloud.ibm.com/registration/payment',
#   'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"macOS"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
#   'x-requested-with': 'XMLHttpRequest'
# }

# response = session.request("GET", url, headers=headers, data=payload)

# print(response.text)

# url = "https://cloud.ibm.com/registration/upgrade_account?originatingPage=/registration/payment"

# payload = json.dumps({
#   "contacts": [
#     {
#       "profile": {
#         "iamId": "IBMid-6970009V77",
#         "userId": email_address,
#       },
#       "firstName": secure_first_name,
#       "lastName": secure_last_name,
#       "companyName": "UCLA",
#       "addressLine1": "910 Weyburn Pl",
#       "city": "Los Angeles",
#       "state": "California",
#       "countryCode": "US",
#       "postalCode": "90024-2852",
#       "regionCode": "CA",
#       "emailAddress": email_address,
#       "phoneNum": "+14244444444",
#       "type": "SOLD_TO",
#       "classification": "COMPANY",
#       "taxExempted": False,
#       "industry_code": "UNASSIGNED"
#     },
#     {
#       "profile": {
#         "iamId": "IBMid-6970009V77",
#         "userId": email_address,
#       },
#       "firstName": "Eric",
#       "lastName": "Lee",
#       "companyName": "UCLA",
#       "addressLine1": "910 Weyburn Pl",
#       "city": "Los Angeles",
#       "state": "California",
#       "countryCode": "US",
#       "postalCode": "90024-2852",
#       "regionCode": "CA",
#       "emailAddress": email_address,
#       "phoneNum": "+14244444444",
#       "type": "BILL_TO",
#       "industry_code": "UNASSIGNED"
#     }
#   ],
#   "countryCode": "US",
#   "billingCountryCode": "US",
#   "currencyCode": "USD",
#   "portalSourceIndicator": "CONSOLE",
#   "locale": "en",
#   "sessionId": "RHQ08PQHP3PC1",
#   "verificationCode": "",
#   "reqType": "PAYGO_UPGRADE",
#   "useV5Orders": True,
#   "channel": "C",
#   "bssWalletId": "f3eac93fc3a018c65a2ac328ad547a69",
#   "accountId": "a0368f8241544f9497fd87f716c4efed",
#   "loginContext": "defaultId=repulsivecarla@mitico.org"
# })
# headers = {
#   'authority': 'cloud.ibm.com',
#   'accept': 'application/json',
#   'accept-language': 'en-US,en;q=0.9',
#   'content-type': 'application/json',
#   'origin': 'https://cloud.ibm.com',
#   'referer': 'https://cloud.ibm.com/registration/payment',
#   'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"macOS"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'transaction-id': 'RHQ08PQHP3PC1',
#   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# }

# response = session.request("POST", url, headers=headers, data=payload)

# print(response.text)
