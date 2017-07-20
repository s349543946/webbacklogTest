#-*- coding:UTF-8 -*-
#@ 2017.7.20
#@ author:FuYuQian
#@ content:UI test for Resource allocation vs P2 contract

from selenium import webdriver
import time
import os

class login:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.url="http://127.0.0.1:8000/webbacklog/login/?next=/webbacklog/rscalcvsp2/"
        self.driver.get(self.url)

    def __del__(self):
        self.driver.quit()

    #测试登录的logo
    def loginLogo(self):
        driver=self.driver
        logo =driver.find_element_by_link_text("Webbacklog")
        logo.click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        t=driver.find_element_by_xpath("/html/body/div/div[1]/a/b").text
        print t
        return t

    #测试登录的输入框login-box-body
    def loginBox(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_class_name("login-box-body")
        except:
            succ=0
        return succ

    #测试输入提示框login-box-msg
    def loginBoxMsg(self):
        driver=self.driver
        print driver.find_element_by_class_name("login-box-msg").text
        return driver.find_element_by_class_name("login-box-msg").text

    #测试email输入
    def emailId(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").clear()
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").send_keys("123")
            time.sleep(1)
        except:
            succ=0
        return succ

    #测试密码输入
    def passwd(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").clear()
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("123456")
            time.sleep(1)
        except:
            succ=0
        return succ

    #测试邮箱输入的图标
    def Icon_email(self):
        driver=self.driver
        time.sleep(1)
        succ=1
        try:
            #driver.find_element_by_class_name("glyphicon glyphicon-envelope form-control-feedback")
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/span")
        except:
            succ=0
        print succ
        return succ

    #测试密码输入的图标
    def Icon_passwd(self):
        driver = self.driver
        time.sleep(1)
        succ = 1
        try:
            #driver.find_element_by_class_name("glyphicon glyphicon-lock form-control-feedback")
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/span")
        except:
            succ = 0
        print succ
        return succ

    #测试remember me的复选框
    def RememerMe(self):
        driver=self.driver
        time.sleep(1)
        succ=1
        try:
            driver.find_element_by_css_selector('input[type=checkbox]').click()
            time.sleep(1)
        except:
            succ=0
        return succ

    #测试登录按钮
    def submit(self):
        driver=self.driver
        time.sleep(1)
        succ=1
        try:
            driver.find_element_by_css_selector('button[type=submit]').click()
            time.sleep(0.5)
        except:
            succ=0
        return succ

def myTest():
    myT=login()
    #myT.loginLogo()
    #myT.loginBox()
    #myT.loginBoxMsg()
    #myT.emailId()
    #myT.passwd()
    #myT.Icon_email()
    #myT.Icon_passwd()
    #myT.RememerMe()
    #myT.submit()

if __name__=='__main__':
    myTest()