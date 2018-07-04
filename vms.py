class Vehicle:
    # Function to get the objects listed below and extract the variables within them add adding them to the list vehicles
    def __init__(self, name, seats, licence, avaiable, renter, cost):
        self._name = name
        self._seats = seats
        self._licence = licence
        self._available = avaiable
        self._renter = renter
        self._cost = cost
        vehicles.append(self)

    # Function to display the vehicles in the rent option
    # Used to format this infomation to make it look cleaner
    def _display_vehicles(self):
        print('----------------------')
        print('Name : {}'.format(self._name))
        print('Seats : {}'.format(self._seats))
        print('Licence : {}'.format(self._licence))
        print('${} per day'.format(self._cost))
        print('----------------------')

    # Function to display the vehicles in the return option
    # Same as above except showing who is renting the car 
    def _display_vehicles_rented(self):
        print('----------------------')
        print('Name : {}'.format(self._name))
        print('Seats : {}'.format(self._seats))
        print('Licence : {}'.format(self._licence))
        print('${} per day'.format(self._cost))
        print('Rented by : {}'.format(self._renter))
        print('----------------------')

    # Used to change the availability variable to false and set the renter name.
    def _rent_vehicle(self):
        self._renter = renter_name
        self._available = False

    # Used to set the availability to True and set the renter name to blank 
    def _return_vehicle(self):
        self._renter = ''
        self._available = True

# Setting the list to empty that stores the objects.
vehicles = []

# Setting the objects that will be displayed in the list 
Vehicle('Ford Falcon', 5 , 'GTF724', True, '', 80)
Vehicle('Dodge Challenger', 4 , 'BAT528', True, '', 110)
Vehicle('Subaru WRX', 5 , 'GOX654', False, 'Betty', 100)
Vehicle('Toyota Supra', 4 , 'MHQ287', True, '', 95)
Vehicle('Ford Ranger', 5 , 'RAQ812', True, '', 90)
Vehicle('Honda Odyssey', 7 , 'NPQ114', False, 'John', 65)    


# Welcome message and while true loop so that you can do multiple things in one session
print("Welcome to BRAD's vehicle rental system")
while True:
    print("Input 1 to rent a vehicle.")
    print("Input 2 to return a vehicle.")
    print("Input 3 to add a new vehicle.")
    # Error catching for insuring the input is 1 , 2 or 3
    while True:
        try:
            x = int(input(':'))
            if x == 1 or x == 2 or x==3:
                break
            else:
                print('Please enter either 1 to rent a vehicle or 2 to return')
        except:
            print('Please enter an integer. \n Either 1 to rent a vehicle or 2 to return')
    # Code for displaying vehicles and renting a vehicle
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
    # Code for returning a vehicle
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
    # Code for adding a new car
    elif x == 3:
        name = input('Name of car : ')
        seats = input('Number of seats :')
        licence = input('Licence plate number : ')
        cost = input('Cost for one day : ')

        Vehicle(name, seats , licence , True, '', cost)

