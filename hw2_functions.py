# EX 1

def sum_of_numbers(*args,**kwargs):
    my_sum=0
    for i in args:
        if type(i) in [int, float]:
            my_sum = my_sum+i

    return my_sum

sum_of_parameters=sum_of_numbers(1,5,-3,'abc',[12,56,'cad'])
print(f'sum of parameters {sum_of_parameters}')
sum_of_parameters=sum_of_numbers()
print(f'sum of parameters {sum_of_parameters}')
sum_of_parameters=sum_of_numbers(2,4,'abc',param_1=2)
print(f'sum of parameters {sum_of_parameters}')

# EX 2

# def recursive_sum(n):
# total_sum=int()
# sum_of_even_numbers=int()
# sum_of_odd_numbers=int()
#     if n == 0:
#         return 0,0,0
#     total_sum=n+total_sum
#     if n % 2 == 0:
#         sum_of_even_numbers=n+sum_of_even_numbers)
#
#     else:
#         sum_of_odd_numbers=n+sum_of_odd_numbers
#
#     return total_sum,even_numbers,odd_numbers
# print(recursive_sum(5))




def recursive_sum(n):

    # total_sum=int()
    # sum_of_even_numbers=int()
    # sum_of_odd_numbers=int()

    if n < 0:
        return (0,0,0)

    all_numbers,even_numbers,odd_numbers=recursive_sum(n-1)
    total_sum=n+all_numbers
    if n%2==0:
        sum_of_even_numbers=n+even_numbers
        sum_of_odd_numbers=odd_numbers
    else:
        sum_of_odd_numbers = n+odd_numbers
        sum_of_even_numbers=even_numbers
    return total_sum,sum_of_even_numbers,sum_of_odd_numbers   #returneaza tuplu, nu poti sa folosesti rezultatul ca int


print(recursive_sum(5))

# EX 3
def is_integer():
    read_me=input('write something here: ')
    try:
        number=int(read_me)
        return number
    except:
        return 0

print(f' Result  {is_integer()}')

