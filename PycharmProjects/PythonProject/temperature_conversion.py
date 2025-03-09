# Python temperature conversion

temp = float(input("Enter the temperature: "))
unit = input("Celsius or Fahrenheit? (C or F): ")

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}" + "\u00b0F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}" + "\u00b0C")
else:
    print(f"{unit} is an invalid unit of measurement.")

