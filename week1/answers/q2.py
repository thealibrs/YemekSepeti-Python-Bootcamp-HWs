def lastFirstTwo(words):
    """
       Kullanici tarafindan girilen bir metnin 
       ilk iki ve son iki karakterini ekrana yazdiran 
       Python programini yaziniz.
    """
    result = words[:2]+words[len(words)-2:]
    return print(result)
