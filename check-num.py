import requests
# use mobile web 
url = "https://mbapp.jsph.org.cn/mobile/online/GetReservationScheduleNew_H5.do"

payload = "{\"content\":{\"ResourceTypeID\":\"002\",\"DiagOrgID\":\"\",\"ResourceID\":\"0544\",\"HospID\":\"0101|0102|0106\",\"ReserDate\":\"\"}}"
headers = {
   'X-Requested-With': 'XMLHttpRequest',
# use your cookie 
   'Cookie': 'isShow=ok; your cookie',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json; charset=UTF-8',
   'Accept': '*/*',
   'Host': 'mbapp.jsph.org.cn',
   'Connection': 'keep-alive'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
