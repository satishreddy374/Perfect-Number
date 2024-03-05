# Reading the Input number from User and converting into Integer Datatype.
number = int(input())

# Store all the divisors of input number in an empty list.
divisors_list = []

# Given range value from 1 to given input number. (excluding input number value)
for i in range(1, number):
    
    # Checking, if the given range value is a divisor of the input number or not.
    is_divisor = number % i == 0 
    if (is_divisor):
        # Adding all the divisors of the input number to an empty list.
        divisors_list.append(i)


# Calculating the Sum of all the divisors of the input number.
sum_of_divisors_list = sum(divisors_list)

# Checking Whether, the given input number is a perfect number or not.
is_number_a_perfect_number = (sum_of_divisors_list == number)


if (is_number_a_perfect_number):
    result = "Yes, {} is a Perfect Number...".format(number)
    print(result)

else:
    result = "No, {} is not a Perfect Number...".format(number)
    print(result)
    


