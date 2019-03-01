#coding:utf-8
from django.http import HttpResponse

from app.models import Activity
from app.models import User
import json
from django.core import serializers
from django.http import JsonResponse
from app.AESUtil import AESUtils

#数据库操作
def testdb(request):
    list = Activity.objects.all()

    # list2 = {}

    list3 = []
    i = 1
    for var in list:
        data = {}
        data['id'] = i
        data['cname'] = var.cname
        data['ctime'] = var.ctime
        data['address'] = var.address
        data['price'] = var.price
        data['photo'] = var.photo
        data['urlLink'] = var.urlLink
        #
        # list2['id'] = i
        # list2['data'] = data

        list3.append(data)
        i += 1

    # a = json.dumps(data)
    # b = json.dumps(list2)

    # 将集合或字典转换成json 对象
    c = json.dumps(list3)
    return HttpResponse(c)



def testdb2(request):
    list = Activity.objects.all()
    data = {}
    data['list'] = json.loads(serializers.serialize("json", list))
    return JsonResponse(data)

def test(request):
    response = 'Welcome to cx World !'
    return HttpResponse("<p>" + response + "</p>")

def parseData(request):
    response = ""
    if(request.method == 'POST'):
        print("parseData : " + "post data !")
        # postBody = request.body
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")

        # d = request.POST.get('d' , "")
        # print("d: " , d)
        # pc = AESUtils('744cx185185cx744')  # 初始化密钥
        # list2 = pc.decrypt(d)
        # print("list 解密 ：" , list2)
        # #因为末尾有3个特殊字符，所以需要先过滤掉后3个字符
        # list4 = list2[:-3]
        # text = json.loads(list4)
        # print("text :" , text)

        # text = {}
        # text['username'] = username
        # text['password'] = password
        # text['email'] = email
        # text['phone'] = phone

        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.phone = phone
        # for var in text:
        #     name = var['name']
        #     value = var['value']
        #     if(name == 'username'):
        #         user.username = value
        #     elif(name == 'password'):
        #         user.password = value
        #     elif(name == 'email'):
        #         user.email = value
        #     elif(name == 'phone'):
        #         user.phone = value
        #添加保存到数据库
        user.save()
        print("cx postData" , "username : " + user.username +":password : " + user.password + ":email : " + user.email + ":phone:" + user.phone)
        #作为json 数组返回给客户端
        data = {}
        data['username'] = user.username
        data['password'] = user.password
        data['email'] = user.email
        data['phone'] = user.phone

        # res = {}
        # res['username'] = user.username
        # res['email'] = user.email
        # res['phone'] = user.phone
        #
        # # 返回给客户端的结果
        # resJson = json.dumps(res)
        # print("resJson : " , resJson)
        # # AES 加密返回
        # # data['d'] = pc.encrypt(resJson)
        # d2 = pc.encrypt(resJson)
        # print("加密返回的结果 : " , d2)
        #
        # d3 = pc.decrypt(d2)
        # print("解密返回的结果:" + d3)
        list = {}
        list['data'] = data
        list['state'] = 1
        list['msg'] = "Post 正常"
        response = json.dumps(list)
    elif(request.method == 'GET'):
        print("parseData : " + "get data !")

        username = request.GET.get('username' , "")
        password = request.GET.get('password' , "")
        email = request.GET.get('email' , "")
        phone = request.GET.get('phone' , "")

        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.phone = phone

        #保存一条用户数据
        user.save()
        print("cx getData" , "username : " + username +":password : " + password + ":email : " + email + ":phone:" + phone)
        # 作为json 数组返回给客户端
        data = {}
        data['username'] = username
        data['password'] = password
        data['email'] = email
        data['phone'] = phone

        list = {}
        list['data'] = data
        list['state'] = 1
        list['msg'] = "Get 正常"
        response = json.dumps(list)
    else:
        print("parseData : not get and not post !")
        response = "not get and not post"
    return HttpResponse(response)


# def parseDataTest(request):
#     response = ""
#     if(request.method == 'POST'):
#         print("parseData : " + "post data !")
#         # postBody = request.body
#         username = request.POST.get('username', "")
#         password = request.POST.get('password', "")
#         email = request.POST.get('email', "")
#         phone = request.POST.get('phone', "")
#
#         d = request.POST.get('d' , "")
#         print("d: " , d)
#         pc = PrpCrypt('744cx185185cx744')  # 初始化密钥
#         list2 = pc.decrypt(d)
#         print("list 解密 ：" , list2)
#         #因为末尾有3个特殊字符，所以需要先过滤掉后3个字符
#         list4 = list2[:-3]
#         text = json.loads(list4)
#         print("text :" , text)
#         user = User()
#         for var in text:
#             name = var['name']
#             value = var['value']
#             if(name == 'username'):
#                 user.username = value
#             elif(name == 'password'):
#                 user.password = value
#             elif(name == 'email'):
#                 user.email = value
#             elif(name == 'phone'):
#                 user.phone = value
#         #添加保存到数据库
#         user.save()
#         print("cx postData" , "username : " + user.username +":password : " + user.password + ":email : " + user.email + ":phone:" + user.phone)
#         #作为json 数组返回给客户端
#         data = {}
#         # data['username'] = user.username
#         # data['password'] = user.password
#         # data['email'] = user.email
#         # data['phone'] = user.phone
#
#         res = {}
#         res['username'] = user.username
#         res['email'] = user.email
#         res['phone'] = user.phone
#
#         # 返回给客户端的结果
#         resJson = json.dumps(res)
#         print("resJson : " , resJson)
#         # AES 加密返回
#         # data['d'] = pc.encrypt(resJson)
#         d2 = pc.encrypt(resJson)
#         print("加密返回的结果 : " , d2)
#
#         d3 = pc.decrypt(d2)
#         print("解密返回的结果:" + d3)
#         list = {}
#         list['data'] = d2
#         list['state'] = 1
#         list['msg'] = "Post 正常"
#         response = json.dumps(list)
#     elif(request.method == 'GET'):
#         print("parseData : " + "get data !")
#
#         username = request.GET.get('username' , "")
#         password = request.GET.get('password' , "")
#         email = request.GET.get('email' , "")
#         phone = request.GET.get('phone' , "")
#
#         user = User()
#         user.username = username
#         user.password = password
#         user.email = email
#         user.phone = phone
#
#         #保存一条用户数据
#         user.save()
#         print("cx getData" , "username : " + username +":password : " + password + ":email : " + email + ":phone:" + phone)
#         # 作为json 数组返回给客户端
#         data = {}
#         data['username'] = username
#         data['password'] = password
#         data['email'] = email
#         data['phone'] = phone
#
#         list = {}
#         list['data'] = data
#         list['state'] = 1
#         list['msg'] = "Get 正常"
#         response = json.dumps(list)
#     else:
#         print("parseData : not get and not post !")
#         response = "not get and not post"
#     return HttpResponse(response)

