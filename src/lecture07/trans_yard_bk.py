while True:
    meter = float(input("長さは何cm？"))
    if meter > 0:
        yard = meter / 91.4
        print(meter, "cmは", yard, "ydですね")
    else:
        print("変換を終了します")
        break    