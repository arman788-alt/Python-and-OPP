# WAY_01
a = float(input())


print("NOTAS:")
for i in [100, 50, 20, 10, 5, 2]:
    print(f"{int(a/i)} nota(s) de R$ {i}.00")
    a = float(f"{a%i:.2f}")


print("MOEDAS:")
for i in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:

           print(f"{int(a/i)} moeda(s) de R$ {i:.2f}")
           a = float(f"{a%i:.2f}")


    


    


# Way_02

# a = float(input())

# print("NOTAS:")
# for i in [100, 50, 20, 10, 5, 2]:
#     print(f"{int(a/i)} nota(s) de R$ {i}.00")
#     a = float(f"{a%i:.2f}")

# print("MOEDAS:")
# for i in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:

#     if i == 1:
#         print(f"{int(a/i)} moeda(s) de R$ 1.00")
#         a = float(f"{a%i:.2f}")


    
#     elif i == 0.50:
#         print(f"{int(a/i)} moeda(s) de R$ 0.50")
#         a = float(f"{a%i:.2f}")
    
#     elif i == 0.25:
#         print(f"{int(a/i)} moeda(s) de R$ 0.25")
#         a = float(f"{a%i:.2f}")

#     elif i == 0.10:
#         print(f"{int(a/i)} moeda(s) de R$ 0.10")
#         a = float(f"{a%i:.2f}")

#     elif i == 0.05:
#         print(f"{int(a/i)} moeda(s) de R$ 0.05")
#         a = float(f"{a%i:.2f}")


#     elif i == 0.01:
#         print(f"{int(a/i)} moeda(s) de R$ 0.01")
#         a = float(f"{a%i:.2f}")


    
    





