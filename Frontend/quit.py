from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QPushButton, QLabel


def quit(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" 江湖再见")
    page.grid.addWidget(label_main, 0, 0)
    # 文本
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      去留无意,望天上云卷云舒。\n      路过万水千重，期待与你温柔重逢。")
    page.grid.addWidget(label_content, 1, 0)
    # 撑空白的地方
    label_empty = QLabel()
    page.grid.addWidget(label_empty, 2, 0, 2, 1)
    # 退出标题
    qbtn = QPushButton('去意已决')
    qbtn.clicked.connect(QCoreApplication.instance().quit)
    qbtn.setStyleSheet('''
        QPushButton:hover{color:red}
        QPushButton{font-size:30px;
                    font-weight:200;
        }''')
    page.grid.addWidget(qbtn, 4, 0)



