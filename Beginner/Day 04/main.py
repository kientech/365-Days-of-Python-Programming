# Coding With Kien - 365 Days of Python Programming
# Beginner - Apr 05, 2024

# Application that converts temperature from Celsius to Fahrenheit and vice versa

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()