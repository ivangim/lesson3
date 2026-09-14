class smartphone:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number
    def print_info(self):
        print(f"{self.brand} {self.model}, номер: {self.number}")
catalog = ([
    smartphone(brand="Apple",model="iphone 16 Pro",number="+79245768357"),
    smartphone(brand="Samsung",model="Galaxy S25",number="+79095070123"),
    smartphone(brand="Samsung",model="Galaxy S21",number="+79096752069"),
    smartphone(brand="Xiaomi",model="Mi 11",number="+79147075438"),
    smartphone(brand="Tecno SPARK",model="30 Pro",number="+79240945083"),
])
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
from smartphone import Smartphone