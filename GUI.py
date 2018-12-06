# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import qdarkstyle
import pyqtgraph as pg
import numpy as np
import pandas as pd
import datetime
import time
import matplotlib.pyplot as plt
import calendar

config = {
    'apiKey' : 'AIzaSyC6AVSfidmgJtRioSQBgvP4nvv-qzy5XtU',
    "authDomain": "feldamobile-app.firebaseapp.com",
    "databaseURL": "https://feldamobile-app.firebaseio.com",
    "storageBucket": "feldamobile-app.appspot.com"
}

class Ui_Felda(object):
    def __init__(self,parent = None):
        super(Ui_Felda,self).__init__()
        Felda.setObjectName("Felda")
        Felda.resize(1960, 1080)

        self.event_data = []
        self.centralwidget = QtWidgets.QWidget(Felda)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 200))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.Fixed_complaints = QtWidgets.QLCDNumber(self.centralwidget)
        self.Fixed_complaints.setObjectName("Fixed_complaints")
        self.verticalLayout.addWidget(self.Fixed_complaints)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout.addWidget(self.lcdNumber_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Over_Budget = QtWidgets.QCheckBox(self.centralwidget)
        self.Over_Budget.setObjectName("Over_Budget")
        self.horizontalLayout.addWidget(self.Over_Budget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.MainMap = QtWidgets.QTabWidget(self.centralwidget)
        self.MainMap.setMinimumSize(QtCore.QSize(600, 300))
        self.MainMap.setObjectName("MainMap")

        self.Event_Table = QtWidgets.QWidget()
        self.Event_Table.setObjectName("Event_Table")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Event_Table)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.Event_Table)
        self.tableWidget.setRowCount(200)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.MainMap.addTab(self.Event_Table, "")
        self.Item_table = QtWidgets.QWidget()
        self.Item_table.setObjectName("Item_table")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Item_table)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 576, 665))
        self.tableWidget_2.setRowCount(200)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setObjectName("tableWidget_2")

        self.MainMap.addTab(self.Item_table, "")
        self.Statistics = QtWidgets.QWidget()
        self.Statistics.setObjectName("Statistics")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Statistics)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MainMap.addTab(self.Statistics, "")
        self.gridLayout.addWidget(self.MainMap, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Pending_complaints = QtWidgets.QLCDNumber(self.centralwidget)
        self.Pending_complaints.setObjectName("Pending_complaints")
        self.verticalLayout_2.addWidget(self.Pending_complaints)
        spacerItem = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.Event_List = QtWidgets.QListWidget(self.centralwidget)
        self.Event_List.setObjectName("Event_List")
        item = QtWidgets.QListWidgetItem()
        self.Event_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Event_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Event_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Event_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Event_List.addItem(item)
        self.verticalLayout_2.addWidget(self.Event_List)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        Felda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Felda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLiscence = QtWidgets.QMenu(self.menubar)
        self.menuLiscence.setObjectName("menuLiscence")
        Felda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Felda)
        self.statusbar.setObjectName("statusbar")
        Felda.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(Felda)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(Felda)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Felda)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuLiscence.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuLiscence.menuAction())

        self.retranslateUi(Felda)
        self.MainMap.setCurrentIndex(1)
        self.Event_List.itemSelectionChanged.connect(self.viewDetails)
        self.Event_List.itemClicked.connect(self.viewDetails)
        QtCore.QMetaObject.connectSlotsByName(Felda)

    def get_data(self):
        self.firebase = pyrebase.initialize_app(config)

        self.db = self.firebase.database()
        self.df= self.db.child('userProfile').get().val()

        self.costs = []
        self.item_costs = []
        self.item_names = []
        self.item_emails = []
        self.item_dates = []
        self.revenue = []
        self.dates = []
        self.emails = []
        #getting list of events
        for users,user_info in self.df.items():
            for user_key in user_info:
                for events, event_info in user_info['eventList'].items():
                    self.emails.append(user_info['email'])
                    self.costs.append(event_info['cost'])
                    self.revenue.append(event_info['revenue'])
                    self.dates.append(event_info['date'])
                    if "itemList" in event_info:
                        for item, item_info in event_info['itemList'].items():
                            self.item_costs.append(item_info['price'])
                            self.item_emails.append(user_info['email'])
                            self.item_names.append(item_info['name'])
                            self.item_dates.append(event_info['date'])

        self.event_data = pd.DataFrame(
            {'email':self.emails,
             'cost': self.costs,
             'date': self.dates,
             'revenue': self.revenue
            })
        self.item_data = pd.DataFrame(
            {'name': self.item_names,
             'cost': self.item_costs,
             'date': self.item_dates,
             'email': self.item_emails
            })


    def fillList(self):

        self.Event_List.clear()
        for count, row in enumerate(self.event_data.index.values):
            item = QtWidgets.QListWidgetItem()
            self.Event_List.addItem(item)
            item = self.Event_List.item(count)
            item.setText(str(self.event_data['email'][row]) +' @ ' + str(self.event_data['date'][row]))

    def fill_item(item, value):
        item.setExpanded(True)
        if type(value) is dict:
          for key, val in sorted(value.iteritems()):
            child = QTreeWidgetItem()
            child.setText(0, unicode(key))
            item.addChild(child)
            fill_item(child, val)
        elif type(value) is list:
          for val in value:
            child = QTreeWidgetItem()
            item.addChild(child)
            if type(val) is dict:
              child.setText(0, '[dict]')
              fill_item(child, val)
            elif type(val) is list:
              child.setText(0, '[list]')
              fill_item(child, val)
            else:
              child.setText(0, unicode(val))
            child.setExpanded(True)
        else:
          child = QTreeWidgetItem()
          child.setText(0, unicode(value))
          item.addChild(child)

        def fill_widget(widget, value):
          widget.clear()
          fill_item(widget.invisibleRootItem(), value)



    def retranslateUi(self, Felda):
        _translate = QtCore.QCoreApplication.translate
        Felda.setWindowTitle(_translate("Felda", "Felda"))
        self.label_5.setText(_translate("Felda", "TextLabel"))
        self.label_2.setText(_translate("Felda", "Number of events this month"))
        self.label_3.setText(_translate("Felda", "Total Cash Spent this month (RM)"))
        self.label_4.setText(_translate("Felda", "Average Spending per event (RM)"))
        self.Over_Budget.setText(_translate("Felda", "OverBudget"))
        self.MainMap.setToolTip(_translate("Felda", "<html><head/><body><p>sdafasdf</p></body></html>"))
        self.MainMap.setWhatsThis(_translate("Felda", "<html><head/><body><p>sadasd</p></body></html>"))
        self.MainMap.setTabText(self.MainMap.indexOf(self.Event_Table), _translate("Felda", "Event Table"))
        self.MainMap.setTabText(self.MainMap.indexOf(self.Item_table), _translate("Felda", "Item table"))
        self.MainMap.setTabText(self.MainMap.indexOf(self.Statistics), _translate("Felda", "Statistics"))
        self.label.setText(_translate("Felda", "Number of Active Users"))
        __sortingEnabled = self.Event_List.isSortingEnabled()
        self.Event_List.setSortingEnabled(False)
        item = self.Event_List.item(0)
        item.setText(_translate("Felda", "Newest Report"))
        item = self.Event_List.item(1)
        item.setText(_translate("Felda", "2nd Newest Report"))
        item = self.Event_List.item(2)
        item.setText(_translate("Felda", "3rd Newest Report"))
        item = self.Event_List.item(3)
        item.setText(_translate("Felda", "Can\'t add anything yet without the database"))
        item = self.Event_List.item(4)
        item.setText(_translate("Felda", "Hadi for president"))
        self.Event_List.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Felda", "Last Week Summary"))
        self.menuFile.setTitle(_translate("Felda", "File"))
        self.menuEdit.setTitle(_translate("Felda", "Edit"))
        self.menuHelp.setTitle(_translate("Felda", "Help"))
        self.menuLiscence.setTitle(_translate("Felda", "License"))
        self.actionAbout.setText(_translate("Felda", "About"))
        self.actionOpen.setText(_translate("Felda", "Open"))
        self.actionSave.setText(_translate("Felda", "Save"))
        self.get_data()
        self.fillList()


class TableWidget(QtWidgets.QTableWidget):
    def __init__(self, df, parent=None):
        QtWidgets.QTableWidget.__init__(self)
        self.df = df
        self.fillTable(df)
        self.setHorizontalHeaderLabels(df.columns)

    def fillTable(self, df):
        #Self Explanatory
        self.clearContents()# Clear previous content
        nRows = len(self.df.index)
        nColumns = len(self.df.columns)
        self.setRowCount(nRows)
        self.setColumnCount(nColumns)
        self.setSortingEnabled(True)

        #Ez stuffz
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                x = self.df.iloc[i, j]
                self.setItem(i, j, QtWidgets.QTableWidgetItem(str(x)))

    def getNewValues(self, df):
        self.fillTable(df)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Felda = QtWidgets.QMainWindow()
    ui = Ui_Felda()
    ui.__init__(Felda)
    Felda.show()
    sys.exit(app.exec_())

