age = int(input("年齢を入力してください："))
if age >= 0:
    if age < 3:
        print("無料です")
    elif age < 13:
        print("半額です")
    elif age < 65:
        print("通常料金です")
    else:
        print("無料です")
else:
    print("正の整数を入力してください")
