from PyQt5.QtWidgets import QLabel


def about(page):
    # 标题
    label_main = QLabel()
    label_main.setFont(page.font_main)
    label_main.setText(" 毛遂自荐")
    page.grid.addWidget(label_main, 0, 0)
    # 文本
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      这是期权价格计算器的开发人员。\n      为您的使用保驾护航。\n      来去匆匆，请多指教。")
    page.grid.addWidget(label_content, 1, 0)
    # 另一段文本
    label_content = QLabel()
    label_content.setFont(page.font_content)
    label_content.setText("      杨宇昊 3160105521\n      张天暖 3160103915\n      程   龙 3160104356")
    page.grid.addWidget(label_content, 2, 0, 1, 1)

    # 撑空白
    label_empty = QLabel()
    page.grid.addWidget(label_empty, 4, 0)