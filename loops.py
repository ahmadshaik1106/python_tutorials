#                            LOOPS
# =================================================================

# =================================================================
#                          while loop
# =================================================================

def while_loop_1():
    a = 1
    while a<11:
        print(a)
        a += 1 #if this line is missed, the loop will turn into infinite loop

# while_loop_1()
# =================================================================

def while_loop_2():
    a = 1
    while True:
        if a == 11:
            break
        print(a)
        a += 1

# while_loop_2()



# =================================================================
#                          sequence matters
# =================================================================
       

def while_loop_3():
    # prints as expected
    a = 1
    while True:
        if a == 11:       # breaks before printing a,so 11 will not be printed
            break
        print(a)
        a += 1
# while_loop_3()
# =================================================================

def while_loop_4():
    # prints as expected
    a = 1
    while True:
        print(a)          
        a += 1
        if a == 11:       # breaks in last iteration,a==11 in last iteration.so,11 will not be printed
            break
# while_loop_4()
# =================================================================

def while_loop_5():
    a = 1
    while True:
        print(a)   # a will be 11 in last iteration
        if a == 11:
            break   #breaks after printing 11
        a += 1 
# while_loop_5()
# =================================================================

def while_loop_6():
    '''print squares until user quits'''
    done = False
    a = 1
    while not done:
        print(f'{a} x {a} = {a**2}')
        i = input("press q to quit/enter to continue ").lower()
        a += 1
        if i == 'q':
            done = True

# while_loop_6()




# =================================================================
#                          range based for loop
# =================================================================

def for_loop_1(): #one parameter
    stop_at_num = 11  
    for i in range(stop_at_num):
        print(i) #prints from 0 to 10
# for_loop_1()
# =================================================================

def for_loop_2():
    start_at_num = 5
    stop_at_num = 11  
    for i in range(start_at_num,stop_at_num): #two parameters
        print(i) #prints from 5 to 10
# for_loop_2()
# =================================================================

def for_loop_3():
    start_at_num = 5
    stop_at_num = 11
    skip_num = 3
    for i in range(start_at_num,stop_at_num,skip_num): #three parameters
        print(i) #prints from 5 two values in sequence and print 3rd value within the range
# for_loop_3()
# =================================================================

def for_loop_4():
    for i in range(10,-1,-1): 
        print(i) # starts at 10 ends at 0(since second parameter is exclusive),decrement by 1

# for_loop_4()
# =================================================================

def for_loop_5():
    for i in range(10,-1,-2): 
        print(i) # starts at 10 ends at 0(since second parameter is exclusive),decrement by 2
# for_loop_5()
# =================================================================


# =================================================================
#                        enhanced based for loop
# =================================================================

def enhanced_loop_1():
    fruits = ['orange','pomegranate','mango','pine apple','apple','guava'] 
    for fruit in fruits: #works lists
        print(fruit)

# enhanced_loop_1()

# =================================================================

def enhanced_loop_2():
    word = 'python'
    for letter in word:
        print(letter)

# enhanced_loop_2()

# =================================================================

def enhanced_loop_3():
    data = {
        "name":"pyboy",
        "language":"python",
        "graduation":"CS"
    }
    for key in data.keys():
        print(f'{key}   {data[key]}')
# enhanced_loop_3()

# =================================================================
#                        enumerate function
# =================================================================


# print index values along with element using enhanced for loop

def index_and_element_1(): #this code will collapse if we have a duplicate element.It shows index of first occurance of element as index
    elements = [1,2,3,4,5,6,7,1]
    for element in elements:
        print(f"elements[{elements.index(element)}] is {element}")
# index_and_element_1()   #BUGGY CODE
# =================================================================


# print index values along with element using range based for loop
def index_and_element_2():
    elements = [1,2,3,4,5,6,7]
    for i in range(len(elements)):
        print(f"elements[{i}] is {elements[i]}")

# index_and_element_2()  # works fine but code is a bit lengthy
# =================================================================


#we can the same functionality with enumerate function
def index_and_element_3():
    elements = [1,2,3,4,5,6,7]
    for index,element in enumerate(elements):
        print(f"elements[{index}] is {element}")
# index_and_element_3()
# =================================================================





# =================================================================
#                        nested loops
# =================================================================
# using while loop
def nested_loop1():
    list1 = [[1,2,3],[4,5,6]]
    length_of_list1 = len(list1)
    i = 0
    while i < length_of_list1:
        length_of_sub_list = len(list1[i])
        j = 0
        while j < length_of_sub_list:  #<----+
            print(list1[i][j],end=' ') #     |-- We can replace this block with 
            j += 1 # <-----------------------+   range based or enhanced for loop
        print()
        i += 1
nested_loop1()

# using range based loop
def nested_loop2():
    list1 = [[1,2,3],[4,5,6]]
    for i in range(len(list1)):
        for j in range(len(list1[i])): #<-----------+
                                                #   |--We can replace this block with
            print(list1[i][j],end=' ') #<-----------+  while loop or enhanced for loop
        print()
# nested_loop2()

# using enhanced loop
def nested_loop3():
    list1 = [[1,2,3],[4,5,6]]
    for sub_list in list1:
        for element in sub_list:#<-----------+
                                         #   |--We can replace this block with
            print(element,end=' ')#<---------+  while loop or range based for loop
        print()
# nested_loop3()