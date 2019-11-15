
# 5-8 Paint Job Estimator
# Shaun Hayworth
# CIS 2
# 11-14-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/5-8-Paint-Job-Estimator

# Program calculates and displays labor and material costs for painting a given
# space. Uses the cost_estimate function for calculations and printing the
# results to the screen.

# Initialize global constants for the number of feet per gallon of paint, the
# hours of labor per one gallon of paint, and the labor cost per hour.
FEET_PER_GALLON = 112
LABOR_HOURS = 8
LABOR_PER_HOUR = 35.0


def main():
    """ Executes the mainline program logic
    """
    # Prompt the user for the square footage of wall space and the price per
    # gallon of paint.
    wall_space = int(input('Enter wall space in sqare feet: '))
    price_per_gallon = float(input('Enter paint price per gallon: '))

    # Call the cost_estimate function and pass wall_space and price_per_gallon
    # as arguments
    cost_estimate(wall_space, price_per_gallon)


def cost_estimate(feet, paint):
    """ Calculates the amount of paint needed, the hours of labor needed, and the
    total cost of labor and paint and prints the results to the screen.
    """
    # If feet parameter is evenly divisible by FEET_PER_GALLON, assign the
    # quotient to paint_needed. Otherwise, add 1 to the quotient and assign it
    # to paint_needed.
    if feet % FEET_PER_GALLON == 0:
        paint_needed = feet // FEET_PER_GALLON
    else:
        paint_needed = (feet // FEET_PER_GALLON) + 1

    # Calculate the total hours and cost of labor, the total cost of paint, and
    # the total estimated cost of the job.
    labor_needed = paint_needed * LABOR_HOURS
    paint_cost = paint_needed * paint
    labor_cost = labor_needed * LABOR_PER_HOUR
    total_estimate = paint_cost + labor_cost

    # Print the results to the screen.
    print(f'Gallons of paint: {paint_needed}')
    print(f'Hours of labor: {labor_needed}')
    print(f'Paint charges: ${paint_cost:,.2f}')
    print(f'Labor charges: ${labor_cost:,.2f}')
    print(f'Total cost: ${total_estimate:,.2f}')

# Call the main() function to execute the program.
main()
