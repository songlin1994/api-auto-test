import pytest
import allure
from Common import Assert
from Common import Request
import requests
import json

assertions = Assert.Assertions()
request = Request.Request()
myToken = ''
head2 = {'Authorization' : myToken}

# @allure.severity("critical")
# 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.feature("功能模块")
class TestShoppingTrolley(object):

    @allure.story("登录")
    def test_case_example(self):
        data = {"password": "123456", "username": "admin"}
        post_request = request.post_request("http://qa.guoyasoft.com:8099/admin/login", json=data)
        assertions.assert_code(post_request.status_code, 200)
        respJson = post_request.json()
        respData = respJson['data']
        tokenBody = respData['token']
        tokenHead = respData['tokenHead']
        global myToken
        myToken = tokenHead + ' ' + tokenBody
        head2 = {'Authorization': myToken}
        get = request.get_request(url='http://qa.guoyasoft.com:8099/admin/info', headers=head2)
        assertions.assert_code(get.status_code, 200)


    @allure.story("其他")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    def test_case(self):
        data = {"password": "123456", "username": "admin"}
        global myToken
        print(myToken)
        head2 = {'Authorization': myToken}
        get = request.get_request(url='http://qa.guoyasoft.com:8099/admin/info', headers=head2)
        headers = get.request.headers
        print(headers)
        assertions.assert_code(get.status_code, 200)


