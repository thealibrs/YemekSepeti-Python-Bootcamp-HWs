"""kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. """

def takeInput():
    numbers = list()
    for i in range(10):
        num = int(input(f"enter {i+1}. number"))
        numbers.append(num)
    return numbers

def scrapNumbers(arr):

    odd, even = list(), list()

    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
    return print(f"EVEN => {even}  ODD => {odd}")

scrapNumbers(takeInput())