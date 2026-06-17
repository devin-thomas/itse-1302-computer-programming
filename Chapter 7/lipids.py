#Devin Thomas
#ITSE 1302-003
#June 28, 2023


def main():
    print("This program calculates the percentage of calories in a food item that come from fat.")
    fat_grams = get_fat_grams()
    fat_calories = calc_fat_calories(fat_grams)
    total_calories = get_total_calories(fat_calories)
    fat_calorie_percentage = divide_and_conquer(fat_calories, total_calories)
    show_calc(fat_calorie_percentage)

def get_fat_grams():
    while True:
        try:
            fat_grams = float(input("Enter the number of fat grams in the food item: "))
            if fat_grams < 0:
                print("The number of fat grams cannot be less than 0. Please try again.")
                continue
            else:
                return fat_grams
        except ValueError:
            print("Invalid input. Please enter a number.")

def calc_fat_calories(fat_grams):
    return fat_grams * 9

def get_total_calories(fat_calories):
    while True:
        try:
            total_calories = float(input("Enter the total number of calories in the food item: "))
            if total_calories <= 0:
                print("The total number of calories cannot be 0 or less. Please try again.")
                continue
            elif total_calories < fat_calories:
                print("The total calories cannot be less than the calories from fat. Please try again.")
                continue
            else:
                return total_calories
        except ValueError:
            print("Invalid input. Please enter a number.")

def divide_and_conquer(fat_calories, total_calories):
    return fat_calories / total_calories

def show_calc(fat_calorie_percentage):
    print(f"The percentage of calories that come from fat is {fat_calorie_percentage * 100:.2f}%")
    if fat_calorie_percentage < 0.3:
        print("This food is low in fat.")

main()
