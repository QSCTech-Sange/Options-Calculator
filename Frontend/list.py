from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QLabel


def list(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" 一览无遗")
    page.grid.addWidget(label_main, 0, 0)
    # 文本
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      这是算法展示\n")
    page.grid.addWidget(label_content, 1, 0)
    # B-S 模型
    label_bs = QLabel()
    label_bs.setFont(page.font_content)
    label_bs.setText("      B-S 模型\n")
    page.grid.addWidget(label_bs, 3, 0)
    webview_bs = QWebEngineView()
    webview_bs.setUrl(
        QUrl('https://wiki.mbalib.com/wiki/Black-Scholes%E6%9C%9F%E6%9D%83%E5%AE%9A%E4%BB%B7%E6%A8%A1%E5%9E%8B'))
    webview_bs.show()
    page.grid.addWidget(webview_bs, 4, 0)
    # 撑空白
    label_empty = QLabel()
    page.grid.addWidget(label_empty, 4, 0)
