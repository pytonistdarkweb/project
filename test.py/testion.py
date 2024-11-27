class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f'Vehicle Make: {self.make}, Model: {self.model}'

class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def display_info(self):
        return super().display_info() + f', Doors: {self.number_of_doors}'

class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)
        self.payload_capacity = payload_capacity

    def display_info(self):
        return super().display_info() + f', Payload Capacity: {self.payload_capacity} lbs'

# Создание объектов
my_car = Car('Toyota', 'Corolla', 4)
my_truck = Truck('Ford', 'F-150', 2000)

# Вывод информации
print(my_car.display_info())
print(my_truck.display_info())




# начнем с начала с первой строчки тут объявляется класс "Vehicle" в нем объявляется функция с инициализатором "def init "атрибуты ссылкой на них дальше в этом же классе объявляется функция которая выступает методом который возвращается текст в "f-формате" с атрибутами которые записаны в фигурные скобки  
# дальше идет создание нового класса который наследует уже класс "Vehicle" и его атрибуты помимо этого создает свой атрибут в функции инициализаторе "self.number_of_doors = number_of_doors" после объявляется метод который возвращает метод из класса "Vehicle" и конкатинирует его с атрибутом из своего класса после 
# создается еще класс который создает метод инициализатор который импортирует атрибут из первого класса  и создает свой атрибут после создает метод который возвращает  метод из первого класса и конкатинирует его со своим "self.payload_capacity" после создается экземпляр класса "Car" который передает значения в свой класс своим атрибутам 
# и еще атрибутам первого унаследованного класса так же работает и следующий экземпляр а точнее 3 класс и все они в конце с помощь встроенной функции  print используют унаследованный метод из первого класса