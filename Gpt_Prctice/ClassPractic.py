# 차의 정보와, 주행거리를 업데이트하는 클래스
# 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
# 차의 정보 표시 함수
    def describe_car(self):
        print(f'This car is a {self.year} {self.make} {self.model}')

# 차의 주행거리 표시 함수
    def read_odometer(self):
        print(f'This car has driven {self.odometer_reading} miles.')

# 주행거리 업데이트 함수
    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You con't roll back an odometer!")

# 주행거리 증가시키는 함수
    def increment_odometer(self, miles):
        if miles >0:
            self.odometer_reading += miles
        else:
            print("You con't roll back an odometer!")

# 클래스 사용하기
my_car = Car('Toyota', 'Corolla', 2005) # Car클래스의 인자로 3개를 주고 my_car변수에 담는다.
my_car.describe_car() # 출력 :This car is a 2005 Toyota Corolla
my_car.read_odometer() # 출력 : This car has driven 0 miles
my_car.update_odometer(5000) # 주행거리를 5000으로 설정해준다
my_car.read_odometer() # 출력 : This car has driven 5000 miles
my_car.increment_odometer(500)
my_car.read_odometer() # 출력: 'This car has drive 5500 miles
"""
This car is a 2005 Toyota Corolla
This car has driven 0 miles.
This car has driven 5000 miles.
This car has driven 5500 miles.
"""


