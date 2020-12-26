def my_function():
    print("Hello from my function!")

def my_function_with_args(username,greeting):
    print("Hello, %s ,From My Function!,I wish you %s"%(username,greeting))

def sum_two_numbers(a,b):
    return a + b

my_function()

#prints - "Hello,Jhon Doe,From my functon!, I wish you a great year!"
my_function_with_args("John Doe","a great year!")


x=sum_two_numbers(1,2)
