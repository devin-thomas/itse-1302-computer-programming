#Devin Thomas
#ITSE 1302-003
#June 26, 2023

def intro():
    # Inform the user of the purpose of the program
    print("This program calculates your total monthly and annual automobile costs.")

def get_costs():
    costs = []
    cost_types = ["loan", "insurance", "gas", "oil", "tires", "maintenance"]
    
    # Prompt the user to enter the monthly cost for each type
    for cost_type in cost_types:
        while True:
            try:
                cost = float(input(f"Enter the monthly {cost_type} payment: $"))
                if cost < 0:
                    print("Invalid input. Please enter a positive number.")
                else:
                    costs.append(cost)
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return costs

def calc(costs):
    # Calculate the total monthly cost and the total annual cost
    monthly = sum(costs)
    annual = monthly * 12
    return monthly, annual

def show_calcs(monthly, annual):
    # Display the total monthly and annual costs
    print(f"Total monthly cost: ${monthly:.2f}")
    print(f"Total annual cost: ${annual:.2f}")

def main():
    intro()
    costs = get_costs()
    monthly, annual = calc(costs)
    show_calcs(monthly, annual)

# Run the program
main()
