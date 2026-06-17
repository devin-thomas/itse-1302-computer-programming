def calculate_elasticity():
    # Get labels for the two types of numbers.
    label1 = input("Please enter the label for the first type of number: ")
    label2 = input("Please enter the label for the second type of number: ")

    # Get two values for each label.
    val1_a = float(input(f"Please enter the first value for {label1}: "))
    val1_b = float(input(f"Please enter the second value for {label1}: "))
    val2_a = float(input(f"Please enter the first value for {label2}: "))
    val2_b = float(input(f"Please enter the second value for {label2}: "))

    # Ask which is the numerator and denominator.
    numerator_label = ""
    while numerator_label not in ["1", "2"]:
        numerator_label = input(f"Which label is in the numerator (Press 1 for {label1}, 2 for {label2}): ")

    if numerator_label == "1":
        num_a, num_b = val1_a, val1_b
        den_a, den_b = val2_a, val2_b
    else:
        num_a, num_b = val2_a, val2_b
        den_a, den_b = val1_a, val1_b

    # Calculate the percentage changes using the midpoint method.
    num_change = (num_b - num_a) / ((num_b + num_a) / 2)
    den_change = (den_b - den_a) / ((den_b + den_a) / 2)

    # Calculate the elasticity.
    elasticity = num_change / den_change

    # Convert to absolute value, round to 2 decimal places, and return.
    # elasticity = abs(elasticity)
    elasticity_rounded = round(elasticity, 2)

    elasticity_status = ""
    if abs(elasticity) > 1:
        elasticity_status = " (Elastic)"
    elif abs(elasticity) < 1:
        elasticity_status = " (Inelastic)"
    elif abs(elasticity) == 1:
        elasticity_status = " (Unit Elastic)"

    print(f"The calculated elasticity is {elasticity_rounded}{elasticity_status}")

if __name__ == "__main__":
    calculate_elasticity()
