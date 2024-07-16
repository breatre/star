from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Star")
        self.setGeometry(100, 100, 800, 600)

        # 设置中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        label = QLabel("Welcome to Star!")
        layout.addWidget(label)

        central_widget.setLayout(layout)
