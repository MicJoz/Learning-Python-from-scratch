def chessboard(n=8):
    display = ""
    for i in range(n):
        if display != "":
            display += "\n"
        if i % 2 == 0:
            for j in range(n):
                if j % 2 == 0:
                    continue
                else:
                    display += "# "
        else:
            for j in range(n):
                if j % 2 == 0:
                    continue
                else:
                    display += " #"
    return display


c = chessboard()
print(c)
