import requests

params = {'q' : 'stellar blade girl'}

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Priority": "u=1, i",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-686293f0-7838908f17bd61695c6fd686"
  }


response = requests.get('https://httpbin.org/headers', headers= headers) #позволяет посмотреть что мы отправили на какой либо сайт. в данном случае 

#print(response.status_code)

#print(response.headers)

#print(response.content)

#print(response.text)

data = {'custname' : 'Матвей',
        'custtel' : '+7 988 628 75 32',
        'custemail' : 'sutormin.p@gmail.com',
        "delivery": "19:30", 
        "size": "large", 
        "topping": 
            ["bacon", 
            "onion"],
        'commensts' : 'suck my cock'
         }


response1 = requests.post('https://httpbin.org/post', headers= headers, data= data)
print(response1.text)



session = requests.Session()
save_token = session.get('https://httpbin.org/form/post')
response2 = requests.post('https://httpbin.org/post', headers= headers, data= data, allow_redirects=True)
print(response1.text)