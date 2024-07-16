from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QMessageBox
from scraper.web_scraper import fetch_data
from urllib.parse import urlparse


def is_valid_url(url):  # 添加URL验证方法
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def show_error_message(message):  # 添加错误消息显示方法
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setText("An error occurred")
    msg_box.setInformativeText(message)
    msg_box.setWindowTitle("Error")
    msg_box.exec_()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Star")
        self.setGeometry(100, 100, 800, 600)

        # 设置中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 布局
        layout = QVBoxLayout()

        # 标签和按钮
        self.label = QLabel("Enter URL to fetch data:")
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Enter URL here...")
        self.button = QPushButton("Fetch Data")
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        # 添加控件到布局
        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.result_text)

        central_widget.setLayout(layout)

        # 连接按钮点击事件
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        url = self.text_edit.toPlainText()
        if is_valid_url(url):  # 添加URL验证
            try:
                data = fetch_data(url)
                self.result_text.clear()
                if data:
                    for item in data:
                        self.result_text.append(item.get_text())
                else:
                    self.result_text.append("No data found or error occurred.")
            except Exception as e:
                print(f"Error in on_button_clicked: {e}")
                show_error_message(str(e))
        else:
            show_error_message("Invalid URL. Please enter a valid URL.")  # 添加无效URL提示

