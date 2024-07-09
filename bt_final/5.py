from math import isqrt

def count_square_pairs_optimized(N):
    count = 0

    for i in range(1, N + 1):
        square_root_i = isqrt(i)
        count += min(i, square_root_i * 2)

    return count

# Đọc input
N = int(input())

# Gọi hàm và in kết quả
result = count_square_pairs_optimized(N)
print(result)