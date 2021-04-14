#                         FUNCTIONS
# =================================================================

# =================================================================
#                 the four types of functions
# =================================================================


def func_type1():
    print("no parameter needed and returns nothing/None by default")
#try by uncommenting both lines individually
# func_type1()
# print(func_type1())

def func_type2(x):
    print(f'square of {x} is { x**2}')
    print("parameter is needed and returns nothing/None by default")

#try by uncommenting both lines individually
# func_type2()
# print(func_type2(2))


def func_type3():
    print("no parameter needed and returns square of 2")
    return 2**2
    print("something") # this will not be executed

#try by uncommenting both lines individually
# func_type3()
# print(func_type3())

def func_type4(x):
    print(f"parameter needed and returns square of {x}")
    return x**2

#try by uncommenting both lines individually
# func_type4()
# print(func_type4(2))

# =================================================================
#                   default parameters
# =================================================================

def get_username(username = "Guest"):
    print(username)
# get_username()
# get_username("pyboy")

def add(a,b=0):
    return a+b

# print(add()) # error
# print(add(5))
# print(add(5,16))

def add_2(a=0,b=0):
    return a+b
# print(add()) #no error
# print(add(5))
# print(add(5,16))

'''
# THROWS ERROR while compiling
def price_after_discount(discount = .15,price):
                        #    ^
                        #    | --> default parameter must be at end
    return price-discount*price

# print(price_after_discount(100)) # error
'''

def price_after_discount(price,discount = .15):
    return price-discount*price


# print(price_after_discount(100)) # normal days
# print(price_after_discount(100,0.5)) # festive season
#             #               ^    ^
#             #               |    |
#             #           price   discount(50% = 0.5)


# print(price_after_discount(0.5,100)) # BUGGY CODE we must follow order
                                     # (sequence metioned in function definition)



# =================================================================
#                   keyworded parameters
# =================================================================


def price_after_discount(price,discount = .15):
    return price-discount*price

# print(price_after_discount(100,0.5))
# print(price_after_discount(price=100,discount=0.5)) 
# print(price_after_discount(discount=0.5,price=100)) # order changed but works as the above lines


# =================================================================
#                   variable number of parameters
# =================================================================

# packing and unpacking
def pack_unpack():
    numbers = 1,2,3,4,5  #save multiple values in the form of tuple.It ia called packing
    print(*numbers)      #prints individual elements

    first_num,second_num,*rest_of_nums = numbers
    #|--------------------------------|
    #                 ^
    #                 |
    #             unpacking
    print('first_num',first_num)
    print('second_num',second_num)
    print('rest_of_nums',rest_of_nums)
# pack_unpack()


# *args as parameter
def add(*args):
    print(sum(args))
# add(1,2,3)


#we can use parameters normal parameters
def add(a,*args):
    print(a) # a is first parameter passed in function call
    print(args)
# add(1,2,3)
#also try with one parameter


# we can also use default parameters
def add(a,b=0,*args):
    print(a) # a is first parameter passed in function call
    print(b) #
    print(args)
# add(1,2,3)
#also try with one parameter

# **kwargs (keyworded arguments)

def kwargs_demo(**kwargs):
    
    print(kwargs)
    for key in kwargs:
        print(f'{key} {kwargs[key]}')


# kwargs_demo(name="pyboy",skill="python",language="CS")


'''
# COMPILATION ERROR
# UNPACKING is not possible with **kwargs

def kwarg_demo_1():

    kwargs = (name="pyboy",skill="python",language="CS")
    print(**kwargs)

'''

'''
# def kwarg_demo_1():
# COMPILATION ERROR
    kwargs = {'name': 'pyboy', 'skill': 'python', 'language': 'CS'}
    print(**kwargs)

kwarg_demo_1()
'''


# =================================================================
#    lambda functions(functions without name/anonymous functions)
# =================================================================


square = lambda num : num * num #-->return value without using return keyword
#          ^     ^
#          |     |
#    keyword     parameter

print(square(5))

# square1 = lambda num : return num * num # error  (should not use return)
# square1(2)


square2 = lambda num : print(num * num) #-->single line statement without returning anything
square2(6) # no need to print

# using two variables
add = lambda num1,num2 : num1 + num2
print(add(6,2))

# using default parameter
add = lambda num1,num2=0 : num1 + num2
print(add(2))

# using variable number of arguments
add = lambda *args : (sum (args))
print(add(1,2,3,4,5,6))

# using normal parameter with *args
add = lambda n,*args : (n,sum (args))
print(add(1,2,3,4,5,6))

# using **kwargs
data = lambda **kwargs : kwargs
print(data(name="pyboy",skill="python",degree="CS"))