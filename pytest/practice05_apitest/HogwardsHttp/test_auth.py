import requests
from requests.auth import HTTPBasicAuth
'''def test_auth():
    r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/banana/123",
                     auth=HTTPBasicAuth("banana","123"))
    print(r.text)
def test_sms():
     header = {'X-Qiniu-Uid': '1810775223'}
     r = requests.get(url= "http://sms-portal-sms-env-dev.qa.qiniu.io/v1/signature",headers=header)
     print(r.text)'''
def test_sms1():
     header = {
         'X-Qiniu-Uid': '1810775223',
         'Authorization': "Qiniu QxZugR8TAhI38AiJ_cptTl3RbzLyca3t-AAiH-Hh:rr0VKtHZQtjauaKGFzoj-jyHowk=",
         'Content-Type': "application/x-www-form-urlencoded"
         }
     
     r = requests.get(url= "http://sms.qiniuapi.com/v1/signature" ,headers=header)
     print(r.text)

    