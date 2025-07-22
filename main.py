from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import datetime
import os
import sys
import shutil
import requests
import json

import ArmyFormationMapMainGUI
import ArmyFormationMapMainGUI_smallUI_MultiEQBt

IconImg_path = "GUIimg"
configFilePath = r"Main_config.json"

checkInListStatus = False
ClearInfoSec = 10

# 讀 config
with open(configFilePath, encoding="utf-8") as configFile:
    MainConfigDict = json.load(configFile, encoding="utf-8")
APIURL = MainConfigDict["APIURL"]
EQPID = MainConfigDict["EQPID"]
try:
    WorkEQ1 = MainConfigDict["WorkEQ1"]
except:
    WorkEQ1 = ""
try:
    WorkEQ2 = MainConfigDict["WorkEQ2"]
except:
    WorkEQ2 = ""
try:
    WorkEQ3 = MainConfigDict["WorkEQ3"]
except:
    WorkEQ3 = ""
try:
    WorkEQ4 = MainConfigDict["WorkEQ4"]
except:
    WorkEQ4 = ""
try:
    WorkEQ5 = MainConfigDict["WorkEQ5"]
except:
    WorkEQ5 = ""
try:
    WorkEQ6 = MainConfigDict["WorkEQ6"]
except:
    WorkEQ6 = ""

BGStyle = '''
    color: #2A3340;
    background-color: #E9F0F2;
'''

class Main(QMainWindow, ArmyFormationMapMainGUI_smallUI_MultiEQBt.Ui_MainWindow):
    # [主畫面] 開啟執行
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.centralwidget.setStyleSheet(BGStyle)
        self.setWindowIcon(QIcon(os.path.join(IconImg_path, 'card.png')))
        
        self.showMaximized()

        self.CardID.setFocus()

        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        # op = QtWidgets.QGraphicsOpacityEffect()
        # op.setOpacity(0)
        # self.CardID.setGraphicsEffect(op)
        
        # 資訊
        self.UserName = ''
        self.UserID = ''
        self.CardStatusTextStr = ''

        # 工作站點
        self.EQText.setText(EQPID)

        # 顯示/隱藏工作EQD 區域
        self.WorkEQcheckedStatus = False
        self.closeWorkEQDiv()

        # 選取工作區域
        self.clickEQStr = ''
        self.EQ1Bt.clicked.connect(lambda:self.clickEQButton('EQ1'))
        self.EQ2Bt.clicked.connect(lambda:self.clickEQButton('EQ2'))
        self.EQ3Bt.clicked.connect(lambda:self.clickEQButton('EQ3'))
        self.EQ4Bt.clicked.connect(lambda:self.clickEQButton('EQ4'))
        self.EQ5Bt.clicked.connect(lambda:self.clickEQButton('EQ5'))
        self.EQ6Bt.clicked.connect(lambda:self.clickEQButton('EQ6'))
        
        # 刷進人員清單
        self.GetCheckInList()
        self.CheckInList.itemClicked.connect(self.selectCheckInList)
        self.CheckInList.itemDoubleClicked.connect(self.selectCheckInList)
        self.CheckInList.itemEntered.connect(self.selectCheckInList)
        self.CheckInList.itemPressed.connect(self.selectCheckInList)
        self.CheckInList.itemActivated.connect(self.selectCheckInList)

        # 時鐘
        self.clockTimePoint = 0
        self.timer_clock = QtCore.QTimer()                           # 加入定時器
        self.timer_clock.timeout.connect(self.update_clock_QTimer)   # 設定定時要執行的 function
        self.timer_clock.start(1000)                                 # 啟用定時器，設定間隔時間

        # 寫入刷卡人資訊
        self.HID_State = False
        self.timer_HID = QtCore.QTimer()                       # 加入定時器
        self.timer_HID.timeout.connect(self.update_HID_info)   # 設定定時要執行的 function
        self.timer_HID.start(100)                              # 啟用定時器，設定間隔時間

        # 定期清空
        self.Clear_check_Count = 0
        self.timer_Clear = QtCore.QTimer()                          # 加入定時器
        self.timer_Clear.timeout.connect(self.update_clear_info)    # 設定定時要執行的 function
        self.timer_Clear.start(1000)                                # 啟用定時器，設定間隔時間

        # 抓資訊上拋
        self.timer_UploadInfo = QtCore.QTimer()                           # 加入定時器
        self.timer_UploadInfo.timeout.connect(self.update_checkin_info)   # 設定定時要執行的 function
        self.timer_UploadInfo.start(500)                                  # 啟用定時器，設定間隔時間
        
        # 拋存活
        self.update_SurviveInfo() # 打開先拋一次
        self.timer_SurviveInfo = QtCore.QTimer()                           # 加入定時器
        self.timer_SurviveInfo.timeout.connect(self.update_SurviveInfo)    # 設定定時要執行的 function
        self.timer_SurviveInfo.start(1800000)                              # 啟用定時器，設定間隔時間

    # 時間更新
    def update_clock_QTimer(self):
        # 現在時間
        datetime_dt = datetime.datetime.today()
        datetime_str = datetime_dt.strftime("%m-%d %H:%M")
        if self.clockTimePoint == 1:
            datetime_str = datetime_str.replace(":", " ")
            self.clockTimePoint = 0
            # 設置時間
            self.TimeText.display(datetime_str)
        else:
            # 設置時間
            self.TimeText.display(datetime_str)
            self.clockTimePoint += 1
    
    # 顯示/隱藏工作EQD 區域
    def closeWorkEQDiv(self):
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0)

        if WorkEQ1 != "":
            # 改名字
            self.EQ1Bt.setText(WorkEQ1)
        else:
            # # 隱藏
            # self.EQ1Title.setHidden(True)
            # self.EQ1Bt.setHidden(True)
            
            # 刪除
            self.delete_widgets_by_name(self.EQ1Div, self.EQ1Title, self.EQ1Bt)

            # 改區域占比
            self.EQClickButtomLayout.setColumnStretch(0, 1)

        if WorkEQ2 != "":
            # 改名字
            self.EQ2Bt.setText(WorkEQ2)
        else:
            # # 隱藏
            # self.EQ2Title.setHidden(True)
            # self.EQ2Bt.setHidden(True)
            
            # 刪除
            self.delete_widgets_by_name(self.EQ2Div, self.EQ2Title, self.EQ2Bt)
            
            # 改區域占比
            self.EQClickButtomLayout.setColumnStretch(1, 1)

        if WorkEQ3 != "":
            # 改名字
            self.EQ3Bt.setText(WorkEQ3)
        else:
            # # 隱藏
            # self.EQ3Title.setHidden(True)
            # self.EQ3Bt.setHidden(True)
            
            # 刪除
            self.delete_widgets_by_name(self.EQ3Div, self.EQ3Title, self.EQ3Bt)
            
            # 改區域占比
            self.EQClickButtomLayout.setColumnStretch(2, 1)

        if WorkEQ4 != "":
            # 改名字
            self.EQ4Bt.setText(WorkEQ4)
        else:
            # # 隱藏
            # self.EQ4Title.setHidden(True)
            # self.EQ4Bt.setHidden(True)
            
            # 刪除
            self.delete_widgets_by_name(self.EQ4Div, self.EQ4Title, self.EQ4Bt)
            
            # 改區域占比
            self.EQClickButtomLayout.setColumnStretch(3, 1)

        if WorkEQ5 != "":
            # 改名字
            self.EQ5Bt.setText(WorkEQ5)
        else:
            # # 隱藏
            # self.EQ5Title.setHidden(True)
            # self.EQ5Bt.setHidden(True)
            
            # 刪除
            self.delete_widgets_by_name(self.EQ5Div, self.EQ5Title, self.EQ5Bt)
            
            # 改區域占比
            self.EQClickButtomLayout.setColumnStretch(4, 1)

        if WorkEQ6 != "":
            # 改名字
            self.EQ6Bt.setText(WorkEQ6)
        else:
            # # 隱藏
            # self.EQ6Title.setHidden(True)
            # self.EQ6Bt.setHidden(True)
            
            # 刪除
            self.delete_widgets_by_name(self.EQ6Div, self.EQ6Title, self.EQ6Bt)
            
            # 改區域占比
            self.EQClickButtomLayout.setColumnStretch(5, 1)

    # 删除沒用到的widget
    def delete_widgets_by_name(self, widget, Title, Bt):
        widget.deleteLater()
        Title.deleteLater()
        Bt.deleteLater()

    # 點工作EQ BT 清掉其他BT狀態
    def clickEQButton(self, clickButtonName):
        if clickButtonName == "EQ1":
            self.clickEQStr = WorkEQ1
            try:
                self.EQ2Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ3Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ4Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ5Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ6Bt.setChecked(False)
            except:
                pass
        elif clickButtonName == "EQ2":
            self.clickEQStr = WorkEQ2
            try:
                self.EQ1Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ3Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ4Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ5Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ6Bt.setChecked(False)
            except:
                pass
        elif clickButtonName == "EQ3":
            self.clickEQStr = WorkEQ3
            try:
                self.EQ1Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ2Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ4Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ5Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ6Bt.setChecked(False)
            except:
                pass
        elif clickButtonName == "EQ4":
            self.clickEQStr = WorkEQ4
            try:
                self.EQ1Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ2Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ3Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ5Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ6Bt.setChecked(False)
            except:
                pass
        elif clickButtonName == "EQ5":
            try:
                self.clickEQStr = WorkEQ5
            except:
                pass
            try:
                self.EQ1Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ2Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ3Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ4Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ6Bt.setChecked(False)
            except:
                pass
        elif clickButtonName == "EQ6":
            try:
                self.clickEQStr = WorkEQ6
            except:
                pass
            try:
                self.EQ1Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ2Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ3Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ4Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ5Bt.setChecked(False)
            except:
                pass
        
        self.CardID.setFocus()

        # 改點擊狀態
        self.WorkEQcheckedStatus = True

    # 讀 HID 資訊, 查詢 HID 資訊 & 刷進刷出狀態
    def update_HID_info(self):
        CardIDText = self.CardID.text()
        if CardIDText != "" and not self.HID_State and len(CardIDText) == 8:
            self.HID_State = True
            # 查HID API取得資訊
            data ={
                "action_name": "ArmyFormationMap",
                "action_type":"Select_CardHID",
                "HID": CardIDText}
            proxy = "10.97.4.3:8080"
            timeoutSec = 60
            proxies = {
            "http": "http://"+proxy,
            "https": "http://"+proxy,
            }

            r=requests.post(APIURL + "sql_api/ArmyFormationMap_Web_API.asp?", data=json.dumps(data), proxies=proxies, timeout=timeoutSec)
            
            self.UserName = ''
            self.UserID = ''
            self.CardStatusTextStr = ''
            if len(r.json()['Data']) > 0:
                self.UserName = r.json()['Data'][0]['UserName']
                self.UserID = r.json()['Data'][0]['UserID']

                # 查刷卡狀態 API取得資訊
                data ={
                    "action_name": "ArmyFormationMap",
                    "action_type":"Select_CheckInStatus",
                    "CheckInUserID": self.UserID}
                proxy = "10.97.4.3:8080"
                timeoutSec = 60
                proxies = {
                "http": "http://"+proxy,
                "https": "http://"+proxy,
                }

                r=requests.post(APIURL + "sql_api/ArmyFormationMap_Web_API.asp?", data=json.dumps(data), proxies=proxies, timeout=timeoutSec)

                if len(r.json()['Data']) > 0:
                    CheckInStatus = r.json()['Data'][0]['CheckInStatus']
                    if CheckInStatus == '刷進(In)':
                        self.CardStatusTextStr = '刷出(Out)'
                    elif CheckInStatus == '刷出(Out)':
                        self.CardStatusTextStr = '刷進(In)'
                else:
                    self.CardStatusTextStr = '刷進(In)'

                if self.UserName != '' and self.CardStatusTextStr != '':
                    # 寫入資訊
                    self.CardUserText.setText(self.UserName)
                    self.CardStatusText.setText(self.CardStatusTextStr)
                else:
                    print("異常!!!, UserName:", self.UserName, '   CardStatusTextStr:', self.CardStatusTextStr)

            else:
                self.CardID.setText("")
                QMessageBox.critical(self,"Fail","查無此卡片資訊，請建立資料後再刷卡，感謝~",QMessageBox.Yes,QMessageBox.Yes)

            self.HID_State = False
        elif len(CardIDText) > 8:
            # 清空
            self.CardID.setText("")

    # 定期清空工作EQ選取狀態、刷卡人
    def update_clear_info(self):
        CardIDText = self.CardID.text()
        if self.WorkEQcheckedStatus or CardIDText != '':
            self.Clear_check_Count += 1
        
        if self.Clear_check_Count >= ClearInfoSec:
            # 刷卡人
            self.CardID.setText("")
            self.CardUserText.setText("Plz swipe your card")
            self.CardStatusText.setText("-")
            self.UserName = ''
            self.UserID = ''
            self.CardStatusTextStr = ''

            # 工作EQ
            try:
                self.EQ1Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ2Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ3Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ4Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ5Bt.setChecked(False)
            except:
                pass
            try:
                self.EQ6Bt.setChecked(False)
            except:
                pass
            self.WorkEQcheckedStatus = False
            self.clickEQStr = ''

            # 重新Focus
            self.CardID.setFocus()

            # 重製 count
            self.Clear_check_Count = 0
    
    # 刷進人員清單
    def GetCheckInList(self):
        # 清掉 List，重新加項目
        self.CheckInList.clear()

        # 查刷進人員列表 API取得資訊
        data ={
            "action_name": "ArmyFormationMap",
            "action_type":"Select_NowCheckInUser",
            "CheckInEQPID": EQPID}
        proxy = "10.97.4.3:8080"
        timeoutSec = 60
        proxies = {
        "http": "http://"+proxy,
        "https": "http://"+proxy,
        }

        r=requests.post(APIURL + "sql_api/ArmyFormationMap_Web_API.asp?", data=json.dumps(data), proxies=proxies, timeout=timeoutSec)
        
        if len(r.json()['Data']) > 0:
            icon = ""
            for i in r.json()['Data']:
                icon = QIcon(os.path.join(IconImg_path, 'user.png'))
                infoStr = f" {i['CheckInUserName']}  {i['ChekInTime'][5:-3]}"  # .strftime('%m-%d %H:%M')
                self.CheckInList.addItem(QListWidgetItem(icon, infoStr))

    # 選取人員清單
    def selectCheckInList(self):
        self.CardID.setFocus()

    # 資料寫入
    def update_checkin_info(self):
        if self.UserID != '' and self.UserName != '' and self.CardStatusTextStr != '' and self.WorkEQcheckedStatus:
            data ={
                "action_name": "ArmyFormationMap",
                "action_type":"Insert_UserCheckIn",
                "CheckInUserID": self.UserID,
                "CheckInUserName": self.UserName,
                "CheckInStatus": self.CardStatusTextStr,
                "CheckInEQPID": EQPID,
                "CheckInWorkEQ": self.clickEQStr}
            print(data)
            proxy = "10.97.4.3:8080"
            timeoutSec = 60
            proxies = {
            "http": "http://"+proxy,
            "https": "http://"+proxy,
            }

            r=requests.post(APIURL + "sql_api/ArmyFormationMap_Web_API.asp?", data=json.dumps(data, default=str), proxies=proxies, timeout=timeoutSec)
            
            time.sleep(1)
            # 強制大於重製秒數
            self.Clear_check_Count = ClearInfoSec
            self.update_clear_info()

            self.GetCheckInList()

    # 上拋存活
    def update_SurviveInfo(self):
        data ={
            "action_name": "ArmyFormationMap",
            "action_type":"Insert_Survive",
            "EQPID": EQPID,
            "checkInType": '刷卡機'}
        proxy = "10.97.4.3:8080"
        timeoutSec = 60
        proxies = {
        "http": "http://"+proxy,
        "https": "http://"+proxy,
        }

        r=requests.post(APIURL + "sql_api/ArmyFormationMap_Web_API.asp?", data=json.dumps(data, default=str), proxies=proxies, timeout=timeoutSec)
        

    def closeEvent(self, event):
        print('window close')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    
    sys.exit(app.exec_())
    
