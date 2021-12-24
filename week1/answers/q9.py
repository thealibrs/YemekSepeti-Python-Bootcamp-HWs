"""liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. 
"""
def removeFirstThree(arr):
    arr.pop(arr.index(3))
    return print(arr)


liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
removeFirstThree(liste)