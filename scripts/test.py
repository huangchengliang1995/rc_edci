import allure
import pytest


class Test_01:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是我的测试步骤1")
    def test_01(self):
        print("--->test_01")
        allure.attach("我是一个标题", "我是里面的具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是我的测试步骤2")
    def test_02(self):
        print("--->test_02")
        allure.attach("我是一个标题", "我是里面的具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是我的测试步骤3")
    def test_03(self):
        print("--->test_03")
        allure.attach("我是一个标题", "我是里面的具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是我的测试步骤4")
    def test_04(self):
        print("--->test_04")
        allure.attach("我是一个标题", "我是里面的具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是我的测试步骤5")
    def test_05(self):
        print("--->test_05")
        allure.attach("我是一个标题", "我是里面的具体内容")
        assert True