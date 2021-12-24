
"""
Bir listeyi bir sözlükte sıralamak için bir Python programı yazın <br>
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
"""

def sortDict(my_dict):
    for k,v in my_dict.items():
        my_dict[k] = sorted(v)

    return print(my_dict)



num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
#print(num)
sortDict(num)

