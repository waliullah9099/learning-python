class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity


    def make_noice(self):
        print("hahhahha")


    @property
    def number_of_wheels(self):
        return self.__number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.__number_of_wheels = number


tesla_model_s = Vehicle(4, 'electric', 5, 250)
# print(tesla_model_s.number_of_wheels)

tesla_model_s.number_of_wheels = 2
# print(tesla_model_s.number_of_wheels)

tesla_model_s.make_noice()




class Person:
    def __init__(self, name):
        self.name = name


moin = Person("Moin ALI")
moin.name = "Samiul"
# print(moin.name)



class Person2:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

    def update_email(self, new_email):
        self._email = new_email

tk = Person2('TK', "tk@mail.com")
# print(tk._email)
tk.update_email("new_tk@mail.com")
# print(tk._email)

# Public Method 

class Person3:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._age

habiba = Person3('Habiba', 16)
# print(habiba.show_age())


# Non-public Method 

class Person4:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def get_age(self):
        return self._show_age()

    def _show_age(self):
        return self._age

habiba = Person4('Habiba', 16)
# print(habiba.get_age())


# Inheritance 

class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

my_car = Car(4, 5, 250)
tahar_car = Car(2, 3, 5)
print(my_car.number_of_wheels, my_car.seating_capacity)
print(tahar_car.number_of_wheels, tahar_car.maximum_velocity, tahar_car.seating_capacity)




  
