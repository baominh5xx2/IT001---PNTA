def prime_factors(n):
    factors = []
    # Phân tích thành phần nguyên tố của số
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

# Sử dụng
number = 10
result = prime_factors(number)
print(f"Prime factors of {number}: {result}")
