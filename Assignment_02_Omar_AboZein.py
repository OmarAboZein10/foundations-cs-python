def digitsCount(number):
    #Base case will check if the number entered is less than 10 it will return 1 , 
    #the abs() function here is to ensure that the code takes the value of the integer despite its sign
    if abs(number) < 10:
        return 1
    else:
        #Recursively the function will eliminate the last digit and count the rest
        return 1 + digitsCount(abs(number) // 10)

try:
    #prompting the user to enter an integer with the input monitored with a try and except method for invalid entries.
    user_input = int(input("Enter an integer: "))
    Count = digitsCount(user_input)
    print(f"The number of digits in {user_input} is {Count}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
