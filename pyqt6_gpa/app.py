import sys
from PyQt6.QtCore import Qt
import controller


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
        self.container.setStyleSheet("background-color: beige;")
        self.title_label = QLabel("GPA Calculator")
        h1_font = self.title_label.font()
        h1_font.setPointSize(30)
        self.title_label.setFont(h1_font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(self.title_label, 0, 0)
        self.grade_inputs = QWidget
        self.grade_spinboxes = []
       
# Area where user enters class grades
        class_label = QLabel("Enter your class grade here:")
        h2_font = class_label.font()
        h2_font.setPointSize(20)
        class_label.setFont(h2_font)

        #Period 1
        class_1_container = QGroupBox("Period 1 ")
        class_1_container_layout = QGridLayout()
        class_1_container.setLayout(class_1_container_layout)
        enter_class1_title = QLineEdit("Enter class name here...")
        self.enter_grade_class_1 = QDoubleSpinBox()
        self.enter_grade_class_1.setMinimum(0)
        self.enter_grade_class_1.setMaximum(4.0)
        self.grade_spinboxes.append(self.enter_grade_class_1)
        class_1_container.setStyleSheet("background-color: white;")
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
        self.grade_spinboxes.append(self.enter_grade_class_2)
        class_2_container.setStyleSheet("background-color: white;")
        class_2_container_layout.addWidget(enter_class2_title, 0, 0)
        class_2_container_layout.addWidget(self.enter_grade_class_2, 0 , 1)
       
        #Period 3
        class_3_container = QGroupBox("Period 3 ")
        class_3_container_layout = QGridLayout()
        class_3_container.setLayout(class_3_container_layout)
        enter_class3_title = QLineEdit()
        self.enter_grade_class_3 = QDoubleSpinBox()
        self.enter_grade_class_3.setMinimum(0)
        self.enter_grade_class_3.setMaximum(4.0)
        self.grade_spinboxes.append(self.enter_grade_class_3)
        class_3_container.setStyleSheet("background-color: white;")
        class_3_container_layout.addWidget(enter_class3_title, 0, 0)
        class_3_container_layout.addWidget(self.enter_grade_class_3, 0 , 1)
       
        #Period 4
        class_4_container = QGroupBox("Period 4 ")
        class_4_container_layout = QGridLayout()
        class_4_container.setLayout(class_4_container_layout)
        enter_class4_title = QLineEdit()
        self.enter_grade_class_4 = QDoubleSpinBox()
        self.enter_grade_class_4.setMinimum(0)
        self.enter_grade_class_4.setMaximum(4.0)
        self.grade_spinboxes.append(self.enter_grade_class_4)
        class_4_container.setStyleSheet("background-color: white;")
        class_4_container_layout.addWidget(enter_class4_title, 0, 0)
        class_4_container_layout.addWidget(self.enter_grade_class_4, 0 , 1)
       
        #Period 5
        class_5_container = QGroupBox("Period 5 ")
        class_5_container_layout = QGridLayout()
        class_5_container.setLayout(class_5_container_layout)
        enter_class5_title = QLineEdit()
        self.enter_grade_class_5 = QDoubleSpinBox()
        self.enter_grade_class_5.setMinimum(0)
        self.enter_grade_class_5.setMaximum(4.0)
        self.grade_spinboxes.append(self.enter_grade_class_5)
        class_5_container.setStyleSheet("background-color: white;")
        class_5_container_layout.addWidget(enter_class5_title, 0, 0)
        class_5_container_layout.addWidget(self.enter_grade_class_5, 0 , 1)
       
        #Period 6
        class_6_container = QGroupBox("Period 6 ")
        class_6_container_layout = QGridLayout()
        class_6_container.setLayout(class_6_container_layout)
        enter_class6_title = QLineEdit()
        self.enter_grade_class_6 = QDoubleSpinBox()
        self.enter_grade_class_6.setMinimum(0)
        self.enter_grade_class_6.setMaximum(4.0)
        self.grade_spinboxes.append(self.enter_grade_class_6)
        class_6_container.setStyleSheet("background-color: white;")
        class_6_container_layout.addWidget(enter_class6_title, 0, 0)
        class_6_container_layout.addWidget(self.enter_grade_class_6, 0 , 1)
       
        #Period 7
        class_7_container = QGroupBox("Period 7 ")
        class_7_container_layout = QGridLayout()
        class_7_container.setLayout(class_7_container_layout)
        enter_class7_title = QLineEdit()
        self.enter_grade_class_7 = QDoubleSpinBox()
        self.enter_grade_class_7.setMinimum(0)
        self.enter_grade_class_7.setMaximum(4.0)
        self.grade_spinboxes.append(self.enter_grade_class_7)
        class_7_container.setStyleSheet("background-color: white;")
        class_7_container_layout.addWidget(enter_class7_title, 0, 0)
        class_7_container_layout.addWidget(self.enter_grade_class_7, 0 , 1)
       
        #Period 8
        class_8_container = QGroupBox("Period 8 ")
        class_8_container_layout = QGridLayout()
        class_8_container.setLayout(class_8_container_layout)
        enter_class8_title = QLineEdit()
        self.enter_grade_class_8 = QDoubleSpinBox()
        self.enter_grade_class_8.setMinimum(0)
        self.enter_grade_class_8.setMaximum(4.0)
        self.grade_spinboxes.append(self.enter_grade_class_8)
        class_8_container.setStyleSheet("background-color: white;")
        class_8_container_layout.addWidget(enter_class8_title, 0, 0)
        class_8_container_layout.addWidget(self.enter_grade_class_8, 0 , 1)
       
# Title & Description
        calc_desc_container = QLabel("How does the GPA calculator work?")
        description = QLabel("The app requires you to put an input for each of your classes, which is it's current grade. It will calculate the average of all those inputs, and it will display your school's GPA.")
        description.setWordWrap(True)
        description.setFixedWidth(200)
        description.setFixedHeight(100)
        warning = QLabel("WARNING: IF YOU DO NOT INPUT ANY GRADES, THE APP WILL CLOSE!")
        warning.setWordWrap(True)
        warning.setFixedWidth(200)
        warning.setFixedHeight(100)
        calc_desc_container.setWordWrap(True)
        calc_desc_container.setFixedWidth(200)
        calc_desc_container.setFixedHeight(100)
        calc_desc_container_layout = QGridLayout()
        calc_desc_container.setLayout(calc_desc_container_layout)
        calc_desc_container_layout.addWidget(description)
        calc_desc_container.setStyleSheet("font-size: 20px;")
       
# add calculate function as button
        self.push_button = QPushButton("Calculate!")
        self.push_button.clicked.connect(self.get_gradegpa)
        self.push_button.setStyleSheet("background-color: lightgreen;")

# Description of app
        info_label = QLabel("The GPA calculator app allows you to...")
        h2_font = info_label.font()
        h2_font.setPointSize(50)
        info_label.setFont(h2_font)
        info_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        info_label.setAlignment(Qt.AlignmentFlag.AlignTop)

# Display the average
        self.results_window = QLabel("Your GPA is....")
        self.results_window.setStyleSheet("font-size: 20px;")
       
# Calls the function
        self.main_layout.addWidget(class_1_container, 1, 0)
        self.main_layout.addWidget(class_2_container, 2, 0)
        self.main_layout.addWidget(class_3_container, 3, 0)
        self.main_layout.addWidget(class_4_container, 4, 0)
        self.main_layout.addWidget(class_5_container, 5, 0)
        self.main_layout.addWidget(class_6_container, 6, 0)
        self.main_layout.addWidget(class_7_container, 7, 0)
        self.main_layout.addWidget(class_8_container, 8, 0)
        self.main_layout.addWidget(calc_desc_container, 1, 1,)
        self.main_layout.addWidget(description, 2, 1)
        self.main_layout.addWidget(warning, 3, 1)
        self.main_layout.addWidget(self.push_button, 5, 1)
        self.main_layout.addWidget(self.results_window, 6, 1)

# Controller Calculation to main
    def get_gradegpa(self):
        """Calculate gpa"""
        grades = [spinbox.value() for spinbox in self.grade_spinboxes]
        grades = [grade for grade in grades if grade > 0]
        result = controller.get_gradegpa(grades)
        self.results_window.setText(result)
        self.results_window.setStyleSheet("font-size: 20px;")
       
# List
        grade_list = []
        grade = self.enter_grade_class_1.value()
        if grade > 0:
            grade_list.append(grade)


        grade = self.enter_grade_class_2.value()
        if grade > 0:
                grade_list.append(grade)


        grade = self.enter_grade_class_3.value()
        if grade > 0:
                grade_list.append(grade)


        grade = self.enter_grade_class_4.value()
        if grade > 0:
                grade_list.append(grade)


        grade = self.enter_grade_class_5.value()
        if grade > 0:
                grade_list.append(grade)


        grade = self.enter_grade_class_6.value()
        if grade > 0:
                grade_list.append(grade)


        grade = self.enter_grade_class_7.value()
        if grade > 0:
                grade_list.append(grade)


        grade = self.enter_grade_class_8.value()
        if grade > 0:
                grade_list.append(grade)

        results = controller.get_gradegpa(grade_list)
        print(results)
        self.results_window.setText(results)

app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()
