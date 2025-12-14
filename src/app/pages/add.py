from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QComboBox, QPushButton, QCalendarWidget
from app.api import base_url
import requests

def create_layout():
    widget = QWidget()
    layout = QVBoxLayout(widget)
    label1 = QLabel("Name")
    layout.addWidget(label1)
    product_input = QLineEdit()
    layout.addWidget(product_input)

    label2 = QLabel("Type")
    layout.addWidget(label2)
    types = QComboBox()
    types.addItems(["Fruits", "Vegetables", "Grains", "Dairy", "Meats", "Fats and Oils", "Other"])
    layout.addWidget(types)

    label3 = QLabel("QTY")
    layout.addWidget(label3)
    quantityInput = QLineEdit()
    layout.addWidget(quantityInput)

    label4 = QLabel("Store")
    layout.addWidget(label4)
    stores = QComboBox()
    stores.addItems(["Costco", "Trader Joes", "Wal-Mart", "Target", "Other"])
    layout.addWidget(stores)

    label5 = QLabel("Date Stored")
    layout.addWidget(label5)
    calendar = QCalendarWidget()
    layout.addWidget(calendar)

    button = QPushButton("Submit")

    button.clicked.connect(lambda checked: create_product({
        'name': product_input.text(),
        'type': types.currentText(),
        'quantity': int(quantityInput.text()),
        'store': stores.currentText(),
        'stored_at': calendar.selectedDate().toString('yyyy-MM-dd')
    }))
    layout.addWidget(button)

    return widget 

def create_product(product):
    print(product)
    url = base_url + '/products'
    response = requests.post(url, json=product)
    if response.status_code != 200:
        print('Could not create product...', response)
        return

    print('Product created successfully')
    return
