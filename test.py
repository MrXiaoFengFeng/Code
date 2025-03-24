# import allure

# @allure.step("打印信息")
# def print_to_allure(message):
#     print(message)
#     allure.attach(message, name="打印信息", attachment_type=allure.attachment_type.TEXT)

# # 调用函数记录每条信息
# print_to_allure("Hello Word!！！！！")
# print_to_allure("Hello Word2!！！！！")
# print_to_allure("Hello Word3!！！！！")
# print_to_allure("Hello Word4!！！！！")
# print_to_allure("Hello Word5!！！！！")
# print_to_allure("Hello Word6!！！！！")
# print_to_allure("Hello Word7!！！！！")
# print_to_allure("通了!！！！！")

import allure
import pytest

@allure.step("步骤 1: 打印信息")
def print_message(message):
    print(message)
    allure.attach(message, name="打印信息", attachment_type=allure.attachment_type.TEXT)

@allure.feature("Allure 报告验证")
class TestAllureDemo:
    @allure.story("测试用例 1: 验证打印功能")
    def test_print_message(self):
        print_message("Hello, Allure! 这是第一条信息。")
        assert True

    @allure.story("测试用例 2: 验证断言失败")
    def test_failed_case(self):
        print_message("这是一个失败的测试用例。")
        # assert False, "故意失败以验证 Allure 报告"
        assert True, "故意失败以验证 Allure 报告"

    @allure.story("测试用例 3: 验证附件功能")
    def test_attachment(self):
        with allure.step("添加文本附件"):
            allure.attach("这是一个文本附件", name="附件内容", attachment_type=allure.attachment_type.TEXT)
        assert True

