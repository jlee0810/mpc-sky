import requests
import subprocess
import json
from aws_metadata import encrypt_metadata
import urllib.parse
import re

email = "dlwnsdnjs0810@gmail.com"
password = "1237789Ab!"
session = requests.Session()

basemd = {"metrics":{"el":0,"script":0,"capabilities":0,"h":0,"gpu":0,"batt":0,"dnt":0,"math":0,"perf":0,"auto":0,"tz":0,"fp2":0,"lsubid":0,"browser":0,"tts":0,"input":0,"canvas":0,"captchainput":0,"pow":0},"start":1715822740733,"interaction":{"clicks":4,"touches":0,"keyPresses":13,"cuts":0,"copies":0,"pastes":0,"keyPressTimeIntervals":[296636,51,62,262,194,130,103,8,339],"mouseClickPositions":["420,743","150,429","209,472","99,348"],"keyCycles":[1,150,128,142,75,53,72,153,112,28],"mouseCycles":[983,120,97,104,81],"touchCycles":[]},"scripts":{"dynamicUrls":["/static/js/awsc-panorama.js","/static/js/signin-helper.js","/static/js/metrics-helper-jquery.js","/static/js/constants.js","/static/js/password-manager-helper.js","/static/js/panorama-helper.js","/static/js/common/load-globals.js","/static/js/common/request-parameters.js","/static/js/fwcim-cdn-prod.js","/static/js/common/init-fwcim.js","/static/js/jquery.min.js","/static/js/u2f-api.js","/static/js/login-root.js","/static/js/performance.js","/static/js/AWSMarketingTargetServiceAnalyticsClientSignin.js","/static/js/common/init-marketing-analytics.js","/static/js/panorama-nav-init.js"],"inlineHashes":[-910695020,1198914864,1612960339,1456104868,321474291,-2101725796,1138188723],"elapsed":2,"dynamicUrlCount":17,"inlineHashesCount":7},"capabilities":{"css":{"textShadow":1,"WebkitTextStroke":1,"boxShadow":1,"borderRadius":1,"borderImage":1,"opacity":1,"transform":1,"transition":1},"js":{"audio":True,"geolocation":True,"localStorage":"supported","touch":False,"video":True,"webWorker":True},"elapsed":0},"history":{"length":4},"gpu":{"vendor":"Google Inc. (Apple)","model":"ANGLE (Apple, ANGLE Metal Renderer: Apple M2 Pro, Unspecified Version)","extensions":["ANGLE_instanced_arrays","EXT_blend_minmax","EXT_clip_control","EXT_color_buffer_half_float","EXT_depth_clamp","EXT_disjoint_timer_query","EXT_float_blend","EXT_frag_depth","EXT_polygon_offset_clamp","EXT_shader_texture_lod","EXT_texture_compression_bptc","EXT_texture_compression_rgtc","EXT_texture_filter_anisotropic","EXT_texture_mirror_clamp_to_edge","EXT_sRGB","KHR_parallel_shader_compile","OES_element_index_uint","OES_fbo_render_mipmap","OES_standard_derivatives","OES_texture_float","OES_texture_float_linear","OES_texture_half_float","OES_texture_half_float_linear","OES_vertex_array_object","WEBGL_blend_func_extended","WEBGL_color_buffer_float","WEBGL_compressed_texture_astc","WEBGL_compressed_texture_etc","WEBGL_compressed_texture_etc1","WEBGL_compressed_texture_pvrtc","WEBGL_compressed_texture_s3tc","WEBGL_compressed_texture_s3tc_srgb","WEBGL_debug_renderer_info","WEBGL_debug_shaders","WEBGL_depth_texture","WEBGL_draw_buffers","WEBGL_lose_context","WEBGL_multi_draw","WEBGL_polygon_mode"]},"battery":{},"dnt":None,"math":{"tan":"-1.4214488238747245","sin":"0.8178819121159085","cos":"-0.5753861119575491"},"performance":{"timing":{"connectStart":1715822739605,"navigationStart":1715822739174,"secureConnectionStart":1715822739607,"fetchStart":1715822739600,"domContentLoadedEventStart":1715822740230,"responseStart":1715822739827,"domInteractive":1715822740230,"domainLookupEnd":1715822739605,"responseEnd":1715822739828,"redirectStart":0,"requestStart":1715822739742,"unloadEventEnd":0,"unloadEventStart":0,"domLoading":1715822739834,"domComplete":1715822740311,"domainLookupStart":1715822739605,"loadEventStart":1715822740311,"domContentLoadedEventEnd":1715822740230,"loadEventEnd":1715822740312,"redirectEnd":0,"connectEnd":1715822739742}},"automation":{"wd":{"properties":{"document":[],"window":[],"navigator":[]}},"phantom":{"properties":{"window":[]}}},"end":1715823049063,"timeZone":-8,"flashVersion":None,"plugins":"PDF Viewer Chrome PDF Viewer Chromium PDF Viewer Microsoft Edge PDF Viewer WebKit built-in PDF ||1600-900-875-24-*-*-*","dupedPlugins":"PDF Viewer Chrome PDF Viewer Chromium PDF Viewer Microsoft Edge PDF Viewer WebKit built-in PDF ||1600-900-875-24-*-*-*","screenInfo":"1600-900-875-24-*-*-*","lsUbid":"X19-1633319-9437254:1715822740","referrer":"https://console.aws.amazon.com/","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36","location":"https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-2_6ecbe5b4d8a000a5&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=VJDhDlwY4ijqqTiHv5tmRAe9gLvC_XJkX729xp1gJ3k&code_challenge_method=SHA-256","webDriver":False,"form":{},"canvas":{"hash":-615056301,"emailHash":None,"histogramBins":[14330,43,44,41,53,35,36,31,63,38,24,26,25,37,36,32,37,19,24,40,32,26,23,29,43,22,29,27,43,15,25,36,19,20,22,22,29,23,36,33,21,19,46,30,14,24,35,35,35,30,42,72,29,14,32,27,24,26,21,23,20,36,18,25,153,15,25,28,12,16,18,13,12,33,24,23,23,18,23,26,20,21,10,31,19,41,15,18,24,11,19,31,16,25,17,16,51,24,40,40,75,21,526,33,31,15,16,19,23,61,36,12,20,23,24,40,16,18,25,41,23,22,22,13,19,20,35,31,193,42,26,16,10,19,13,21,24,35,18,12,17,11,20,37,17,31,58,33,19,16,19,21,21,88,11,20,20,13,46,22,19,21,28,14,41,16,10,38,33,11,33,18,24,31,15,15,11,21,18,28,23,17,31,12,17,26,16,18,25,15,12,138,29,16,28,21,30,24,26,18,27,41,42,51,62,90,31,42,30,52,32,25,31,33,49,28,28,35,32,24,23,30,24,33,40,38,38,39,22,23,32,37,38,27,34,63,43,55,34,40,42,40,35,45,39,60,48,47,40,45,46,68,58,61,80,13315]},"token":{"isCompatible":True,"pageHasCaptcha":0},"auth":{"form":{"method":"get"}},"errors":[],"version":"4.0.0"}

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

oauth = (response.headers['Location'])

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

response = session.request("GET", next, headers=headers)

basemd['location'] = next
md = urllib.parse.quote_plus(encrypt_metadata(json.dumps(basemd)))
csrf_token = re.search(r'<meta name="csrf_token" content="(.+?)"', response.text).group(1)
session_id = re.search(r'<meta name="session_id" content="(.+?)"', response.text).group(1)
("CSRF Token:", csrf_token)
# print("Session ID:", session_id)
# print("Code Challenge:", code_challenge)
# print(session.cookies.get_dict())

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

print(response.text)
# response_values = json.loads(response.text)

# ces = response_values["properties"]["CES"]
# captchaObfuscation = response_values["properties"]["captchaObfuscationToken"]
# captchaURL = response_values["properties"]["CaptchaURL"]

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
# print("Captcha URL: ", captchaURL)
# captcha_val = input("Enter the captcha value: ")

# url = "https://signin.aws.amazon.com/signin"

# payload = f"action=resolveAccountType&redirect_uri={uri}&email={email}&metadata1={md}&csrf={csrf_token}&sessionId={session_id}&uapifpd=&captcha_token={ces}&captcha_guess={captcha_val}&captchaObfuscationToken={captchaObfuscation}"
# headers = {
#   'accept': '*/*',
#   'accept-language': 'en-US,en;q=0.9',
#   'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#   'origin': 'https://signin.aws.amazon.com',
#   'priority': 'u=1, i',
#   'referer': f'https://signin.aws.amazon.com/signin?redirect_uri={uri}&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256',
#   'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"macOS"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#   'x-requested-with': 'XMLHttpRequest'
# }

# response = session.request("POST", url, headers=headers, data=payload)

# print(response.text)

basemd = {"metrics":{"el":0,"script":0,"capabilities":0,"h":0,"gpu":0,"batt":0,"dnt":0,"math":0,"perf":0,"auto":0,"tz":0,"fp2":0,"lsubid":0,"browser":0,"tts":0,"input":0,"canvas":0,"captchainput":0,"pow":0},"start":1715828368513,"interaction":{"clicks":7,"touches":0,"keyPresses":28,"cuts":0,"copies":0,"pastes":0,"keyPressTimeIntervals":[2031,149,248,277,554,305,1255,753,95],"mouseClickPositions":["183,497","94,493","224,552","231,469","230,460","212,505","301,356"],"keyCycles":[2,95,148,126,73,149,69,100,64,75],"mouseCycles":[95,86,67,83,67,81,92],"touchCycles":[]},"scripts":{"dynamicUrls":["/static/js/awsc-panorama.js","/static/js/signin-helper.js","/static/js/metrics-helper-jquery.js","/static/js/constants.js","/static/js/password-manager-helper.js","/static/js/panorama-helper.js","/static/js/common/load-globals.js","/static/js/common/request-parameters.js","/static/js/fwcim-cdn-prod.js","/static/js/common/init-fwcim.js","/static/js/jquery.min.js","/static/js/u2f-api.js","/static/js/login-root.js","/static/js/performance.js","/static/js/AWSMarketingTargetServiceAnalyticsClientSignin.js","/static/js/common/init-marketing-analytics.js","/static/js/panorama-nav-init.js"],"inlineHashes":[-910695020,1198914864,1612960339,1456104868,321474291,-2101725796,1138188723],"elapsed":2,"dynamicUrlCount":17,"inlineHashesCount":7},"capabilities":{"css":{"textShadow":1,"WebkitTextStroke":1,"boxShadow":1,"borderRadius":1,"borderImage":1,"opacity":1,"transform":1,"transition":1},"js":{"audio":True,"geolocation":True,"localStorage":"supported","touch":False,"video":True,"webWorker":True},"elapsed":1},"history":{"length":15},"gpu":{"vendor":"Google Inc. (Apple)","model":"ANGLE (Apple, ANGLE Metal Renderer: Apple M2 Pro, Unspecified Version)","extensions":["ANGLE_instanced_arrays","EXT_blend_minmax","EXT_clip_control","EXT_color_buffer_half_float","EXT_depth_clamp","EXT_disjoint_timer_query","EXT_float_blend","EXT_frag_depth","EXT_polygon_offset_clamp","EXT_shader_texture_lod","EXT_texture_compression_bptc","EXT_texture_compression_rgtc","EXT_texture_filter_anisotropic","EXT_texture_mirror_clamp_to_edge","EXT_sRGB","KHR_parallel_shader_compile","OES_element_index_uint","OES_fbo_render_mipmap","OES_standard_derivatives","OES_texture_float","OES_texture_float_linear","OES_texture_half_float","OES_texture_half_float_linear","OES_vertex_array_object","WEBGL_blend_func_extended","WEBGL_color_buffer_float","WEBGL_compressed_texture_astc","WEBGL_compressed_texture_etc","WEBGL_compressed_texture_etc1","WEBGL_compressed_texture_pvrtc","WEBGL_compressed_texture_s3tc","WEBGL_compressed_texture_s3tc_srgb","WEBGL_debug_renderer_info","WEBGL_debug_shaders","WEBGL_depth_texture","WEBGL_draw_buffers","WEBGL_lose_context","WEBGL_multi_draw","WEBGL_polygon_mode"]},"battery":{},"dnt":None,"math":{"tan":"-1.4214488238747245","sin":"0.8178819121159085","cos":"-0.5753861119575491"},"performance":{"timing":{"connectStart":1715828367856,"navigationStart":1715828367683,"secureConnectionStart":0,"fetchStart":1715828367856,"domContentLoadedEventStart":1715828368011,"responseStart":1715828367941,"domInteractive":1715828368011,"domainLookupEnd":1715828367856,"responseEnd":1715828367942,"redirectStart":0,"requestStart":1715828367857,"unloadEventEnd":0,"unloadEventStart":0,"domLoading":1715828367945,"domComplete":1715828368029,"domainLookupStart":1715828367856,"loadEventStart":1715828368029,"domContentLoadedEventEnd":1715828368011,"loadEventEnd":1715828368029,"redirectEnd":0,"connectEnd":1715828367856}},"automation":{"wd":{"properties":{"document":[],"window":[],"navigator":[]}},"phantom":{"properties":{"window":[]}}},"end":1715828383507,"timeZone":-8,"flashVersion":None,"plugins":"PDF Viewer Chrome PDF Viewer Chromium PDF Viewer Microsoft Edge PDF Viewer WebKit built-in PDF ||1600-900-875-24-*-*-*","dupedPlugins":"PDF Viewer Chrome PDF Viewer Chromium PDF Viewer Microsoft Edge PDF Viewer WebKit built-in PDF ||1600-900-875-24-*-*-*","screenInfo":"1600-900-875-24-*-*-*","lsUbid":"X13-7453931-5894188:1715823850","referrer":"https://console.aws.amazon.com/","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36","location":"https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-2_11388c7d3f877e7f&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=doHj6owblxeaqt0EamkVd7sJzXWHxmtRqmShtHCpuv4&code_challenge_method=SHA-256","webDriver":False,"form":{},"canvas":{"hash":-615056301,"emailHash":None,"histogramBins":[14330,43,44,41,53,35,36,31,63,38,24,26,25,37,36,32,37,19,24,40,32,26,23,29,43,22,29,27,43,15,25,36,19,20,22,22,29,23,36,33,21,19,46,30,14,24,35,35,35,30,42,72,29,14,32,27,24,26,21,23,20,36,18,25,153,15,25,28,12,16,18,13,12,33,24,23,23,18,23,26,20,21,10,31,19,41,15,18,24,11,19,31,16,25,17,16,51,24,40,40,75,21,526,33,31,15,16,19,23,61,36,12,20,23,24,40,16,18,25,41,23,22,22,13,19,20,35,31,193,42,26,16,10,19,13,21,24,35,18,12,17,11,20,37,17,31,58,33,19,16,19,21,21,88,11,20,20,13,46,22,19,21,28,14,41,16,10,38,33,11,33,18,24,31,15,15,11,21,18,28,23,17,31,12,17,26,16,18,25,15,12,138,29,16,28,21,30,24,26,18,27,41,42,51,62,90,31,42,30,52,32,25,31,33,49,28,28,35,32,24,23,30,24,33,40,38,38,39,22,23,32,37,38,27,34,63,43,55,34,40,42,40,35,45,39,60,48,47,40,45,46,68,58,61,80,13315]},"token":{"isCompatible":True,"pageHasCaptcha":0},"auth":{"form":{"method":"get"}},"errors":[],"version":"4.0.0"}
loc = f"https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-2_11388c7d3f877e7f&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge={code_challenge}&code_challenge_method=SHA-256"
basemd['location'] = loc
md = encrypt_metadata(json.dumps(basemd))

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
