from House import House

class module_5_3:
    print('-----Домашняя работа по уроку "Перегрузка операторов"-----')
    h1 = House('ЖК Эльбрус', 10)
    h2 = House('ЖК Акация', 20)
    
    print(h1)
    print(h2)
    # __eq__
    print(h1 == h2) 
    
    
    # __add__
    h1 = h1 + 10 
    print(h1)
    print(h1 == h2)
    
    # __iadd__
    h1 += 10 
    print(h1)
    
    # __radd__
    h2 = 10 + h2 
    print(h2)
    
     # __gt__
    print(h1 > h2)
    # __ge__
    print(h1 >= h2) 
    # __lt__
    print(h1 < h2) 
    # __le__
    print(h1 <= h2) 
    # __ne__
    print(h1 != h2) 