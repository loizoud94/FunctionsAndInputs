# FunctionsAndInputs

## Overview
FunctionsAndInputs is a Python program designed to assist users in planning and estimating the cost of a holiday. The program reads data from four accompanying text files, each containing information about airports, flight costs, hotel costs, and car hire costs. The user can input their desired destination, the number of nights to stay at a hotel, and the number of days to hire a car. The program then calculates and displays the estimated cost of the entire holiday, including flights, hotel stay, and car hire.

## Features
- **Data Files:**
  - `airports.txt`: Contains a list of airports that can be flown to directly from Manchester.
  - `plane_cost.txt`: Specifies the cost of flights from Manchester to each airport.
  - `rental_cars.txt`: Lists the cost of car hire at each destination.
  - `airports_hotels.txt`: Provides the cost of staying at a hotel in each city.

- **Functions:**
  - `hotel_cost`: Calculates the cost of a hotel stay based on the city and the number of nights.
  - `plane_cost`: Calculates the cost of round-trip flights from Manchester to a specified city.
  - `car_rental`: Computes the cost of hiring a car for a given number of days.
  - `holiday_cost`: Combines the costs of hotel stay, flights, and car hire to determine the total holiday cost.

## Usage
1. **Run the Program:**
   - Execute the program in any Python interpreter.

2. **Choose Destination:**
   - Enter the desired city or airport code to which you would like to fly.
   - Optionally, view the full list of available destinations.
<img width="394" alt="Screenshot 2024-01-19 at 17 50 53" src="https://github.com/loizoud94/FunctionsAndInputs/assets/152619396/6f0ee954-fb8a-4e09-a942-173db4c68573">

3. **Provide Details:**
   - Specify the number of nights you wish to stay at a hotel.
   - Indicate the number of days you plan to hire a car.

4. **View Holiday Details:**
   - The program will display the estimated cost breakdown for your holiday, including flights, hotel, and car hire.
     <img width="640" alt="Screenshot 2024-01-19 at 17 49 24" src="https://github.com/loizoud94/FunctionsAndInputs/assets/152619396/4f12395f-03ce-4bbc-884a-68c67a663d81">

## Data Files
- `airports.txt`: Lists airports that can be flown to directly from Manchester.
- `plane_cost.txt`: Specifies flight costs to each destination.
- `rental_cars.txt`: Provides car hire costs for each city.
- `airports_hotels.txt`: Indicates hotel costs for each city.

## Contributing
If you have ideas for improvements or would like to contribute to the Holiday Planner, feel free to fork the repository and open a pull request.

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code for both commercial and non-commercial purposes.

Feel free to customize and enhance the program to better suit your needs. Enjoy holiday planning!
