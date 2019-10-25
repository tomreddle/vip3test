# 导入requests
import requests,json

# 根据参数中的方法类型判断使用方法（假定只有post 和 get）
# 根据接口中的参数个数判断是否需要传参，如需传参则还需判断参数的类型（假定只有data\json）
# 获取不同类型的响应内容


class Confighttp(object):
    def __init__(self, urlstr, interface_type, parameter_type=None, payload=None):
        self.urlstr = urlstr
        self.payload = payload
        self.interface_type = interface_type
        self.parameter_type = parameter_type

    def getrequest(self):
        if self.parameter_type == 'data':
            return requests.get(url=self.urlstr, params=self.payload)
        if self.parameter_type == 'json':
            return requests.get(url=self.urlstr, params=json.dumps(self.payload))
        if self.parameter_type is None:
            return requests.get(url=self.urlstr)

    def postrequest(self):
        if self.parameter_type == 'data':
            return requests.post(url=self.urlstr, data=self.payload)
        if self.parameter_type == 'json':
            return requests.post(url=self.urlstr, json=self.payload)
        if self.parameter_type is None:
            return requests.post(url=self.urlstr)

    def dorequest(self):
        if self.interface_type == 'POST':
            return self.postrequest()
        if self.interface_type == 'GET':
            return self.getrequest()


if __name__ == '__main__':
    param1 = ['1', 'https://www.wanandroid.com', '/user/login', 'POST',
              "{'username': 'haoyiran', 'password': '123456'}", 'data']
    print(param1[1]+param1[2])
    print(param1[3])
    print(param1[5])
    print(param1[4])
    interface1 = Confighttp(param1[1]+param1[2], param1[3], param1[5], eval(param1[4]))
    r = interface1.dorequest()
    print(r.text)
# c = "{'username': 'haoyiran', 'password': '123456'}"
# print(dict(c))


