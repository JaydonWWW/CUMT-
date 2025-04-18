# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bmi_cal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_BMI计算器(object):
    def setupUi(self, BMI计算器):
        if not BMI计算器.objectName():
            BMI计算器.setObjectName(u"BMI\u8ba1\u7b97\u5668")
        BMI计算器.resize(500, 200)
        BMI计算器.setMinimumSize(QSize(500, 200))
        BMI计算器.setMaximumSize(QSize(500, 200))
        self.centralwidget = QWidget(BMI计算器)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 200))
        self.centralwidget.setMaximumSize(QSize(500, 200))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 40))
        self.label.setMaximumSize(QSize(80, 40))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI Light"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 40))
        self.label_2.setMaximumSize(QSize(80, 40))
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 40))
        self.label_3.setMaximumSize(QSize(90, 40))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.weightLine = QLineEdit(self.centralwidget)
        self.weightLine.setObjectName(u"weightLine")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightLine.sizePolicy().hasHeightForWidth())
        self.weightLine.setSizePolicy(sizePolicy)
        self.weightLine.setMinimumSize(QSize(300, 40))
        self.weightLine.setMaximumSize(QSize(300, 40))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.weightLine)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_4)

        self.heightLine = QLineEdit(self.centralwidget)
        self.heightLine.setObjectName(u"heightLine")
        sizePolicy.setHeightForWidth(self.heightLine.sizePolicy().hasHeightForWidth())
        self.heightLine.setSizePolicy(sizePolicy)
        self.heightLine.setMinimumSize(QSize(300, 40))
        self.heightLine.setMaximumSize(QSize(300, 40))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.heightLine)

        self.bmi = QLineEdit(self.centralwidget)
        self.bmi.setObjectName(u"bmi")
        sizePolicy.setHeightForWidth(self.bmi.sizePolicy().hasHeightForWidth())
        self.bmi.setSizePolicy(sizePolicy)
        self.bmi.setMinimumSize(QSize(300, 40))
        self.bmi.setMaximumSize(QSize(300, 40))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.bmi)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_5)


        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)

        self.calculate = QPushButton(self.centralwidget)
        self.calculate.setObjectName(u"calculate")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calculate.sizePolicy().hasHeightForWidth())
        self.calculate.setSizePolicy(sizePolicy1)
        self.calculate.setFont(font1)

        self.gridLayout.addWidget(self.calculate, 1, 1, 1, 1)

        BMI计算器.setCentralWidget(self.centralwidget)

        self.retranslateUi(BMI计算器)

        QMetaObject.connectSlotsByName(BMI计算器)
    # setupUi

    def retranslateUi(self, BMI计算器):
        BMI计算器.setWindowTitle(QCoreApplication.translate("BMI计算器", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("BMI计算器", u"\u4f53\u91cd\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("BMI计算器", u"\u8eab\u9ad8\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("BMI计算器", u"BMI\u6307\u6570:", None))
        self.label_4.setText(QCoreApplication.translate("BMI计算器", u"kg", None))
        self.label_5.setText(QCoreApplication.translate("BMI计算器", u"m", None))
        self.calculate.setText(QCoreApplication.translate("BMI计算器", u"\u8ba1\u7b97", None))
    # retranslateUi

