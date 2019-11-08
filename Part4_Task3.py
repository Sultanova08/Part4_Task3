# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”
# class Car ():
#     def __init__(self,make,model,year,odometer,fuel,km):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.fuel = 70
#         self.km = input ('Enter the km :')
#     def drive (self): 
#         self.odometer = self.odometer + km
#         print(f"Car drived {self.odometer}km")
#     if one_gallon < self.fuel:
#         print("The car drove {} miles".format(miles))
#     elif self.fuel == 0:
#             print("The car drove 0 miles")
#     else:
#        newMiles = milesDriven * miles
#        print("The car drove {} miles".format(newMiles))

#     self.fuel -= one_gallon
#     self.odometer += miles      

# def __subtract_fuel(self, volume):
#     # Even more argument tests removed.
#     if volume + self.fuel <= self.capacity:
#         self.fuel += volume

# # The method "tripRange()" is equivalent to "car.efficiency" so is removed
        

# new_car = Car('Mayram', 'Honda', 2008, None, None, [])    
# print(new_car.odometer)
# print(new_car.km)
# print(f"Distance {new_car.odometer}")
# new_car.drive()        


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, km):
        self.odometer += km   #self.odometr = self.odometr + km

    def __subtract_fuel(self, km):
        self.fuel -= km/10

    def drive(self, km):
        if (self.fuel - km/10) >= 0:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print('Let’s drive!')
        else:
            print('Need more fuel, please, fill more!')

car = Car('Mercedes', 'S-class', 2009)
car.drive(650)
print(car.odometer, car.fuel)
car.drive(50)
print(car.odometer, car.fuel)
car.drive(20)
print(car.odometer)



