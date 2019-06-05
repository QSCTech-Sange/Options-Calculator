from PyQt5.QtWidgets import QLabel, QLineEdit


def result(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" 激扬文字")
    page.grid.addWidget(label_main, 0, 0, 1, 2)
    # 文字
    label_hint = QLabel()
    label_hint.setFont(page.font_content)
    label_hint.setText("      为您整理出期权价格的计算结果")
    page.grid.addWidget(label_hint, 1, 0, 1, 2)

    # BS价格
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      BS 方法计算价格")
    page.grid.addWidget(label_content, 2, 0)
    page.line_bs = QLineEdit(page.widget)
    page.line_bs.setEnabled(False)
    page.line_bs.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_bs, 2, 1)

    # MC价格
    label_mc = QLabel()
    label_mc.setFont(page.font_content)
    label_mc.setText("      蒙特卡罗方法计算价格")
    page.grid.addWidget(label_mc, 3, 0)
    page.line_mc = QLineEdit(page.widget)
    page.line_mc.setEnabled(False)
    page.line_mc.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_mc, 3, 1)

    # 二叉树价格
    label_bt = QLabel()
    label_bt.setFont(page.font_content)
    label_bt.setText("      二叉数方法计算价格")
    page.grid.addWidget(label_bt, 4, 0)
    page.line_bt = QLineEdit(page.widget)
    page.line_bt.setEnabled(False)
    page.line_bt.setStyleSheet("QLineEdit{background-color:white;color:black}")
    page.grid.addWidget(page.line_bt, 4, 1)
