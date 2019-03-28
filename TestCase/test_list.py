import allure
import pytest
from Common import Assert
from Common import Request

# 新建一个 Assert.Assertions() 的对象 对象名: assertions
assertions = Assert.Assertions()
request = Request.Request()


@allure.feature("演示模块")
class Testdemo(object):

    @allure.story("演示功能")
    @pytest.mark.parametrize("pwd,name,msg",
            [('123456','admin','成功'),('1234561','admin','错误'),('123456','admin1','错误')],
            ids=['登录成功','密码错误','用户名错误'])
    def test_case_demo(self,pwd,name,msg):
        login_data = {"password": pwd, "username": name}
        login_resp = request.post_request(url="http://qa.guoyasoft.com:8099/admin/login", json=login_data)
        # .assert_code 用来断言 状态码 ; 第一个参数 填 响应的状态码, 第二个参数 期望值
        assertions.assert_code(login_resp.status_code, 200)
        # 获取响应正文  字典格式
        login_resp_json = login_resp.json()
        # .assert_in_text 用来断言字符 第一个参数填 比较多的那个字符; 第二参数填 这个字符 是否存在第一个字符里面
        assertions.assert_in_text(login_resp_json['message'], msg)