# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArmyFormationMapMainGUI_smallUI_MultiEQBt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 714)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/JonnyGHChen/.designer/backup/GUIimg/card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.EQClickButtomLayout = QtWidgets.QGridLayout()
        self.EQClickButtomLayout.setContentsMargins(-1, 15, -1, -1)
        self.EQClickButtomLayout.setObjectName("EQClickButtomLayout")
        self.EQ5Div = QtWidgets.QVBoxLayout()
        self.EQ5Div.setContentsMargins(-1, 10, -1, -1)
        self.EQ5Div.setObjectName("EQ5Div")
        self.EQ5Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EQ5Title.setFont(font)
        self.EQ5Title.setAlignment(QtCore.Qt.AlignCenter)
        self.EQ5Title.setObjectName("EQ5Title")
        self.EQ5Div.addWidget(self.EQ5Title)
        self.EQ5Bt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EQ5Bt.sizePolicy().hasHeightForWidth())
        self.EQ5Bt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.EQ5Bt.setFont(font)
        self.EQ5Bt.setStyleSheet("QPushButton {\n"
"                background-color: #7E5399;\n"
"                color: #FFFFFF;\n"
"                border-style: outset;\n"
"                padding: 2px;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: #583A68;\n"
"            }\n"
"QPushButton:checked{\n"
"                    background-color: #e9b311;\n"
"                }")
        self.EQ5Bt.setCheckable(True)
        self.EQ5Bt.setObjectName("EQ5Bt")
        self.EQ5Div.addWidget(self.EQ5Bt)
        self.EQ5Div.setStretch(0, 10)
        self.EQ5Div.setStretch(1, 90)
        self.EQClickButtomLayout.addLayout(self.EQ5Div, 1, 4, 1, 1)
        self.EQ1Div = QtWidgets.QVBoxLayout()
        self.EQ1Div.setContentsMargins(-1, 10, -1, -1)
        self.EQ1Div.setObjectName("EQ1Div")
        self.EQ1Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EQ1Title.setFont(font)
        self.EQ1Title.setAlignment(QtCore.Qt.AlignCenter)
        self.EQ1Title.setObjectName("EQ1Title")
        self.EQ1Div.addWidget(self.EQ1Title)
        self.EQ1Bt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EQ1Bt.sizePolicy().hasHeightForWidth())
        self.EQ1Bt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.EQ1Bt.setFont(font)
        self.EQ1Bt.setStyleSheet("QPushButton {\n"
"                background-color: #7E5399;\n"
"                color: #FFFFFF;\n"
"                border-style: outset;\n"
"                padding: 2px;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: #583A68;\n"
"            }\n"
"QPushButton:checked{\n"
"                    background-color: #e9b311;\n"
"                }")
        self.EQ1Bt.setCheckable(True)
        self.EQ1Bt.setObjectName("EQ1Bt")
        self.EQ1Div.addWidget(self.EQ1Bt)
        self.EQ1Div.setStretch(0, 10)
        self.EQ1Div.setStretch(1, 90)
        self.EQClickButtomLayout.addLayout(self.EQ1Div, 1, 0, 1, 1)
        self.EQ2Div = QtWidgets.QVBoxLayout()
        self.EQ2Div.setContentsMargins(-1, 10, -1, -1)
        self.EQ2Div.setObjectName("EQ2Div")
        self.EQ2Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EQ2Title.setFont(font)
        self.EQ2Title.setAlignment(QtCore.Qt.AlignCenter)
        self.EQ2Title.setObjectName("EQ2Title")
        self.EQ2Div.addWidget(self.EQ2Title)
        self.EQ2Bt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EQ2Bt.sizePolicy().hasHeightForWidth())
        self.EQ2Bt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.EQ2Bt.setFont(font)
        self.EQ2Bt.setStyleSheet("QPushButton {\n"
"                background-color: #7E5399;\n"
"                color: #FFFFFF;\n"
"                border-style: outset;\n"
"                padding: 2px;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: #583A68;\n"
"            }\n"
"QPushButton:checked{\n"
"                    background-color: #e9b311;\n"
"                }")
        self.EQ2Bt.setCheckable(True)
        self.EQ2Bt.setChecked(False)
        self.EQ2Bt.setObjectName("EQ2Bt")
        self.EQ2Div.addWidget(self.EQ2Bt)
        self.EQ2Div.setStretch(0, 10)
        self.EQ2Div.setStretch(1, 90)
        self.EQClickButtomLayout.addLayout(self.EQ2Div, 1, 1, 1, 1)
        self.EQ3Div = QtWidgets.QVBoxLayout()
        self.EQ3Div.setContentsMargins(-1, 10, -1, -1)
        self.EQ3Div.setObjectName("EQ3Div")
        self.EQ3Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EQ3Title.setFont(font)
        self.EQ3Title.setAlignment(QtCore.Qt.AlignCenter)
        self.EQ3Title.setObjectName("EQ3Title")
        self.EQ3Div.addWidget(self.EQ3Title)
        self.EQ3Bt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EQ3Bt.sizePolicy().hasHeightForWidth())
        self.EQ3Bt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.EQ3Bt.setFont(font)
        self.EQ3Bt.setStyleSheet("QPushButton {\n"
"                background-color: #7E5399;\n"
"                color: #FFFFFF;\n"
"                border-style: outset;\n"
"                padding: 2px;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: #583A68;\n"
"            }\n"
"QPushButton:checked{\n"
"                    background-color: #e9b311;\n"
"                }")
        self.EQ3Bt.setCheckable(True)
        self.EQ3Bt.setObjectName("EQ3Bt")
        self.EQ3Div.addWidget(self.EQ3Bt)
        self.EQ3Div.setStretch(0, 10)
        self.EQ3Div.setStretch(1, 90)
        self.EQClickButtomLayout.addLayout(self.EQ3Div, 1, 2, 1, 1)
        self.EQ4Div = QtWidgets.QVBoxLayout()
        self.EQ4Div.setContentsMargins(-1, 10, -1, -1)
        self.EQ4Div.setObjectName("EQ4Div")
        self.EQ4Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EQ4Title.setFont(font)
        self.EQ4Title.setAlignment(QtCore.Qt.AlignCenter)
        self.EQ4Title.setObjectName("EQ4Title")
        self.EQ4Div.addWidget(self.EQ4Title)
        self.EQ4Bt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EQ4Bt.sizePolicy().hasHeightForWidth())
        self.EQ4Bt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.EQ4Bt.setFont(font)
        self.EQ4Bt.setStyleSheet("QPushButton {\n"
"                background-color: #7E5399;\n"
"                color: #FFFFFF;\n"
"                border-style: outset;\n"
"                padding: 2px;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: #583A68;\n"
"            }\n"
"QPushButton:checked{\n"
"                    background-color: #e9b311;\n"
"                }")
        self.EQ4Bt.setCheckable(True)
        self.EQ4Bt.setObjectName("EQ4Bt")
        self.EQ4Div.addWidget(self.EQ4Bt)
        self.EQ4Div.setStretch(0, 10)
        self.EQ4Div.setStretch(1, 90)
        self.EQClickButtomLayout.addLayout(self.EQ4Div, 1, 3, 1, 1)
        self.EQ6Div = QtWidgets.QVBoxLayout()
        self.EQ6Div.setContentsMargins(-1, 10, -1, -1)
        self.EQ6Div.setObjectName("EQ6Div")
        self.EQ6Title = QtWidgets.QLabel(self.centralwidget)
        self.EQ6Title.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EQ6Title.setFont(font)
        self.EQ6Title.setAlignment(QtCore.Qt.AlignCenter)
        self.EQ6Title.setObjectName("EQ6Title")
        self.EQ6Div.addWidget(self.EQ6Title)
        self.EQ6Bt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EQ6Bt.sizePolicy().hasHeightForWidth())
        self.EQ6Bt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.EQ6Bt.setFont(font)
        self.EQ6Bt.setStyleSheet("QPushButton {\n"
"                background-color: #7E5399;\n"
"                color: #FFFFFF;\n"
"                border-style: outset;\n"
"                padding: 2px;\n"
"                border-width: 3px;\n"
"                border-radius: 10px;\n"
"                border-color: #583A68;\n"
"            }\n"
"QPushButton:checked{\n"
"                    background-color: #e9b311;\n"
"                }")
        self.EQ6Bt.setCheckable(True)
        self.EQ6Bt.setObjectName("EQ6Bt")
        self.EQ6Div.addWidget(self.EQ6Bt)
        self.EQ6Div.setStretch(0, 10)
        self.EQ6Div.setStretch(1, 90)
        self.EQClickButtomLayout.addLayout(self.EQ6Div, 1, 5, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setStyleSheet("QWidget{\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    border-color:#131B63;\n"
"    border-radius: 10px;\n"
"    background: #131B63;\n"
"}")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.EQClickButtomLayout.addWidget(self.line_3, 0, 0, 1, 6)
        self.EQClickButtomLayout.setColumnStretch(0, 20)
        self.EQClickButtomLayout.setColumnStretch(1, 20)
        self.EQClickButtomLayout.setColumnStretch(2, 20)
        self.EQClickButtomLayout.setColumnStretch(3, 20)
        self.EQClickButtomLayout.setColumnStretch(4, 20)
        self.EQClickButtomLayout.setColumnStretch(5, 20)
        self.EQClickButtomLayout.setRowStretch(0, 10)
        self.gridLayout_4.addLayout(self.EQClickButtomLayout, 1, 0, 1, 1)
        self.CheckInInfoLayout = QtWidgets.QGridLayout()
        self.CheckInInfoLayout.setObjectName("CheckInInfoLayout")
        self.CheckInList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckInList.sizePolicy().hasHeightForWidth())
        self.CheckInList.setSizePolicy(sizePolicy)
        self.CheckInList.setMinimumSize(QtCore.QSize(491, 416))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.CheckInList.setFont(font)
        self.CheckInList.setStyleSheet("QWidget{\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    border-color:#024302;\n"
"    border-radius: 10px;\n"
"    background: #B4D9AD;\n"
"}")
        self.CheckInList.setAutoScroll(True)
        self.CheckInList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.CheckInList.setIconSize(QtCore.QSize(40, 40))
        self.CheckInList.setResizeMode(QtWidgets.QListView.Fixed)
        self.CheckInList.setObjectName("CheckInList")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/JonnyGHChen/.designer/backup/GUIimg/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.CheckInList.addItem(item)
        self.CheckInInfoLayout.addWidget(self.CheckInList, 1, 0, 1, 1)
        self.CheckInTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.CheckInTitle.setFont(font)
        self.CheckInTitle.setStyleSheet("QWidget{\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    border-color:#594022;\n"
"    border-radius: 10px;\n"
"    background-color: #88B0BF;\n"
"    background: #FFF7DB;\n"
"}")
        self.CheckInTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.CheckInTitle.setObjectName("CheckInTitle")
        self.CheckInInfoLayout.addWidget(self.CheckInTitle, 0, 0, 1, 1)
        self.CheckInInfoLayout.setRowStretch(0, 10)
        self.CheckInInfoLayout.setRowStretch(1, 90)
        self.gridLayout_4.addLayout(self.CheckInInfoLayout, 1, 1, 1, 1)
        self.EQInfoLayout = QtWidgets.QGridLayout()
        self.EQInfoLayout.setContentsMargins(-1, 20, -1, -1)
        self.EQInfoLayout.setObjectName("EQInfoLayout")
        self.EQInfoDiv = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.EQInfoDiv.setFont(font)
        self.EQInfoDiv.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EQInfoDiv.setAutoFillBackground(False)
        self.EQInfoDiv.setStyleSheet("QWidget{\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    border-color:#024302;\n"
"    border-radius: 10px;\n"
"    background: #B4D9AD;\n"
"}")
        self.EQInfoDiv.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.EQInfoDiv.setObjectName("EQInfoDiv")
        self.formLayout = QtWidgets.QFormLayout(self.EQInfoDiv)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.EQTitle = QtWidgets.QLabel(self.EQInfoDiv)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.EQTitle.setFont(font)
        self.EQTitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EQTitle.setStyleSheet("QLabel {\n"
"    background-color: #B4D9AD;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"}")
        self.EQTitle.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EQTitle.setObjectName("EQTitle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.EQTitle)
        self.EQText = QtWidgets.QLabel(self.EQInfoDiv)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.EQText.setFont(font)
        self.EQText.setStyleSheet("QLabel {\n"
"    background-color: #B4D9AD;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"}")
        self.EQText.setAlignment(QtCore.Qt.AlignCenter)
        self.EQText.setObjectName("EQText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.EQText)
        self.line = QtWidgets.QFrame(self.EQInfoDiv)
        self.line.setStyleSheet("Line{\n"
"    border-width:3px;\n"
"    border-color:#024302;\n"
"    background: #024302;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.TimeTitle = QtWidgets.QLabel(self.EQInfoDiv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TimeTitle.sizePolicy().hasHeightForWidth())
        self.TimeTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.TimeTitle.setFont(font)
        self.TimeTitle.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.TimeTitle.setAutoFillBackground(False)
        self.TimeTitle.setStyleSheet("QLabel {\n"
"    background-color: #B4D9AD;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"}")
        self.TimeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeTitle.setObjectName("TimeTitle")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.TimeTitle)
        self.TimeText = QtWidgets.QLCDNumber(self.EQInfoDiv)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.TimeText.setFont(font)
        self.TimeText.setStyleSheet("QLCDNumber {\n"
"    background-color: #729b6a;\n"
"    border-width: 2px;\n"
"    border-color:#024302;\n"
"    border-radius: 5px;\n"
"}")
        self.TimeText.setDigitCount(11)
        self.TimeText.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.TimeText.setProperty("value", -2147483648.0)
        self.TimeText.setProperty("intValue", -2147483648)
        self.TimeText.setObjectName("TimeText")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.TimeText)
        self.EQInfoLayout.addWidget(self.EQInfoDiv, 0, 0, 1, 1)
        self.CardInfoDiv = QtWidgets.QWidget(self.centralwidget)
        self.CardInfoDiv.setStyleSheet("QWidget{\n"
"    border-style:solid;\n"
"    border-width:3px;\n"
"    border-color:#024302;\n"
"    border-radius: 10px;\n"
"    background: #B4D9AD;\n"
"}")
        self.CardInfoDiv.setObjectName("CardInfoDiv")
        self.formLayout_2 = QtWidgets.QFormLayout(self.CardInfoDiv)
        self.formLayout_2.setContentsMargins(20, 20, 20, 20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.CardUserTitle = QtWidgets.QLabel(self.CardInfoDiv)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.CardUserTitle.setFont(font)
        self.CardUserTitle.setStyleSheet("QLabel {\n"
"    background-color: #B4D9AD;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"}")
        self.CardUserTitle.setObjectName("CardUserTitle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.CardUserTitle)
        self.line_2 = QtWidgets.QFrame(self.CardInfoDiv)
        self.line_2.setStyleSheet("Line{\n"
"    border-width:3px;\n"
"    border-color:#024302;\n"
"    background: #024302;\n"
"}")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.CardStatusTitle = QtWidgets.QLabel(self.CardInfoDiv)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.CardStatusTitle.setFont(font)
        self.CardStatusTitle.setStyleSheet("QLabel {\n"
"    background-color: #B4D9AD;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"}")
        self.CardStatusTitle.setObjectName("CardStatusTitle")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.CardStatusTitle)
        self.CardStatusText = QtWidgets.QLabel(self.CardInfoDiv)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.CardStatusText.setFont(font)
        self.CardStatusText.setStyleSheet("QLabel {\n"
"    background-color: #B4D9AD;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"}")
        self.CardStatusText.setAlignment(QtCore.Qt.AlignCenter)
        self.CardStatusText.setObjectName("CardStatusText")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CardStatusText)
        self.CardUserText = QtWidgets.QLabel(self.CardInfoDiv)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(15)
        self.CardUserText.setFont(font)
        self.CardUserText.setStyleSheet("QLabel {\n"
"    background-color: #B4D9AD;\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"}")
        self.CardUserText.setAlignment(QtCore.Qt.AlignCenter)
        self.CardUserText.setObjectName("CardUserText")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CardUserText)
        self.EQInfoLayout.addWidget(self.CardInfoDiv, 0, 2, 1, 1)
        self.CardID = QtWidgets.QLineEdit(self.centralwidget)
        self.CardID.setObjectName("CardID")
        self.EQInfoLayout.addWidget(self.CardID, 0, 1, 1, 1)
        self.EQInfoLayout.setColumnStretch(0, 47)
        self.EQInfoLayout.setColumnStretch(1, 6)
        self.EQInfoLayout.setColumnStretch(2, 47)
        self.gridLayout_4.addLayout(self.EQInfoLayout, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_4.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 60)
        self.gridLayout_4.setColumnStretch(1, 40)
        self.gridLayout_4.setRowStretch(0, 30)
        self.gridLayout_4.setRowStretch(1, 40)
        self.gridLayout_4.setRowStretch(2, 30)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "L8A 刷卡"))
        self.EQ5Title.setText(_translate("MainWindow", "EQ5"))
        self.EQ5Bt.setText(_translate("MainWindow", "XXX500"))
        self.EQ1Title.setText(_translate("MainWindow", "EQ1"))
        self.EQ1Bt.setText(_translate("MainWindow", "XXX100"))
        self.EQ2Title.setText(_translate("MainWindow", "EQ2"))
        self.EQ2Bt.setText(_translate("MainWindow", "XXX200"))
        self.EQ3Title.setText(_translate("MainWindow", "EQ3"))
        self.EQ3Bt.setText(_translate("MainWindow", "XXX300"))
        self.EQ4Title.setText(_translate("MainWindow", "EQ4"))
        self.EQ4Bt.setText(_translate("MainWindow", "XXX400"))
        self.EQ6Title.setText(_translate("MainWindow", "EQ6"))
        self.EQ6Bt.setText(_translate("MainWindow", "XXX600"))
        __sortingEnabled = self.CheckInList.isSortingEnabled()
        self.CheckInList.setSortingEnabled(False)
        item = self.CheckInList.item(0)
        item.setText(_translate("MainWindow", " 陳冠宏 05/09 02:53"))
        self.CheckInList.setSortingEnabled(__sortingEnabled)
        self.CheckInTitle.setText(_translate("MainWindow", "Login Personnel List"))
        self.EQTitle.setText(_translate("MainWindow", "EQP："))
        self.EQText.setText(_translate("MainWindow", "EQP Name"))
        self.TimeTitle.setText(_translate("MainWindow", "Time："))
        self.CardUserTitle.setText(_translate("MainWindow", "Name："))
        self.CardStatusTitle.setText(_translate("MainWindow", "State："))
        self.CardStatusText.setText(_translate("MainWindow", "-"))
        self.CardUserText.setText(_translate("MainWindow", "Plz swipe your card"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
