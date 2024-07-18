def disp_options():
    print("Choose an option for Temperature Conversion from the following mentioned : ")
    print("1. Celsius to Fahrenheit.")
    print("2. Celsius to kelvin.")
    print("3. Fahrenheit to Celsius.")
    print("4. Fahrenheit to kelvin.")
    print("5. kelvin to Celsius.")
    print("6. kelvin to Fahrenheit.")
    print("7.Exit...")

def conversion(n):
    if n==1:
        m=int(input("Please enter the Temperature in Celsius.."))
        print(f"In fahrenheit Temperature : {(m * 9/5)+ 32}°F")
    elif n==2:
        m=int(input("Please enter the Temperature in Celsius.."))
        print(f"In kelvin Temperature : {m+273.15}°K")
    elif n==3:
        m=int(input("Please enter the Temperature in fahrenheit.."))
        print(f"In Celsius Temperature : {(m-32) * 5/9}°C")
    elif n==4:
        m=int(input("Please enter the Temperature in fahrenheit.."))
        print(f"In Kelvin Temperature : {(m+459.67)*5/9}°K")
    elif n==5:
        m=int(input("Please enter the Temperature in Kelvin.."))
        print(f"In Celsius Temperature : {m-273.15}°C")
    elif n==6:
        m=int(input("Please enter the Temperature in Kelvin.."))
        print(f"In fahrenheit Temperature : {(m*9/5)-459.67}°F")
    elif n==7:
        print("Exiting.........")
    else:
        print("Invalid option!!!,Try with mentioned options only.")

def main():
    while True:
        disp_options()
        try:
            option=int(input("Enter your option:"))
        except ValueError:
            print("Sorry!!!Invalid option...try with valid one.")
            continue
        if option==7:
            conversion(option)
            break
        else:
            conversion(option)

main()