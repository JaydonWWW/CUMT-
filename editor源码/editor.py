
import sys

from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QFontDatabase, QIcon,QFont
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget,  QStatusBar, QAction, QFileDialog, \
	QMessageBox, QTextEdit, QFontComboBox, QComboBox, QWidgetAction, QDialog,QLabel,QColorDialog



class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		#*args 允许你传递任意数量的位置参数。
		#**kwargs 允许你传递任意数量的关键字参数。
		super(MainWindow, self).__init__(*args, **kwargs)
		#继承Mainwindow,从而继承QMainwindow
		self.setWindowTitle('多文档编辑器')

		self.editors = []
		self.paths = []
		self.path = None

		self.tabs = QTabWidget()
		self.tabs.setDocumentMode(True)
		self.tabs.setTabsClosable(True)
		self.tabs.tabCloseRequested.connect(self.close_current_tab)#关闭标签栏中的文件，tabcloseRequested是QTabWidget里的一个变量，用于接收
		self.tabs.currentChanged.connect(self.change_text_editor)

		self.add_new_tab()

		self.createmenubar()
		self.createstatusbar()
		self.createtoolbar()

		self.setCentralWidget(self.tabs)



		self.show()
	

	def createmenubar(self):
		menubar = self.menuBar()#menuBar()函数是QTwidget类里包含的构造菜单栏的函数，这里创造一个菜单栏叫“menubar”
		menubar_items = {##以字典的形式储存菜单按键，再以列表的形式储存一个个的子菜单，再用元组将子菜单和快捷键和函数绑定
			'&文件': [
				("&新建", "Ctrl+N", self.add_new_tab),
				("&打开", "Ctrl+O", self.file_open),
				("&保存", "Ctrl+S", self.file_save),
				("&另存为", "Ctrl+Shift+S", self.save_as),
				("&打印", "Ctrl+P", self.print_document),
		
			],
			'&编辑': [
				("&剪切", "Ctrl+X", self.cut_document),
				("&复制", "Ctrl+C", self.copy_document),
				("&粘贴", "Ctrl+V", self.paste_document),
				None,
				("&撤回", "Ctrl+Z", self.undo_document),
				("&恢复", "Ctrl+Y", self.redo_document)
			],
			'&查看': [
				("&左对齐", "", self.align_left),
				("&右对齐", "", self.align_right),
				("&居中", "", self.align_center),
				("&适应", "", self.align_justify)
			],
		}
		
		
		
		#遍历上述的菜单栏字典，将菜单填入menubar这个菜单栏中
		for menuitem, actions in menubar_items.items():
			menu = menubar.addMenu(menuitem)
			for act in actions:
				if act:
					text, shortcut, callback = act#文本、快捷键、回调函数
					action = QAction(text, self)#先创建一个QAction对象，并设置其文本内容
					action.setShortcut(shortcut)#设置快捷键
					action.triggered.connect(callback)#将 action 的 triggered 信号连接到回调函数 callback
					menu.addAction(action)
				else:
					menu.addSeparator()#添加一个分隔符


		fontBox = QFontComboBox(self)
		fontBox.currentFontChanged.connect(self.fontfamily)

		fontSize = QComboBox(self)
		fontSize.setEditable(True)
		fontSize.setMinimumContentsLength(3)

		fontSize.activated.connect(self.fontsize)

		fontSizes = [
			'6', '7', '8', '9', '10', '11', '12', '13', '14',
			'15', '16', '18', '20', '22', '24', '26', '28',
			'32', '36', '40', '44', '48', '54', '60', '66',
			'72', '80', '88', '96'
		]

		fontSize.addItems(fontSizes)
		font_family = QWidgetAction(self)
		font_family.setDefaultWidget(fontBox)

		settings = menubar.addMenu('字体')
		menu_font = settings.addMenu("字体")
		menu_font.addAction(font_family)

		font_size = QWidgetAction(self)
		font_size.setDefaultWidget(fontSize)
		menu_size = settings.addMenu("大小")
		menu_size.addAction(font_size)

		color_choice=QAction("选择颜色",self)
		color_choice.triggered.connect(self.change_color)
		settings.addAction(color_choice)

	def change_color(self):
		color=QColorDialog.getColor()
		if color.isValid():
			self.current_editor.setTextColor(color)

	def setbold(self):
		if self.current_editor.fontWeight()>=QFont.Bold:
			self.current_editor.setFontWeight(QFont.Normal)
		else:
			self.current_editor.setFontWeight(QFont.Bold)

	
	def setitalic(self):
		if self.current_editor.fontItalic():
			self.current_editor.setFontItalic(False)
		else:
			self.current_editor.setFontItalic(True)
	
	def setunderline(self):
		if self.current_editor.fontUnderline():
			self.current_editor.setFontUnderline(False)
		else:
			self.current_editor.setFontUnderline(True)
	

	def createtoolbar(self):
		items = (
			('F:/code/pyqt-text-editor-master/editor/icons/new1.png', '新建 (Ctrl + N)', self.add_new_tab),
			('F:/code/pyqt-text-editor-master/editor/icons/open1.png', '打开 (Ctrl + O)', self.file_open),
			('F:/code/pyqt-text-editor-master/editor/icons/save1.png', '保存 (Ctrl + S)', self.file_save),
			('F:/code/pyqt-text-editor-master/editor/icons/save_as1.png', '另存为  (Ctrl + Shift + S)', self.save_as),
			None,
			('F:/code/pyqt-text-editor-master/editor/icons/cut1.png', '剪切 (Ctrl + X)', self.cut_document),
			('F:/code/pyqt-text-editor-master/editor/icons/copy1.png', '复制 (Ctrl + C)', self.copy_document),
			('F:/code/pyqt-text-editor-master/editor/icons/paste1.png', '粘贴 (Ctrl + V)', self.paste_document),
			None,
			('F:/code/pyqt-text-editor-master/editor/icons/undo1.png', '撤销 (Ctrl + Z)', self.undo_document),
			('F:/code/pyqt-text-editor-master/editor/icons/redo1.png', '恢复 (Ctrl + Y)', self.redo_document),
			None,
			('F:/code/pyqt-text-editor-master/editor/icons/print1.png', '打印 (Ctrl + P)', self.print_document),
			None,
			('F:/code/pyqt-text-editor-master/editor/icons/bold1.png','加粗',self.setbold),
			None,
			('F:/code/pyqt-text-editor-master/editor/icons/italic1.png','斜体',self.setitalic),
			None,
			('F:/code/pyqt-text-editor-master/editor/icons/underline1.png','下划线',self.setunderline)
		)

		self.toolbar = self.addToolBar("工具栏")

		for item in items:
			if item:
				icon, text, callback = item
				action = QAction(QIcon(icon), text, self)
				action.triggered.connect(callback)
				self.toolbar.addAction(action)
			else:
				self.toolbar.addSeparator()


	def createstatusbar(self):
		self.status = QStatusBar()
		self.word_count_Label=QLabel("个字")
		self.status.addWidget(self.word_count_Label,1)
		self.setStatusBar(self.status)
		


	def update_word_count(self):
		text=self.current_editor.toPlainText()
		#从QTextEdit中提取提取纯文本内容
		count=0
		for i in text:
			if i==" ":
				continue
			count+=1
		#添加将空格去除的列表
		self.word_count_Label.setText(f"{count} 个字")
	

	def dialog_critical(self, s):
		dlg = QMessageBox(self)
		dlg.setText(s)
		dlg.setIcon(QMessageBox.Critical)
		dlg.show()

	def change_text_editor(self, index):#改变编辑的文件，就是将选中的文件放在修改的界面中
		if index < len(self.editors) and index != -1:
			self.current_editor = self.editors[index]
			self.update_word_count()

	def file_open(self):#QFileDialog.getOpenFileName 方法来弹出一个文件选择对话框，让用户选择要打开的文件。
		path, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "Text documents (*.txt);All files (*.*)")
		if path:
			self._open_file_tab(path)

	def _open_file_tab(self, path):
		try:
			with open(path, 'r') as f:
				text = f.read()
				self.add_new_tab(path, text)
				self.paths.append(path)

		except Exception as e:
			self.dialog_critical(str(e))

	def create_editor(self, text):#创建一个文本编辑器的组件
		editor = QTextEdit(text)
		fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
		fixedfont.setPointSize(16)
		editor.setFont(fixedfont)
		self.current_editor=editor
		self.current_editor.textChanged.connect(self.update_word_count)
		return editor

	def remove_editor(self, index):
		self.tabs.removeTab(index)
		if index < len(self.editors):
			del self.editors[index]
			del self.paths[index]

	def save_as(self):
		new_path, _ = QFileDialog.getSaveFileName(self, '另存为')
		if new_path:
			self._save_to_path(new_path)

	def print_document(self):
		calprinter = QPrintDialog()#打印对话框类
		if calprinter.exec_() == QDialog.Accepted:
			self.current_editor.document().print_(calprinter.printer())

	def add_new_tab(self, label='未命名', text=''):
		editor = self.create_editor(text)
		editor.textChanged.connect(self.update_word_count)
		label = str(label) if label else '未命名'
		self.tabs.addTab(editor, label)
		self.editors.append(editor)
		self.current_editor = editor
		self.paths.append(label)
		self.path = label

	def file_save(self):
		if self.path == "未命名":
			return self.save_as()

		self._save_to_path(self.path)

	def _save_to_path(self, path):
		index = self.tabs.currentIndex()
		self.paths[index] = path
		self.path = path
		try:
			file = open(path, 'w')
			if file:
				text = self.current_editor.toPlainText()
				file.write(text)
				file.close()

		except Exception as e:
			self.dialog_critical(str(e))


	def current_tab_changed(self, i):
		self.path = self.paths[i]
		

	def close_current_tab(self, i):
		self.tabs.removeTab(i)#移除标签页
		if self.tabs.count() < 1:#如果标签页全部关闭，则关闭整个界面
			self.quit()
		else:
			index = self.tabs.currentIndex()
			self.path = self.paths[index]
			

	def quit(self):#关闭整个界面
		self.close()

	def undo_document(self):
		self.current_editor.undo()

	def redo_document(self):
		self.current_editor.redo()

	def cut_document(self):
		self.current_editor.cut()

	def copy_document(self):
		self.current_editor.copy()

	def paste_document(self):
		self.current_editor.paste()

	def align_left(self):
		self.current_editor.setAlignment(Qt.AlignLeft)

	def align_right(self):
		self.current_editor.setAlignment(Qt.AlignRight)

	def align_center(self):
		self.current_editor.setAlignment(Qt.AlignCenter)

	def align_justify(self):
		self.current_editor.setAlignment(Qt.AlignJustify)
		
	def fontfamily(self, font):
		self.current_editor.setCurrentFont(font)

	def fontsize(self, fontsize):
		self.current_editor.setFontPointSize(int(fontsize))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setApplicationName('多文档编辑器')

	window = MainWindow()
	sys.exit(app.exec_())
