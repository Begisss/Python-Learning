def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum(k):
    total = 0
    for digit in str(k):
        print(f"Raqam: {digit}, Butun son sifatida: {int(digit)}")
        total += int(digit)
    print(f"Yakuniy yig‘indi: {total}")
    return total

def powers_of_two(N):
    k = 1
    while True:
        power = 2 ** k
        if power > N:
            break
        print(power, end=' ')
        k += 1
