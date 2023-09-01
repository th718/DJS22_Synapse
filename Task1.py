# start(inclusive) end(exclusice)
# prime number give binary
# not prime number give array of divisors
#create dict
#take input , num in range
def is_prime(num):
    if(num<2):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def divisors_and_prime(start, end):
    arrays = {}
    for num in range(start, end):
        if is_prime(num):
            arrays[num] = bin(num)
        else:
            arrays[num] = get_divisors(num)
    return arrays
print("start:")
start_range = int(input())
print("end:")
end_range = int(input())

range_dict = divisors_and_prime(start_range, end_range)
print(range_dict)
