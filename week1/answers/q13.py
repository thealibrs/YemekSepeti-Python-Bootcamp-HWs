"""
dict1={1:10, 2:20}
Yukarıdaki sözlüğe bir eleman ekleyiniz. 
Beklenen Çıktı :{1:10, 2:20, 3:30}
"""

k = int(input())
v = int(input())

dict1 = {1:10, 2:20}

dict1.setdefault(k,v)

print(dict1)

