class BoardingPass:
    def __init__(self, passenger_name, from_location, to_location, arrival_time, departure_time, terminal, electronic_ticket):
        # Initialize attributes with provided values
        self.passenger_name = passenger_name
        self.from_location = from_location
        self.to_location = to_location
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.terminal = terminal
        self.electronic_ticket = electronic_ticket

    def display_boarding_pass(self):
        # Display boarding pass details
        print("Boarding Pass:")
        print(f"Passenger: {self.passenger_name}")
        print(f"From: {self.from_location}  To: {self.to_location}")
        print(f"Arrival Time: {self.arrival_time}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Terminal: {self.terminal}")
        print(f"Electronic Ticket: {self.electronic_ticket}")

    def update_boarding_pass(self, new_flight_details):
        # Update boarding pass details with new information
        self.from_location = new_flight_details.get('from_location', self.from_location)
        self.to_location = new_flight_details.get('to_location', self.to_location)
        self.arrival_time = new_flight_details.get('arrival_time', self.arrival_time)
        self.departure_time = new_flight_details.get('departure_time', self.departure_time)
        self.terminal = new_flight_details.get('terminal', self.terminal)
        self.electronic_ticket = new_flight_details.get('electronic_ticket', self.electronic_ticket)


class Passenger:
    def __init__(self, name, location_from, location_to):
        # Initialize passenger attributes
        self.name = name
        self.location_from = location_from
        self.location_to = location_to


# User input to create Passenger object
passenger_name = input("Enter passenger name: ")
from_location = input("Enter departure location: ")
to_location = input("Enter destination location: ")

# Create Passenger object
passenger = Passenger(name=passenger_name, location_from=from_location, location_to=to_location)

# User input to create BoardingPass object
boarding_pass_info = {
    "passenger_name": passenger_name,
    "from_location": from_location,
    "to_location": to_location,
    "arrival_time": input("Enter arrival time: "),
    "departure_time": input("Enter departure time: "),
    "terminal": input("Enter terminal: "),
    "electronic_ticket": input("Enter electronic ticket number: "),
}

# Create BoardingPass object
boarding_pass = BoardingPass(**boarding_pass_info)

# Display initial boarding pass details
boarding_pass.display_boarding_pass()

# User input to update BoardingPass object
update_choice = input("Do you want to update the boarding pass? (yes/no): ").lower()
if update_choice == "yes":
    new_flight_details = {
        "from_location": input("Enter updated departure location: "),
        "to_location": input("Enter updated destination location: "),
        "arrival_time": input("Enter updated arrival time: "),
        "departure_time": input("Enter updated departure time: "),
        "terminal": input("Enter updated terminal: "),
        "electronic_ticket": input("Enter updated electronic ticket number: "),
    }

    # Update and display the boarding pass with new information
    boarding_pass.update_boarding_pass(new_flight_details)
    boarding_pass.display_boarding_pass()
else:
    print("Boarding pass not updated.")
def display_boarding_pass(self):
    print("Boarding Pass:")
    print(f"Passenger: {self.passenger_name}")
    print(f"From: {self.from_location}  To: {self.to_location}")
    print(f"Arrival Time: {self.arrival_time}")
    print(f"Departure Time: {self.departure_time}")
    print(f"Terminal: {self.terminal}")
    print(f"Electronic Ticket: {self.electronic_ticket}")
def display_boarding_pass(self):
    print("Boarding Pass:")
    print(f"Passenger: {self.passenger_name}")
    print(f"From: {self.from_location}  To: {self.to_location}")
    print(f"Arrival Time: {self.arrival_time}")
    print(f"Departure Time: {self.departure_time}")
    print(f"Terminal: {self.terminal}")
    print(f"Electronic Ticket: {self.electronic_ticket}")
    #Step 1: Class Definitions
#a. Defining BoardingPass:
class BoardingPass:
    def __init__(self, passenger_name, from_location, to_location, arrival_time, departure_time, terminal, electronic_ticket):
        self.passenger_name = passenger_name
        self.from_location = from_location
        self.to_location = to_location
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.terminal = terminal
        self.electronic_ticket = electronic_ticket


#Just a basic Python BoardingPass class explanation. The characteristics of this class correspond to different boarding pass data. Here's a quick rundown of each quality:

#passenger_name: The passenger's name.

#from_location: the location of departure.

#to_location: The place of arrival.

#arrival_time: The moment of arrival at the target location.

#departure_time: The time at which you leave the departure point.

#terminal: The details of the terminal.

#electronic_ticket: The number assigned to the electronic ticket.

#It is possible to generate boarding pass objects with particular information for various people and flights using this class.

#b. Defining display_boarding_pass:
def display_boarding_pass(self):
    print("Boarding Pass:")
    print(f"Passenger: {self.passenger_name}")
    print(f"From: {self.from_location}  To: {self.to_location}")
    print(f"Arrival Time: {self.arrival_time}")
    print(f"Departure Time: {self.departure_time}")
    print(f"Terminal: {self.terminal}")
    print(f"Electronic Ticket: {self.electronic_ticket}")
    #Explanation: The BoardingPass class defines the display_boarding_pass function. The boarding pass details are printed using this approach.

#The self parameter indicates that display_boarding_pass is a method in the BoardingPass class.

#Using print statements, the technique outputs a formatted version of the boarding pass details.

#Every line in the output relates to a distinct BoardingPass class attribute.

#c. Defining update_boarding_pass:
def update_boarding_pass(self, new_flight_details):
    # Update boarding pass details with new information
    self.from_location = new_flight_details.get('from_location', self.from_location)
    self.to_location = new_flight_details.get('to_location', self.to_location)
    self.arrival_time = new_flight_details.get('arrival_time', self.arrival_time)
    self.departure_time = new_flight_details.get('departure_time', self.departure_time)
    self.terminal = new_flight_details.get('terminal', self.terminal)
    self.electronic_ticket = new_flight_details.get('electronic_ticket', self.electronic_ticket)
    #Reasoning: The BoardingPass class now has an update_boarding_pass function implemented. This method updates the boarding pass attributes based on the information provided, and it accepts a dictionary named new_flight_details as an argument.

#The BoardingPass class has a method called update_boarding_pass.

#It accepts as an argument a dictionary called new_flight_details, which is probably updated.

#To update just the requested attributes from new_flight_details, the function uses the get method for each attribute. A key maintains its current value if it is missing from the dictionary.

#This makes it possible to change the boarding pass in a flexible way by changing just the desired attributes.

#d. Defining Passenger:
class Passenger:
    def __init__(self, name, location_from, location_to):
        # Initialize passenger attributes
        self.name = name
        self.location_from = location_from
        self.location_to = location_to
        #The explanation: Created a Python Passenger class. The init function of this class initializes a passenger's attributes.

#The three characteristics of the Passenger class are name, location_from, and location_to.

#When an object is created, a unique method in Python classes called the init method is called. The object's attributes are initialized.

#A reference to the class instance is contained in the self parameter. It is used to gain access to the instance's properties and functions.

#The method allocates the three parameters—name, location_from, and location_to—to the appropriate instance attributes.

#Step 2: User Input for Passenger
passenger_name = input("Enter passenger name: ")
from_location = input("Enter departure location: ")
to_location = input("Enter destination location: ")

passenger = Passenger(name=passenger_name, location_from=from_location, location_to=to_location)
#The explanation:
#The code asks the user to provide the passenger's name, place of departure, and location of destination.

#With the entered data, a Passenger object is created.

#Step 3: User Input for BoardingPass
boarding_pass_info = {
    "passenger_name": passenger_name,
    "from_location": from_location,
    "to_location": to_location,
    "arrival_time": input("Enter arrival time: "),
    "departure_time": input("Enter departure time: "),
    "terminal": input("Enter terminal: "),
    "electronic_ticket": input("Enter electronic ticket number: "),
}

boarding_pass = BoardingPass(**boarding_pass_info)
#Explanation:

#The code asks the user to enter the terminal, arrival and departure times, and electronic ticket number in order to complete the boarding pass.

#With the entered data, a BoardingPass object is created.

#Step 4: Display Initial Boarding Pass
boarding_pass.display_boarding_pass()
#Explanation:

#To show the initial boarding pass details, the code calls the display_boarding_pass method.

#Step 5: User Input to Update Boarding Pass
update_choice = input("Do you want to update the boarding pass? (yes/no): ").lower()
if update_choice == "yes":
    new_flight_details = {
        "from_location": input("Enter updated departure location: "),
        "to_location": input("Enter updated destination location: "),
        "arrival_time": input("Enter updated arrival time: "),
        "departure_time": input("Enter updated departure time: "),
        "terminal": input("Enter updated terminal: "),
        "electronic_ticket": input("Enter updated electronic ticket number: "),
    }

    boarding_pass.update_boarding_pass(new_flight_details)
    boarding_pass.display_boarding_pass()
else:
    print("Boarding pass not updated.")
    #Explanation:

#The code manages the answer and asks the user if they want to update the boarding pass.

#The BoardingPass object is updated and new details are prompted for if the user choose to update.

#The user is then informed that the boarding pass has not been updated or the revised details are displayed.
#from datetime import datetime

class Airport:
    def __init__(self, name):
        self.name = name

class Passenger:
    def __init__(self, name, phone_number, seat_number):
        self.name = name
        self.phone_number = phone_number
        self.seat_number = seat_number

class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time, gate):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.gate = gate

class BoardingPassSystem:
    def generateBoardingPass(self, passenger, flight):
        return f"Boarding Pass: {passenger.name}, Flight: {flight.flight_number}"

    def viewBoardingPass(self, boarding_pass):
        print(boarding_pass)

    def updatePassengerInfo(self, passenger, new_seat_number):
        passenger.seat_number = new_seat_number

# Create objects for all classes
airport = Airport("DXB Airport")
passenger = Passenger("Alya", "98753567", "07F")
flight = Flight("987", "Dubai", "London", datetime(2024, 2, 25, 8, 0),
                datetime(2024, 2, 25, 10, 0), "Gate4")
boardingPassSystem = BoardingPassSystem()

# Generate boarding pass
boarding_pass = boardingPassSystem.generateBoardingPass(passenger, flight)

# View boarding pass information
print("\n\t\tView the Boarding pass")
boardingPassSystem.viewBoardingPass(boarding_pass)

# Update passenger information
print("\n\t\tTo Update the Boarding pass Information")
boardingPassSystem.updatePassengerInfo(passenger, "10A")

# Generate and view updated boarding pass information
print("\n\t\tView the Boarding pass After Updating the Boarding pass Information")
updated_boarding_pass = boardingPassSystem.generateBoardingPass(passenger, flight)
boardingPassSystem.viewBoardingPass(updated_boarding_pass)
