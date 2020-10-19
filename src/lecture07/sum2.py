end = num = int(input("最後の数値を入力してください："))
sum = 0
while num > 0:
    sum += num
    num -= 1
print(str(end) + "までの総和：", sum)
