#Question 1#
def factorial(n):
  if n < 0:
    return "Factorial for negative numbers doesn't exist"
  elif n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)
num = -1
while num < 0:
  user_input = input("Enter a non-negative integer: ")

  if user_input.isnumeric():
    num = int(user_input)
    if num < 0:
      print("Please enter a non-negative integer.")
  else:
    print("Invalid input. Please enter a non-negative integer.")

result = factorial(num)
print(str(num) + "! = " + str(result))


print("---------------------------------------------")

######################################################


#Question 2#
def find_divisors():
  num = int(input("Enter an integer: "))

  while (num <= 0):
    num = (int(input("Invalid please enter a positive integer:")))

  divisors = [1]  

  for i in range(2, num // 2 + 1):
    if num % i == 0:
      divisors.append(i)

  divisors.append(num) 

  return divisors

divisor_list = find_divisors()
if divisor_list:
  print("Divisors of the entered number: " + str(divisor_list))


print("---------------------------------------------")

######################################################

#Question 3#


def reverseString(string1):
  reversed_string = ""
  for i in range(len(string1) - 1, -1, -1):
    reversed_string += string1[i]
  return reversed_string
string2 = input("Enter a string: ")
reversed_input = reverseString(string2)

print("Reversed string:", reversed_input)
print("---------------------------------------------")

##################################################################################################3


#Question 4#
def evenNumbers(list1):
  even_numbers = []
  for number in list1:
      if number % 2 == 0:
          even_numbers.append(number)
  return even_numbers

user_input = input("Enter a list of integers: ")
even_List = evenNumbers(user_input)
print("Even numbers from the original list:",even_List )
print("-------------------------------------------")

##############################################################################################################


#Question 5#
def strongPassword(password):
  # first we check the length requirement#
  if len(password) < 8:
      return False
# setting our boolean variables to false as we yet to know if they are true or not#
  is_upper = False
  is_lower = False
  is_digit = False
  is_special = False

  special_characters = "#?!$"
 #iterating through the string and checking if it satisfies the critera for a strong password#
  for char in password:
      if char.isupper():
          is_upper = True
      if char.islower():
          is_lower = True
      if char.isdigit():
         is_digit = True
      if char in special_characters:
          is_special = True

  return is_upper and is_lower and is_digit and is_special

# Get input from the user
user_password = input("Enter a password: ")

# Check if the password is strong
if strongPassword(user_password):
  print("Strong password")
else:
  print("Weak password")
  print("------------------------------------------------------------------------")

#########################################################################################################33

#Question 6 (FSW)#

def is_valid_ipv4(ip):
 
  parts = ip.split(".")

  if len(parts) != 4:
      return False

  for part in parts:
      if not part.isdigit():
          return False

      num = int(part)
      if not (0 <= num <= 255):
          return False

  return True

ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
  print(ip_address + " is a valid IPv4 address.")
else:
  print(ip_address + " is not a valid IPv4 address.")



