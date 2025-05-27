
# input hisebe string ke spilt function er maddhome list e convert korechi, then map function er maddhome list er protiti item ke float e convert kore then map o object ke list e convert korechi.


a,b,c = list(map(float,input().split()))

Triangle = 0.5*a*c
Circle = 3.14159*c**2
Trapezium = 0.5*(a+b)*c
Square = b**2
Rectangle = a*b


print(f"TRIANGULO: {Triangle:.3f}")
print(f"CIRCULO: {Circle:.3f}")
print(f"TRAPEZIO: {Trapezium:.3f}")
print(f"QUADRADO: {Square:.3f}")
print(f"RETANGULO: {Rectangle:.3f}")



