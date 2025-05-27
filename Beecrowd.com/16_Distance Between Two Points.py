x1,y1 = list(map(float, input().split(" ")))

x2,y2 = list(map(float, input().split(" ")))

import math
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)


print(f"{distance:.4f}")