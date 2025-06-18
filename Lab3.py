Number = int(input("Enter a positive integer: "))
even_sum = 0

for n in range(1, Number + 1):
    if n % 2 == 0:
     even_sum += n

print (f"The sum of even numbers between 1 and {Number} is {even_sum}")



   
