def is_prime(num):
    prime = True

    for value in range(2, (num - 1)):

        if num % value == 0:
            prime = False
            break
    return prime

print(is_prime(73))