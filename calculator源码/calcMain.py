from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QMessageBox
from enum import Enum
import operator, math
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
import sys,os
#QRegularExpressionValidator和QRegularExpression都是用来规定

OPERATOR_DICT = {operator.add: '+', operator.sub: '-', operator.mul: '*', operator.truediv: '/',operator.mod:'%'}
#初始化函数中，_operator就是用来接收operator类中运算符函数的变量，这个变量在OPERATOR_DICT这个字典里充当键值的角色，这个变量在setOperator函数中会与digiDisplay中呈现的算式合并（字符串合并）

#去除小数点后多余的0
def deletezero(num_str):
    if '.' in num_str:
        num_str = num_str.rstrip('0').rstrip('.')
    return num_str
#rstrip 是 Python 字符串方法之一，用于删除字符串右侧（结尾）的指定字符（默认为空白字符，包括空格、换行符等）。
# 这个方法不会修改原始字符串，而是返回一个新的字符串。


uiLoader = QUiLoader()
#QUiLoader可以动态地加载.ui文件

def processPath(path):
    '''
    :param path: 相对于根目录的路径
    :return: 拼接好的路径
    '''
    if getattr(sys, 'frozen', False):  # 判断是否存在属性frozen，以此判断是打包的程序还是源代码。false为默认值，即没有frozen属性时返回false
        base_path = sys._MEIPASS  # 该属性也是打包程序才会有，源代码尝试获取该属性会报错
    else:
        base_path = os.path.abspath(".")  # 当源代码运行时使用该路径
    return os.path.join(base_path, path)



#计算状态类，status是个枚举类，通过继承Enum，来给status中的变量加上标识符，不必另赋数字或字符串
class status(Enum):
    INPUT_NUM1 = 1  #输入第一个数字
    SET_OPERATOR = 2  #输入运算符
    INPUT_NUM2 = 3  #输入第二个数字
    CALCULATED = 4  #计算完成


class calcMainWindow:
    def __init__(self):#初始化


        #这里的self.ui指的是Qwidget对象，包含所有ui文件里的组件，Qwidget是所有用户界面对象的基类
        #载入计算器的UI文件
        self.ui = uiLoader.load(processPath('calculator.ui'))#加载calculator.ui文件，动态地加载，在用QT designer修改ui界面的时候，在保存修改后的ui文件后，这里加载的便是修改后的ui文件
        #不用每次修改ui文件后重新将ui文件转换成py文件
        
        self.status = status.INPUT_NUM1  #默认是输入第一个数字
        self.__newDigitFlag = True  
        #__newDigitFlag 用于指示用户是否刚开始输入新的数字。如果用户输入了一个数字，__newDigitFlag 会被设置为 False，
        # 表示后续的输入将追加到当前输入的数字上，而不是替换它
        self.__num1 = None  
        self.__num2 = None
        self.bmi_cal_window=None   
        #lambda创造匿名函数，这里直接将一个函数作为参数传递
        #数字按键部署
        self.ui.zeroButton.clicked.connect(lambda : self.inputDigit(0))
        self.ui.oneButton.clicked.connect(lambda : self.inputDigit(1))
        self.ui.twoButton.clicked.connect(lambda : self.inputDigit(2))
        self.ui.threeButton.clicked.connect(lambda : self.inputDigit(3))
        self.ui.fourButton.clicked.connect(lambda : self.inputDigit(4))
        self.ui.fiveButton.clicked.connect(lambda : self.inputDigit(5))
        self.ui.sixButton.clicked.connect(lambda : self.inputDigit(6))
        self.ui.sevenButton.clicked.connect(lambda : self.inputDigit(7))
        self.ui.eightButton.clicked.connect(lambda : self.inputDigit(8))
        self.ui.nineButton.clicked.connect(lambda : self.inputDigit(9))
       
        self.ui.dotButton.clicked.connect(self.setDot)
        
        self.ui.revButton.clicked.connect(self.Reverse)
       

        self._operator = None # 初始化时运算符置为None
        self.ui.addButton.clicked.connect(lambda : self.setOperator(operator.add))
        self.ui.subButton.clicked.connect(lambda : self.setOperator(operator.sub))
        self.ui.mulButton.clicked.connect(lambda : self.setOperator(operator.mul))
        self.ui.divButton.clicked.connect(lambda : self.setOperator(operator.truediv))
        self.ui.equalButton.clicked.connect(self.equal)
        self.ui.equalButton.setStyleSheet("QPushButton {background-color: lightblue;}")
        self.ui.percentButton.clicked.connect(lambda : self.setOperator(operator.mod))
        

        self.ui.invButton.clicked.connect(self.inverse)
        self.ui.squareButton.clicked.connect(self.square)
        self.ui.sqrtButton.clicked.connect(self.sqrt)
        
        self.ui.ceButton.clicked.connect(self.CE)
        self.ui.cButton.clicked.connect(self.C)
        self.ui.delButton.clicked.connect(self.DEL)


        self.ui.pushButton.clicked.connect(self.switch)

    def switch(self):
        if not self.bmi_cal_window:
            self.bmi_cal_window = bmi_calwindow(self)  # 创建 BMI 计算器窗口实例
        self.bmi_cal_window.ui.show()  # 显示 BMI 窗口

    #输入数字
    def inputDigit(self, digit):
        digit = str(digit)
        if self.status == status.INPUT_NUM1:
            if self.__newDigitFlag:
                self.ui.digitDisplay.setText(str(digit))
                self.__newDigitFlag = False
            else:
                if self.ui.digitDisplay.text()!='0':
                    self.ui.digitDisplay.setText(self.ui.digitDisplay.text()+digit)
                elif self.ui.digitDisplay.text()=='0' and digit!='0':
                    self.ui.digitDisplay.setText(digit)
                else:
                    pass
            self.__num1 = float(self.ui.digitDisplay.text())
        elif self.status == status.SET_OPERATOR:
            self.__newDigitFlag = True
            self.status = status.INPUT_NUM2
            self.inputDigit(digit)
        elif self.status == status.INPUT_NUM2:
            if self.__newDigitFlag:
                self.ui.digitDisplay.setText(str(digit))
                self.__newDigitFlag = False
            else:
                if self.ui.digitDisplay.text()!='0':
                    self.ui.digitDisplay.setText(self.ui.digitDisplay.text()+digit)
                elif self.ui.digitDisplay.text()=='0' and digit!='0':
                    self.ui.digitDisplay.setText(digit)
                else:
                    pass
            self.__num2 = float(self.ui.digitDisplay.text())
        elif self.status == status.CALCULATED:
            self.__newDigitFlag = True
            self.status = status.INPUT_NUM1
            self.inputDigit(digit)
        else:
            raise Exception('错误')
    
    def setDot(self):
        if self.__newDigitFlag:
            self.ui.digitDisplay.setText('0.')
        else:
            if '.' not in self.ui.digitDisplay.text():
                self.ui.digitDisplay.setText(self.ui.digitDisplay.text()+'.')
        self.__newDigitFlag = False
    
    def Reverse(self):
        if self.ui.digitDisplay.text()=='0':
            return
        num_str = self.ui.digitDisplay.text()
        if num_str.startswith('-'):
            self.ui.digitDisplay.setText(self.ui.digitDisplay.text().lstrip('-'))
        else:
            self.ui.digitDisplay.setText('-'+self.ui.digitDisplay.text())
        if self.status in (status.INPUT_NUM1, status.CALCULATED):
            self.ui.digitUpDisplay.setText('negate({})'.format(deletezero(num_str)))
            self.__num1 = -self.__num1
        elif self.status in (status.INPUT_NUM2, status.SET_OPERATOR):
            if self.status == status.SET_OPERATOR:
                self.__num2 = float(num_str)
                self.status = status.INPUT_NUM2
            self.__num2 = -self.__num2
        else:
            raise Exception('错误')
        

    #将运算符压入digiDisplay里
    def setOperator(self, _operator):
        print(self.status, self.__num1, self.__num2)
        self.__newDigitFlag = True
        if self.status == status.INPUT_NUM1:
            self._operator = _operator
            self.status = status.SET_OPERATOR
        elif self.status == status.SET_OPERATOR:
            self._operator = _operator
        elif self.status == status.INPUT_NUM2:
            result = self._operator(self.__num1, self.__num2)
            self._operator = _operator
            self.status = status.SET_OPERATOR
            self.__num1 = result
            self.ui.digitDisplay.setText(deletezero(str(result)))
        elif self.status == status.CALCULATED:
            self._operator = _operator
            self.status = status.SET_OPERATOR
        else:
            raise Exception('错误')
        self.ui.digitUpDisplay.setText(self.ui.digitDisplay.text()+' '+OPERATOR_DICT[self._operator])
        
    def equal(self):
        print(self.status, self.__num1, self.__num2)
        self.__newDigitFlag = True
        #这里self._operator是已经被赋了operator函数中的运算符函数，例如add（a，b）返回的就是a+b
        if self.status == status.INPUT_NUM1:
            if self._operator is None:
                self.ui.digitUpDisplay.setText(deletezero(self.ui.digitDisplay.text())+' =')
                self.status = status.CALCULATED
                return
            else:
                result = self._operator(self.__num1, self.__num2)
        elif self.status == status.SET_OPERATOR:
            self.__num2 = self.__num1
            result = self._operator(self.__num1, self.__num2)
        elif self.status == status.INPUT_NUM2:
            result = self._operator(self.__num1, self.__num2)
        elif self.status ==status.CALCULATED:
            result = self._operator(self.__num1, self.__num2)
        else:
            raise Exception('错误')
        self.ui.digitUpDisplay.setText(deletezero(str(self.__num1))+' '+OPERATOR_DICT[self._operator]+' '+ deletezero(str(self.__num2)) +' =')
        self.ui.digitDisplay.setText(deletezero(str(result)))
        self.__num1 = result
        self.status = status.CALCULATED

#取倒数
    def inverse(self):
        __num = float(self.ui.digitDisplay.text())
        if __num == 0:
            self.ui.digitDisplay.setText("错误")
            return
        res = 1/__num
        num_str = self.ui.digitDisplay.text()
        if self.status in (status.INPUT_NUM1, status.CALCULATED):
            self.ui.digitUpDisplay.setText('1/{}'.format(deletezero(num_str)))
            self.__num1 = res
        elif self.status in (status.INPUT_NUM2, status.SET_OPERATOR):
            if self.status == status.SET_OPERATOR:
                self.__num2 = float(num_str)
                self.status = status.INPUT_NUM2
            self.__num2 = res
        else:
            raise Exception('错误')
        self.ui.digitDisplay.setText(str(res))
        self.__newDigitFlag = True
#取平方
    def square(self):
        __num = float(self.ui.digitDisplay.text())
        res = __num**2
        num_str = self.ui.digitDisplay.text()
        if self.status in (status.INPUT_NUM1, status.CALCULATED):
            print(num_str)
            self.ui.digitUpDisplay.setText('sqr({})'.format(deletezero(num_str)))
            self.__num1 = res
        elif self.status in (status.INPUT_NUM2, status.SET_OPERATOR):
            if self.status == status.SET_OPERATOR:
                self.__num2 = float(num_str)
                self.status = status.INPUT_NUM2
            self.__num2 = res
        else:
            raise Exception('错误')
        self.ui.digitDisplay.setText(str(res))
        self.__newDigitFlag = True

#取平方根
    def sqrt(self):
        __num = float(self.ui.digitDisplay.text())
        res = math.sqrt(__num)
        num_str = self.ui.digitDisplay.text()
        if self.status in (status.INPUT_NUM1, status.CALCULATED):
            self.ui.digitUpDisplay.setText('sqrt({})'.format(deletezero(num_str)))
            self.__num1 = res
        elif self.status in (status.INPUT_NUM2, status.SET_OPERATOR):
            if self.status == status.SET_OPERATOR:
                self.__num2 = float(num_str)
                self.status = status.INPUT_NUM2
            self.__num2 = res
        else:
            raise Exception('错误')
        self.ui.digitDisplay.setText(str(res))
        self.__newDigitFlag = True


    def CE(self):
        self.ui.digitDisplay.setText("0")
        if self.__newDigitFlag:
            self.ui.digitUpDisplay.setText("")

    def C(self):
        self.ui.digitUpDisplay.setText("")
        self.ui.digitDisplay.setText("0")
        self.__num1 = 0
        self.__num2 = None
        self._operator = None
        self.__newDigitFlag = True
        self.status = status.INPUT_NUM1

    def DEL(self):
        if not self.__newDigitFlag:
            currentStr = self.ui.digitDisplay.text()
            if len(currentStr)>1:
                newStr = currentStr[:-1]
            else:
                newStr = "0"
            self.ui.digitDisplay.setText(newStr)
        else:
            self.ui.digitUpDisplay.setText("")    



class bmi_calwindow():
    def __init__(self,parent=None):
        self.ui = uiLoader.load(processPath('bmi_cal.ui'))
        self.ui.show()
        self.weight_data = None
        self.height_data = None
        self.bmi_data = None
        self.ui.calculate.clicked.connect(self.getbmi)

        regx = QRegularExpression("^[1-9]\\d*\\.\\d*|0\\.\\d*[1-9]\\d*$")  # 输入浮点数
        #
        my_regex = QRegularExpressionValidator(regx)
        self.ui.weightLine.setValidator(my_regex)
        self.ui.heightLine.setValidator(my_regex)
        self.ui.bmi.setReadOnly(True)#设置bmi数据只读

    def getbmi(self):
        # 读取输入框中的数据
        self.weight_data = self.ui.weightLine.text()
        self.height_data = self.ui.heightLine.text()

        # 未输入数据则提示
        if self.weight_data==None or  self.height_data==None:
            self.Message1()
            return

        try:
            # 将字符串型转换为浮点数并计算
            weight = float(self.weight_data)
            height = float(self.height_data)
            bmi_ = weight / (height * height)
            self.bmi_data = f"{bmi_:.2f}"
            self.ui.bmi.setText(self.bmi_data)
        except ValueError:
            self.Message2()

        # 计算完成则清空
        self.init()

    def Message1(self):
        QMessageBox.information(self.ui, "提示", "未检测到数据输入")
        return

    def Message2(self):
        QMessageBox.information(self.ui, "提示", "数据类型错误")
        return

    def init(self):
        self.ui.weightLine.clear()
        self.ui.heightLine.clear()
    
if __name__ == '__main__':
    app = QApplication([])#它负责管理 GUI 应用程序的控制流和主要设置，包括事件循环、应用程序的主窗口和全局设置等。
    win = calcMainWindow()
    win.ui.show()
    app.exec()#启动事件循环