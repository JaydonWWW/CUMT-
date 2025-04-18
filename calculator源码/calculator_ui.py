from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"\u8ba1\u7b97\u5668")
        Calculator.resize(600, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Calculator.sizePolicy().hasHeightForWidth())
        Calculator.setSizePolicy(sizePolicy)
        Calculator.setMinimumSize(QSize(600, 800))
        self.actionbmi_calculator = QAction(Calculator)
        self.actionbmi_calculator.setObjectName(u"actionbmi_calculator")
        self.centralwidget = QWidget(Calculator)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.calcModeView = QStackedWidget(self.centralwidget)
        self.calcModeView.setObjectName(u"calcModeView")
        self.pageStd = QWidget()
        self.pageStd.setObjectName(u"pageStd")
        self.verticalLayout = QVBoxLayout(self.pageStd)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.pageStd)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(74, 40))
        self.pushButton.setMaximumSize(QSize(74, 40))

        self.verticalLayout.addWidget(self.pushButton)

        self.digitUpDisplay = QLineEdit(self.pageStd)
        self.digitUpDisplay.setObjectName(u"digitUpDisplay")
        self.digitUpDisplay.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.digitUpDisplay)

        self.digitDisplay = QLineEdit(self.pageStd)
        self.digitDisplay.setObjectName(u"digitDisplay")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.digitDisplay.sizePolicy().hasHeightForWidth())
        self.digitDisplay.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.digitDisplay.setFont(font)
        self.digitDisplay.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.digitDisplay)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(0, 9, -1, -1)
        self.mcButton = QPushButton(self.pageStd)
        self.mcButton.setObjectName(u"mcButton")
        sizePolicy1.setHeightForWidth(self.mcButton.sizePolicy().hasHeightForWidth())
        self.mcButton.setSizePolicy(sizePolicy1)
        self.mcButton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.mcButton.setFont(font1)
        self.mcButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.mcButton)

        self.mrButton = QPushButton(self.pageStd)
        self.mrButton.setObjectName(u"mrButton")
        sizePolicy1.setHeightForWidth(self.mrButton.sizePolicy().hasHeightForWidth())
        self.mrButton.setSizePolicy(sizePolicy1)
        self.mrButton.setMaximumSize(QSize(16777215, 16777215))
        self.mrButton.setFont(font1)
        self.mrButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.mrButton)

        self.maddButton = QPushButton(self.pageStd)
        self.maddButton.setObjectName(u"maddButton")
        sizePolicy1.setHeightForWidth(self.maddButton.sizePolicy().hasHeightForWidth())
        self.maddButton.setSizePolicy(sizePolicy1)
        self.maddButton.setMaximumSize(QSize(16777215, 16777215))
        self.maddButton.setFont(font1)
        self.maddButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.maddButton)

        self.msubButton = QPushButton(self.pageStd)
        self.msubButton.setObjectName(u"msubButton")
        sizePolicy1.setHeightForWidth(self.msubButton.sizePolicy().hasHeightForWidth())
        self.msubButton.setSizePolicy(sizePolicy1)
        self.msubButton.setMaximumSize(QSize(16777215, 16777215))
        self.msubButton.setFont(font1)
        self.msubButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.msubButton)

        self.msButton = QPushButton(self.pageStd)
        self.msButton.setObjectName(u"msButton")
        sizePolicy1.setHeightForWidth(self.msButton.sizePolicy().hasHeightForWidth())
        self.msButton.setSizePolicy(sizePolicy1)
        self.msButton.setMaximumSize(QSize(16777215, 16777215))
        self.msButton.setFont(font1)
        self.msButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.msButton)

        self.mlistButton = QPushButton(self.pageStd)
        self.mlistButton.setObjectName(u"mlistButton")
        sizePolicy1.setHeightForWidth(self.mlistButton.sizePolicy().hasHeightForWidth())
        self.mlistButton.setSizePolicy(sizePolicy1)
        self.mlistButton.setMaximumSize(QSize(16777215, 16777215))
        self.mlistButton.setFont(font1)
        self.mlistButton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.mlistButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ceButton = QPushButton(self.pageStd)
        self.ceButton.setObjectName(u"ceButton")
        sizePolicy1.setHeightForWidth(self.ceButton.sizePolicy().hasHeightForWidth())
        self.ceButton.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Marlett"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.ceButton.setFont(font2)

        self.gridLayout_2.addWidget(self.ceButton, 0, 1, 1, 1)

        self.fiveButton = QPushButton(self.pageStd)
        self.fiveButton.setObjectName(u"fiveButton")
        sizePolicy1.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.fiveButton.setFont(font3)

        self.gridLayout_2.addWidget(self.fiveButton, 3, 1, 1, 1)

        self.eightButton = QPushButton(self.pageStd)
        self.eightButton.setObjectName(u"eightButton")
        sizePolicy1.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy1)
        self.eightButton.setFont(font3)

        self.gridLayout_2.addWidget(self.eightButton, 2, 1, 1, 1)

        self.percentButton = QPushButton(self.pageStd)
        self.percentButton.setObjectName(u"percentButton")
        sizePolicy1.setHeightForWidth(self.percentButton.sizePolicy().hasHeightForWidth())
        self.percentButton.setSizePolicy(sizePolicy1)
        self.percentButton.setMinimumSize(QSize(8, 0))
        self.percentButton.setFont(font2)

        self.gridLayout_2.addWidget(self.percentButton, 0, 0, 1, 1)

        self.sevenButton = QPushButton(self.pageStd)
        self.sevenButton.setObjectName(u"sevenButton")
        sizePolicy1.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy1)
        self.sevenButton.setFont(font3)

        self.gridLayout_2.addWidget(self.sevenButton, 2, 0, 1, 1)

        self.sixButton = QPushButton(self.pageStd)
        self.sixButton.setObjectName(u"sixButton")
        sizePolicy1.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy1)
        self.sixButton.setFont(font3)

        self.gridLayout_2.addWidget(self.sixButton, 3, 2, 1, 1)

        self.delButton = QPushButton(self.pageStd)
        self.delButton.setObjectName(u"delButton")
        sizePolicy1.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies([u"Malgun Gothic Semilight"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.delButton.setFont(font4)

        self.gridLayout_2.addWidget(self.delButton, 0, 3, 1, 1)

        self.divButton = QPushButton(self.pageStd)
        self.divButton.setObjectName(u"divButton")
        sizePolicy1.setHeightForWidth(self.divButton.sizePolicy().hasHeightForWidth())
        self.divButton.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(16)
        font5.setBold(False)
        self.divButton.setFont(font5)

        self.gridLayout_2.addWidget(self.divButton, 1, 3, 1, 1)

        self.equalButton = QPushButton(self.pageStd)
        self.equalButton.setObjectName(u"equalButton")
        sizePolicy1.setHeightForWidth(self.equalButton.sizePolicy().hasHeightForWidth())
        self.equalButton.setSizePolicy(sizePolicy1)
        font6 = QFont()
        font6.setPointSize(32)
        self.equalButton.setFont(font6)
        self.equalButton.setAutoFillBackground(False)
        self.equalButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.equalButton, 5, 3, 1, 1)

        self.subButton = QPushButton(self.pageStd)
        self.subButton.setObjectName(u"subButton")
        sizePolicy1.setHeightForWidth(self.subButton.sizePolicy().hasHeightForWidth())
        self.subButton.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        self.subButton.setFont(font7)

        self.gridLayout_2.addWidget(self.subButton, 3, 3, 1, 1)

        self.invButton = QPushButton(self.pageStd)
        self.invButton.setObjectName(u"invButton")
        sizePolicy1.setHeightForWidth(self.invButton.sizePolicy().hasHeightForWidth())
        self.invButton.setSizePolicy(sizePolicy1)
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(False)
        self.invButton.setFont(font8)

        self.gridLayout_2.addWidget(self.invButton, 1, 0, 1, 1)

        self.dotButton = QPushButton(self.pageStd)
        self.dotButton.setObjectName(u"dotButton")
        sizePolicy1.setHeightForWidth(self.dotButton.sizePolicy().hasHeightForWidth())
        self.dotButton.setSizePolicy(sizePolicy1)
        self.dotButton.setFont(font7)

        self.gridLayout_2.addWidget(self.dotButton, 5, 2, 1, 1)

        self.twoButton = QPushButton(self.pageStd)
        self.twoButton.setObjectName(u"twoButton")
        sizePolicy1.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy1)
        self.twoButton.setFont(font3)

        self.gridLayout_2.addWidget(self.twoButton, 4, 1, 1, 1)

        self.threeButton = QPushButton(self.pageStd)
        self.threeButton.setObjectName(u"threeButton")
        sizePolicy1.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy1)
        self.threeButton.setFont(font3)

        self.gridLayout_2.addWidget(self.threeButton, 4, 2, 1, 1)

        self.mulButton = QPushButton(self.pageStd)
        self.mulButton.setObjectName(u"mulButton")
        sizePolicy1.setHeightForWidth(self.mulButton.sizePolicy().hasHeightForWidth())
        self.mulButton.setSizePolicy(sizePolicy1)
        self.mulButton.setFont(font7)

        self.gridLayout_2.addWidget(self.mulButton, 2, 3, 1, 1)

        self.squareButton = QPushButton(self.pageStd)
        self.squareButton.setObjectName(u"squareButton")
        sizePolicy1.setHeightForWidth(self.squareButton.sizePolicy().hasHeightForWidth())
        self.squareButton.setSizePolicy(sizePolicy1)
        self.squareButton.setFont(font5)

        self.gridLayout_2.addWidget(self.squareButton, 1, 1, 1, 1)

        self.nineButton = QPushButton(self.pageStd)
        self.nineButton.setObjectName(u"nineButton")
        sizePolicy1.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy1)
        self.nineButton.setFont(font3)

        self.gridLayout_2.addWidget(self.nineButton, 2, 2, 1, 1)

        self.sqrtButton = QPushButton(self.pageStd)
        self.sqrtButton.setObjectName(u"sqrtButton")
        sizePolicy1.setHeightForWidth(self.sqrtButton.sizePolicy().hasHeightForWidth())
        self.sqrtButton.setSizePolicy(sizePolicy1)
        self.sqrtButton.setFont(font8)

        self.gridLayout_2.addWidget(self.sqrtButton, 1, 2, 1, 1)

        self.revButton = QPushButton(self.pageStd)
        self.revButton.setObjectName(u"revButton")
        sizePolicy1.setHeightForWidth(self.revButton.sizePolicy().hasHeightForWidth())
        self.revButton.setSizePolicy(sizePolicy1)
        font9 = QFont()
        font9.setPointSize(14)
        font9.setBold(False)
        self.revButton.setFont(font9)

        self.gridLayout_2.addWidget(self.revButton, 5, 0, 1, 1)

        self.cButton = QPushButton(self.pageStd)
        self.cButton.setObjectName(u"cButton")
        sizePolicy1.setHeightForWidth(self.cButton.sizePolicy().hasHeightForWidth())
        self.cButton.setSizePolicy(sizePolicy1)
        self.cButton.setFont(font2)

        self.gridLayout_2.addWidget(self.cButton, 0, 2, 1, 1)

        self.zeroButton = QPushButton(self.pageStd)
        self.zeroButton.setObjectName(u"zeroButton")
        sizePolicy1.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy1)
        self.zeroButton.setFont(font3)

        self.gridLayout_2.addWidget(self.zeroButton, 5, 1, 1, 1)

        self.oneButton = QPushButton(self.pageStd)
        self.oneButton.setObjectName(u"oneButton")
        sizePolicy1.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy1)
        self.oneButton.setFont(font3)

        self.gridLayout_2.addWidget(self.oneButton, 4, 0, 1, 1)

        self.fourButton = QPushButton(self.pageStd)
        self.fourButton.setObjectName(u"fourButton")
        sizePolicy1.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy1)
        self.fourButton.setFont(font3)

        self.gridLayout_2.addWidget(self.fourButton, 3, 0, 1, 1)

        self.addButton = QPushButton(self.pageStd)
        self.addButton.setObjectName(u"addButton")
        sizePolicy1.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy1)
        self.addButton.setFont(font7)

        self.gridLayout_2.addWidget(self.addButton, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 9)
        self.calcModeView.addWidget(self.pageStd)
        self.pageProg = QWidget()
        self.pageProg.setObjectName(u"pageProg")
        self.calcModeView.addWidget(self.pageProg)

        self.gridLayout.addWidget(self.calcModeView, 0, 0, 1, 1)

        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)

        self.calcModeView.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"MainWindow", None))
        self.actionbmi_calculator.setText(QCoreApplication.translate("Calculator", u"bmi\u8ba1\u7b97\u5668", None))
        self.pushButton.setText(QCoreApplication.translate("Calculator", u"BMI\u8ba1\u7b97\u5668", None))
        self.digitDisplay.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.mcButton.setText(QCoreApplication.translate("Calculator", u"MC", None))
        self.mrButton.setText(QCoreApplication.translate("Calculator", u"MR", None))
        self.maddButton.setText(QCoreApplication.translate("Calculator", u"M+", None))
        self.msubButton.setText(QCoreApplication.translate("Calculator", u"M-", None))
        self.msButton.setText(QCoreApplication.translate("Calculator", u"MS", None))
        self.mlistButton.setText(QCoreApplication.translate("Calculator", u"Mlist", None))
        self.ceButton.setText(QCoreApplication.translate("Calculator", u"CE", None))
        self.fiveButton.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.eightButton.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.percentButton.setText(QCoreApplication.translate("Calculator", u"%", None))
        self.sevenButton.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.sixButton.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.delButton.setText(QCoreApplication.translate("Calculator", u"del", None))
        self.divButton.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.equalButton.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.subButton.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.invButton.setText(QCoreApplication.translate("Calculator", u"1/x", None))
        self.dotButton.setText(QCoreApplication.translate("Calculator", u".", None))
        self.twoButton.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.threeButton.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.mulButton.setText(QCoreApplication.translate("Calculator", u"*", None))
        self.squareButton.setText(QCoreApplication.translate("Calculator", u"x\u00b2", None))
        self.nineButton.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.sqrtButton.setText(QCoreApplication.translate("Calculator", u"sqrt(x)", None))
        self.revButton.setText(QCoreApplication.translate("Calculator", u"+/-", None))
        self.cButton.setText(QCoreApplication.translate("Calculator", u"C", None))
        self.zeroButton.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.oneButton.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.fourButton.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.addButton.setText(QCoreApplication.translate("Calculator", u"+", None))
    # retranslateUi

