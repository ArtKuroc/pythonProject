def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        if number == 0 or number == 1:
            print("Составное")

        count = 0
        for i in range(2, number + 1):
            if number % i == 0:
                count += 1

        if count == 1:
            print("Простое")
        else:
            print("Составное")
        return number

    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)