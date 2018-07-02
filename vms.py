class Vehicle:
    def __init__(self, name, seats, licence, avaiable, renter, cost):
        self._name = name
        self._seats = seats
        self._licence = licence
        self._available = avaiable
        self._renter = renter
        self._cost = cost
        vehicles.append(self)

    def _display_vehicles(self):
        print('----------------------')
        print('Name : {}'.format(self._name))
        print('Seats : {}'.format(self._seats))
        print('Licence : {}'.format(self._licence))
        print('${} per day'.format(self._cost))
        print('----------------------')

    def _display_vehicles_rented(self):
        print('----------------------')
        print('Name : {}'.format(self._name))
        print('Seats : {}'.format(self._seats))
        print('Licence : {}'.format(self._licence))
        print('${} per day'.format(self._cost))
        print('Rented by : {}'.format(self._renter))
        print('----------------------')

    def _rent_vehicle(self):
        self._renter = renter_name
        self._available = False

    def _return_vehicle(self):
        self._renter = ''
        self._available = True

vehicles = []

Vehicle('Ford Falcon', 5 , 'GTF724', True, '', 80)
Vehicle('Dodge Challenger', 4 , 'BAT528', True, '', 110)
Vehicle('Subaru WRX', 5 , 'GOX654', False, 'Betty', 100)
Vehicle('Toyota Supra', 4 , 'MHQ287', True, '', 95)
Vehicle('Ford Ranger', 5 , 'RAQ812', True, '', 90)
Vehicle('Honda Odyssey', 7 , 'NPQ114', False, 'John', 65)    


print("Welcome to BRAD's vehicle rental system")
while True:
    print("Input 1 to rent a vehicle.")
    print("Input 2 to return a vehicle.")
    while True:
        try:
            x = int(input(':'))
            if x == 1 or x == 2:
                break
            else:
                print('Please enter either 1 to rent a vehicle or 2 to return')
        except:
            print('Please enter an integer. \n Either 1 to rent a vehicle or 2 to return')
    if x == 1:
        counter = 0
        for v in vehicles:
            if v._available == True:
                counter += 1
                v._display_vehicles()
        if counter == 0:
            print('No Vehicles Available ')
        else:
            chosen_vehicle = input('Please enter the licence of your desired vehicle : ')
            counter = 0
            for b in vehicles:
                if chosen_vehicle in b._licence and b._available == True:
                    renter_name = input('Please enter your name : ')
                    b._rent_vehicle()
                    counter += 1
                    break
            if counter == 0:
                print('No Vehicles found')
            else:
                print("Thanks For renting with BRAD's vehicle rental system")
    elif x == 2:
        counter = 0
        for v in vehicles:
            if v._available == False:
                counter += 1
                v._display_vehicles_rented()
        if counter == 0:
            print('No Vehicles Rented ')
        else:
            chosen_vehicle = input('Please enter the licence of the vehicle you wish to return: ')
            counter = 0
            for b in vehicles:
                if chosen_vehicle in b._licence and b._available == False:
                    b._return_vehicle()
                    counter += 1
                    break
            if counter == 0:
                print('No Vehicles found')


