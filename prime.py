num = int(input("Enter a Number :"))

if num < 2:
     print("not a prime number")
else:
     for i in range(2,num):
       if num%i==0:
          print("not a prime number")
          break
       else:
          print("prime number")
          break

