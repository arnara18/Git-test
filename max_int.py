# take input from user: 
num_int = int(input("Input a number: "))   
max_int = 0

# check if integer is positive 
while num_int > 0: #if positive, the first input is the max
    if max_int < num_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
            
#if number negitive then print max_int
print("The maximum is", max_int)    # Do not change this line
