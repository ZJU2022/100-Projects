#https://docs.mitmproxy.org/stable/addons-examples/#contentview 
from mitmproxy import http

#request 函数名不能修改，是固定的，当请求来的时候回调request方法
def request(flow: http.HTTPFlow) -> None:
    #判断url是否等于预期路径
    if flow.request.pretty_url == "https://www.baidu.com/":
        #如果URL是预期的，我们就会造一个reponse
        flow.response = http.Response.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"},  # (optional) headers
        )