#                   LIST COMPREHENSIONS
# =================================================================

def nums():
    first_10_nums = [x for x in range(1,11)]
    print(first_10_nums)
# nums()

# =================================================================

def odd_nums():
    odd_nums = [num for num in range(1,11,2)]
    print(odd_nums)
# odd_nums()

# =================================================================

def odd_nums_1():
    odd_nums = [num for num in range(1,11) if num %2 !=0]
    print(odd_nums)
# odd_nums_1()

# =================================================================

def copy_list():
    list1 = ['1',2,'3.6',5.7]
    list2 = [element for element in list1]
    print(list2)
# copy_list()

# =================================================================

def decomposing_a_string():
    string = "python"
    decomposed_string = [letter for letter in string]
    print(decomposed_string)
# decomposing_a_string()

# =================================================================


    