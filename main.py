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

primes_generator(29)