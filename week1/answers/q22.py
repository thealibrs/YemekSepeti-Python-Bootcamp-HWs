"""Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız"""


def takeInput():
    numbers = list()
    for i in range(10):
        num = int(input(f"enter {i+1}. number"))
        numbers.append(num)
    return numbers

def mostThree(arr):
    arr1 = sorted(arr)[::-1]
    return print(arr1[:3])


mostThree(takeInput())