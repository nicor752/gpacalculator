import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("GPA Calculator App")
        
        self.UIComponents()

# Setup for the title
    def UIComponents(self):
        self.container = QWidget()
        self.main_layout = QVBoxLayout()
        self.container.setLayout(self.main_layout)
        self.setCentralWidget(self.container)

        self.title_label = QLabel("GPA Calculator")
        h1_font = self.title_label.font()
        h1_font.setPointSize(30)
        self.title_label.setFont(h1_font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.main_layout.addWidget(self.title_label)

        self.left_panel = QWidget()
        self.left_panel_layout = QVBoxLayout()
        self.left_panel.setLayout(self.left_panel_layout)
        self.main_layout.addWidget(self.left_panel)

        left_pane = QVBoxLayout()
        
        right_pane = QVBoxLayout()

# Area where user enters class grades
        class_label = QLabel("Enter your class grade here:")
        h2_font = class_label.font()
        h2_font.setPointSize(20)
        class_label.setFont(h2_font)

# Results area
        results_label = QLabel("Your unweighted GPA is...")
        h2_font = results_label.font()
        h2_font.setPointSize(25)
        results_label.setFont(h2_font)

# Button calculate
        calculate_label = QLabel("Calculate it!")
        h2_font = calculate_label.font()
        h2_font.setPointSize(50)
        calculate_label.setFont(h2_font)
        calculate_label.setAlignment(Qt.AlignmentFlag.AlignRight)

# Description of app
        info_label = QLabel("The GPA calculator app allows you to...")
        h2_font = info_label.font()
        h2_font.setPointSize(50)
        info_label.setFont(h2_font)
        info_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        info_label.setAlignment(Qt.AlignmentFlag.AlignTop)

        push_button = QPushButton
        
# Calls the function
        
        left_pane.addWidget(self.title_label)

        right_pane.addWidget(results_label)
        left_pane.addWidget(class_label)
        right_pane.addWidget(calculate_label)
        

        self.main_layout.addLayout(left_pane)
        self.main_layout.addLayout(right_pane)




app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()