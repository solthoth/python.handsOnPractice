def get_prime_factors(input: int) -> list:
    factors = []
    divisor = 2
    while divisor <= input:
        if input % divisor == 0:
            factors.append(divisor)
            input = input // divisor
        else:
            divisor += 1
    return factors


def main():
    values = get_prime_factors(1)
    assert values == []
    values = get_prime_factors(2)
    assert values == [2]
    values = get_prime_factors(13)
    assert values == [13]
    values = get_prime_factors(630)
    assert values == [2,3,3,5,7]

if __name__ == "__main__":
    main()