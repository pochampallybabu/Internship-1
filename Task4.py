def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")
    
    while True:
       
        try:
            temperature = float(input("Enter the temperature you want to convert: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        
        print("Choose the conversion direction:")
        print("1: Celsius to Fahrenheit")
        print("2: Fahrenheit to Celsius")
        print("3: Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            converted_temp = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
        elif choice == '2':
            converted_temp = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
        
        print()  

if __name__ == "__main__":
    main()
