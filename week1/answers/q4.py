def isPolindrome(word):
    """ 
    Kullanici tarafindan girilen bir kelimenin 
    palindrom olup olmadigini karsilastirma 
    operatöründen faydalanarak print() fonksiyonu ile ekrana yazdiriniz. 
    """
    
    return word == word[::-1]