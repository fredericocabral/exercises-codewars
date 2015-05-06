def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_even(n):
    return n % 2 == 0


def is_multiple_of_10(n):
    return n % 10 == 0


def number_property(n):
    return [is_prime(n), is_even(n), is_multiple_of_10(n)]
