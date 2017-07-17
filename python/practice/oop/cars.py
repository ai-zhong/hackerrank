class Car(object):
    wheels = 4
    def __init__(self, make, mode):
        self.make = make
        self.mode = mode
        self.miles = 0
        print('Car initiated with make=%s mode=%s miles=%s' % (self.make, self.mode, self.miles))


    def drive(self, miles):
        print('Car is Driving: mode=%s' % (self.mode))
        self.miles += miles
        self.check_miles()

    def stop(self):
        print('Car has stopped. mode=%s' % (self.mode))
        self.check_miles()

    def check_miles(self):
        print('Car has run: %s miles' %(self.miles))

    def check_car_info(self):
        print("price = %4.2f" %(self.check_price(self.mode)))

    @staticmethod
    def check_price(mode):
        if mode == "Best":
            price = 9000
        else:
            raise NotImplementedError("Error!")
        return price

    @classmethod
    def check_wheels(cls):
        print(cls.wheels)


if __name__ == '__main__':
    Car.check_wheels()
    toyota = Car('Japan', 'Best')
    toyota.check_car_info()

    miles_to_run = 25
    while toyota.miles <= 70:
        toyota.drive(miles_to_run)

    toyota.stop()