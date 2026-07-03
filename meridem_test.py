import os
os.system("cls")
print('')

t = 3
for i in range(t+t):
    print(f"trial {i}")
    print("-" * 20)

    print(f"t = {t}")
    print(f"i = {i}")

    g = t + 1
    print(f"g = {g}")

    t = t - g
    print(f"t = {t}")
    print("-" * 20)
    