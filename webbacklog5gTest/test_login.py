#-*- coding:UTF-8 -*-
#@ 2017.7.20
#@ author:FuYuQian
#@ content:pytest for login

import pytest
from login import *

class TestLogin:
    def setup_class(self):
        self.myT=login()

    def teardown_class(self):
        self.myT.driver.quit()

    def test_loginLogo(self):
        aim="Webbacklog"
        t=self.myT.loginLogo()
        assert (aim==t)

    def test_loginBox(self):
        aim=1
        succ=self.myT.loginBox()
        assert(aim==succ)

    def test_loginBoxMsg(self):
        aim="Sign in to start your session"
        t=self.myT.loginBoxMsg()
        assert(aim==t)

    def test_emailId(self):
        aim=1
        succ=self.myT.emailId()
        assert(aim==succ)

    def test_passwd(self):
        aim=1
        succ=self.myT.passwd()
        assert(aim==succ)

    def test_IconEmainID(self):
        aim=1
        succ=self.myT.Icon_email()
        assert (aim==succ)

    def test_IconPasswd(self):
        aim=1
        succ=self.myT.Icon_passwd()
        assert (aim==succ)

    def test_rememberMe(self):
        aim=1
        succ=self.myT.RememerMe()
        assert (aim==succ)

    def test_submit(self):
        aim=1
        succ=self.myT.submit()
        assert (aim==succ)

if __name__=="__main__":
    pytest.main("test_login.py")
