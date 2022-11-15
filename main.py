#the functions find and return a list of prime numbers\n'
#  '            with n primes in it.
#  '    :param n: number of primes the function needs to return\n'
#  '    :return: list that contains the amount of n prime numbers.\n'
# proposed Solution:\n'
# prime numbers are the numbers that can\'t be divided by 2,3,5,7,11 and \n'
# subsequntly by any of the multiplication products of those numbers.\n'
# define the list of the dividers[2,3,5,7,11]\n'
# create 2 loops ; main loop is for the number of results to be generated\n'
# with the internal loop for each number examined - division by the number in the  list, \n'
# If the division result is not a  whole number,add 1 to the  Prime_indicator field. If Prime_inidicator is \n'
# equal the number of items in the list - the newly found Prime NUmber is added to the resulting output list.\n'

def primes_generator(n):

    dividers = (2,3,5,7,11)
    next_result = 1
    resulting_list=["result is -"]
    while len(resulting_list) <= n:
        prime_indicator = 0
        for i in range(len(dividers)):
            remainder = next_result%int(dividers[i])
            if (remainder!= 0 or next_result//(dividers[i]) == 1):
                 prime_indicator=prime_indicator +1
        if prime_indicator == len(dividers):
           resulting_list.append(next_result)
        next_result=next_result+1
        i=0
    print(resulting_list)
def input_list():
    my_input = []
    str_input = []
    i=0
    while str_input != "x":
        str_input = input("Input your coordinates in pairs:")
        if str_input != "x":
            my_input.append(str_input.split(" "))
            i=i+1
    return (my_input)
def orthogonal_number(vectors):
    pairs=-1
    orthogonal = 0
    vector2X = 1
    vector2Y = 1
    iterations =0
    for pairs in vectors:
        for coords in pairs:
            vector1X = int(pairs[0])
            vector1Y = int(pairs[1])
            if (vector1Y*vector2Y) + (vector1X*vector2X) == 0:
                orthogonal=orthogonal+1
            vector2X = vector1X
            vector2Y = vector1Y
            iterations = iterations+1
    if iterations >= len(vectors):
        print("orthogonal pairs total",orthogonal)
        return(orthogonal)

coord_for_calc=input_list()
orthogonal_number(coord_for_calc)

how_many_nums = input("How many prime numbers would you like to be generated:")
primes_generator(int(how_many_nums))