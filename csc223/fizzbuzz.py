#i=1;
#while i<= 100:
#    print(i)
#    i+=1

def fizzbuzz(x):
    for i in range(1,x+1):
        if i % 3==0 and i % 5 == 0:
            print("FizzBuzz")
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(10)
