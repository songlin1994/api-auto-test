from Common import Request, Assert, read_excel
import allure
import pytest

request = Request.Request()
assertion = Assert.Assertions()

idsList=[]

excel_list = read_excel.read_excel_list('../document/注册.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())

url = 'http://192.168.1.137:1811/'

@allure.feature('退货模块')
class Test_th:

    @allure.story('注册')
    @pytest.mark.parametrize('phone,name,pwd,repwd,msg',excel_list,ids=idsList)
    def test_sign_up(self,phone,name,pwd,repwd,msg):
        json = { "phone": phone, "pwd": pwd, "rePwd": repwd,"userName": name}
        signup_resp = request.post_request(url=url + 'user/signup', json=json)
        resp_json = signup_resp.json()

        assertion.assert_in_text(resp_json['respDesc'],msg)


    def test_login(self):
        post_request = request.post_request(url=url + 'user/lock', params={'userName': 'asd123'},headers={"Content-Type": "application/x-www-form-urlencoded"})
        json = post_request.json()
        print(json)