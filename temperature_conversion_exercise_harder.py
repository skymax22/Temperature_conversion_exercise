while True:
    temp = input("Please enter your temperature, or 'q' to quit: ").strip()
    if temp.lower() == 'q':
        print("Thank you for playing!")
        break
    try:
        temp = float(temp)
        if temp < - 200 or temp > 200:
            print("That seems like an unrealistic temperature. Please try again.")
            continue
    except ValueError:
        print("Please enter a valid temperature.")
        continue

    valid_units = ['c', 'f']

    while True:
        unit = input("Celsius or Fahrenheit? (C or F): ").strip().lower()

        if unit not in valid_units:
            print("Invalid units. Please try again.")
            continue

        if unit == "c":
            temp = round((temp * 9) / 5 + 32, 1)
            print(f"The temperature in Fahrenheit is: {temp}°F")
            if temp <= 32:
                print("You look as cold as ice")
            elif temp >= 90:
                print("You bring warmth wherever you go")
        elif unit == "f":
            temp = round((temp - 32) * 5 / 9, 1)
            print(f"The temperature in Celsius is: {temp}°C")
            if temp <= 0:
                print("You look as cold as ice")
            elif temp >= 32:
                print("You bring warmth wherever you go")
        break