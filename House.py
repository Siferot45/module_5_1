class House:
    
    def __init__(self, name, number_of_floors):
        
        self.name = name
        self.number_of_floors = number_of_floors
        
    def go_to(self, new_floor):
        
        if self.number_of_floors >= new_floor >= 1:
            for floor in range(1, new_floor +1):
                print(f"Этаж: {floor}")
                
        else:   
            print('Такого этажа не существует') 
