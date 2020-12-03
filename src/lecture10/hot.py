# 最高気温のリスト
max_temp = [22, 26, 21, 23, 27, 24, 22, 25, 24, 26]
for t in max_temp:
    if 25 <= t:
        max_temp.remove(t)
# 作成したリストを表示
print(max_temp)
