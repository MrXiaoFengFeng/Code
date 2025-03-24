import allure

@allure.step("打印信息")
def print_to_allure(message):
    print(message)
    allure.attach(message, name="打印信息", attachment_type=allure.attachment_type.TEXT)

# 调用函数记录每条信息
print_to_allure("Hello Word!！！！！")
print_to_allure("Hello Word2!！！！！")
print_to_allure("Hello Word3!！！！！")
print_to_allure("Hello Word4!！！！！")
print_to_allure("Hello Word5!！！！！")
print_to_allure("Hello Word6!！！！！")
print_to_allure("Hello Word7!！！！！")
print_to_allure("通了!！！！！")
