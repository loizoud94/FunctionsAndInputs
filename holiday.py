# holiday

"""
Although this task relates to defining and calling functions, I wanted to challenge myself to cope with a larger dataset,
and provide the user with a richer choice.
This script reads from 4 .txt files, contained in which are details pertaining to every airport to which you can fly directly from Manchester.
"""

# Define the functions for later use


def hotel_cost(city_hotel, num_nights):
    hotel = city_hotel * num_nights
    return hotel

def plane_cost(flight):
    plane = flight * 2
    return plane

def car_rental(car_hire, rental_days):
    car = car_hire * rental_days
    return car

def holiday_cost(hotel_cost, plane_cost, car_rental):
    holiday = hotel_cost + plane_cost + car_rental
    return holiday

import copy # using a copy function later on

# The next two for loops create a clean list wherein each item is a list of 2 elements:
# ['airport', 'airport code']

with open('airports.txt', 'r') as airports_file:
    airports_list = []
    for line in airports_file:
        dummy_list = line.split('(') # splits "Aberdeen (ABZ)" into ['Aberdeen ', 'ABZ)']
        airports_list.append(dummy_list)

    for item in airports_list: # Remove unwanted characters from both elements in each 'dummy_list' within airports_list
        item[0] = item[0][:-1]
        item[1] = item[1][0:3]

    airports_list_lower = copy.deepcopy(airports_list) # Retain airports list but work with a copy to deal with different cases in input

    for item in airports_list_lower:
        item[0] = item[0].lower()
        item[1] = item[1].lower()

    full_list = [] # Create a list wherein no elements are themselves lists but all elements of all lists in airports_list are retained.
    for item in airports_list:
        full_list.append(item[0])
        full_list.append(item[1])

    full_list_lower = [] # Retain full_list but cope with different case input
    for item in airports_list_lower:
        full_list_lower.append(item[0])
        full_list_lower.append(item[1])
    
# Creating a list and a dictionary for each of the remaining 3 .txt files
# The keys in all three dictionaries are the airports and the values pertain to the prices: cost of flights, car hire and hotels

with open('plane_cost.txt', 'r') as plane_cost_file:
    plane_cost_list = []
    for line in plane_cost_file:
        dummy_list = line.split(':')
        plane_cost_list.append(dummy_list)
    
    plane_cost_dict = {}
    for item in plane_cost_list:
        plane_cost_dict[item[0]] = item[1][2:-1] # Removing unwanted characters from the values in the dictionary

with open('rental_cars.txt', 'r') as rental_cars_file:
    rental_cars_list = []
    for line in rental_cars_file:
        dummy_list = line.split(':')
        rental_cars_list.append(dummy_list)

    rental_cars_dict = {}
    for item in rental_cars_list:
        rental_cars_dict[item[0]] = item[1][2:-1]


with open('airports_hotels.txt', 'r') as airports_hotels_file:
    airports_hotels_list = []
    for line in airports_hotels_file:
        dummy_list = line.split(':')
        airports_hotels_list.append(dummy_list)

    airports_hotels_dict = {}
    for item in airports_hotels_list:
        airports_hotels_dict[item[0]] = item[1][2:-1]


# Provide an option to view full list of airports that can be flown to, or just continue with choosing destination

user_input = 3
while user_input != 2:
    print("Choose from the below options by entering 1 or 2.")
    print("Enter 1 to see the full list of destinations available.")
    print("Enter 2 to choose a destination.")
    try: # Cope with invalid input
        user_input = int(input(""))
    except ValueError:
        print("\nInvalid input.\n")
        continue

    if user_input == 1:
        f = open('airports.txt', "r") # Most readable form of the list of airports is the full .txt document
        print("\nList of airports:")
        print(f.read())
        f.close() # Ensure file is closed
        user_input = 2 # Proceed automatically to option 2 after viewing the list of destinations
        city_flight = input("\nPlease enter a city or airport code to which you would like to fly: \n")
        city_flight_lower = city_flight.lower() # Separate variable to capture different cases necessary to retain the inputted spelling in the error message output
        while city_flight_lower not in full_list_lower: # Reject any airport that can't be flown to directly from Manchester
            city_flight = input(f"\nSorry. We do not fly to {city_flight}. Please enter a city or airport code to which you would like to fly:\n") # returns {city flight} exactly as user inputted
            city_flight_lower = city_flight.lower()

    elif user_input == 2:
        city_flight = input("\nPlease enter a city or airport code to which you would like to fly: \n")
        city_flight_lower = city_flight.lower()
        while city_flight_lower not in full_list_lower:
            city_flight = input(f"\nSorry. We do not fly to {city_flight}. Please enter a city or airport code to which you would like to fly:\n")
            city_flight_lower = city_flight.lower()

    else:
        print("\nInvalid input.\n")

index = full_list_lower.index(city_flight_lower)
if index % 2 == 0: # Each even index in full_list maps onto half itself in airports_list
    airports_list_index = index / 2
else: # Each odd index in full_list maps onto half of (itself minus 1) in airports_list
    airports_list_index = (index - 1) / 2

airports_list_index = int(airports_list_index)
city = airports_list[airports_list_index][0] # The first item in each list within airports_list is the airport name, rather than the code

num_nights = -1
while num_nights < 0:
    try:
        num_nights = int(input(f"\nFor how many nights do you wish to stay at a hotel in {airports_list[airports_list_index][0]}? ")) # Correct capitalised airport name
        if num_nights < 0:
            print("Sorry, that is an invalid amount of nights. Try again.") # Reject negative number of nights
    except ValueError:
        print("Sorry, that is an invalid amount of nights. Please enter a whole number.") # Reject non-integer input

rental_days = -1
while rental_days < 0:
    try:
        rental_days = int(input("\nFor how many days do you wish to hire a car on this holiday? "))
        if rental_days < 0:
            print("Sorry, that is an invalid amount of days. Please enter a whole number.") # Reject negative number of days
    except ValueError:
        print("Sorry, that is an invalid amount of days. Please enter a whole number.") # Reject non-integer input

city_hotel = int(airports_hotels_dict[city]) # Casting the values in each dictionary to integers
flight = int(plane_cost_dict[city])
car_hire = int(rental_cars_dict[city])

final_hotel_cost = hotel_cost(city_hotel, num_nights) # Calling the four functions
car_hire_cost = car_rental(car_hire, rental_days)
flight_cost = plane_cost(flight)
full_holiday_cost = holiday_cost(final_hotel_cost, flight_cost, car_hire_cost)

print("Checkout \n") # Printing output of final details
print("Full details of your chosen holiday:")
print(f"You are flying to {city}, staying at a hotel there for {num_nights} nights.")
print(f"While there, you have elected to rent a car for {rental_days} days in total.")
print(f"\tThe cost of your hotel stay is £{final_hotel_cost}.")
print(f"\tThe cost of your rental car is £{car_hire_cost}.")
print(f"\tThe cost of your return flights to {city} from Manchester Airport is £{flight_cost}.")
print(f"In total your holiday, including flights, hotel and car hire will cost £{full_holiday_cost}.")