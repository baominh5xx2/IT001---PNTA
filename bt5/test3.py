import time

# Lấy thời gian ban đầu
start_time = time.time()

# Đoạn code bạn muốn đo thời gian chạy ở đây
a,b = 10,2000000
import math
def ktra(n):
  for i in range(2,math.isqrt(n)+1):
    if n % i ==0:
      return False
  return True
count = 0
if int(a) <= 12:
    if int(a)>=3:
         count+=3
         if int(a)>=5:
              count-=1
              if int(a)>=7:
                   count-=1
    for i in range(11,int(b)+1,2):
                if(ktra(i)==True) and (ktra(int("".join(reversed(str(i)))))==True):
                    count+=1
else:
    if int(a)%2 != 0:
            for i in range(int(a),int(b)+1,2):
                if(ktra(i)==True) and (ktra(int("".join(reversed(str(i)))))==True):
                    count+=1
    else:
        for i in range(int(a)+1,int(b)+1,2):
                if(ktra(i)==True) and (ktra(int("".join(reversed(str(i)))))==True):
                    count+=1
print(count)
for i in range(1000000):
    pass

# Lấy thời gian sau khi code chạy xong
end_time = time.time()

# Tính thời gian chạy
running_time = end_time - start_time
print(f"Thời gian chạy: {running_time} giây")