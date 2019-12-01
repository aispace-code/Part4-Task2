# и методы имитирующих поведение самолета take off (взлет), fly (летать),
# land приземление). Метод take off должен изменить is_flying на True, а
# land на False. По умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и и
# зменять показания одометра (километраж). Создайте 1 объект класса и используйте все методы класса.
class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying = False):
        self.make = make
        self.model =model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying

    def take_off(self):
        self.is_flying = True

    def fly(self, distance):
        self.odometer += distance
        print('The new value of odometer is ' + str(self.odometer))


    def land(self):
        self.is_flying = False

new_Airplane = Airplane('BX700', 700, 2000, 800, 0)
new_Airplane.fly(1200)




