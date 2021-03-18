from math import sqrt,acos
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

    res = math.degrees(math.atan2(t1, t2)) * -1



    #print(res)
    if  res >= 0:
        return abs(res)

    return 180 - abs(res) + 180

#cкалярное произведение
def skalar_mulp(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]

#getD
def getDeg(vector1,vector2):
    return math.degrees(acos(skalar_mulp(vector1,vector2) / (sqrt(vector1[0]**2 + vector1[1]**2) * sqrt(vector2[0] **2 + vector2[1]**2))))
