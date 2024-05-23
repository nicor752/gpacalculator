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
    QGridLayout,
    QGroupBox
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
        self.main_layout = QGridLayout()

        self.container.setLayout(self.main_layout)
        self.setCentralWidget(self.container)

        self.title_label = QLabel("GPA Calculator")
        h1_font = self.title_label.font()
        h1_font.setPointSize(30)
        self.title_label.setFont(h1_font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(self.title_label, 0, 0)

 

        # self.left_panel = QWidget()
        # self.left_panel_layout = QVBoxLayout()
        # self.left_panel.setLayout(self.left_panel_layout)
        # self.main_layout.addWidget(self.left_panel)

        left_pane = QVBoxLayout()
        
        right_pane = QVBoxLayout()


        self.grade_inputs = QWidget
        

# Area where user enters class grades
        class_label = QLabel("Enter your class grade here:")
        h2_font = class_label.font()
        h2_font.setPointSize(20)
        class_label.setFont(h2_font)

        #Period 1
        class_1_container = QGroupBox("Period 1 ")
        class_1_container_layout = QGridLayout()
        class_1_container.setLayout(class_1_container_layout)
        enter_class1_title = QLineEdit()
        self.enter_grade_class_1 = QDoubleSpinBox()
        self.enter_grade_class_1.setMinimum(0)
        self.enter_grade_class_1.setMaximum(4.0)

        class_1_container_layout.addWidget(enter_class1_title, 0, 0)
        class_1_container_layout.addWidget(self.enter_grade_class_1, 0 , 1)

        #Period 2
        class_2_container = QGroupBox("Period 2 ")
        class_2_container_layout = QGridLayout()
        class_2_container.setLayout(class_2_container_layout)
        enter_class2_title = QLineEdit()
        self.enter_grade_class_2 = QDoubleSpinBox()
        self.enter_grade_class_2.setMinimum(0)
        self.enter_grade_class_2.setMaximum(4.0)

        class_2_container_layout.addWidget(enter_class2_title, 0, 0)
        class_2_container_layout.addWidget(self.enter_grade_class_2, 0 , 1)

        #Period3
        class_3_container = QGroupBox("Period 3 ")
        class_3_container_layout = QGridLayout()
        class_3_container.setLayout(class_3_container_layout)
        enter_class3_title = QLineEdit()
        self.enter_grade_class_3 = QDoubleSpinBox()
        self.enter_grade_class_3.setMinimum(0)
        self.enter_grade_class_3.setMaximum(4.0)

        class_3_container_layout.addWidget(enter_class3_title, 0, 0)
        class_3_container_layout.addWidget(self.enter_grade_class_3, 0 , 1)

        #Title
        calc_desc_container = QGroupBox("How does the GPA calculator work?")
        calc_desc_container_layout = QGridLayout()
        calc_desc_container.setLayout(calc_desc_container_layout)
        
        #Description
        #calc_text = QLabel("Test")
# Results area
        results_label = QLabel("Your unweighted GPA is...")
        h2_font = results_label.font()
        h2_font.setPointSize(25)
        results_label.setFont(h2_font)

#def calculate_grade(self):
        "Calculate GPA"
# All class grades
#def calculate_grade(self):
       # gpa = enter_grade_class_3.value()
       # print(gpa)
        #self.results_window.Text("Your GPA is {gpa}.")

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

        self.push_button = QPushButton("Calcuate!")
        # add calculate function
        self.push_button.clicked.connect(self.calculate_grade)

# Display the average
        self.results_window = QLabel("Average")

            
            
        
# Calls the function
        self.main_layout.addWidget(class_1_container, 1, 0)
        self.main_layout.addWidget(class_2_container, 2, 0)
        self.main_layout.addWidget(class_3_container, 3, 0)
        self.main_layout.addWidget(calc_desc_container, 1, 1)
        #self.main_layout.addWidget(calc_text, 2, 1)
        self.main_layout.addWidget(self.push_button, 2, 1)
        self.main_layout.addWidget(self.results_window, 3, 1)
        



        # right_pane.addWidget(results_label)
        # left_pane.addWidget(class_label)
        # right_pane.addWidget(calculate_label)
        

        # self.main_layout.addLayout(left_pane, 1, 0)
        # self.main_layout.addLayout(right_pane, 1, 2)

    def calculate_grade(self):
        """Calculate gpa"""
        gpa = self.enter_class_grade_1.value()
        print(gpa)
        self.results_window.setText(f"Your GPA is {gpa}.")



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()