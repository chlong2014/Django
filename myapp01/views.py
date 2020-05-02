from django.shortcuts import render
#render请求转发

# Create your views here.
"""
定义视图函数
"""

def test(req):
    return render(req, 'test.html')

# def loginpage(req):
#     return render(req, 'login.html')

"""
页面访问方法
pageName 页面名  模板名
访问此函数 地址栏有对应的参数值  --restFulUrl
"""
def topage(request, pageName):
    return render(request, pageName)

def login(req):
    #获得客户提交的数据, get请求
    username = req.GET.get("username", None)
    userpw = req.GET.get("userpw", None)
    print(username, userpw)
    if "admin" == username and "123456" == userpw:
        print("登陆成功")
        return render(req, 'test.html')
    else:
        return render(req, 'login.html')

def reg(req):
    username = req.POST.get("username")
    useradd = req.POST.getlist("addr")
    print(username, useradd)
    return render(req, "login.html")
