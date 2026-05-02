Num = [[]] * 3
for i in range(3):
	Num[i] = float(input(f"Insira o {i+1}º número"))
Num.sort()
print(f"O maior deles é {Num[2]}")