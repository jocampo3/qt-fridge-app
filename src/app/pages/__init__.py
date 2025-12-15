from PyQt6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QLabel, QWidget, QPushButton
import requests
from app.api import base_url
from app.pages.create import create_layout 
from app.pages.recipes import RecipeWidget

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
        self.tabs.addTab(RecipeWidget(), "Recipes")
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
            button = QPushButton(f"Discard {product.get('name', '')}")
            layout.addWidget(button)
            button.clicked.connect(lambda checked, p=product: self.delete_product(p))

        return widget

    def get_products(self):
        url = base_url + '/products'
        response = requests.get(url)
        data = response.json()
        return data['data']

    def delete_product(self, product):
        id = product.get('id', '')
        url = base_url + '/products/' + str(id)
        response = requests.delete(url)
        if response.status_code != 200:
            print('Could not delete product', response.text)
            return

        print('Product deleted successfully!')
        self.refresh_inventory()
