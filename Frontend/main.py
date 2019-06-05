# 这里绘制的是UI的主界面
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QDesktopWidget,
                             QMessageBox, QMainWindow, QGridLayout, QLabel)
from PyQt5.QtGui import QIcon, QPixmap
import page
import quit
import welcome
import list
import input
import about
import result
import qtawesome


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 添加栅格布局
        # 布局只能添加到Widget里
        # 所以先添加一个Widget
        grid = QGridLayout()
        # 这个叫widget的是主widget。左侧为一列功能键，右侧为页面
        self.widget = QWidget()
        self.widget.setObjectName("main")
        self.widget.setLayout(grid)
        self.setCentralWidget(self.widget)
        grid.setSpacing(15)

        # 这里是左侧的一堆功能键
        self.btn_welcome = QPushButton(qtawesome.icon('fa.sellsy'), '欢迎光临', self)
        self.btn_welcome.clicked[bool].connect(self.button_clicked)
        self.btn_welcome.setObjectName("left")
        self.btn_input = QPushButton(qtawesome.icon('fa.music'), '期权参数', self)
        self.btn_input.clicked[bool].connect(self.button_clicked)
        self.btn_input.setObjectName("left")
        self.btn_result = QPushButton(qtawesome.icon('fa.download'), '查看价格', self)
        self.btn_result.clicked[bool].connect(self.button_clicked)
        self.btn_result.setObjectName("left")
        self.btn_result.setEnabled(False)
        self.btn_list = QPushButton(qtawesome.icon('fa.film'), '算法一览', self)
        self.btn_list.clicked[bool].connect(self.button_clicked)
        self.btn_list.setObjectName("left")
        self.btn_about = QPushButton(qtawesome.icon('fa.star'), '关于我们', self)
        self.btn_about.clicked[bool].connect(self.button_clicked)
        self.btn_about.setObjectName("left")
        self.btn_quit = QPushButton(qtawesome.icon('fa.question'), '退出系统', self)
        self.btn_quit.clicked[bool].connect(self.button_clicked)
        self.btn_quit.setObjectName("left")
        grid.addWidget(self.btn_welcome, 4, 0)
        grid.addWidget(self.btn_input, 5, 0)
        grid.addWidget(self.btn_result, 6, 0)
        grid.addWidget(self.btn_list, 7, 0)
        grid.addWidget(self.btn_about, 8, 0)
        grid.addWidget(self.btn_quit, 9, 0)

        # 这里是每个功能键的页面
        self.page_welcome = page.page(grid, self)
        welcome.welcome(self.page_welcome)
        self.page_result = page.page(grid, self)
        result.result(self.page_result)
        self.page_list = page.page(grid, self)
        list.list(self.page_list)
        self.page_about = page.page(grid, self)
        about.about(self.page_about)
        self.page_quit = page.page(grid, self)
        quit.quit(self.page_quit)
        self.page_input = page.page(grid, self)
        input.input(self.page_input)
        self.page_welcome.show(self)

        # 给布局添加上左侧功能键和LOGO
        logo = QLabel(self)
        directory = "img/logo2.png"
        pix = QPixmap(directory)
        logo.setPixmap(pix)
        grid.addWidget(logo, 1, 0, 3, 1)

        # 设置标题logo
        self.setWindowIcon(QIcon(directory))
        # 居中并绘制
        self.resize(1280, 720)
        self.center()
        self.setWindowTitle('MiniSQL')
        # 导入qss样式
        directory = "style.qss"
        with open(directory, 'r') as f:
            qss_style = f.read()
        self.setStyleSheet(qss_style)
        self.show()
        self.button_change(self.btn_welcome)

    def button_change(self, btn):
        self.btn_welcome.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_input.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_result.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_list.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_about.setStyleSheet('''QPushButton#left{background-color:}''')
        self.btn_quit.setStyleSheet('''QPushButton#left{background-color:}''')
        btn.setStyleSheet('''QPushButton#left{background-color:white;
                            border-color: red;
                            }''')

    # 按下左侧功能键的效果
    def button_clicked(self):
        sender = self.sender()
        if sender.text() == '欢迎光临':
            self.page_welcome.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background.png)}''')
            self.button_change(self.btn_welcome)
        if sender.text() == '期权参数':
            self.page_input.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_2.png)}''')
            self.button_change(self.btn_input)
        if sender.text() == '查看价格':
            self.page_result.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.button_change(self.btn_result)
        if sender.text() == '算法一览':
            self.page_list.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background.png)}''')
            list.list(self.page_list)
            self.button_change(self.btn_list)
        if sender.text() == '关于我们':
            self.page_about.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_2.png)}''')
            self.button_change(self.btn_about)
        if sender.text() == '退出系统':
            self.page_quit.show(self)
            self.widget.setStyleSheet('''QWidget#main{border-image:url(img/background_3.png)}''')
            self.button_change(self.btn_quit)

    # 按退出键弹出确认窗口
    def close_event(self, event):

        reply = QMessageBox.question(self, '退出',
                                     "您确定要退出MiniSQL吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 启动时居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
