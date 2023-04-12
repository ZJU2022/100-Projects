import requests
from jsonpath import jsonpath
from hamcrest import assert_that,equal_to
class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200
    def test_query(self):
        payload={
            "level":1,
            "name":"seveniruby"
        }
        r = requests.get('https://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200
    def test_post_form(self):
        payload={
            "level":1,
            "name":"seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post',data=payload)
        print(r.text)
        assert r.status_code == 200
    def test_headers(self):
        r = requests.get('https://httpbin.testing-studio.com/get',headers={"h":"header demo"})
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']["H"] == "header demo"
    def test_post_json(self):
        payload={
            "level":1,
            "name":"seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post',json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1
        assert jsonpath(r.json(),'$..name')[0] == 'seveniruby'
    def test_hamcrest(self):
         payload={
            "level":1,
            "name":"seveniruby"
        }
         r = requests.post('https://httpbin.testing-studio.com/post',json=payload)
         assert_that(r.json()['json']['name'],equal_to('seveniruby'))
    
    def test_demo(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {
            'User-Agent': 'python2'
                  }
        cookie_data = {"hog":"schopl"}
        r = requests.get(url=url,headers = header,cookies=cookie_data)
        print(r.request.headers)
    
        