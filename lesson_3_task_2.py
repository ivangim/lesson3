
from Smartphone import Smartphone
catalog = [
    Smartphone(brand="Apple",model="iphone 16 Pro",number="+79245768357"),
    Smartphone(brand="Samsung",model="Galaxy S25",number="+79095070123"),
    Smartphone(brand="Samsung",model="Galaxy S21",number="+79096752069"),
    Smartphone(brand="Xiaomi",model="Mi 11",number="+79147075438"),
    Smartphone(brand="Tecno SPARK",model="30 Pro",number="+79240945083"),
]
for Smartphone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")