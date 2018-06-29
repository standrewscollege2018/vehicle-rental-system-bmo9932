class Vehicle:
    def __init__(self, name, seats, licence):
        self._name = name
        self._seats = seats
        self._licence = licence
        self._renter = ''
        self._available = True

def display_vehicle():
    


print("Welcome to BRAD's vehicle rental system")
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
    rent_vehicle()
elif x == 2:
    return_vehicle()




Vehicle('Ford Falcon', 5 , 'GTF724')
Vehicle('Dodge Challenger', 4 , 'BAT528')
Vehicle('Subaru WRX', 5 , 'GOX654')
Vehicle('Toyota Supra', 4 , 'MHQ287')
Vehicle('Ford Ranger', 5 , 'RAQ812')
Vehicle('Honda Odyssey', 7 , 'NPQ114')