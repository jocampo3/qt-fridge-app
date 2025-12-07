from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QComboBox, QPushButton, QCalendarWidget
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 600)
        self.setWindowTitle("Inventory Management")
        layout = QVBoxLayout()

        self.label1 = QLabel("Name")
        layout.addWidget(self.label1)
        self.productInput = QLineEdit(self)
        layout.addWidget(self.productInput)

        self.label2 = QLabel("Type")
        layout.addWidget(self.label2)
        self.types = QComboBox(self)
        self.types.addItems(["Fruits", "Vegetables", "Grains", "Dairy", "Meats", "Fats and Oils", "Other"])
        layout.addWidget(self.types)

        self.label3 = QLabel("QTY")
        layout.addWidget(self.label3)
        self.quantityInput = QLineEdit(self)
        layout.addWidget(self.quantityInput)

        self.label4 = QLabel("Store")
        layout.addWidget(self.label4)
        self.stores = QComboBox(self)
        self.stores.addItems(["Costco", "Trader Joes", "Wal-Mart", "Target", "Other"])
        layout.addWidget(self.stores)

        self.label5 = QLabel("Date Stored")
        layout.addWidget(self.label5)
        self.calendar = QCalendarWidget(self)
        layout.addWidget(self.calendar)

        button = QPushButton("Submit", self)
        button.clicked.connect(self.display)
        layout.addWidget(button)

        self.setLayout(layout)


    def display(self):
        print(self.types.currentText(), f"({self.types.currentText()})")

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
