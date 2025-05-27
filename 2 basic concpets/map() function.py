# Normally:
# def mul_five_times(number):
#     return number*5

# num = [1,2,3,4,5]
# result = []

# for i in num:
#     result.append(mul_five_times(i))

# print(result)





    
# USE MAP FUNCTION:
# Returns the specified iterator with the specified function applied to each item
# Example:1
def mul_five_times(number):

    return number*5

num = [1,2,3,4,5]

result = list(map(mul_five_times,num))

print(result)





# Example:2

# input hisebe string ke spilt function er maddhome list e convert korechi, then map function er maddhome list er protiti item ke float e convert kore then map o object ke list e convert korechi.

# a,b,c = list(map(float,input().split()))

# Triangle = 0.5*a*c
# Circle = 3.14159*c**2
# Trapezium = 0.5*(a+b)*c
# Square = b**2
# Rectangle = a*b

# print(f"TRIANGULO: {Triangle:.3f}")
# print(f"CIRCULO: {Circle:.3f}")
# print(f"TRAPEZIO: {Trapezium:.3f}")
# print(f"QUADRADO: {Square:.3f}")
# print(f"RETANGULO: {Rectangle:.3f}")




# Example:03
# angle1, angle2 = map(int, input("Enter the two angles using space = ").split())

# thirdAngle = 180 - (angle1 + angle2)


# #output
# print("Third angle =",thirdAngle)
