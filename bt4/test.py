import math

def count_integer_coordinates_on_circle(radius):
    r_squared = radius**
    count = 0

    # Duyệt qua từng x và tính y dự kiến
    for x in range(int(-radius), int(radius) + 1):
        y_squared = r_squared - x**2
        # Nếu y^2 là một số nguyên bình phương thì tăng biến đếm
        if y_squared >= 0 and math.isqrt(y_squared)**2 == y_squared:
            count += 1

    return count

radius = 325  # Độ dài bán kính của đường tròn
result = count_integer_coordinates_on_circle(radius)
print("Số tọa độ nguyên trên đường tròn là:", result)
