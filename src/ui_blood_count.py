# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledXXVeaK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from resizable_label import ResizableLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAcceptDrops(True)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")

        self.verticalLayout.addWidget(self.loadButton)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalWidget_2 = QWidget(self.centralwidget)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setMinimumSize(QSize(0, 40))
        self.horizontalWidget_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.horizontalWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.erythrocyteLabel = QLabel(self.horizontalWidget_2)
        self.erythrocyteLabel.setObjectName(u"erythrocyteLabel")

        self.horizontalLayout_3.addWidget(self.erythrocyteLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.horizontalWidget_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.inputImage = ResizableLabel(self.groupBox)
        self.inputImage.setObjectName(u"inputImage")
        self.inputImage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.inputImage)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.outputImage = ResizableLabel(self.groupBox_2)
        self.outputImage.setObjectName(u"outputImage")
        self.outputImage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.outputImage)


        self.verticalLayout_4.addWidget(self.groupBox_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.intermediateImage = ResizableLabel(self.groupBox_3)
        self.intermediateImage.setObjectName(u"intermediateImage")
        self.intermediateImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.intermediateImage)

        self.horizontalWidget_21 = QWidget(self.groupBox_3)
        self.horizontalWidget_21.setObjectName(u"horizontalWidget_21")
        self.horizontalWidget_21.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_21)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.horizontalWidget_21)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.stageLabel = QLabel(self.horizontalWidget_21)
        self.stageLabel.setObjectName(u"stageLabel")

        self.horizontalLayout_2.addWidget(self.stageLabel)


        self.verticalLayout_6.addWidget(self.horizontalWidget_21)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.previousButton = QPushButton(self.groupBox_3)
        self.previousButton.setObjectName(u"previousButton")

        self.horizontalLayout_4.addWidget(self.previousButton)

        self.nextButton = QPushButton(self.groupBox_3)
        self.nextButton.setObjectName(u"nextButton")

        self.horizontalLayout_4.addWidget(self.nextButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addWidget(self.groupBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Blood Count", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of erythocytes:", None))
        self.erythrocyteLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.inputImage.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output Image", None))
        self.outputImage.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Intermediate Image", None))
        self.intermediateImage.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stage:", None))
        self.stageLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.previousButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u">", None))
    # retranslateUi

