"""
sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 

ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. 

"""

def manipulate(my_dict):
    return print({k.replace(" ",""):v  for k,v in my_dict.items()})



sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 
manipulate(sozluk)
