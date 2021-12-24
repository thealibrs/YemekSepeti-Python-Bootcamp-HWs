"""Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız."""


def count(sentence):
    upper, lower = list(), list()

    for c in sentence.replace(" ",""):
        if c.isupper():
            upper.append(c)
        else:
            lower.append(c)
    
    return print(upper, lower)


count("asSADASDDASdasd asdsad afaf asdsad qwqwdf fasaf")
