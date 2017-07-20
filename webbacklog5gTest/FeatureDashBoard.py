#-*- coding:utf-8  -*-
#@ 2017/7/18
#@ author:FuYuQian
#@ content: UI test of feature Dashboard

from selenium import webdriver
import os
import time

class FeatureDashBoard():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/webbacklog/featuredashboard/#5G17A_CT;All;Effort;")
        self.driver.maximize_window()

    def __del__(self):
        self.driver.quit()

    #加载load界面
    def load(self):
        self.driver.get("http://127.0.0.1:8000/webbacklog/featuredashboard/#5G17A_CT;All;Effort;")

    #测试H1的title
    def H1title(self):
        driver=self.driver
        h1=driver.find_element_by_tag_name("h1")
        print(h1.text)
        return h1.text

    # 测试右边栏的提示
    def ol(self):
        driver=self.driver
        mylist=[0,0,0]
        succ=1
        try:
            driver.find_element_by_link_text("Home").click()
            driver.back()
            time.sleep(0.5)
        except:
            succ=0
        mylist[0]=succ
        mylist[1]=driver.find_element_by_link_text("Release mgmt.").text
        time.sleep(0.5)
        mylist[2]=driver.find_element_by_xpath("/html/body/div/div[1]/section[1]/ol/li[3]").text
        time.sleep(0.5)
        return mylist

    #测试h3的文本和帮助按钮
    def h3(self):
        driver=self.driver
        mylist=[0,0]
        mylist[0]=driver.find_element_by_id("panel-title").text
        succ=1
        try:
            driver.find_element_by_class_name("help").click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
        except:
            succ=0
        mylist[1]=succ
        return mylist

    #测试footer的文本显示和“nokia"的链接
    def footer(self):
        driver=self.driver
        self.load()
        succ=1
        try:
            time.sleep(1)
            print driver.find_element_by_class_name("main-footer").text
            driver.find_element_by_link_text("Nokia").click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
        except:
            succ=0
        return succ

    #测试dataTables_length
    def dataTables_length(self):
        driver=self.driver
        self.load()
        driver.find_element_by_name("table-feature_length").click()
        time.sleep(1)
        mylist=[0 for i in range(4)]
        mylist[0]=driver.find_element_by_xpath("//*[@id='table-feature_length']/label/select/option[1]").text
        mylist[1]=driver.find_element_by_xpath("//*[@id='table-feature_length']/label/select/option[2]").text
        mylist[2]=driver.find_element_by_xpath("//*[@id='table-feature_length']/label/select/option[3]").text
        mylist[3]=driver.find_element_by_xpath("//*[@id='table-feature_length']/label/select/option[4]").text
        return mylist

    #测试SystemRealse按键
    def systemRelease(self):
        driver=self.driver
        driver.find_element_by_id("systemRelease").click()
        time.sleep(1)

        #下拉框中的每一个选项都点击一遍
        succ=1
        try:
            s = 1
            while s<=14:
                xpath="/html/body/div/div[1]/section[2]/div/section/div/div[2]/div/div[1]/div[1]/ul/li["+str(s)+"]"
                driver.find_element_by_xpath(xpath).click()
                #刷新页面看效果
                driver.refresh()
                time.sleep(2)
                driver.find_element_by_id("systemRelease").click()
                s=s+1
        except:
            succ=0
        return succ

    #测试RnD Commitment:按键
    def RnDCommitment(self):
        driver=self.driver
        driver.find_element_by_id("systemRdCmt").click()
        time.sleep(1)

        # 下拉框中的每一个选项都点击一遍
        succ=1
        try:
            s = 1
            while s <= 3:
                xpath = "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div/div[1]/div[2]/ul/li[" + str(s) + "]"
                driver.find_element_by_xpath(xpath).click()
                # 刷新页面看效果
                driver.refresh()
                time.sleep(2)
                driver.find_element_by_id("systemRdCmt").click()
                s = s + 1
        except:
            succ=0
        return succ


    #测试viewSelect按键
    def viewSelect(self):
        driver=self.driver
        driver.find_element_by_id("viewSelect").click()
        time.sleep(1)

        # 下拉框中的每一个选项都点击一遍
        succ=1
        try:
            s = 1
            while s <= 2:
                xpath = "/html/body/div/div[1]/section[2]/div/section/div/div[2]/div/div[1]/div[3]/ul/li[" + str(s) + "]"
                driver.find_element_by_xpath(xpath).click()
                # 刷新页面看效果
                driver.refresh()
                time.sleep(2)
                driver.find_element_by_id("viewSelect").click()
                s = s + 1
        except:
            succ=0
        return succ

    #测试search按键
    def search(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_xpath("//*[@id='table-feature_filter']/label/input").send_keys("haha")
            time.sleep(1)
            self.load()
            time.sleep(1)
        except:
            succ=0
        return succ

    #测试表格的行normal head
    def normalHead(self):
        driver=self.driver
        self.load()
        time.sleep(3)

        #依次点击表头的元素并输出内容
        mylist=[[0] for i in range(13)]
        s=1
        while s<=14:
            xpath="//*[@id='table-feature_wrapper']/div[2]/div/div/div[3]/div[1]/table/thead/tr/th["+str(s)+"]"
            if s<=2:
                es = driver.find_elements_by_xpath(xpath)
                print es[0].text
                mylist[s-1]=es[0].text
                es[0].click()
            elif s<=13:
                xpath = "//*[@id='table-feature_wrapper']/div[2]/div/div/div[2]/div[1]/div/table/thead/tr/th[" + str(s) + "]"
                e = driver.find_element_by_xpath(xpath)
                print e.text
                mylist[s-1]=e.text
                e.click()
            else:
                xpath="//*[@id='table-feature_wrapper']/div[2]/div/div/div[2]/div[1]/div/table/thead/tr/th[14]"
                e = driver.find_element_by_xpath(xpath)
                #print e.text
                #e.click()            最后一行不能点击，也不能输出文本值，无解
            time.sleep(1)
            s=s+1
        return mylist

    #测试第一列columnName，读取文本值并点击，并打印非控制，可用于测试是否全满
    def column1Name(self):
        time.sleep(1)
        driver=self.driver
        self.load()
        time.sleep(3)
        num=0
        s=1
        while s<=6:
            xpath="//*[@id='table-feature_wrapper']/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr["+str(s)+"]/td[1]/div/a"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                driver.find_element_by_xpath(xpath).click()
                time.sleep(1)
                driver.back()
                time.sleep(2)
                num=num+1
            s=s+1
        print num

    # 测试第二列FeatureComponentTitle，读取非空文本值,并打印非空值
    def column2FeatureComponentTitle(self):
        time.sleep(1)
        driver=self.driver
        self.load()
        time.sleep(1)
        num=0
        s=1
        while s<=6:
            xpath="//*[@id='table-feature_wrapper']/div[2]/div/div/div[3]/div[2]/div/table/tbody/tr["+str(s)+"]/td[2]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num=num+1
            s=s+1
        print num

    # 测试第三列Ram，读取非空文本值,并打印非空值
    def column3Ram(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr["+str(s)+"]/td[3]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第四列Contribution from External BLs，读取非空文本值,并打印非空值
    def column4Contributionfrom(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr["+str(s)+"]/td[4]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第五列FS Status，读取非空文本值,并打印非空值
    def column5FS(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr["+str(s)+"]/td[5]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第六列Total Resource Demand[h]，读取非空文本值,并打印非空值
    def column6TotalResourceDemand(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr["+str(s)+"]/td[6]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第七列Total Progress，读取非空文本值,并打印非空值
    def column7TotalProgress(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr["+str(s)+"]/td[7]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第八列Sub-Feature Completion，读取非空文本值,并打印非空值
    def column8SubFeature(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr[" + str(s) + "]/td[8]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第九列5G_FT Resource Demand[h]，读取非空文本值,并打印非空值
    def column95G_FTResource(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr[" + str(s) + "]/td[9]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num


    # 测试第十列5G_FT Progress，读取非空文本值,并打印非空值
    def column105G_FTProgress(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr[" + str(s) + "]/td[10]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第十一列5G_FT Sub-Feature Completion，读取非空文本值,并打印非空值
    def column115GFTSub_Feature(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr[" + str(s) + "]/td[11]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第十二列5G_FT Progress Per Plan，读取非空文本值,并打印非空值
    def column125G_FTProgress(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr[" + str(s) + "]/td[12]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第十三列5G_FT Progress Per Plan，读取非空文本值,并打印非空值
    def column135G_FTProgressPerPlan(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr[" + str(s) + "]/td[13]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

    # 测试第十四列RAM Input Comment，读取非空文本值,并打印非空值
    def column14RAMInputComment(self):
        time.sleep(1)
        driver = self.driver
        self.load()
        time.sleep(1)
        num = 0
        s = 1
        while s <= 6:
            xpath = "//*[@id='table-feature']/tbody/tr[" + str(s) + "]/td[14]"
            if driver.find_element_by_xpath(xpath).text:
                print driver.find_element_by_xpath(xpath).text
                time.sleep(1)
                num = num + 1
            s = s + 1
        print num

def myTest():
    myT= FeatureDashBoard()
    #myT.H1title()
    #myT.ol()
    #myT.h3()
    #myT.footer()
    #myT.dataTables_length()
    #myT.systemRelease()
    #myT.RnDCommitment()
    #myT.viewSelect()
    #myT.search()
    myT.normalHead()
    #myT.column1Name()
    #myT.column2FeatureComponentTitle()
    #myT.column3Ram()
    #myT.column4Contributionfrom()
    #myT.column5FS()
    #myT.column6TotalResourceDemand()
    #myT.column7TotalProgress()
    #myT.column8SubFeature()
    #myT.column95G_FTResource()
    #myT.column105G_FTProgress()
    #myT.column115GFTSub_Feature()
    #myT.column125G_FTProgress()
    #myT.column135G_FTProgressPerPlan()
    #myT.column14RAMInputComment()

if __name__ == '__main__':
    myTest()
