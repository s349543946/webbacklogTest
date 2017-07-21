# -*- coding:utf-8 -*-
# This Python file uses the following encoding: utf-8

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# 引入unittest 包
# import  unittest,time,re
import pytest
from  selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time



class Testwebbacklog_EER:
    # setup 用于设置初始化的部分
    # setup is used to set the initialization section
    def setup(self):
        self.driver = webdriver.Chrome()
        # 超时重连
        # Timeout reconnection
        self.driver.implicitly_wait(30)
        # 设置浏览路径
        # Set browse path
        self.base_url = "http://127.0.0.1:8000/webbacklog/featureBuild/"
        # 脚本运行错误打印到这个列表中
        # Script run error print to this list
        self.verificationErrors = []
        # 是否继续接受下一下警告
        # Would  like to proceed with the next warning
        self.accept_next_alert = True

    #某张表格对应的Xpath矩阵
    #one table matrix of Xpath
    csjl = {"//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[1]/td[1]/span": "FT",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[1]/td[2]" : "27",
            "//*[@id='table1']/tbody/tr[1]/td[3]": "27",
            "//*[@id='table1']/tbody/tr[1]/td[4]/div/span": "100.0%",
            "//*[@id='table1']/tbody/tr[1]/td[5]": "29",
            "//*[@id='table1']/tbody/tr[1]/td[6]": "0.0",
            "//*[@id='table1']/tbody/tr[1]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[1]/td[8]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[1]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[1]/td[10]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[1]/td[11]": "0",
            "//*[@id='table1']/tbody/tr[1]/td[12]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[1]/td[13]/a": "Not Done",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[2]/td[1]/span": "Committed",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[2]/td[2]": "27",
            "//*[@id='table1']/tbody/tr[2]/td[3]": "27",
            "//*[@id='table1']/tbody/tr[2]/td[4]/div/span": "100.0%",
            "//*[@id='table1']/tbody/tr[2]/td[5]": "29",
            "//*[@id='table1']/tbody/tr[2]/td[6]": "0.0",
            "//*[@id='table1']/tbody/tr[2]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[2]/td[8]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[2]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[2]/td[10]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[2]/td[11]": "0",
            "//*[@id='table1']/tbody/tr[2]/td[12]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[2]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[3]/td[1]/span": "Customer features",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[3]/td[2]": "19",
            "//*[@id='table1']/tbody/tr[3]/td[3]": "19",
            "//*[@id='table1']/tbody/tr[3]/td[4]": "",
            "//*[@id='table1']/tbody/tr[3]/td[5]": "21",
            "//*[@id='table1']/tbody/tr[3]/td[6]": "0.0",
            "//*[@id='table1']/tbody/tr[3]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[4]/td[8]": "",
            "//*[@id='table1']/tbody/tr[3]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[3]/td[10]": "",
            "//*[@id='table1']/tbody/tr[3]/td[11]": "0",
            "//*[@id='table1']/tbody/tr[3]/td[12]": "",
            "//*[@id='table1']/tbody/tr[3]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[4]/td[1]/span": "Internal features",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[4]/td[2]": "8",
            "//*[@id='table1']/tbody/tr[4]/td[3]": "8",
            "//*[@id='table1']/tbody/tr[4]/td[4]": "",
            "//*[@id='table1']/tbody/tr[4]/td[5]": "8",
            "//*[@id='table1']/tbody/tr[4]/td[6]": "0.0",
            "//*[@id='table1']/tbody/tr[4]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[4]/td[8]": "",
            "//*[@id='table1']/tbody/tr[4]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[4]/td[10]": "",
            "//*[@id='table1']/tbody/tr[4]/td[11]": "0",
            "//*[@id='table1']/tbody/tr[4]/td[12]": "",
            "//*[@id='table1']/tbody/tr[4]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[5]/td[1]/span": "Ext BL",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[5]/td[2]" : "7",
            "//*[@id='table1']/tbody/tr[5]/td[3]": "2",
            "//*[@id='table1']/tbody/tr[5]/td[4]/div/span": "28.57%",
            "//*[@id='table1']/tbody/tr[5]/td[5]": "3",
            "//*[@id='table1']/tbody/tr[5]/td[6]": "7786.0",
            "//*[@id='table1']/tbody/tr[5]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[5]/td[8]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[5]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[5]/td[10]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[5]/td[11]": "7785",
            "//*[@id='table1']/tbody/tr[5]/td[12]/div/span": "99.99%",
            "//*[@id='table1']/tbody/tr[5]/td[13]/a":"Not Done",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[6]/td[1]/span": "Committed",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[6]/td[2]": "6",
            "//*[@id='table1']/tbody/tr[6]/td[3]": "2",
            "//*[@id='table1']/tbody/tr[6]/td[4]/div/span": "33.33%",
            "//*[@id='table1']/tbody/tr[6]/td[5]": "3",
            "//*[@id='table1']/tbody/tr[6]/td[6]": "30.0",
            "//*[@id='table1']/tbody/tr[6]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[6]/td[8]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[6]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[6]/td[10]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[6]/td[11]": "29",
            "//*[@id='table1']/tbody/tr[6]/td[12]/div/span": "96.67%",
            "//*[@id='table1']/tbody/tr[6]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[7]/td[1]/span": "Customer features",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[7]/td[2]": "6",
            "//*[@id='table1']/tbody/tr[7]/td[3]": "2",
            "//*[@id='table1']/tbody/tr[7]/td[4]": "",
            "//*[@id='table1']/tbody/tr[7]/td[5]": "3",
            "//*[@id='table1']/tbody/tr[7]/td[6]": "30.0",
            "//*[@id='table1']/tbody/tr[7]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[7]/td[8]": "",
            "//*[@id='table1']/tbody/tr[7]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[7]/td[10]": "",
            "//*[@id='table1']/tbody/tr[7]/td[11]": "29",
            "//*[@id='table1']/tbody/tr[7]/td[12]": "",
            "//*[@id='table1']/tbody/tr[7]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[8]/td[1]/span": "Other state",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[8]/td[2]": "1",
            "//*[@id='table1']/tbody/tr[8]/td[3]": "0",
            "//*[@id='table1']/tbody/tr[8]/td[4]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[8]/td[5]": "0",
            "//*[@id='table1']/tbody/tr[8]/td[6]": "7756.0",
            "//*[@id='table1']/tbody/tr[8]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[8]/td[8]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[8]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[8]/td[10]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[8]/td[11]": "7756",
            "//*[@id='table1']/tbody/tr[8]/td[12]/div/span": "100.0%",
            "//*[@id='table1']/tbody/tr[8]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[9]/td[1]/span": "Customer features",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[9]/td[2]": "1",
            "//*[@id='table1']/tbody/tr[9]/td[3]": "0",
            "//*[@id='table1']/tbody/tr[9]/td[4]": "",
            "//*[@id='table1']/tbody/tr[9]/td[5]": "0",
            "//*[@id='table1']/tbody/tr[9]/td[6]": "7756.0",
            "//*[@id='table1']/tbody/tr[9]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[9]/td[8]": "",
            "//*[@id='table1']/tbody/tr[9]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[9]/td[10]": "",
            "//*[@id='table1']/tbody/tr[9]/td[11]": "7756",
            "//*[@id='table1']/tbody/tr[9]/td[12]": "",
            "//*[@id='table1']/tbody/tr[9]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[10]/td[1]/span": "Customer Total",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[10]/td[2]": "26",
            "//*[@id='table1']/tbody/tr[10]/td[3]": "21",
            "//*[@id='table1']/tbody/tr[10]/td[4]/div/span": "80.77%",
            "//*[@id='table1']/tbody/tr[10]/td[5]": "24",
            "//*[@id='table1']/tbody/tr[10]/td[6]": "7786.0",
            "//*[@id='table1']/tbody/tr[10]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[10]/td[8]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[10]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[10]/td[10]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[10]/td[11]": "7785",
            "//*[@id='table1']/tbody/tr[10]/td[12]/div/span": "99.99%",
            "//*[@id='table1']/tbody/tr[10]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[11]/td[1]/span": "Internal Total",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[11]/td[2]": "8",
            "//*[@id='table1']/tbody/tr[11]/td[3]": "8",
            "//*[@id='table1']/tbody/tr[11]/td[4]/div/span": "100.0%",
            "//*[@id='table1']/tbody/tr[11]/td[5]": "8",
            "//*[@id='table1']/tbody/tr[11]/td[6]": "0.0",
            "//*[@id='table1']/tbody/tr[11]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[11]/td[8]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[11]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[11]/td[10]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[11]/td[11]": "0",
            "//*[@id='table1']/tbody/tr[11]/td[12]/div/span": "invalid",
            "//*[@id='table1']/tbody/tr[11]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[12]/td[1]/span": "Grand Total",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[12]/td[2]": "34",
            "//*[@id='table1']/tbody/tr[12]/td[3]": "29",
            "//*[@id='table1']/tbody/tr[12]/td[4]/div/span": "85.29%",
            "//*[@id='table1']/tbody/tr[12]/td[5]": "32",
            "//*[@id='table1']/tbody/tr[12]/td[6]": "7786.0",
            "//*[@id='table1']/tbody/tr[12]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[12]/td[8]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[12]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[12]/td[10]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[12]/td[11]": "7785",
            "//*[@id='table1']/tbody/tr[12]/td[12]/div/span": "99.99%",
            "//*[@id='table1']/tbody/tr[12]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[13]/td[1]/span": "Committed Total",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[13]/td[2]": "33",
            "//*[@id='table1']/tbody/tr[13]/td[3]": "29",
            "//*[@id='table1']/tbody/tr[13]/td[4]/div/span": "87.88%",
            "//*[@id='table1']/tbody/tr[13]/td[5]": "32",
            "//*[@id='table1']/tbody/tr[13]/td[6]": "30.0",
            "//*[@id='table1']/tbody/tr[13]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[13]/td[8]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[13]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[13]/td[10]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[13]/td[11]": "29",
            "//*[@id='table1']/tbody/tr[13]/td[12]/div/span": "96.67%",
            "//*[@id='table1']/tbody/tr[13]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[14]/td[1]/span": "Groomed Total",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[14]/td[2]": "1",
            "//*[@id='table1']/tbody/tr[14]/td[3]": "0",
            "//*[@id='table1']/tbody/tr[14]/td[4]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[14]/td[5]": "0",
            "//*[@id='table1']/tbody/tr[14]/td[6]": "7756.0",
            "//*[@id='table1']/tbody/tr[14]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[14]/td[8]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[14]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[14]/td[10]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[14]/td[11]": "7756",
            "//*[@id='table1']/tbody/tr[14]/td[12]/div/span": "100.0%",
            "//*[@id='table1']/tbody/tr[14]/td[13]": "",

            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[15]/td[1]/span": "Grand Total",
            "//*[@id='table1_wrapper']/div/div[3]/div[2]/div/table/tbody/tr[15]/td[2]": "34",
            "//*[@id='table1']/tbody/tr[15]/td[3]": "29",
            "//*[@id='table1']/tbody/tr[15]/td[4]/div/span": "85.29%",
            "//*[@id='table1']/tbody/tr[15]/td[5]": "32",
            "//*[@id='table1']/tbody/tr[15]/td[6]": "7786.0",
            "//*[@id='table1']/tbody/tr[15]/td[7]": "0",
            "//*[@id='table1']/tbody/tr[15]/td[8]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[15]/td[9]": "0",
            "//*[@id='table1']/tbody/tr[15]/td[10]/div/span": "0.0%",
            "//*[@id='table1']/tbody/tr[15]/td[11]": "7785",
            "//*[@id='table1']/tbody/tr[15]/td[12]/div/span": "99.99%",
            "//*[@id='table1']/tbody/tr[15]/td[13]": ""
        }
    # 测试脚本
    # Test script
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        #找到帮助按钮
        #find help button
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[1]/div[1]/div/div[1]/i").click()
        time.sleep(1)

        # 找到x按钮
        # find close button
        driver.find_element_by_xpath("//*[@id='featurebuildModal']/div/div/div/div/div[1]/button").click()
        time.sleep(1)

        #测试home
        #test home
        driver.find_element_by_xpath("/html/body/div/div[1]/section[1]/ol/li/a").click()
        time.sleep(1)
        #回退
        #back
        driver.back()
        time.sleep(1)

        #测试页面文字
        #test title
        title = driver.find_element_by_xpath("/html/body/div/div[1]/section[1]/h1").text
        assert title == u'Feature Build Entry & Exit   Under Construction'

        #选择5g17,1706,all,pred这张表格
        #chose 5g17,1706,all,pred table
        driver.find_element_by_xpath("//*[@id='systemRelease']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[2]/ul/li[1]/a").click()
        driver.find_element_by_xpath("//*[@id='fbSelect']").click()
        driver.find_element_by_xpath( "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[3]/ul/li[1]/a").click()
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[1]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)
        #测试该表格数据
        #test table data
        for key in self.csjl.keys():
            bjl = driver.find_element_by_xpath(key)
            jl = bjl.text
            if jl =="Not Done":
                    bjl.click()
                    time.sleep(1)

                    #调到第2页
                    #jump to 2
                    driver.find_element_by_xpath("//*[@id='tbl-notdone_paginate']/ul/li[3]/a")
                    time.sleep(1)

                    #搜索框输入"5GC000224"
                    #search input "5GC000224"
                    driver.find_element_by_xpath("//*[@id='tbl-notdone_filter']/label/input").send_keys("5GC000224")
                    time.sleep(1)

                    # 回退
                    # back
                    driver.back()
                    time.sleep(1)
                    # 选择5g17,1706,all,pred这张表格
                    # chose 5g17,1706,all,pred table
                    driver.find_element_by_xpath("//*[@id='systemRelease']").click()
                    driver.find_element_by_xpath(
                        "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[2]/ul/li[1]/a").click()
                    driver.find_element_by_xpath("//*[@id='fbSelect']").click()
                    driver.find_element_by_xpath(
                        "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[3]/ul/li[1]/a").click()
                    driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
                    driver.find_element_by_xpath(
                        "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[1]/a").click()
                    driver.find_element_by_xpath("//*[@id='viewSelect']").click()
                    driver.find_element_by_xpath(
                        "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
            assert jl == self.csjl[key]

        # 选择5g17,1706,FT,pred这张表格
        #chose 5g17,1706,FT,pred table
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17,1706,FT,e这张表格
        # chose 5g17,1706,FT,e table
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath( "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[2]/a").click()
        time.sleep(1)

        # 选择5g17,1706,EXT,pred这张表格
        # chose 5g17,1706,EXT,pred table
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[3]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17,1707,EXT,pred这张表格
        # chose 5g17,1707,EXT,pred table
        driver.find_element_by_xpath("//*[@id='fbSelect']").click()
        driver.find_element_by_xpath( "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[3]/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[1]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17,1707,FT,pred这张表格
        # chose 5g17,1707,FT,pred table
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17,1707,FT,e这张表格
        # chose 5g17,1707,FT,e table
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath( "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[2]/a").click()
        time.sleep(1)

        # 选择5g17,1707,EXT,pred这张表格
        # chose 5g17,1707,EXT,pred table
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[3]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17A5G,1706,all,pred这张表格
        # chose 5g17A5G,1706,all,pred table
        driver.find_element_by_xpath("//*[@id='systemRelease']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[2]/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='fbSelect']").click()
        driver.find_element_by_xpath( "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[3]/ul/li[1]/a").click()
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[1]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17A5G,1706,FT,pred这张表格
        # chose 5g17A5G,1706,FT,pred table
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17A5G,1706,FT,e这张表格
        # chose 5g17A5G,1706,FT,e table
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath( "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[2]/a").click()
        time.sleep(1)

        # 选择5g17A5G,1706,EXT,pred这张表格
        # chose 5g17A5G,1706,EXT,pred table
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[3]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17A5G,1707,EXT,pred这张表格
        # chose 5g17A5G,1707,EXT,pred table
        driver.find_element_by_xpath("//*[@id='fbSelect']").click()
        driver.find_element_by_xpath( "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[3]/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[1]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17A5G,1707,FT,pred这张表格
        # chose 5g17A5G,1707,FT,pred table
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)

        # 选择5g17A5G,1707,FT,e这张表格
        # chose 5g17A5G,1707,FT,e table
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath( "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[2]/a").click()
        time.sleep(1)

        # 选择5g17A5G,1707,EXT,pred这张表格
        # chose 5g17A5G,1707,EXT,pred table
        driver.find_element_by_xpath("//*[@id='lifeCycleSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[4]/ul/li[3]/a").click()
        driver.find_element_by_xpath("//*[@id='viewSelect']").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
        time.sleep(1)



    # 用来查找页面元素是否存在
    # Used to find if the page element exists
    def is_elemet_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    # 对弹窗异常处理
    # Exception handling of popups
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True

    # 关闭警告和对文本框的处理
    # Close warnings and handle text boxes
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # 清理工作如退出浏览器等
    # Cleanup tasks such as exiting browsers, etc.
    def teardown(self):
        self.driver.quit()
        # 对前面verificationErrors方法获得的列表进行比较如果不为空则打印列表报错信息
        # Compare the list obtained by the previous verificationErrors method, and print the list if you are not empty
        assert self.verificationErrors == []


if __name__ == "__main__":
    pytest.main("test_pytest_webbacklog_EER.py")


