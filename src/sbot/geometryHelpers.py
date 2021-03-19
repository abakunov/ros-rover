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


#перевод из квантерниона в углы эйлера
def quaternion_to_euler(quant):

        w = quant.w
        x = quant.x
        y = quant.y
        z = quant.z

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        X = math.degrees(math.atan2(t0, t1))

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = math.degrees(math.asin(t2))

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        Z = math.degrees(math.atan2(t3, t4))

        return X, Y, Z

#cкалярное произведение
def skalar_mulp(vector1, vector2):
    #print(vector1,vector2)
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]

#getD
def getDeg(vector1,vector2):
    #print(skalar_mulp(vector1,vector2) )
    ln1 = sqrt(vector1[0]**2 + vector1[1]**2)
    ln2 = sqrt(vector2[0]**2 + vector2[1]**2)
    #print(math.degrees(acos(skalar_mulp(vector1,vector2) / (ln1 * ln2))))
    return math.degrees(acos(skalar_mulp(vector1,vector2) / (ln1 * ln2)))
