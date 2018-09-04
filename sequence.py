n = int(input("Enter the length of the sequence: ")) # Do not change this line
the_sum= 0
count = 1
num_1 = 1
num_2 = 2
num_3 = 3

if n == 1:
    print(num_1)
elif n == 2:
    print(num_1)
    print(num_2)
else:
    print(num_1)
    print(num_2)
    print(num_3)

while n >= count:
    count += 1
    the_sum = num_1 + num_2 + num_3
    print(the_sum)
    num_1=num_2
    num_2=num_3
    num_3=the_sum