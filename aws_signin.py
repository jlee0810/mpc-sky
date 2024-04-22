import requests
import subprocess
import re
import json

email = "dlwnsdnjs0810@gmail.com"
password = "1237789Ab!"
session = requests.Session()

url = "https://aws.amazon.com/"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'priority': 'u=0, i',
  'referer': 'https://www.google.com/',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = session.request("GET", url, headers=headers, data=payload)

url = "https://vs.aws.amazon.com/token"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'access-control-request-headers': 'content-type',
  'access-control-request-method': 'POST',
  'origin': 'https://aws.amazon.com',
  'priority': 'u=1, i',
  'referer': 'https://aws.amazon.com/',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = session.request("OPTIONS", url, headers=headers, data=payload)

print(response.text)

url = "https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin"

payload = {}
headers = {
  'authority': 'console.aws.amazon.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'referer': 'https://aws.amazon.com/',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-site',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

url = "https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin&hashArgs=%23"

payload = {}
headers = {
  'authority': 'console.aws.amazon.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'referer': 'https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = session.request("GET", url, headers=headers, data=payload, allow_redirects=False)
cookies = session.cookies.get_dict()
code_verifier = cookies["aws-creds-code-verifier"]
command = ["python", "code_challenge.py", code_verifier]
result = subprocess.run(command, capture_output=True, text=True)
code_challenge = result.stdout.strip()

oauth = (response.headers['Location'])
print(oauth)

headers = {
  'authority': 'console.aws.amazon.com',
  'host': 'us-east-2.signin.aws.amazon.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,ko-US;q=0.8,ko;q=0.7,zh-CN;q=0.6,zh;q=0.5,ja-JP;q=0.4,ja;q=0.3',
  'referer': 'https://console.aws.amazon.com/',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
response = session.request("GET", oauth, headers=headers, data=payload, allow_redirects=False)
next = response.headers['Location']
print(next)

headers = {
  'authority': 'console.aws.amazon.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,ko-US;q=0.8,ko;q=0.7,zh-CN;q=0.6,zh;q=0.5,ja-JP;q=0.4,ja;q=0.3',
  "Accept-Encoding": "gzip, deflate, br, zstd",
  'referer': 'https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

sp = next.split("&")
for i in sp:
    if "redirect" in i:
        uri = i.split("=")[1].strip()
print(uri)

response = session.request("GET", next, headers=headers)
csrf_token = re.search(r'<meta name="csrf_token" content="(.+?)"', response.text).group(1)
session_id = re.search(r'<meta name="session_id" content="(.+?)"', response.text).group(1)
print("CSRF Token:", csrf_token)
print("Session ID:", session_id)
print("Code Challenge:", code_challenge)
print(session.cookies.get_dict())

url = "https://signin.aws.amazon.com/metrics/fingerprint"

payload = "name=IsFingerprintFileLoaded:Success&value=1&operation=AWSSignin:FingerprintMetrics:OnLoad"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://signin.aws.amazon.com/metrics/pageload"

payload = "path=%2Fsignin&perf_data=%7B%22connectStart%22%3A1713813511267%2C%22navigationStart%22%3A1713813510806%2C%22secureConnectionStart%22%3A1713813511275%2C%22fetchStart%22%3A1713813511258%2C%22domContentLoadedEventStart%22%3A1713813512355%2C%22responseStart%22%3A1713813511846%2C%22domInteractive%22%3A1713813512355%2C%22domainLookupEnd%22%3A1713813511267%2C%22responseEnd%22%3A1713813511848%2C%22redirectStart%22%3A0%2C%22requestStart%22%3A1713813511410%2C%22unloadEventEnd%22%3A0%2C%22unloadEventStart%22%3A0%2C%22domLoading%22%3A1713813511851%2C%22domComplete%22%3A1713813513199%2C%22domainLookupStart%22%3A1713813511267%2C%22loadEventStart%22%3A1713813513199%2C%22domContentLoadedEventEnd%22%3A1713813512355%2C%22loadEventEnd%22%3A0%2C%22redirectEnd%22%3A0%2C%22connectEnd%22%3A1713813511410%7D"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://aws.amazon.com/csds/v2/metrics"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'access-control-request-headers': 'content-type',
  'access-control-request-method': 'POST',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': 'https://signin.aws.amazon.com/',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = session.request("OPTIONS", url, headers=headers, data=payload)

print(response.text)

url = "https://aws.amazon.com/csds/v2/metrics"

payload = json.dumps({
  "input": {
    "requestBody": [
      {
        "metricName": "impression",
        "locationX": "40",
        "locationY": "120",
        "clientTimestamp": "2024-04-22T19:18:33.551Z",
        "pageURL": f"https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256",
        "namespace": "target-service",
        "ctaURL": "https://reinforce.awsevents.com/?sc_icampaign=event_aws-reInforce-ver-a_w15y24&sc_ichannel=ha&sc_icontent=awssm-1715302_event&sc_iplace=signin&trk=5571679f-334e-4215-bafb-75e33a33a803~ha_awssm-1715302_event",
        "organizationId": "aws-signin",
        "slotType": "image_banner",
        "campaignId": "aws-console-signin-aws-reinforce-apr2024-1715302",
        "contentVariantType": "",
        "algorithmVariantType": "WEIGHTED_RANDOM_DEFAULT",
        "contentId": "site-merch-content#aws-console-signin-aws-reinforce-apr2024-ver-a-1715302",
        "channel": "ha",
        "experimentId": "DEFAULT_EXP",
        "targetingIdentifier": "accountId",
        "locale": "en_US",
        "region": "us-east-1",
        "slotId": "signin-banner"
      }
    ]
  }
})
headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': 'https://signin.aws.amazon.com/',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://us-east-1.prod.pr.analytics.console.aws.a2z.com/panoramaroute"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'access-control-request-headers': 'content-type',
  'access-control-request-method': 'POST',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': 'https://signin.aws.amazon.com/',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = session.request("OPTIONS", url, headers=headers, data=payload)

print(response.text)

url = "https://us-east-1.prod.pr.analytics.console.aws.a2z.com/panoramaroute"

payload = "{\"appEntity\":\"aws-signin\",\"awsUserInfo\":\"\",\"awsUserInfoSigned\":\"\",\"batchRequest\":[{\"eventSource\":\"polaroid\",\"eventType\":\"performance\",\"timestamp\":\"1713813513198\",\"operationalData\":{\"metricList\":[{\"metricName\":\"firstContentfulPaint\",\"metricValue\":1590.0999999996275,\"metricUnit\":\"Milliseconds\"}]},\"requestId\":\"8b069227-912e-429d-9c49-f61ff7761f46\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"requestUri\":\"https://signin.aws.amazon.com/signin\",\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\"},{\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"timestamp\":\"1713813513199\",\"eventValue\":\"853\",\"eventSource\":\"panorama\",\"eventType\":\"view\",\"eventContext\":\"https://signin.aws.amazon.com/signin\",\"eventDetail\":\"https://signin.aws.amazon.com/signin\",\"requestId\":\"bebe8880-2b67-4da2-addd-848bea9cf8fe\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"requestUri\":\"https://signin.aws.amazon.com/signin\"},{\"eventType\":\"pano-cust_sign-in-flow\",\"eventContext\":\"\",\"eventValue\":\"\",\"eventDetail\":\"Started\",\"timestamp\":\"1713813512366\",\"eventSource\":\"panorama\",\"requestId\":\"abe94750-aff6-43f2-a7b0-aeaf93368b6f\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"requestUri\":\"https://signin.aws.amazon.com/signin\",\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\"},{\"eventType\":\"pano-cust_account-resolver\",\"eventContext\":\"\",\"eventValue\":\"\",\"eventDetail\":\"Presentation\",\"timestamp\":\"1713813512367\",\"eventSource\":\"panorama\",\"requestId\":\"37c0cd25-7060-4954-93d1-0603d80715c6\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"requestUri\":\"https://signin.aws.amazon.com/signin\",\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\"},{\"eventSource\":\"polaroid\",\"eventType\":\"performance\",\"timestamp\":\"1713813513200\",\"operationalData\":{\"metricList\":[{\"metricName\":\"timeToFirstByte\",\"metricValue\":1040.199999999255,\"metricUnit\":\"Milliseconds\"}]},\"requestId\":\"8e14f002-7b3d-4704-a569-d70de386c68e\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"requestUri\":\"https://signin.aws.amazon.com/signin\",\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\"},{\"eventSource\":\"polaroid\",\"eventType\":\"performance\",\"timestamp\":\"1713813513200\",\"operationalData\":{\"metricList\":[{\"metricName\":\"pageLoadTime\",\"metricValue\":2394,\"metricUnit\":\"Milliseconds\",\"metricDetails\":\"{\\\"rawPerformance\\\":{\\\"timeOrigin\\\":1713813510806.7,\\\"timing\\\":{\\\"connectStart\\\":1713813511267,\\\"navigationStart\\\":1713813510806,\\\"secureConnectionStart\\\":1713813511275,\\\"fetchStart\\\":1713813511258,\\\"domContentLoadedEventStart\\\":1713813512355,\\\"responseStart\\\":1713813511846,\\\"domInteractive\\\":1713813512355,\\\"domainLookupEnd\\\":1713813511267,\\\"responseEnd\\\":1713813511848,\\\"redirectStart\\\":0,\\\"requestStart\\\":1713813511410,\\\"unloadEventEnd\\\":0,\\\"unloadEventStart\\\":0,\\\"domLoading\\\":1713813511851,\\\"domComplete\\\":1713813513199,\\\"domainLookupStart\\\":1713813511267,\\\"loadEventStart\\\":1713813513199,\\\"domContentLoadedEventEnd\\\":1713813512355,\\\"loadEventEnd\\\":1713813513200,\\\"redirectEnd\\\":0,\\\"connectEnd\\\":1713813511410},\\\"navigation\\\":{\\\"type\\\":0,\\\"redirectCount\\\":0}}}\"}]},\"requestId\":\"a8a8f90a-c84a-4286-9800-284d92285b22\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"requestUri\":\"https://signin.aws.amazon.com/signin\",\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\"},{\"eventSource\":\"polaroid\",\"eventType\":\"performance\",\"timestamp\":\"1713813513200\",\"operationalData\":{\"metricList\":[{\"metricName\":\"domContentLoadedTime\",\"metricValue\":1549,\"metricUnit\":\"Milliseconds\"}]},\"requestId\":\"afe6e90b-db74-4a6b-8415-ebefd70e8626\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"requestUri\":\"https://signin.aws.amazon.com/signin\",\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\"}],\"batchRequestId\":\"f944c3b4-c3ed-4077-998b-52f35546832a\",\"consoleRegion\":\"us-east-1\",\"consoleService\":\"login\",\"visitorInfo\":\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaWQiOiJkNDdkMGQyZS02M2E0LTQ1YjAtYWMwNC0yMTg4MDc3YjUxNjciLCJ1YXQiOjE3MTM4MTM0OTQzMDUsImV4cCI6MTc0NTM0OTQ5NDMwNSwicHZkIjoiYXdzLmFtYXpvbi5jb20ifQ.bWMHHVBEB3UXm-3caIxahEWVkIQtINtMC6zYbfSD5EU\"}"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json; charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': 'https://signin.aws.amazon.com/',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)


url = "https://us-east-1.prod.pr.analytics.console.aws.a2z.com/panoramaroute"

payload = "{\"appEntity\":\"aws-signin\",\"awsUserInfo\":\"\",\"awsUserInfoSigned\":\"\",\"batchRequest\":[{\"eventSource\":\"polaroid\",\"eventType\":\"performance\",\"timestamp\":\"1713813553084\",\"operationalData\":{\"metricList\":[{\"metricName\":\"largestContentfulPaint\",\"metricValue\":2308.5999999996275,\"metricUnit\":\"Milliseconds\"}]},\"requestId\":\"00ec7d83-2830-4833-83dc-e30d26eaea36\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"requestUri\":\"https://signin.aws.amazon.com/signin\",\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\"},{\"eventSource\":\"polaroid\",\"eventType\":\"performance\",\"timestamp\":\"1713813553085\",\"operationalData\":{\"metricList\":[{\"metricName\":\"firstInputDelay\",\"metricValue\":2.400000000372529,\"metricUnit\":\"Milliseconds\"}]},\"requestId\":\"c39df25d-1978-4acf-9051-f528006d1f1c\",\"service\":\"login\",\"consoleRegion\":\"us-east-1\",\"version\":\"2.8.16-signin\",\"modality\":\"web\",\"browserLanguage\":\"en-US\",\"domain\":\"Prod\",\"browserCookies\":\"\",\"referrer\":\"https://signin.aws.amazon.com/signin\",\"requestUri\":\"https://signin.aws.amazon.com/signin\",\"pageUrlPath\":\"https://signin.aws.amazon.com/signin\"}],\"batchRequestId\":\"0d4661b1-3530-48a3-9c57-34d04d31b79e\",\"consoleRegion\":\"us-east-1\",\"consoleService\":\"login\",\"visitorInfo\":\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaWQiOiJkNDdkMGQyZS02M2E0LTQ1YjAtYWMwNC0yMTg4MDc3YjUxNjciLCJ1YXQiOjE3MTM4MTM0OTQzMDUsImV4cCI6MTc0NTM0OTQ5NDMwNSwicHZkIjoiYXdzLmFtYXpvbi5jb20ifQ.bWMHHVBEB3UXm-3caIxahEWVkIQtINtMC6zYbfSD5EU\"}"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json; charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': 'https://signin.aws.amazon.com/',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://signin.aws.amazon.com/signin"

payload = f"action=resolveAccountType&redirect_uri={uri}&email={email}&metadata1=ECdITeCs%3AOSwJm5JT5S5EJ5FgYESBRtihMeVzsSx6vWQFy8MslNLo2oBw%2Fi3Ms33o7IbN6hXGT8TAI5JTMsAi1HhqdrZFOTbvIjfx4JisriHAp3uaR8OvGlZopKmArLN7SCUd3eBNOZ2UC%2F%2FtkgDji3%2BG%2FCHdne6D7Ewv2HhY9THJcrLM%2FnfrU%2F8g4Kjf%2FPLbLGKlmOZC0yipfxaJPbEWI%2FfFXNlnyTJLMpbVA731RUaC5tI6F4GqfgvcyT2S0zI6%2B2tRPInUL0v9I4P7KEf6o0NtfWUoMoDHnNUQh%2BUKXWBHvwl768efYHNBNAlvfEp8DNQaJE64AZCYggk15Egyb5K2fTg4HiYiu7Kk2HH6f%2Fw70Q8%2FJuaGT3WSdukl6HKf2gtOo3R10mONxO8RJD6b8ai4iwf40K7Svs5DJUzHaGoI%2FazQNOkdZQSdxIAHcjvPlFlibcP%2BKNOf%2F0n%2FS9fqkDKt5MRCJXMDHnAN2aINEhpxhpm5YXMz4051R4N3a3FPwOLWnFR2nmjIu3PJ98DBPO%2BWMfy0kFOEcnrvVWh2SRdrnZ9n3Iec7UBczMCxV8th0vkeHHWG5VJsbDjGFTetHYSmp%2F%2F4u7QUzupvnF4DbD0HkPqhmoRVqdVI%2FL01O%2BT78792FftLdNLViFYLziCbWTqmofryIDJkPgcgEME3dC6n03G6iCYFYjsmGDEHsn66CEWvkIZfEDBcgG38Xl6zDEbActZxAllcNq4AeVmLYupck47QzsqDXm7Yf7QW4Gj5dLo%2FijBKgCgeT4EiWKkw10VxfAh4NOMVfg0GfZgA6QQAvHWj0eGF7I9iyQlHZ1if%2BbwxFAnXpvNfbfC7up0DTS7NuJ5w5q%2F9UDszNYZvGDthL9cT9SftV2uXZqQE9E34suRQCFU20P3qJIm6JikYS0m3D9ZGqrRKjwn0f9hkzJKZS0xUymuzNuCGIGZtVGUDFodqTZqb3ptuuFB8HDHJ4rlkaR%2BjzVyaddURDPJzCihvFnTKLLOJLz%2FD%2FnkEWazleupHOgFnN6SZ8keOh2k1M%2BeWlydmzVchDry9KP64JOtIWy45v0wVevRkZ%2BUvJ2%2BaUaHViYNHjWAeMfKki1FPL%2FfFiPjFjpTbGKsqomuLX5DED%2Br%2B%2B4LBOuER0QGpwAdG6icRvc%2FFMbSkfsatV3dEaAqEOvDvbPdiI2Cz50HMKJmPOZQHbbqTKwIqEJR4amFMkiV%2BHmn2Nxf7U5ScxKcfxC1jo%2BUaOk1gv6%2F61S99FQmJoWNZEQQ1AcLjyX6ovzJvp245w3UvkWKVtwZNNl4AO8QRIf10MwJxXFQpBWkTVaTGADefNhIjYVs3Ti%2B3lreJUNI50dcJzv4R%2Byqk2btTvrFK5bgdML4w2VYUV6pGdn9Yv7GiDrRSvLOBRH%2FU7AE%2FlpDi1SlvcqvYjmS5dca%2BNusa%2FogaE8FqUX7ouWgLOEx4bglk3LkB7ogsg9cYPMy4p1tx8hdzHh854njbfAsU02%2FV7uqTv%2By6VAtHqhVMre9phtB52byfzzXQj3HYcHKpWIWikAh8xryKEb2hbadQoW%2BJf4kw28es2JzPR7XL966LLOi2dCISflZM3KsotPrPyOoktTTtVUtlYlYCUdPAzVje8aMUUL%2BlREzt14BmHVXFYzx317b38%2FH6lgK36qwbh3bNUSnZeE%2FgSrPMGuN93WAdiB2STAXIcMwPMtxtfJdlvnejgVH4a2wG0aT2YIoKqtFqlAvnq10Kla1XAH%2F7J7qj0QUm7t4mcEhJHKwZc6FI2e2OGsqf4Gu5aY3a5Wl6WMG6BvwGCFjlTPb6PBBJjPFl69bOhZqVEyDYkoXFcuvXKYesRXlLRDuhE1JVLwtAuvu6LHpYmWc2vWESSY6gyYFVEfVlnEIsNtUsz3BZb5unWpRo3ATJK%2FYKJYc6K1YoDndqecX7TBencXkvOVdWCBMhprueWheqYzDQO0DzkthvF254F%2FGRhlnmphBFreAQmgN%2BQJy8%2FJxoLg4ZjmTYp8eEH5K%2FwVVBls%2BTEnvVmnvOGvtaVZ5%2BzsJprEa%2Bq89FVAHzIj2XNk2kqotI4N2KV2vDUCbFBOoVabUJjgNcAq6zA1W0Xeduq5mMnh750xd%2B5WUdBDlbiBzDJW0PgF5Xi0wQ4wheTA7XVtNfNLdGPB9xgjJk6z4IYGeBIF1u1LE4ya27U9hggKNxKNn19IjT9IpkJKJm2qa9ug%2FpezjDfTorNfhE80N1kB6aryzURGWn7dxhrJPJhcKOWsIxcWfWhTAagUIYy6wHcDQcwJTe2cuL14K7qQCxJ%2BZHfUhAwdDUCwC2ApPMippkkTpzAcZqdPedXEjlpZ%2F4qbAwYta3i%2Fu%2B%2FxMANcLBym0L77wKXvD9EtOZHmHzcuGn2qoXvT9X83qJoBYwPccVVkoC6Yk3ZfvlD%2BSL16NRk%2BFG1ag6WWLR%2F7pdjT0oqUdbSsVc5goYuwb6ikG1IOYsfvAZb%2B8jYVD9QovqmdFIPm0%2FftMOEMZdzln9NVmDls49VcS5lAN%2FdegKfmx7L25COpjseFprZbucdm5tNvRK8CK3QAOIrquMbXVwEZQAnb6%2BR20FWiddWHTMGhmT8S844rAnz2urRA%2FCbD8fwSgmnt%2FRvkbnfxpkFNRGH3VvsnOWenRsUKwC5RLzM9jSKIR03T5nEACQqhX0nUtL3u3ipgM3yYBRscs5hMiBYu2DmZTF447i28YLRXxOFE9O2q%2BlkFKfz5g722MqHXOt%2F8UZlVnacEq8i95%2Be%2Fjcof2jKdCSlQ9i0CpKSn939k3CMaNZaYClT1337ukkZ8aHGQ6p2Vd5yJFNbwArpvPjfiEEyB8yK04%2Bea3yqAHVSGqyzk5EOevp6iaT2CoaZIvxL3f%2FFijt8RBB7qo2iNFdoChEuMR7tMNcg%2BY58x%2Bb98aYWOeDSjejqKaoko%2B87hWziujQWwmp2luahLRGzdhxLx49SaUDAn886NKV9qqgxbYuI1FrqNPqfPIqLIgVfn7FISb%2F46oUqWKPlx1Dy3d0M5xOuvsQcSio8pC%2FW%2BLteoDq6qGvdJng9atzTmrNI14HFUdTM3aNSgYUw7zFQIE7zpgVhqyv6nnHnRJ%2FY4nmRsvoevFYcaMcL8XSsIjAHXHu%2BRvpPiui5qoFLXlmqXHLdw%2BBIKE3a5%2BfAMaKWwm2Qyhs4%2FN0AckYPLCwJoZ6pp6inPLwNDx%2FmzayUlwlcYsadr5MBph01YNZROQX1%2FnvVo%2FRgqT6%2BwC9YlwRzOG58ipG5iAppkjeM8tQPyaURDaS4jYii5CnFXU%2Bb4KnZUlqJa8XmlOl6CqC6zk6IzSqjb8Zmon%2BJVRVeQV1iZ9qlfIoC%2F5oQJzz%2B68E9%2F1mT9WXaKxKmKPXimrQFt5fBdkY3RMHXBwp2t9XcEP%2Fr7G42sF6Nz%2F29f86dvKXjv4Y8EBWOix%2BUGhesuV1imdzk%2FyIUwcoHa7Kn2jOuv1K9BiFKO6SzFii3hzuiVV7fjJ1fMwRnL4UWYRj3PHz3r4Jv4rhyxYEg5kj9IThVxXp4w%2F%2BG%2FkiDa9KG%2B%2FAWMzWGbEEt9nC1eqkd4WbUNxOt6MOlRMKu1IFq%2FTtLu%2F746aQxj6gRJIQHHW5RDLhyhugBxbtTd1CLXCb5BznkDFYcDZlTyXFwSohqLeBOUNu6qMNGrVrJNQdAbw3kE9YMVtabbRWEAEQ9p7k%2Ftg8zXrzvPdryiSDOVeic9QqaI75%2B03nbkhkPjyfPSZKF1LbOd6CPNB3LbZrYeQjG8%2B2Z7LrJym2RDAe%2Fe4tYJHXmjFirMX6o6PD7nSFRL3ErA50ZrpHvdtBf8uCYeL3v0mBSa8GtkGnvgE%2FQP3Z6xIXMXWf%2F1PPdFkkAhoo%2BfuuSZhrDVhTnUHnBZzZKbV2qIWO5OD0P%2Fld9eOLOs3VEhvLkYiv4gWB4bz0sEBNznU%2Bg5wiHCS1NPXfNtwrPQ42BFA9SFfBYzuFsmtIFPeQWN%2F95cB9gG1iaW70SrMkr156VZdxOugf3uHNcJLfORdLZM0hmqZWQYbnQoYJ3aoiZuYED7RGGuqDhY0tZApZGja%2B8SRudMxPyBXgQyGtCW%2B%2F3gg6zQmoCBBL1a5eAv2gwu9JDw%2FUd70aFMGDtwfV4IDktmRS0SJdudr2zP%2FCMDbi7D7hHLYKGMSUVYawDY%2F%2Fy0cI23NrOlk9afQvyGtRcMRWihOAL2nBoaNetpEXOgGIMuJALdrjmGzmPKsyqY%2Fx1W3Ri0x29lzXn9Umu6sVLngVJezPAvev9m8%2F0teD3Q7om9X%2FiIMKn%2FndjPIPI1aEuCfTh%2B7sFGFVPUPkP3Z7PiRQPp56qI%2B4k%2B3v0J%2FGnpr%2FY%2ByuTHskEjx3TMBSUfQD2igN1cSgakTeM0krEm1YNyerSk%2BYxgvZfUUmUTzl35sKkQ2%2BbrrhVNXucIPdt5RFm%2BRq7jCfFPOEg8VAr8TM6p6Jij1g8fc9J5K7kGKbQeniCjliWYwZx69HMUrBYuBJlyxFgtWlGTYiyohlFYNWap%2F8UMeTUsNypsppwjghFZCraFlwWMM5ahrt841f%2BlSPgJWTE5xaRXhRBKJ5HZjcM669QJlJ2mhcRFHUvAwDShRmqZY98rGNtPQy%2FlR3QTHhXSYJqQDi9AIvVKkG22zAu9J3mupX7S0d454NzYX7w%2BEc5EwiI8fRocnGeGFlTdEu4KwWSVescGYEDamq077kVyQzbAv9UWT6IdbE5LINdFujsuHBBOI%2BzJOub4DQPySETPx5oZxP1uj1furbKrCer63dbYCbHMRrWQulmkqkISjfx0LZlmw84C2vE8H4M08ybQpYTFQtL7ygGnVr%2FPncf6L64PSWg9VL%2FcYq4nOQtSWt7oKEO5%2BCvsf4rtckN2JklrXtDn65oTdQ86fwA9X1x2MmWSeHm3Dm%2FvohNIhi%2BWIF1rHp01fyGN2y8A5v%2BGX92BDd08v52g7e9yvjbzYh9DyEkUnAKDfQn%2BYgNkub%2BZ8S3Yy%2BBiMyppWGs6ayPA0WMX1Xt9e7StUIeMNv52YpMfm5ljPDCvNdrn7ZPjeZQYzCDSIxudT%2BJQIiyxo4aOqZuAo7Wd%2Bd5Id4%2FuSJOg%2FPkHDqcj9GwuDIZ1tIDrqtTGKI60mS4dCrUA8CgYywUxUvhjXMrYDofv3PgyY%2BBqdPWtQDPadSgKnAci4iwXkjwPuGu9Mt5orRWhtVj6cD4V%2FNe%2FZ6GRuDWIb%2B6FbA1T3xTyt8beLG%2FPgYSQkhILbd1RwwzUc2%2FFJOvpofDYqGoVsRm908coDwXL%2FgGTTSXdqtN160b26ZSjfmBnjehT1rBrceOjNQbsT7pUZ4xNWUWL3Ng0VvLl3%2B3%2B2REaKThCoU6Y1mh0yfNwS8ruMyzXYa4vrthWMvBZ7MbKBC1eBuPX2HcnFVIICsDehRUgVHrRz%2Fa2aZFKblp3hPa97ZnNMmmXHPrMtyAQ2CFVubO4rksUQrMKM4nS9yCTPcOCIpJP3K6OWmYK9I87LeX6%2F6MVvICRGI4b3%2BZUubd7ZuKZR9zEOJm%2B30r%2FUY%2F%2Fe7Y%2Bu%2BEPJGU%2BYxhAbY3iDz8XlICfcHFwB0ZIQ6OZcAEfnjoxubkqHa5jEN%2BwgKDpLLnuW8PRO2bBuPZLllPgKGE9nJLWXueZ6mqec%2FwuyzNnaCAMg5m9YMayULXSSSVAROu1MaVGyYwARO1%2BzM11tRcG04QytpUr4wUebxDquQ3xtbIcItfDdUP03bru75Bnew4uL1Qch1vwjMa34BxvcRzI96mTP4Kj4JnAKIemX608anRjwpsKgPfidNXKR5%2F7P9bX4U7ffO5YUzWUM72EmbqUNqFFbZ5%2BGptBghWk1zHDLnYQXqtoVdvXB8z3537ynq%2BToPXniaPOjPQrURyucsCs%2FsBRjs%2F%2BltfD4Pp7aEr6plDJddJ2t5zo3JbwzqwsnOatkauSMRxgyriBr%2BLfjFvri4jeS6dF48FNoJUSyfN0qP%2BRJZXJdyzqNbPNLCXaeVx3koDZvtkzwx43O0BTxrrClnWt5isJRxIyoPjlJh%2FYaSY20eH%2F6ZSrExRrumg7h0ZSl6MeevZEBXgtqsMd%2Fg%2BElnoILU39ZZ%2FNyyKoE9Bpg33puvAJMcBQUPSn5pfdMU2SgijHuqiFVbDGBrWANgOoagUJEYSJxzMhMiA4R8GU1a2n9abn%2BbdIB3Jvvr6Aq3mbDwHq200oIXn3W56xbYF2KxIaHpi%2FAtXdYyRJjai%2B7%2BxfmKptGysUBrg8VkD00sKJ9d9mwJIfi8%2F54aZNGvikm%2BkuGzkvf%2BDWiyW7uD7Y8dqNGK4qgNQBU0YpS2UwJ8IrLPupq9sEaihDvXwvU%2FCjfC9Y%2BDdm5zOaSSqD%2F712ZWkuc8CNcW4BlP5Ikv9ds%2B5idd9IHdDtgLPQSRi4ccpKh6puBREZZhnnOoHHPtk2F%2Bou5epZoejDEJzvnNXwr3ISZm5F9kr%2F1msoqjqBTj5BQm2ilMSLabQmACplyZiUNLEPlwb9QPUYHfTVV8nzRTEj4U0i7TeY4XGU44fkyCPPR%2BWByoX%2Fxa4zlo9IY2XGg%2BxGkQW1fT%2Bqj9oL7MR9vvQKsLtcW3wVuMuMXkNQmI7xJm2uKQ6%2FY1%2Borii0mE9zCXrn%2B0kljPdyt2S03CbZFRBCwpPJmOnMEEQKQsyNnUP0xS9VvE4iXlDjFM%2F3y46HxKMItzQFeUxKEYWeixMZMiz0Kod9itXtysWB89s8yiJX7NHQoYyPoQKFQG8zQedehfVRZie2XU4yHO2lmUm6nO0jo%2Bzv4%2FMP9RmjHVQjRng%2FBKkePtGM3i5y3Q4GlHxmqFECQMS8JjSV%2Bla2zEd8%2B2zUIi7oeX3GpNMNbup9WCu5H%2Bwf9MzB%2FiXgNpjCqoB5ywbjw2DHgBXJ0cABozL6kwCG1v6orLluX9NnVBik%2BOpZwEePJfVYKL9e8wG5ysgJJOxvNHVDxaE5lu%2FvpmvkSjKtJWlVt5j0rWVZs5z5L0khIXm1dFIOMS8cnh95rIzumd9cg8jPwUpvFX7Zgk%2BVTNGVNOrqgX4gMHvbwoKbSIKa41bxwannY7BD9sjLbqIIfbcL%2Fe386Mo%2B0oLySfRlGvI6EczARlefkqtUJbw%2FyEry4e8siFNfmgj7w7mC%2BQfIr1hY9GJbKY5GHvIVOiN8PFaIjY%2FI1D03euD5ajgqJS%2Fjns0yAtRSTZawmh0CQlHhmaxrD%2BQ4ZK8xeGkyP1FHVQCpqppu25ky1%2Ff2dXrUqcLt9eX777ENVdWnLd9FCleDWDp9%2BTDj62d%2BRUn3vduL5wjMjQHlXxyG%2F3fxHOLZLYG1ZKo0WbuXlPVcOteYazervLTEAc9QVO1wljmj2z57zhcKUwCh1MPtaGTNrUPKdlBhvNiSicottxEh3O0JxBFbNn&csrf={csrf_token}&sessionId={session_id}&uapifpd="
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
  'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = session.request("POST", url, headers=headers, data=payload)
print(response.text)

url = "https://signin.aws.amazon.com/metrics/fingerprint"

payload = "name=IsFingerprintGenerated:Success&value=ECdITeCs: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&operation=AWSSignin:FingerprintMetrics:ResolveAccount"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://signin.aws.amazon.com/metrics/ajax"

payload = "path=%2Fsignin&ajaxAction=resolveAccountType&startTime=1713813554412&endTime=1713813554740&statusCode=200"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://signin.aws.amazon.com/mfa"

payload = f"email={email}&redirect_uri={uri}&csrf={csrf_token}&sessionId={session_id}&rememberMfa=false"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://signin.aws.amazon.com/signin"

payload = f"action=authenticateRoot&email={email}&password={password}&redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&csrf={csrf_token}&sessionId={session_id}&metadata1=ECdITeCs%3A3ar4TCtYcVXmiWTNkV1UhcEWzZki70vpvSoPRl42U3SzdZIPOqJ53BIFSrql1IcBdNnZDeVJ5m8mrWVx3%2FKAwgr5kUxGILwGa8au9IDQWC%2FazzdmwwbGEWN6tgjAU8kqnmxc69yiLA61eIX99Gqc0yxNAS6xB3HEwSs6s7SvQtVGk6uBLnE0%2FIKD%2FLJa9o9cwEnURrt5l2KCKWBK2yzn0CYzHJpc60fZ%2B%2F6YcFchGj1O4X%2F2xRhnkjSA3OC4VI6hxIFm0oKKaN%2Bvvs30XLhw18soVP8u5mmBGoDyJB%2BZ5yJeJ%2B%2BEH4SxxkNAEbPCoKhom8rvJyzKb7uJpX7dpLzbY6XEc8P402tw9DEMP%2B3MS4cKvVrHCBMO40f4aLStoZoozoUSweEleIx9ixTvNZdKy%2Buo2d664bwEo%2BneaMFROt2SNJYBvY5kqEv9viIM1NmgvmJVZFKHb9MdBBfURuxMdLoGzQFwJlbhL1vJa8PwJlUPFZGl0gg0G0QVzisTNYe1mWo%2BrPDwGZhVWRffeISGeoX6ySJVJWt9CCFPzOpqlFDAQV3UTQbvcSTTGT5g8zkwupdESZNerIbr%2BHPVGu4Co1Q25X1f4xII32RYJw6G5WR1aFSs9u4Li79eW7U88rvI6wmgJHWEANUORjUv%2BJzoyKWMgBOVwInYrAzgVQzJLAj8%2BA8bcdlVKmDLkaIwfh2B%2B32Oa1ultHfixpLTL1TpFFTiEF70wTCFiD66CD7RyckpVspqnKFIT0haGenV6ldgSY2cwoyzAGm3DR6oWjqFje60tBpc32Zwl%2FKlP64Oy%2Bzbr1oYKtS4YYeS3IyE%2FwIz0ermvTMKvGuQRD4EvgnDn8Xk3A3bY173TM6X29LaDpZOysXwhJO5v5OTvvZcCYY1QOqcnEKEWKCVmp2KQubSlNlNgsFipMLE8BcvkL%2By7QPt0%2F%2FqujSQ%2FtFW%2BPCuu%2BiWVsuej6o7guWZAY3o1z6Wj8Ck7Y9D6U1zuuNI4KrV5uTzeRLm77uln%2BeD7Wr%2Fs1wnja3tNvWhqPp0LM20K4cJ20pgjxN6gqOsOtDCvr8WtMKvK%2Bv72EUZC0nFDA9ZyXdQSbEeiHsjWtrEmkro7l6yM90EDo40ZmGxijx2gmWjduMzEOgo9pWAz5mhGqmPhFmHsnYsZicOR77xYCxs%2Barr8oiMEsYcM0hVvGJNNMptAnV9wF0bT2MSIHIw5vbGyCI59uus%2BjEl3v%2BhXvHv3zCagB99apovjXX452%2FJDU0I3BxpPF%2FnyS1JdkeflYjcSnI%2F8%2BRKL7G%2BdamHU0d5N4GW2QVKuDD%2BwJ8GE8HPdnM9qNr%2FCHVjgCWhEd%2FyWWtvvXvlCVjMAan4pPMK60LGg%2B5Nc5%2BlQxGQgVXI34MuebtFDkOvHFhoFn8YcwCqL4C0IqvKlwBOI59vdAUjPoM7hk3M%2FPUG2MuOaHhuPvMXElo1zhHqvqRqp9Nt4iZxcKtZeBayAgVMHJcYZPNs40OaJRD4svzcrOrNlvtAXSg9X34inbjyJY%2Fd9kv2%2Fowh4OI9EPe3bWwh8ijCEGWtCoCCjN5GyqWbUwekGzL61EQ2N4JyhPfXugAsvgfXou2B%2BMU8NoH2nM2iMQEJ8qPikfZJgkxkGPX9ipXUz5s77kZ9EdeOMl4JlYM9ACKu9notFbmLScswK0wxexWwoohLRqxor8qYjY%2BRpRGt8Tc8MxVWDVg52IH%2FTqax6dsyIDQf%2Fw4no8EzIjBjqbNKrXefJDooJL7h4UEe7csyqxYq2sjwgxS2FUelI8D9PbNgt9%2BAYwsa2TRxGxmJbRd0PdYSlvM9kUci2c1IOUW3BEj9A8oOsNBHoIneq5nZVwQ3Qiinuj49aiDyeD%2FpJkMPOOT7rnZzXTU5Q5Bldf9pnHfmaNnVOpsKmzfypCfhPo6DffmNTTYDkI7EyOoU6PEZxqMbIHe0coudRqMvSHjqESoi2ple2BuCc3TIjizJFHVj4tcCNhXvjSrTG7%2BN%2FXA2kh%2BY1FUTWPmjLdoRyU%2BqSohjI%2FnNEjokGQ6ub63LgbdLM1ay%2Fu35RKL7vNpKuBl5j0UxS5OncBHXL3Z9mFitAf%2FFddpiOsAJTji1UMDhf3O1XW%2B8s%2BWY6joU5vO7yqMJcWWbdQ7d5qFh8DA1CrKjAbMXPVzmi4vVnXrgRwatsWtYuDkIMekTsli7IsQJkexziLtISrk6KoFi4oXo1eEwJ6lV3721b4NTKoimevYNtmOLSk5ycwdKNx3KYkEQFcPScQaqfZ0zxGq2G7OUR5NDLtTSiVEimk%2BWtN2q1kh%2FhqJOaLRQ2F8JHp58eJ36lmA0chgDgVxDch165o8F6sLxtemOmOy9pIw1YbRKMxsJca71PTs3XFIn5Sfvo%2BHnRI0Z2eAKGw2Ob7Xk26xmKiDw0lPhqQxsAtyz%2FupbyG9vbTsPSzgJsZPTuY2EZJNNRXTKKi%2FTkSlv4YIf8WglbTjJNqzbIoBRidDc3yYibnMQXgWRfrdTKigLSSht4odSXKoWso29f8w16gGMlERC96dWvIJgjNEKls%2Bw4If4OuVQnqv4iBg2pbz5zm%2Bp69EScVMLl5HgvIcS3lcUTrY4N2gt7EnkjcT8j%2BFBruiAt%2BU4qnXbSeRTBXIpiMAIv3IU10naWCwCWAI3AyHVkApIejcBoaJPLVLbpUeo2Tu65Lx5nJGTeqxCrtdIX3y0zcCrLoS1Gbt7aVVsBYdf63yCtiyZz7S%2FcylEN%2B7rwCWuxBPhgTHgU8q96PeXuAzlL2eTC5bgUp1BcELz6NQssg2t6JsfoeKiCd78Lcvsg1B0F3wb2FtHphisPoTp5VXwEN87jWc80lBqjcSpyurSsZOtmek0tPqJPpddm%2FPuya2fgHrhuhw%2FcAYkhXDjlSxrSixWW8eSIJsrPK3BMhyoZVI0J8etABPZTmOjWbjJR9DRdWCsdTIWNZKmN%2Fz%2F6jRSA2Kgt%2Bt3RNnJie%2BgGhbY2D5tqxb%2Fvi0ZrIgGqhQ0hG3kKCCepXvwlKqNVF%2FbAVYtM6H2TUIYRQwqn34aAA%2BUIXOMQVgvjIYGYJWBFaaUHQIBJRR2ICdhLoJfdAal%2FqxGatlN1Jte2m0s1itVHyg%2FosVm6pFEQ1T%2Fmk%2BYVwH2TL4FDQU%2Fpf1CGR7OIgFLEBCv75etbV%2BG58hyX8Onc1ElvRD56sEoWSI36EYxYtF3F%2BYzRP2vihmlAwvD%2B%2BFAQ4jA6gtcmkkaQkcJ7Z4hLHRXEcBwQVegyRirL7jT%2Fx1d0Cqy4ZNgWPdxuu26i3PbbbWx8jGNm0CzOITrLdeebwRTxoh6y1zr4wycooUPVw6K3oB4qdHqE%2BCN3luddLnRlINa3RAD3NnTlDloXqnGWbdz6mfCURdACtfWGpfHrz2G79mFEsv4E04oSV5icOEr9NyguwmoCo8SJnY2F%2BQEOOszjoZctC2SXnnduqhQfKdoUOxK2pFuG6lA8HfAPE1wi6Gv5UKiqNGpryORKNwoBtkvyUa%2BqWXRIG4O%2BanvkveJkgDCv6YPj97YBfyK%2B0aLAv42jJKhmR8ltMDtVyek%2BO2m0tCEHejGY8qC4%2F6XIN23cScZnbABkCGDO%2Bhf4ePDTlwGYaY9x4qgPvKL9Tgxd5kQlURK1ZXhEZIxM0DoZ3NU1Q6%2FdOdfpGzRAyV2tdD5e00U0CZWvIsnOpgzV1Qy7z5%2BK%2BUQcJ7qvd7Kt8w5yrdd5d2QKzsdWJaDjLqGPZEgWKdQc5uzZpV48wNkeIqVsEc%2FxPce%2B0znj2b6txznmNZURgasrQes3YMFfHMPC87mpXmf89IKE4K902F7fgoYzlBi1giIi9Qf2j9DTRPLeDKYcouSnbpAl4GhQkddUxH63M461IWdyuAmuGUgCmCf6Q57cHsmYjX6wbzOG%2F%2FoZRU2ApEibueC3BvETsyybhK52Cs8FltANpM%2Fy7%2FUWBwb1UffbMEKsYnDerejRbr7vQ9E%2BOrzeb1%2FcSrEfI7I%2FwssPP1w7WiJhvvr3vHMfuFagqHmYYuRIy7uEVgcVWYIsyETzDluoMUV1OANFHC6cx6jCxN4XShfeQBddHL%2B4i6iiZnKFdYtmJWKPGW6jbxCdH%2FP9TfaO3piywvTy3DpGnFSOKYEO1gLI898tL%2BqZ%2FKMdQTqa6Vd9tW6peHqKH7xAg7SJhf0Ca56JTG3AwXRZPaSJMen%2Bh%2FxMX9v%2FEeBHyofrUxlZQs7MLnjhlm18EtiL2WPd39zr2A8jfmH29b7kNSe3sn6bU4DIyrAZgsjKoOCK1%2BEV2k4f7tV%2Bc52WDDQsRo0cKZ8oTjR6a5Rdr%2Bz5FrUkaDQQI6KoqlIXsOYHWhdinWfbG9ttzZZuFT%2BvxzCd6LMUAXQb%2FpzS4Bw9mE8Nch6e1bzdIhhcG2FZpwleFyycTnuKvXG9bTCpi%2BChY1eHLPicayJDg0%2BzH53f8OcpHtipBXyx%2FKpvnOiZ9%2FuIco6TZXxqkUx03v%2FM6I95%2B%2Bi89Vy6T6RWpC5mlOZXEL2waoPEaPhRJbN6RXGuj9Muj4l6jQkvBF8Qdp66PaX8YP7ez2dLLFYZeQPfGmOTWH0rjxVGjhnf1RVKVIXX2UZTL5rT6DJmt8Rom9V5TZVBi9QCp70CjtDmfAJctK1WUfTcgJ%2FzpGmQ3GNPTWcAUJvpUtmGCXvBkH6oQO5bPQEp5duPNCw6GdUa%2BTXZfe2BJdHLg0T66NG2uv9%2BfjoxKbKyG75OkHlhzpHuYgJv1HbWCCuEJLX2Qog8V6Bu%2BJbvS1WWxZ2unhwxPvFw1Gp3z6b3JusAmhdZngRlIp%2BAKv3wtszNmiPMxUaUT0H5rA9iOdfZLJKtxlLoGTxvg7pt6Ul0rOnH2zCOnYsfUG9d4rBNTQseR3uM7dZG3vyULwuRlrnBfYupvGKOhkY1LZo6qNMSP3P6XC7vejM%2FMDUnWZuVQW9BVgtGlDf6%2F87bT2lV947Jjo7ALyMtgXhWEQ4WdOUyPZnf2OSBXdAI%2FGQU8mIEapwb82uRsEnEhnzLLb5PTJZiZTJOQ0XKTiiBT1nWJdppOEBnuFOFPF0jdGXylLV276A%2BL0TxNVLp1tZHy48RGTBy0vEL7RDrmtFAP7kqzTSg7q%2Bat2hmoJqr3PA4izIyQQsPC6yamZitEzhA5p%2BrCVOrSL2iGoGmxbfpU4R2IkVtWce5QJzYXsJSkoZlaW4%2BZk4wIqFLbHbhEw6rI1%2Ft%2FzLMtBBisdr0lyLkyNuo6bpIKwIYUAzkN%2F%2Bm7p%2BJec%2BOXlHO6VZdd6w9jLD%2BLdxWS2M5cFr7t7rgsMl9CTaBhr2PQEiwaD0sMHxVNVoe5Yj%2FoIZx2DDxnSW7KiC9s8P%2FQ58yH3mxA19Gm4bU3sxnRHlVA5Y3jXzAafOgy62aE63gy2LtFgWXiq1wcDt6w8KaZZo9Zqbu3R9Pys31tRkSm%2BitNURMObv%2FyQaRCacWKMHONpq1h8Z6bWHgGwzw5lJoBNbqMZ8Q870SgKZFSAgrMJk0h7XSGcK5vgnur3uL33aYdT%2Bh9MpdeKX%2F3JyUxjSi4NHrRLqKfTmpTraJpfUftoDY%2FE4nSSTrzu6%2B%2Bt2v7JiocAF%2FgRCdlaLzzO0BvlFpPWfgIf7iRjEKxDbU7z2gYmgSzXI2ROVRCXbi%2B13PZe8%2FE%2F3PXAfM3JYktz7QT4kUzsxQg%2BPK%2FMrF3s2Q1ZB9g0p7%2FQJqKe8g%2F%2BNSNlakDea%2FC6eEChaqZUdV2eF0UUUMabuKZzdereSnPq8TAB8qvWipa9n1jvRlkgzeRfgH%2B1tWXbBDIYJYPyQSCt%2F3J1HaQMcMBnyJ1TEY4ty4aC5lWuFMk96TY31I2sMPifbwAVWZtklW24nP9Th2hO2oBGZp%2BfdRc7g3jW3M1KaTTjChphDhMj6mn8o12yuxih1viJZJZp%2Bpegjtipfj90quopkMwH8bdRMXW%2F6Y3jCp%2Bg8X8eIuOHuQ6aZbrof2JrJZ1zTC1Q8AAcOxqiBQmphWYNOu%2F69ChdIoDzED9msN4IxSt3V9lpHd2kttVufaGZBmCL2omEyWb7ZZ95jiG8qEEcKOZM6bOX5Ni30wVOaW0hPQmhzmV5aMpRzMlhRJZwR8i0n%2Fwbburepkpep%2F0KFhJezJI2KybNjhck0Qe9yvuXTMF8%2FaWESIXZcFd9zAOapLPe6Ib4JZuMCSjsoXK41vwLJ0c5cJw4uyjHllr7068YUcFTdhrVVSiYh42o%2Fon7UJ1F55nrEkbwkSOOVFJFU5hoDwig7FOR4lLTu9ENrs%2BIPfhAs3n0ju0FXeEv72mnFnrkDLqCFePU5TS4%2F7UQF2eqFUnHQ0dMdHkGnbj2U3w%2F%2BfbwJk7NJ2iWBihB%2FzvyAltfT1zf6sxJMmWwK2yqIi2JYOYt7PbcO%2FNCnPgiybt1kK9OQUqaYxbxtOCCpIujvsayTgp1S7w8bDIg6%2Fy1abT%2BKFEbUTz693bgZiIh0sRgHs%2FM5ta8cfVK3XeptKOaFJH8wX%2BzBhRbuPJDfhDRMFppQRjVi2%2B8CA5Ygom%2FTETEOhITglL18ZZP1ecPsVC9BDw1zHLjjHFp41mrPQT1UW8OX%2FjjD9pFbpktACPO5JXePTbd06VmoOHfSmg3%2FoEo72LbTVF2I7CqG2xDTNnGClMubfIAhcj%2Fqk0hfhxgCnGnCP8Otiu%2B12KJDQgel7PoBYUm1nF8dXX88r6dK87zTWwKZBY18xvqb6QOKEZs%2FSiXBJspnuqEapKR1LYIInRSLSUv5Lz15Ne6C4LeFLdPxk%2Bw%2FBBW2aABuipRtb4m9qAMEhkgOKYLk8G6cwVC5zLTZVD%2BcxkmF3p4BKUuiAVhbH4EBVdN8zzENThPK%2BFfJebcmGIxktucogSaUMEcR2ToNWCgdwzOYOGlSkbRroFiKNGxqV0HoiyM4gDDzIMvJER8Nz%2FF1z8GGAZ2lFH6kqmsj2FEy6Odo%2Fv3m4r%2FRN5KTSR3ZjBmLNUA4ZaMH3R%2B9j74QrjBjUBFIE1Zvpes3Nt9omVEgPgr28QJtAmP8rI4AmDlTaD2lQG2cMegM2SjWz7d4JqXcUYpqJAda8rx%2Fi0wC5KbXzpGGeaAyi%2F7PdB61G%2FChkUlYuL8wmgADn530CTJ6aNYcyG41YdplB7%2BoELDybG%2BR%2FyxRVZ8UE0%2B8rSlQZXWY%2FpHgHuKmm%2FD2uTwXzGO4UPcLppn2WaSvlRJqTif%2BiC4nSyGqu45gOZt6nWwSd2HpGg6Vm8RPCXItBa%2FW52YLRpGPVMrz1hj19Ox4Kl4ff%2F3QN7GkXdirllvTQk4dsVN3DGvnyE7dhGi1Zv1QkE6eEBHxi8d51x8WWqM%2BvGJQmxuYOTO%2FfrSR6puPy%2F7Rn7hGfGbzbPngIePILsWsWcxriHp4s0Zx8R%2B02MGw3%2FI%3D&rememberMfa=false&code_challenge={code_challenge}&code_challenge_method=SHA-256&mfaSerial="
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
  'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = session.request("POST", url, headers=headers, data=payload)

print(response.text)