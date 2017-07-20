#-*- coding:UTF-8 -*-
#@ 2017/7/18
#@ author:FuYuQian
#@ content: pytest of FeatureDashBoard.py
#1  完成了最基本的函数调用测试
#2  待改进：
#3       在pytest中增加函数返回值的与设想值的判断
#4       下次边写函数边测试，而不是全部写完再写test_文件
#5       在原文件中增加一些try,catch语句，更加方便。
import pytest
from FeatureDashBoard import*

class TestFeatureDashBoard(object):

    def setup_class(self):
        self.myT=FeatureDashBoard()

    def test_H1title(self):
        aim="Feature Dashboard"
        title=self.myT.H1title()
        assert (aim==title)

    def test_ol(self):
        aimlist=[1,"Release mgmt.","Feature Dashboard"]
        list=self.myT.ol()
        for i in range(len(aimlist)):
            assert (aimlist[i]==list[i])

    def test_h3(self):
        aimlist=["Feature Dashboard",1]
        list=self.myT.h3()
        for i in range(len(aimlist)):
            assert (aimlist[i]==list[i])

    def test_footer(self):
        aim=1
        succ=self.myT.footer()
        assert(aim==succ)

    def test_dataTables_length(self):
        aimlist=['10','25','50','100']
        list=self.myT.dataTables_length()
        for i in range(len(aimlist)):
            assert (aimlist[i]==list[i])

    def test_systemRelease(self):
        aim=1
        succ=self.myT.systemRelease()
        assert (aim==succ)

    def test_RnDCommitment(self):
        aim=1
        succ=self.myT.RnDCommitment()
        assert(aim==succ)

    def test_viewSelect(self):
        aim=1
        succ=self.myT.viewSelect()
        assert(aim==succ)

    def test_search(self):
        aim=1
        succ=self.myT.search()
        assert(aim==succ)

    def test_normalHead(self):
        aimlist=["Name","Feature Component Title","RAM","Contribution from External BLs","FS Status","Total Resource Demand[h]","Total Progress","Sub-Feature Completion","5G_FT Resource Demand[h]","5G_FT Progress","5G_FT Sub-Feature Completion","5G_FT Progress Per Plan","RAM Input Status"]
        list=self.myT.normalHead()
        for i in range(len(aimlist)):
            assert(aimlist[i]==list[i])

    def test_column1Name(self):
        self.myT.column1Name()

    def test_column2FeatureComponentTitle(self):
        self.myT.column2FeatureComponentTitle()

    def test_column3Ram(self):
         self.myT.column3Ram()

    def test_column4Contributionfrom(self):
        self.myT.column4Contributionfrom()

    def test_column5FS(self):
        self.myT.column5FS()

    def test_column6TotalResourceDemand(self):
        self.myT.column6TotalResourceDemand()

    def test_column7TotalProgress(self):
        self.myT.column7TotalProgress()

    def test_column8SubFeature(self):
        self.myT.column8SubFeature()

    def test_column95G_FTResource(self):
        self.myT.column95G_FTResource()

    def test_column105G_FTProgress(self):
        self.myT.column105G_FTProgress()

    def test_column115GFTSub_Feature(self):
        self.myT.column115GFTSub_Feature()

    def test_column125G_FTProgress(self):
        self.myT.column125G_FTProgress()

    def test_column135G_FTProgressPerPlan(self):
        self.myT.column135G_FTProgressPerPlan()

    def test_column14RAMInputComment(self):
        self.myT.column14RAMInputComment()


    def teardown_class(self):
        self.myT.driver.quit()
        pass

if __name__=='__main__':
    pytest.main("test_FeatureDashBoard.py")
