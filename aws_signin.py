import requests
import subprocess
import json
from aws_metadata import encrypt_metadata
import urllib.parse
import re

email = "dlwnsdnjs0810@gmail.com"
password = "123789Ab!"
session = requests.Session()

basemd = {"metrics":{"el":0,"script":3,"capabilities":1,"h":0,"gpu":8,"batt":0,"dnt":0,"math":1,"perf":0,"auto":0,"tz":0,"fp2":0,"lsubid":0,"browser":0,"tts":0,"input":1,"canvas":8,"captchainput":0,"pow":0},"start":1718718881990,"interaction":{"clicks":1,"touches":0,"keyPresses":2,"cuts":0,"copies":0,"pastes":0,"keyPressTimeIntervals":[2],"mouseClickPositions":["184,514"],"keyCycles":[2,0],"mouseCycles":[112,76],"touchCycles":[]},"scripts":{"dynamicUrls":["/static/js/awsc-panorama.js","/static/js/signin-helper.js","/static/js/metrics-helper-jquery.js","/static/js/constants.js","/static/js/password-manager-helper.js","/static/js/panorama-helper.js","/static/js/common/load-globals.js","/static/js/common/request-parameters.js","/static/js/fwcim-cdn-prod.js","/static/js/common/init-fwcim.js","/static/js/jquery.min.js","/static/js/u2f-api.js","/static/js/login-root.js","/static/js/performance.js","/static/js/AWSMarketingTargetServiceAnalyticsClientSignin.js","/static/js/common/init-marketing-analytics.js","/static/js/panorama-nav-init.js","chrome-extension://pbanhockgagggenencehbnadejlgchfc/js/pageScript.bundle.js"],"inlineHashes":[-688792631,1198914864,1612960339,1456104868,321474291,-2101725796,1138188723],"elapsed":3,"dynamicUrlCount":18,"inlineHashesCount":7},"capabilities":{"css":{"textShadow":1,"WebkitTextStroke":1,"boxShadow":1,"borderRadius":1,"borderImage":1,"opacity":1,"transform":1,"transition":1},"js":{"audio":True,"geolocation":True,"localStorage":"supported","touch":False,"video":True,"webWorker":True},"elapsed":0},"history":{"length":50},"gpu":{"vendor":"Google Inc. (Apple)","model":"ANGLE (Apple, ANGLE Metal Renderer: Apple M2 Pro, Unspecified Version)","extensions":["ANGLE_instanced_arrays","EXT_blend_minmax","EXT_clip_control","EXT_color_buffer_half_float","EXT_depth_clamp","EXT_disjoint_timer_query","EXT_float_blend","EXT_frag_depth","EXT_polygon_offset_clamp","EXT_shader_texture_lod","EXT_texture_compression_bptc","EXT_texture_compression_rgtc","EXT_texture_filter_anisotropic","EXT_texture_mirror_clamp_to_edge","EXT_sRGB","KHR_parallel_shader_compile","OES_element_index_uint","OES_fbo_render_mipmap","OES_standard_derivatives","OES_texture_float","OES_texture_float_linear","OES_texture_half_float","OES_texture_half_float_linear","OES_vertex_array_object","WEBGL_blend_func_extended","WEBGL_color_buffer_float","WEBGL_compressed_texture_astc","WEBGL_compressed_texture_etc","WEBGL_compressed_texture_etc1","WEBGL_compressed_texture_pvrtc","WEBGL_compressed_texture_s3tc","WEBGL_compressed_texture_s3tc_srgb","WEBGL_debug_renderer_info","WEBGL_debug_shaders","WEBGL_depth_texture","WEBGL_draw_buffers","WEBGL_lose_context","WEBGL_multi_draw","WEBGL_polygon_mode"]},"battery":{},"dnt":None,"math":{"tan":"-1.4214488238747245","sin":"0.8178819121159085","cos":"-0.5753861119575491"},"performance":{"timing":{"connectStart":1718718881079,"navigationStart":1718718880858,"secureConnectionStart":0,"fetchStart":1718718881079,"domContentLoadedEventStart":1718718881488,"responseStart":1718718881294,"domInteractive":1718718881488,"domainLookupEnd":1718718881079,"responseEnd":1718718881296,"redirectStart":1718718880866,"requestStart":1718718881081,"unloadEventEnd":0,"unloadEventStart":0,"domLoading":1718718881305,"domComplete":1718718881721,"domainLookupStart":1718718881079,"loadEventStart":1718718881722,"domContentLoadedEventEnd":1718718881488,"loadEventEnd":1718718881723,"redirectEnd":1718718881079,"connectEnd":1718718881079}},"automation":{"wd":{"properties":{"document":[],"window":[],"navigator":[]}},"phantom":{"properties":{"window":[]}}},"end":1718718884967,"timeZone":9,"flashVersion":None,"plugins":"Chrome PDF plug in Chrome portable-document-format Display JjZUxYUx 1079268BnyCJMt 092692||847-796-796-24-*-*-*","dupedPlugins":"Chrome PDF plug in Chrome portable-document-format Display JjZUxYUx 1079268BnyCJMt 092692||847-796-796-24-*-*-*","screenInfo":"847-796-796-24-*-*-*","lsUbid":"X18-9409049-9649454:1718542405","referrer":"https://ap-southeast-2.signin.aws.amazon.com/","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","location":"https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26oauthStart%3D1718718878308%26src%3Dheader-signin%26state%3DhashArgsFromTB_ap-southeast-2_c7deb11f9096ee72&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=3BjrTfX-uFCz7PsKkf8YeOPaQ5tvvT0NYsHNinme67A&code_challenge_method=SHA-256","webDriver":False,"form":{},"canvas":{"hash":-389735874,"emailHash":None,"histogramBins":[14220,157,52,46,58,38,41,27,46,27,31,28,26,40,41,41,39,23,20,37,27,24,27,32,41,19,27,34,36,25,21,46,26,24,28,23,25,22,34,33,24,16,47,34,14,28,35,32,38,21,35,83,30,17,28,30,24,32,19,27,18,31,21,28,152,11,27,24,15,18,17,17,18,35,18,24,16,16,25,28,13,22,10,20,17,38,18,15,22,13,21,27,26,30,17,15,54,18,45,40,78,21,527,22,30,16,18,13,24,57,37,18,24,18,26,38,16,21,23,43,20,18,24,16,16,14,34,34,195,41,20,20,17,14,10,13,21,35,18,15,19,13,20,43,16,27,59,35,13,15,19,20,14,89,9,15,30,9,46,23,11,19,33,13,44,24,16,32,31,9,30,17,24,22,19,15,16,21,13,26,18,19,28,19,21,28,13,19,22,20,12,136,33,28,23,19,24,21,30,19,30,41,42,47,60,92,31,41,27,53,31,23,28,32,46,29,34,28,34,26,23,26,22,34,44,42,35,36,33,20,40,32,33,39,29,53,39,45,35,44,50,42,33,41,43,63,43,53,34,47,43,66,70,57,132,13252]},"token":{"isCompatible":True,"pageHasCaptcha":0},"auth":{"form":{"method":"get"}},"errors":[],"version":"4.0.0"}
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

next = (response.headers['Location'])

sp = next.split("&")
for i in sp:
    if "redirect" in i:
        uri = i.split("=")[1].strip()

url = f"https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
  'accept-language': 'en-US,en;q=0.6',
  'priority': 'u=0, i',
  'referer': 'https://ap-southeast-2.signin.aws.amazon.com/',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-site',
  'sec-fetch-user': '?1',
  'sec-gpc': '1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = session.request("GET", url, headers=headers)

basemd['location'] = uri
md = urllib.parse.quote_plus(encrypt_metadata(json.dumps(basemd)))
csrf_token = re.search(r'<meta name="csrf_token" content="(.+?)"', response.text).group(1)
session_id = re.search(r'<meta name="session_id" content="(.+?)"', response.text).group(1)

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

url = "https://signin.aws.amazon.com/signin"

payload = f"action=resolveAccountType&redirect_uri={uri}&email={email}&metadata1={md}&csrf={csrf_token}&sessionId={session_id}&uapifpd="
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

response_values = json.loads(response.text)

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

basemd = {"metrics":{"el":0,"script":0,"capabilities":0,"h":0,"gpu":0,"batt":0,"dnt":0,"math":0,"perf":0,"auto":0,"tz":0,"fp2":0,"lsubid":0,"browser":0,"tts":0,"input":0,"canvas":1,"captchainput":0,"pow":0},"start":1718719079266,"interaction":{"clicks":5,"touches":0,"keyPresses":2,"cuts":0,"copies":0,"pastes":0,"keyPressTimeIntervals":[3],"mouseClickPositions":["199,501","349,463","233,515","248,569","243,415"],"keyCycles":[2,0],"mouseCycles":[97,69,78,70,49],"touchCycles":[]},"scripts":{"dynamicUrls":["/static/js/awsc-panorama.js","/static/js/signin-helper.js","/static/js/metrics-helper-jquery.js","/static/js/constants.js","/static/js/password-manager-helper.js","/static/js/panorama-helper.js","/static/js/common/load-globals.js","/static/js/common/request-parameters.js","/static/js/fwcim-cdn-prod.js","/static/js/common/init-fwcim.js","/static/js/jquery.min.js","/static/js/u2f-api.js","/static/js/login-root.js","/static/js/performance.js","/static/js/AWSMarketingTargetServiceAnalyticsClientSignin.js","/static/js/common/init-marketing-analytics.js","/static/js/panorama-nav-init.js","chrome-extension://pbanhockgagggenencehbnadejlgchfc/js/pageScript.bundle.js"],"inlineHashes":[-688792631,1198914864,1612960339,1456104868,321474291,-2101725796,1138188723],"elapsed":2,"dynamicUrlCount":18,"inlineHashesCount":7},"capabilities":{"css":{"textShadow":1,"WebkitTextStroke":1,"boxShadow":1,"borderRadius":1,"borderImage":1,"opacity":1,"transform":1,"transition":1},"js":{"audio":True,"geolocation":True,"localStorage":"supported","touch":False,"video":True,"webWorker":True},"elapsed":1},"history":{"length":50},"gpu":{"vendor":"Google Inc. (Apple)","model":"ANGLE (Apple, ANGLE Metal Renderer: Apple M2 Pro, Unspecified Version)","extensions":["ANGLE_instanced_arrays","EXT_blend_minmax","EXT_clip_control","EXT_color_buffer_half_float","EXT_depth_clamp","EXT_disjoint_timer_query","EXT_float_blend","EXT_frag_depth","EXT_polygon_offset_clamp","EXT_shader_texture_lod","EXT_texture_compression_bptc","EXT_texture_compression_rgtc","EXT_texture_filter_anisotropic","EXT_texture_mirror_clamp_to_edge","EXT_sRGB","KHR_parallel_shader_compile","OES_element_index_uint","OES_fbo_render_mipmap","OES_standard_derivatives","OES_texture_float","OES_texture_float_linear","OES_texture_half_float","OES_texture_half_float_linear","OES_vertex_array_object","WEBGL_blend_func_extended","WEBGL_color_buffer_float","WEBGL_compressed_texture_astc","WEBGL_compressed_texture_etc","WEBGL_compressed_texture_etc1","WEBGL_compressed_texture_pvrtc","WEBGL_compressed_texture_s3tc","WEBGL_compressed_texture_s3tc_srgb","WEBGL_debug_renderer_info","WEBGL_debug_shaders","WEBGL_depth_texture","WEBGL_draw_buffers","WEBGL_lose_context","WEBGL_multi_draw","WEBGL_polygon_mode"]},"battery":{},"dnt":None,"math":{"tan":"-1.4214488238747245","sin":"0.8178819121159085","cos":"-0.5753861119575491"},"performance":{"timing":{"connectStart":1718719078369,"navigationStart":1718719078135,"secureConnectionStart":0,"fetchStart":1718719078369,"domContentLoadedEventStart":1718719078764,"responseStart":1718719078576,"domInteractive":1718719078764,"domainLookupEnd":1718719078369,"responseEnd":1718719078577,"redirectStart":1718719078142,"requestStart":1718719078371,"unloadEventEnd":0,"unloadEventStart":0,"domLoading":1718719078584,"domComplete":1718719078996,"domainLookupStart":1718719078369,"loadEventStart":1718719078996,"domContentLoadedEventEnd":1718719078764,"loadEventEnd":1718719078997,"redirectEnd":1718719078369,"connectEnd":1718719078369}},"automation":{"wd":{"properties":{"document":[],"window":[],"navigator":[]}},"phantom":{"properties":{"window":[]}}},"end":1718719084241,"timeZone":9,"flashVersion":None,"plugins":"Chrome PDF plug in Chrome portable-document-format Display JjZUxYUx 1079268BnyCJMt 092692||751-796-796-24-*-*-*","dupedPlugins":"Chrome PDF plug in Chrome portable-document-format Display JjZUxYUx 1079268BnyCJMt 092692||751-796-796-24-*-*-*","screenInfo":"751-796-796-24-*-*-*","lsUbid":"X18-9409049-9649454:1718542405","referrer":"https://ap-southeast-2.signin.aws.amazon.com/","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36","location":"https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26oauthStart%3D1718719074567%26state%3DhashArgsFromTB_ap-southeast-2_918046f496d85c33&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=uHmAzILqsDGZ68PjQshm8plWKkgY18hS3jhX4e7_isI&code_challenge_method=SHA-256","webDriver":False,"form":{},"canvas":{"hash":-389735874,"emailHash":None,"histogramBins":[14220,157,52,46,58,38,41,27,46,27,31,28,26,40,41,41,39,23,20,37,27,24,27,32,41,19,27,34,36,25,21,46,26,24,28,23,25,22,34,33,24,16,47,34,14,28,35,32,38,21,35,83,30,17,28,30,24,32,19,27,18,31,21,28,152,11,27,24,15,18,17,17,18,35,18,24,16,16,25,28,13,22,10,20,17,38,18,15,22,13,21,27,26,30,17,15,54,18,45,40,78,21,527,22,30,16,18,13,24,57,37,18,24,18,26,38,16,21,23,43,20,18,24,16,16,14,34,34,195,41,20,20,17,14,10,13,21,35,18,15,19,13,20,43,16,27,59,35,13,15,19,20,14,89,9,15,30,9,46,23,11,19,33,13,44,24,16,32,31,9,30,17,24,22,19,15,16,21,13,26,18,19,28,19,21,28,13,19,22,20,12,136,33,28,23,19,24,21,30,19,30,41,42,47,60,92,31,41,27,53,31,23,28,32,46,29,34,28,34,26,23,26,22,34,44,42,35,36,33,20,40,32,33,39,29,53,39,45,35,44,50,42,33,41,43,63,43,53,34,47,43,66,70,57,132,13252]},"token":{"isCompatible":True,"pageHasCaptcha":0},"auth":{"form":{"method":"get"}},"errors":[],"version":"4.0.0"}
loc = f"https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-2_11388c7d3f877e7f&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256"
basemd['location'] = loc
md = urllib.parse.quote_plus(encrypt_metadata(json.dumps(basemd)))

url = "https://signin.aws.amazon.com/signin"

payload = f"action=authenticateRoot&email={email}&password={password}&redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&csrf={csrf_token}&sessionId={session_id}&metadata1={md}&rememberMfa=false&code_challenge={code_challenge}&code_challenge_method=SHA-256&mfaSerial="
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://signin.aws.amazon.com',
  'priority': 'u=1, i',
  'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

response = session.request("POST", url, headers=headers, data=payload)
print(response.text)

url = "https://us-east-1.console.aws.amazon.com/iam/home"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
  'accept-language': 'en-US,en;q=0.6',
  'priority': 'u=0, i',
  'referer': 'https://us-east-1.console.aws.amazon.com/',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-site',
  'sec-fetch-user': '?1',
  'sec-gpc': '1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = session.request("GET", url, headers=headers, data=payload)

print(response.text)

