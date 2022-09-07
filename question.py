#TODO: 1. Write a python script to print MySirG N times on the screen
n = int(input('Enter the value of n:'))
for i in range(n):
  print("MySirG")


# TODO: Write a python script to print first N natural numbers.
n = int(input('Enter the value of n:'))
for i in range(n+1):
  if i == 0:
    continue
  else:
    print(i)



#TODO: 3. Write a python script to print first N natural numbers in reverse order
n = int(input('Enter the value of n:'))
for i in range(n,0,-1):
  print(i)


# TODO: Write a python script to print first N odd natural numbers
n = int(input('Enter the value of n:'))
for i in range(n*2):
  if i % 2 !=0:
    print(i)

# TODO: Another way
# n = int(input('Enter the value of n:'))*2
# for i in range(1,n,2):
#   print(i)

# TODO:5. Write a python script to print first N odd natural numbers in reverse order
n = int(input('Enter the value of n:'))*2
for i in range(n):
  if i % 2 !=0:
    print(n-i)



# TODO: 6. Write a python script to print first N even natural numbers

n = int(input('Enter the value of n:'))*2
for i in range(2,n+2,2):
  print(i)

# TODO: Another way
n = int(input('Enter the value of n:'))*2
for i in range(2,n+1):
  if i % 2 == 0:
    print(i)
  

# TODO: 7. Write a python script to print first N even natural numbers in reverse order
n = int(input('Enter the value of n:'))*2
for i in range(0,n):
  if i % 2 ==0:
    print(n-i)


#TODO:8. Write a python script to print squares of first N natural numbers

n = int(input('Enter the value of n:'))
for i in range(1,n+1):
  print(i**2)


# TODO:9. Write a python script to print cubes of first N natural numbers

n = int(input('Enter the value of n:'))
for i in range(1,n+1):
  print(i**3)


#TODO: 10. Write a python script to print first 10 multiples of Nq
n = int(input('Enter the number:'))
for i in range(1,n+1):
  print(i*10)