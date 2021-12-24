
def changeWord(word, old, new):
    """Kullanicidan değişecek metin ve eski harf ve 
    yeni harf bilgisini alarak girilen metin üzerinden
     değişikliği yapip sonucu ekrana yazdiran Python programini yaziniz."""
    result = word.replace(old,new)
    return print(result)