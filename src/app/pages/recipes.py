from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QComboBox, QPushButton, QCalendarWidget
from app.api import base_url
import requests
from openai import OpenAI
import os

class RecipeWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.button = QPushButton("Generate Receipes")
        self.button.clicked.connect(lambda checked: self.generate_recipes())
        layout.addWidget(self.button)

        self.recipe_display = QLabel("Click the button to generate recipes based on your inventory")
        self.recipe_display.setWordWrap(True)
        layout.addWidget(self.recipe_display)

        layout.addStretch()

    def generate_recipes(self):
        self.recipe_display.setText("Generating recipes...")
        products = self.get_products()
        recipes = self.get_ai_recipes(products)
        self.recipe_display.setText(recipes)

    def get_products(self):
        url = base_url + '/products'
        response = requests.get(url)
        data = response.json()
        return data['data']

    def get_ai_recipes(self, products):
        print("getting recipes...")
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        response = client.responses.create(
            model="gpt-4o",
            instructions="You are an 5-Start Michelin that knows how to cook exotic dishes. For the provided product information, you are to provide recipe ideas for breakfast, lunch, and dinner.",
            input=f"{products}"
        )

        print(response)

        return response.output_text
