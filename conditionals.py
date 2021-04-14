#                       CONDITIONAL STATEMENTS
# =================================================================

# =================================================================
#                       simple if statement
# =================================================================
def if_func_1():
    x = 10
    if x == 10:  # works
        print('1st if worked')

    if x == '10': #not works x is type int
        print('2nd if worked')
    
# =================================================================

def if_func_2():

    y = True
    if y:                     # True
        print('3rd if worked')
    
    y = False
    if not y:                 # not True == False
        print('4rd if worked')
        
# =================================================================

def is_divisible(numerator,denominator):
    '''returns a boolean value'''
    return numerator % denominator == 0 

def if_func_3():
    if is_divisible(4,2): # calling a function that returns a boolean value
        print("yes")

# =================================================================
#                   working with multiple conditions
# =================================================================

def multiple_conditions_1():
    # give values 26,15,30,15,60 for num
    num = 26

    if num % 3 == 0 and num % 5 == 0:
        print(f'{num} is divisible by 15')
    
    if num % 2==0 and num % 3 == 0 and num % 5 == 0:
        print(f'{num} is divisible by 30')

# =================================================================

def multiple_conditions_2():
    # give values 26,15,30,15,60 for num
    num = 60

    conditions_for_multiple_of_15 = [
        num % 3 == 0, 
        num % 5 == 0,
        ]
    conditions_for_multiple_of_30 = [
        num % 2 == 0, 
        num % 3 == 0, 
        num % 5 == 0,
        ]
    
    if all(conditions_for_multiple_of_15):
        print(f'{num} is divisible by 15')
    
    if all(conditions_for_multiple_of_30):
        print(f'{num} is divisible by 30')

# =================================================================

def multiple_conditions_3():
    items_in_fridge = ['carrot','potato','cabbage','beet root','okra']

    if 'carrot' in items_in_fridge or 'radish' in items_in_fridge or 'okra' in items_in_fridge or 'tomato' in items_in_fridge:
        print('we can cook a dish')

# =================================================================
def multiple_conditions_4():
    items_in_fridge = ['carrot','potato','cabbage','beet root','okra']
    conditions = [
        'carrot' in items_in_fridge, # True
        'radish' in items_in_fridge, # False
        'okra' in items_in_fridge,   # True
        'tomato' in items_in_fridge, # False
        ]
    
    if any(conditions):
        print('we can cook a dish')
    
    # more code but, more readable

# =================================================================
#               else statment(must followed by if)
# =================================================================


def if_with_else():
    x = 10
    if x == 10: 
        print('x is 10')
    else:   # executes whenever the ``if statement is not executed``
        print('x is not 10')

# if_with_else()

# =================================================================
#                       else if ladder(elif)
# =================================================================

def ladder():
    # try to assign an integer or a float or a string or a list or a tuple,etc to a
    a = 5

    if isinstance(int,a): # built-in method which returns boolean value
        print(f'{a} is integer')

    elif isinstance(float,a):
        print(f'{a} is float')

    elif isinstance(str,a):
        print(f'{a} is string')

    else:
        print(f'{a} is not an integer,not a float and not a string')

# ladder()

# =================================================================
#                       nested if(inner if) 
# =================================================================

def data_of_bird(bird):
    birds_in_our_santury = ['owl','sparrow','penguin','parrot','flemingo','wild chicken','bat','cranes','ostrich',]
    birds_cannot_fly = ['wild chicken','ostrich','penguin']

    if bird in birds_in_our_santury:
        print(f'{bird} lives in our santury')
        if bird in birds_cannot_fly:
            print(f'{bird} cannot fly')
        else: #<-------------+
                        #    |--else optional in our case. But, it could be used if condition goes false.
            pass #-----------+
    else:
        print(f'{bird} do not live in our santury')
        

def nested_if_1():
    bird = 'sparrow'
    data_of_bird(bird)

# nested_if_1()

# =================================================================

def data_about_species_in_xyz_zoo(animal):
    mammals = ['dog','cat','human','bat','rat','squirrel']
    birds = ['owl','sparrow','parrot','bat','pegion']
    amphibians = ['crocodile','frog','tortoise']
    zoo_animals = mammals + birds + amphibians
    if animal in zoo_animals: #<----+    <====================================++
                                #   |-- nested if of first if                 ||
        if animal in mammals: #-----+   #<------+                             ||
            print(f'{animal} is a mammal')     #|-- nested if of second if    ||
            if animal in birds: #---------------+                             ||
                print(f'{animal} is a bird')                                # ||-- else belongs to first if
    else: #===================================================================++
        print(f'{animal} not live in xyz zoo')

def nested_if_2():
    animal = 'bat'
    data_about_species_in_xyz_zoo(animal)

# nested_if_2()

# =================================================================
#                      ternary operator 
# =================================================================

def is_venomous(snake):
    venomous_snakes = ["cobra","viper","krait","mamba","taipan"]
    return snake in venomous_snakes  #return boolean value


def ternary_operator(snake_name):
    print(f"yes,{snake_name} is venomous!!!") if is_venomous(snake_name) else print(f"no,{snake_name} is non venomous")
#                   ^                                  ^                                         ^
#                   |                                  |                                         |
#statement to execute if condition is True         condition                 statement to execute if condition is False

# ternary_operator('python')



# =================================================================
#                      short circuit
# =================================================================

def short_circuit():
    # try changing a as 10abc
    a = '10a'
    if a.isdigit(): print(f"{int(a)}")
    #    ^
    #    |    same as above line
    #    ^
    a.isdigit() and print(f"{int(a)}")
    #-----------------------------------
    if not a.isdigit(): print("type conversion is not possible")
    #    ^
    #    |    same as above line
    #    ^
    not a.isdigit() and print("type conversion is not possible")

# short_circuit()
