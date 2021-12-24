"""
sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız
Beklenen Çıktı :(6,60)
"""

def popItem(myDict):
    return print(myDict.popitem())

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

popItem(car)