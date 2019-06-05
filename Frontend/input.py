from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QDateTimeEdit
from PyQt5.QtCore import QDate, QDateTime, QTime


def input(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" 指点江山")
    page.grid.addWidget(label_main, 0, 0, 1, 4)

    # 介绍文字
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      设定你的期货参数")
    page.grid.addWidget(label_content, 1, 0, 1, 4)

    # 选择当前时间
    label_t0 = QLabel()
    label_t0.setFont(page.font_content)
    label_t0.setText("当前日期")
    page.grid.addWidget(label_t0, 2, 0)
    page.date_edit_t0 = QDateTimeEdit(QDate.currentDate(), page.widget)
    page.date_edit_t0.setDisplayFormat('yyyy-MM-dd')
    page.date_edit_t0.setCalendarPopup(True)
    page.grid.addWidget(page.date_edit_t0, 2, 1)

    # 选择到期时间
    label_t1 = QLabel()
    label_t1.setFont(page.font_content)
    label_t1.setText("到期日期")
    page.grid.addWidget(label_t1, 2, 2)
    page.date_edit_t1 = QDateTimeEdit(QDate.currentDate().addDays(10), page.widget)
    page.date_edit_t1.setDisplayFormat('yyyy-MM-dd')
    page.date_edit_t1.setCalendarPopup(True)
    page.grid.addWidget(page.date_edit_t1, 2, 3)

    # 期权类型 美式欧式
    label_european = QLabel()
    label_european.setFont(page.font_content)
    label_european.setText("美式欧式")
    page.combo_european = QComboBox(page.widget)
    page.combo_european.addItem("欧式期权")
    page.combo_european.addItem("美式期权")
    page.grid.addWidget(label_european, 3, 0)
    page.grid.addWidget(page.combo_european, 3, 1)

    # 期权类型 看涨看跌
    label_kind = QLabel()
    label_kind.setFont(page.font_content)
    label_kind.setText("看涨看跌")
    page.combo_kind = QComboBox(page.widget)
    page.combo_kind.addItem("看涨")
    page.combo_kind.addItem("看跌")
    page.grid.addWidget(label_kind, 3, 2)
    page.grid.addWidget(page.combo_kind, 3, 3)

    # 标的资产现价
    label_s0 = QLabel()
    label_s0.setFont(page.font_content)
    label_s0.setText("标的资产现价")
    page.s0 = QLineEdit(page.widget)
    page.s0.setText('100')
    page.grid.addWidget(label_s0, 4, 0)
    page.grid.addWidget(page.s0, 4, 1)

    # 适用的波动率
    label_sigma = QLabel()
    label_sigma.setFont(page.font_content)
    label_sigma.setText("波动率（%）")
    page.sigma = QLineEdit(page.widget)
    page.sigma.setText('1')
    page.grid.addWidget(label_sigma, 4, 2, )
    page.grid.addWidget(page.sigma, 4, 3)

    # 期权执行价
    label_k = QLabel()
    label_k.setFont(page.font_content)
    label_k.setText("期权执行价")
    page.k = QLineEdit(page.widget)
    page.k.setText('100')
    page.grid.addWidget(label_k, 5, 0)
    page.grid.addWidget(page.k, 5, 1)

    # 适用的无风险利率
    label_r = QLabel()
    label_r.setFont(page.font_content)
    label_r.setText("一年复利计无风险利率(%)")
    page.r = QLineEdit(page.widget)
    page.r.setText('1')
    page.grid.addWidget(label_r, 5, 2)
    page.grid.addWidget(page.r, 5, 3)

    # 股利
    label_dv = QLabel()
    label_dv.setFont(page.font_content)
    label_dv.setText("利率(%)")
    page.dv = QLineEdit(page.widget)
    page.dv.setText('0')
    page.grid.addWidget(label_dv, 6, 0)
    page.grid.addWidget(page.dv, 6, 1)

    # 确定输入按键
    btn_confirm = QPushButton('确定输入')
    page.grid.addWidget(btn_confirm, 7, 0, 1, 4)
    btn_confirm.setStyleSheet('''
            QPushButton:hover{color:red}
            QPushButton{font-size:18px;
                        font-weight:200;
            }''')
    btn_confirm.clicked.connect(page.confirm)
