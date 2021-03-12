from math import sqrt
import math

#Вычисление расстояния между двумя точками
def calculate_dist(first , second ) -> float:
    return sqrt(
            (first.x - second.x) ** 2 + (first.y - second.y) ** 2
        )

#перевод из кванториона в градусы
def quaternion_to_theta(quant):

    t1 = +2.0 * (quant.w * quant.z + quant.x * quant.y)
    t2 = +1.0 - 2.0 * (quant.y ** 2 + quant.z**2)

    res = math.degrees(math.atan2(t1, t2))
    print(res)
    if  res < 0:
        return abs(res)

    return res + 180