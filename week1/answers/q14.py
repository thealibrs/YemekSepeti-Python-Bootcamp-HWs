"""

liste=[1,2,3,4,5]
    a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun 
    b.sözlüğün her alamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin.
Beklenen Çıktı :
a. {1:0,2:0,3:0,4:0,5:0}
b. {1:10,2:20,3:30,4:40,5:50}

"""

def createDict(arr):
    d = {}
    return print({i:i*10 for i in liste})
    # or we can use setdefault


liste=[1,2,3,4,5]
createDict(liste)
