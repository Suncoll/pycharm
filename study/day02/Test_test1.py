import pytest


class Testtest1:
    def setup_class(self):
        print('执行')
    def setup(self):
        print('测试开始')

    @pytest.mark.run(order=2)
    def test_05(self):
        print("测试1")
    @pytest.mark.run(order=1)
    def test_01(self):
        print("测试2")
    def test_03(self):
        print("测试3")
    def test_09(self):
        print("测试4")
    def test_08(self):
        print("测试5")
        assert 1==2
    def teardown(self):
        print('测试结束')
    def teardown_class(self):
        print('结束')
