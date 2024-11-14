from House import House

class module_5_4:
    """
    Домашняя работа по уроку "Различие атрибутов класса и экземпляра"
    """
    print('\n\n-----Домашняя работа по уроку "Различие атрибутов класса и экземпляра"-----')
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)
    
    # Удаление объектов
    del h2
    del h3
    
    print(House.houses_history)