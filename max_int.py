# the user inputs a number.
# a minimum number is set and the first input number becomes the minimum.
# another number is input.
# if the new num_int is higher than the minimum then it will take the name max_int.
# if a negative number is input the loop stops and the max_int is print.





num_int = int(input("Input a number: "))    # Do not change this line

min_int = 0 

while num_int >= 0:
    min_int = num_int 
    num_int = int(input("Input a number: "))
    if num_int > min_int: 
        max_int = num_int
      # Fill in the missing code
print("The maximum is", max_int)    # Do not change this line

