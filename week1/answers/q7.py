"""İki farklı listede tutulan verileri tek bir listede sırasıyla append,extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız 
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = ?????
"""

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = list()

# with append
for i in liste1+liste2:
    liste3.append(i)
print(liste3)

#with extend
liste1.extend(liste2)
print(liste1)

# with +
liste3 = liste1 + liste2
print(liste3)