# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def even_number():
    numb=0
    while numb <=50:
        if numb%2 ==0:
           numb +=1
           print(even_number(numb
                             )) 
           
#    Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime
def prime_number(prime):
    for i in prime:
        if i%2!=0:
            print("prime")
        else:
            print("not prime")
#   Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
 
def add_prime(*a):
    numbs=0
    for i in a:
        if i%2 ==0:
            numbs+=i
            print(numbs)
(add_prime(1,2,3,4,5,6,7))            
             
            
# Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.

def members(a,b):
    sum=a+b
    for num in (a,b):
        if num%3==0:
         print (num)   
    
    
    
    
         
            
       
            
    
    