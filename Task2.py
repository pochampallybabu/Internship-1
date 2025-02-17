def generate_pyramid(rows):
    
    for i in range(1, rows + 1):
      
        print(' ' * (rows - i), end='')

        
        for j in range(1, i + 1):
            print(j, end=' ')

        
        print()


def main():
    
    try:
        rows = int(input("Enter the number of rows for the pyramid: "))
        if rows < 1:
            print("Please enter a positive integer.")
            return
        
        
        generate_pyramid(rows)
        
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
