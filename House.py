class House:
        # Домашняя работа по уроку "Различие атрибутов класса и экземпляра"
    houses_history = []
    
    def __new__(cls, *args):
        cls.houses_history.append(args)
        return object.__new__(cls)
    
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
    
    def __init__(self, name, number_of_floors):
        
        self.name = name
        self.number_of_floors = number_of_floors
        
    def go_to(self, new_floor):
        
        if self.number_of_floors >= new_floor >= 1:
            for floor in range(1, new_floor +1):
                print(f"Этаж: {floor}")
                
        else:   
            print('Такого этажа не существует') 
            
    # Домашняя работа по уроку "Специальные методы классов"
    def __len__(self):
        return self.number_of_floors
    
    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
    
    # Домашняя работа по уроку "Перегрузка операторов"
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
    
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)
    
