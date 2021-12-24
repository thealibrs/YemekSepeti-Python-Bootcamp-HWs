def fun(sentence):
    """Girilen bir metnin son 2 karakterini 
    4 defa çoğaltarak ekrana yazan Python programini yazınız. 
    `*` aritmetik operatöründen faydalanabilirsiniz. """
    answer = sentence[len(sentence)-2:]*4
    return print(answer)
