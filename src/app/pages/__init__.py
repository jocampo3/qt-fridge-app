from PyQt6.QtWidgets import QCheckBox, QMainWindow, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton
import requests
from app.api import base_url
from app.pages.add import create_layout 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700, 600)
        self.setWindowTitle("Inventory Management")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.tabs = QTabWidget()
        self.tabs.addTab(self.product_layout(), "Inventory")
        self.tabs.addTab(create_layout(), "Create")
        self.tabs.currentChanged.connect(self.on_tab_change)
        layout.addWidget(self.tabs)

    def on_tab_change(self, index):
        if index == 0:
            self.refresh_inventory()

    def refresh_inventory(self):
        self.tabs.currentChanged.disconnect(self.on_tab_change)
        
        old_widget = self.tabs.widget(0)
        
        self.tabs.removeTab(0)
        
        if old_widget:
            old_widget.deleteLater()
        
        self.tabs.insertTab(0, self.product_layout(), "Inventory")
        self.tabs.setCurrentIndex(0)
        
        self.tabs.currentChanged.connect(self.on_tab_change)

    def product_layout(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        products = self.get_products()
        for product in products:
            product_info = "\n".join([f"{key}: {value}" for key, value in product.items()])
            label = QLabel(product_info)
            layout.addWidget(label)
            button = QPushButton(f"Delete {product.get('name', '')}")
            layout.addWidget(button)
            button.clicked.connect(lambda checked: self.delete_product(product.get('id')))

        return widget

    def get_products(self):
        url = base_url + '/products'
        response = requests.get(url)
        data = response.json()
        return data['data']

    def delete_product(self, id):
        print(f"{id} deleted!")

        # url = base_url + '/products'
        # response = requests.delete(url)
