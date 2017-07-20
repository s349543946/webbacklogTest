#-*- coding:UTF-8  -*-
# @2017,7,19
# @author:fuYuQian
# @content:pytest test for BurnDown

import pytest
from BurnDown import *
class TestBurnDown:
    def setup_class(self):
        self.myT=BurnDown()

    def test_H1title(self):
        aimTitle="Burn Down"
        title=self.myT.H1title()
        assert (aimTitle==title)

    def test_ol(self):
        aimlist=[1,"Release mgmt.","Burn Down"]
        mylist=self.myT.ol()
        for i in range (3):
            assert (aimlist[i]==mylist[i])

    def test_h3(self):
        aimlist=["Burn Down Charts",1]
        mylist=self.myT.h3()
        for i in range (2):
            assert (aimlist[i]==mylist[i])

    def test_footer(self):
        aimlist=[1,1]
        mylist=self.myT.footer()
        for i in range(2):
            assert (aimlist[i] == mylist[i])

    def test_systemRelease(self):
        aimlist=["5G Future Release","5G Innovation Prototyping","5G16","5G16A","5G16A_SP","5G17","5G17A","5G17A_CT","5G18","5G18A","5G18AD","5G19","5G19A","Others"]
        mylist=self.myT.systemRealse()
        for i in range(len(aimlist)):
            assert (aimlist[i]==mylist[i])

    def test_Team(self):
        aimlist=["5G_FT","5G_CV","ALL"]
        mylist=self.myT.Team()
        for i in range(len(aimlist)):
            assert (aimlist[i]==mylist[i])

    def test_canvas(self):
        aim=1
        succ=self.myT.canvas()
        assert(aim==succ)

    def teardown_class(self):
        self.myT.driver.quit()


if __name__ == '__main__':
    pytest.main("test_BurnDown.py")