from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QPropertyAnimation,QRect

def welcome(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" 别来无恙")
    page.grid.addWidget(label_main, 0, 0)
    # 文本
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      且将新火试新茶。诗酒趁年华。\n      为你的期权接风涤尘。")
    page.grid.addWidget(label_content, 1, 0)
    # 开始探索图片
    hint = QLabel()
    directory = "img/hint.png"
    pix = QPixmap()
    pix.load(directory)
    hint.setPixmap(pix)
    page.grid.addWidget(hint, 2, 0, 1, 1)
    # 撑空白
    label_empty = QLabel()
    page.grid.addWidget(label_empty, 4, 0)
