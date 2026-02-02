import random
import math

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

# Helper function to calculate fuel consumption based on distance
def calculate_fuel(distance):
    return distance * 0.1  # Example: 0.1 units of fuel per distance unit

# Initialize data (Locations, Trucks, Time Windows, and Waste Amounts)
def initialize_data():
    # Locations are given as (x, y) coordinates
    locations = [(0, 0), (2, 4), (5, 6), (7, 2), (9, 3)]
    
    # Time windows for each location (start, end)
    time_windows = [(0, 10), (2, 12), (4, 14), (6, 16), (8, 18)]
    
    # Waste amounts at each location
    waste_amounts = [5, 10, 8, 6, 4]
    
    # Trucks (Each truck has a capacity)
    trucks = [("Truck1", 15), ("Truck2", 15),("Truck3",15)]  # (Truck name, capacity)
    
    return locations, time_windows, waste_amounts, trucks

# Step 1: Enforce Constraints
def enforce_constraints(locations, waste_amounts, trucks, time_windows):
    # Enforce Capacity Constraint (Each truck must not exceed its capacity)
    for i, waste in enumerate(waste_amounts):
        truck_capacity = trucks[i % len(trucks)][1]  # Cycle through trucks
        if waste > truck_capacity:
            print(f"Error: Waste at location {i} exceeds truck capacity!")
            return False
    return True

# Step 2: Route Optimization (Minimize Distance and Fuel Consumption)
def optimize_routes(locations, waste_amounts, trucks, time_windows):
    # Create a list to store routes and total distance
    routes = []
    total_distance = 0
    total_fuel = 0
    
    # Simple heuristic: Use nearest neighbor for route optimization
    # Start from the first location and choose the nearest one at each step
    remaining_locations = list(range(len(locations)))
    
    # Start with the first location
    current_location = 0
    route = [current_location]
    remaining_locations.remove(current_location)
    
    while remaining_locations:
        # Find nearest location
        nearest_location = min(remaining_locations, key=lambda loc: euclidean_distance(locations[current_location], locations[loc]))
        route.append(nearest_location)
        remaining_locations.remove(nearest_location)
        current_location = nearest_location
    
    # Calculate total distance and fuel for the optimized route
    for i in range(len(route) - 1):
        dist = euclidean_distance(locations[route[i]], locations[route[i + 1]])
        fuel = calculate_fuel(dist)
        total_distance += dist
        total_fuel += fuel
    
    routes.append(route)
    return routes, total_distance, total_fuel

# Step 3: Assign Times to Locations (Respect Time Windows)
def assign_times_to_locations(time_windows):
    times = []
    for i, window in enumerate(time_windows):
        # Assign a random time within the window for each location
        start, end = window
        assigned_time = random.randint(start, end)
        times.append(assigned_time)
    return times

# Step 4: Display the Solution (Route, Schedule, and Fuel Consumption)
def display_solution(routes, total_distance, total_fuel, times, locations):
    print("Optimized Routes and Schedule:")
    for route in routes:
        route_locations = [locations[i] for i in route]
        route_times = [times[i] for i in route]
        print("Route:", route_locations)
        print("Times:", route_times)
    
    print(f"Total Distance Traveled: {total_distance} units")
    print(f"Total Fuel Consumption: {total_fuel} units")

# Main function to solve the Waste Management CSP
def solve_waste_management():
    # Step 1: Initialize Data
    locations, time_windows, waste_amounts, trucks = initialize_data()

    # Step 2: Enforce Constraints (Capacity, Time Window, etc.)
    if not enforce_constraints(locations, waste_amounts, trucks, time_windows):
        print("Constraints violated. Cannot proceed.")
        return

    # Step 3: Optimize Routes (Minimize Distance and Fuel Consumption)
    routes, total_distance, total_fuel = optimize_routes(locations, waste_amounts, trucks, time_windows)
    
    # Step 4: Assign Collection Times to Locations
    times = assign_times_to_locations(time_windows)
    
    # Step 5: Display the Solution
    display_solution(routes, total_distance, total_fuel, times, locations)

# Run the Waste Management System
solve_waste_management()