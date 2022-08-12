import logging as console
import random

console.basicConfig(filename="Rent-a-Car.log", level=console.DEBUG, format='%(asctime)s%(message)s')

# to generate random car color and model year
class GenerateRandom:
    def __init__(self):
        console.info(' Accessing GenerateRandom')
        self._car_color = random.choice(['Black', 'Blue', 'Silver', 'White'])
        self._year = random.randint(2015, 2022)

    # sedan details


class Sedan:
    def __init__(self):
        g = GenerateRandom()
        self._charge_per_hr = 200
        self._charge_per_day = 5000
        self._fuel_type = 'Diesel'
        self._car_color = g._car_color
        self._year = g._year

    def car_details(self):
        """To display Sedan car details."""
        console.info(' Accessing Sedan car_details')
        print('\nSedan Car Details:\n\nHourly Charges: {}\nOne Day Charges: {}\nFuel Type: {}\nColor: {}\nYear: {}'
              .format(self._charge_per_hr, self._charge_per_day, self._fuel_type, self._car_color, self._year))


# sedan premium details
class SedanPremium:
    def __init__(self):
        g = GenerateRandom()
        self._charge_per_hr = 300
        self._charge_per_day = 5500
        self._fuel_type = 'Diesel'
        self._car_color = g._car_color
        self._year = g._year

    def car_details(self):
        """To display Sedan Premium car details."""
        console.info(' Accessing Sedan Premium car_details')
        print(
            '\nSedan Premium Car Details:\n\nHourly Charges: {}\nOne Day Charges: {}\nFuel Type: {}\nColor: {}\nYear: {}'
            .format(self._charge_per_hr, self._charge_per_day, self._fuel_type, self._car_color, self._year))


# suv details
class Suv:
    def __init__(self):
        g = GenerateRandom()
        self._charge_per_hr = 500
        self._charge_per_day = 7000
        self._fuel_type = 'Diesel'
        self._car_color = g._car_color
        self._year = g._year

    def car_details(self):
        """To display SUV details."""
        console.info(' Accessing Suv car_details')
        print('\nSUV Car Details:\n\nHourly Charges: {}\nOne Day Charges: {}\nFuel Type: {}\nColor: {}\nYear: {}'
              .format(self._charge_per_hr, self._charge_per_day, self._fuel_type, self._car_color, self._year))


# suv premium details
class SuvPremium:
    def __init__(self):
        g = GenerateRandom()
        self._charge_per_hr = 600
        self._charge_per_day = 7500
        self._fuel_type = 'Diesel'
        self._car_color = g._car_color
        self._year = g._year

    def car_details(self):
        """To display SUV Premium details."""
        console.info(' Accessing SuvPremium car_details')
        print(
            '\nSUV Premium Car Details:\n\nHourly Charges: {}\nOne Day Charges: {}\nFuel Type: {}\nColor: {}\nYear: {}'
            .format(self._charge_per_hr, self._charge_per_day, self._fuel_type, self._car_color, self._year))


class Car:
    @property
    def ask_car(self):
        """To display options."""
        try:
            # class objects to call corresponding functions
            console.info(' Accessing Car Class')
            available_cars = AvailableCars()
            return_car = ReturnCar()
            _ask_user = 0

            while _ask_user != '3':

                print(c)
                _ask_user = input(
                    '\n1. Do you want to Rent-a-Car?\n2. Do you want to Return-a-Car?\n3. Exit\n(Enter 1 or 2 or 3)')

                if _ask_user == '1':
                    available_cars.ask_for_car

                elif _ask_user == '2':
                    return_car.add_car

                elif _ask_user == '3':
                    print('\n** Thank you. Visit Again! **')
                    break

        except Exception as e:
            console.exception('Exception while choosing an option from Car class')
            print(e)


class AvailableCars(Car):
    def __init__(self):
        self.__car_options = ""
        self.__ch = ""
        self.__chosen_car = 0
        self.__chosen_option = ""
        self.__counter = 0

        # total number of cars the car provider has
        self.__no_of_sedan = 7
        self.__no_of_sedan_premium = 5
        self.__no_of_suv = 7
        self.__no_of_suv_premium = 4

    # to display message from car provider
    def __str__(self):
        return '\nRent-a-Car:\n** Travel without purchasing a Car. We provide car on rent. **'

    # sedan
    @property
    def total_sedan_cars(self):
        """To reduce number of available sedan cars."""
        console.info(' Inside total_sedan_cars')
        if self.__counter == 0:
            self.__counter = 1
            return self.__no_of_sedan

        elif self.__counter > 0:
            self.__counter += 1
            return self.__no_of_sedan

    @total_sedan_cars.setter
    def total_sedan_cars(self, value):
        """To set reduced value of self.__no_of_sedan if user books a car"""
        console.info(' Inside total_sedan_cars setter')
        self.__no_of_sedan = int(value)
        return

    @property
    def get_total_sedan_cars(self):
        """To get value of self.__no_of_sedan"""
        console.info(' Inside total_sedan_cars getter')
        return self.__no_of_sedan

    # sedan premium
    @property
    def total_sedan_premium(self):
        """To reduce number of available sedan premium cars."""
        console.info(' Inside total_sedan_premium')
        if self.__counter == 0:
            self.__counter = 1
            return self.__no_of_sedan_premium

        elif self.__counter > 0:
            self.__counter += 1
            return self.__no_of_sedan_premium

    @total_sedan_premium.setter
    def total_sedan_premium(self, value):
        """To set reduced value of self.__no_of_sedan_premium if user books a car."""
        console.info(' Inside total_sedan_premium setter')
        self.__no_of_sedan_premium = int(value)
        return

    @property
    def get_sedan_premium(self):
        """To get value of self.__no_of_sedan_premium"""
        console.info(' Inside total_sedan_premium getter')
        return self.__no_of_sedan_premium

    # suv
    @property
    def total_suv(self):
        """To reduce number of available sedan premium cars."""
        console.info(' Inside total_suv')
        if self.__counter == 0:
            self.__counter = 1
            return self.__no_of_suv

        elif self.__counter > 0:
            self.__counter += 1
            return self.__no_of_suv

    @total_suv.setter
    def total_suv(self, value):
        """To set reduced value of self.__no_of_suv if user books a car."""
        console.info(' Inside total_suv setter')
        self.__no_of_suv = int(value)
        return

    @property
    def get_total_suv(self):
        """To get value of self.__no_of_suv"""
        console.info(' Inside total_suv getter')
        return self.__no_of_suv

    # suv premium
    @property
    def total_suv_premium(self):
        """To reduce number of available SUVs."""
        console.info(' Inside total_suv_premium')
        if self.__counter == 0:
            self.__counter = 1
            return self.__no_of_suv_premium

        elif self.__counter > 0:
            self.__counter += 1
            return self.__no_of_suv_premium

    @total_suv_premium.setter
    def total_suv_premium(self, value):
        """To set reduced value of self.__no_of_suv_premium if user books a car"""
        console.info(' Inside total_suv_premium setter')
        self.__no_of_suv_premium = int(value)
        return

    @property
    def get_total_suv_premium(self):
        """To reduce number of available sedan cars."""
        console.info(' Inside total_suv_premium getter')
        return self.__no_of_suv_premium

    def get_key(self, val):
        """To get key of selected option inside a ask_for_car()"""
        for key, value in self.__car_options.items():
            if val == value:
                return key

    @property
    def ask_for_car(self):
        """To display Car options"""

        try:
            console.info(' Accessing ask_for_car')
            c = Car()
            sdn = Sedan()
            sdn_prm = SedanPremium()
            suv = Suv()
            suv_prm = SuvPremium()

            print("\nChoose a Car:")
            self.__cars = input(
                "1. Sedan\n   4 Seater, 2 Bags\n\n2. Sedan Premium\n(Full-size Sedan)\n   5 Seater, 2 Bags\n\n3. SUV\n   7 Seater, 2 Bags\n\n4. SUV Premium\n(Full-size SUV)\n   7 Seater, 3 Bags\n\nEnter 1 for Sedan, 2 for Sedan Premium, 3 for SUV, 4 for SUV Premium\n")
            self.__car_options = {'1': sdn.car_details, '2': sdn_prm.car_details, '3': suv.car_details,
                                  '4': sdn_prm.car_details}
            self.__chosen_car = self.__car_options.get(self.__cars)
            self.__chosen_car()

            # self.__chosen_option will have the key(option number) of selected option
            self.__chosen_option = self.get_key(self.__chosen_car)

            self.__ch = input("\nConfirm your choice?(y/n) : ")

            # if user confirms booking of a car, then reduce number of cars
            if self.__ch == 'y':
                self.reduce_no_of_cars

            # if user enters 'no' then again display the options
            elif self.__ch == 'n':
                self.ask_for_car

        except Exception as e:
            console.exception('Exception while entering option for choosing a car')
            print(e)

    @property
    def reduce_no_of_cars(self):
        """When user books a car then number of cars of the particular car type will be reduced by 1. And if
        all cars are booked display that the selected car is currently not available."""

        try:
            console.info(' Inside reduce_no_of_cars outer try block')
            try:
                console.info(' Inside reduce_no_of_cars nested try block')
                c = Car()
                # Sedan
                if self.__chosen_option == '1':
                    if self.get_total_sedan_cars == 0:
                        print('\nThis car is currently not available')

                    elif self.get_total_sedan_cars > 0:
                        print('\n☑️ Successfully booked a Sedan.')
                        self.total_sedan_cars -= 1

                # Sedan Premium
                elif self.__chosen_option == '2':
                    if self.get_sedan_premium == 0:
                        print('\nThis car is currently not available')

                    elif self.get_sedan_premium > 0:
                        self.total_sedan_premium -= 1
                        print('\n☑️ Successfully booked a Sedan Premium.')

                # SUV
                elif self.__chosen_option == '3':
                    if self.get_total_suv == 0:
                        print('\nThis car is currently not available')

                    elif self.get_total_suv > 0:
                        self.total_suv -= 1
                        print('\n☑️ Successfully booked a SUV.')

                # SUV Premium
                elif self.__chosen_option == '4':
                    if self.get_total_suv_premium == 0:
                        print('\nThis car is currently not available')

                    elif self.get_total_suv_premium > 0:
                        self.total_suv_premium -= 1
                        print('\n☑️ Successfully booked a SUV Premium.')

            except Exception as e:
                console.exception('Exception while reducing car number nested except')
                print(e)

        except Exception as e:
            console.exception('Exception while reducing car number outer except')
            print(e)


class ReturnCar(Car):
    @property
    def add_car(self):
        """To display car options while returning a car. Number of available cars will be incremented by 1."""

        try:
            console.info("Inside ReturnCar class's try block ")
            available_cars = AvailableCars()
            car_type = input(
                '\nChoose car type to return:\n1. Sedan\n2. Sedan Premium\n3. SUV\n4. SUV Premium\n5. Go Back\n\nEnter 1 for Sedan, 2 for Sedan Premium, 3 for SUV, 4 for SUV Premium, 5 to go back\n')

            # Return Sedan
            if car_type == '1':
                available_cars.total_sedan_cars += 1

            # Return Sedan Premium
            elif car_type == '2':
                available_cars.total_sedan_premium += 1

            # Return SUV
            elif car_type == '3':
                available_cars.total_suv += 1

            # Return SUV Premium
            elif car_type == '4':
                available_cars.total_suv_premium += 1

            elif car_type == '5':
                available_cars.ask_for_car


        except Exception as e:
            console.exception('Exception while incrementing car number')
            print(e)


c = AvailableCars()
c.ask_car