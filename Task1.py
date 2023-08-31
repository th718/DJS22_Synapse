# start(inclusive) end(exclusice)
# prime number give binary
# not prime number give array of divisors

start = int(input())
end = int(input())


def prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    if num % 5 == 0 or num % 7 == 0:
        return False
    if num < 1:
        return False
    if num == 2:
        return True
    else:
        return True


def divisors(num):
    divisors = []
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
            return divisors


def divisors_or_prime(start, end):
    dictionary = {}

    for i in range(int(start), int(end)):
        if prime(num):
            dictionary[num] = (bin(num))
        else:
            dictionary[num]=divisors((num))
            return dictionary
dictionary_dict=divisors_or_prime(start+end)
print(dictionary_dict)
