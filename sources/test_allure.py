#!/usr/bin/env python
# coding=utf-8

import pytest
import allure


@allure.feature('购物车功能')  # 用feature说明产品需求，可以理解为功能模块
class TestShoppingTrolley(object):
    @allure.story('物品加入购物车')  # 用story说明用户场景，可以理解为用例
    @allure.severity('blocker')
    def test_add_shopping_trolley(self):
        """
        用例描述：将物品加入到购物车
        """
        login('刘春明', '密码')  # 步骤1，调用“step函数”
        with allure.step("浏览商品"):  # 步骤2，step的参数将会打印到测试报告中
            allure.attach('笔记本', '商品1')  # attach可以打印一些附加信息
            allure.attach('手机', '商品2')
        with allure.step("点击商品"):  # 步骤3
            pass
        with allure.step("校验结果"):  # 步骤4
            allure.attach('添加购物车成功', '期望结果')
            allure.attach('添加购物车失败', '实际结果')
            assert 'success' == 'success'

    @allure.story('修改购物车物品')
    @allure.severity('critical')
    def test_edit_shopping_trolley(self):
        """
        用例描述：修改购物车的物品
        """
        assert '2' == '22'

    @allure.story('向购物车重复增加物品')
    @allure.severity('normal')
    def test_add_same_shopping_trolley(self):
        """
        用例描述：增加重复的物品到购物车
        """
        assert '1' == '12'

    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('删除购物车中商品')
    @allure.severity('minor')
    def test_delete_shopping_trolley(self):
        """
        用例描述：删除购物车中的物品
        """
        assert '333' == '3233'



@allure.feature('结算功能')  # 用feature说明产品需求，可以理解为功能模块
class TestShoppingPay(object):
    @allure.story('使用微信付款')  # 用story说明用户场景，可以理解为用例
    @allure.severity('trivial')
    def test_pay_by_weixin(self):
     
       assert 'success' == 'success'

    @allure.story('使用支付宝付款')
    def test_pay_by_zhifubao(self):
        pass

    @allure.story('使用银行卡付款')
    def test_pay_by_xinyongka(self):
        pass

    @allure.story('使用钱包零钱付款')
    def test_pay_by_lingqian(self):
        pass


@allure.step('用户登录')  # 将函数作为一个步骤，调用此函数时，报告中输出这个步骤，我把这样的函数叫“step函数”
def login(user, pwd):
    print(user, pwd)
if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])