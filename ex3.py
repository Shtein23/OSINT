from datetime import datetime


def write_in_file(fileOut, a, value):
    fileOut.write(f'{datetime.fromtimestamp(a).strftime("%Y-%m-%d %H:%M:%S")} {value}\n')


fileIn = open('files/ex3_user_1.txt', 'r')
x = fileIn.read().split("\n")
fileIn.close()

online = [[int(y.split(" ")[0]), int(y.split(" ")[1])] for y in sorted(x)]


k = 0
i = online[k][0]
count = len(online)
flag = True

fileOut = open('output_2.txt', 'w')
while i <= online[-1][1]:
    if i > online[k][1] != i - 5 and i - online[k][1] < 5:
        write_in_file(fileOut, online[k][1], "True")

    if online[k][0] <= i <= online[k][1]:
        write_in_file(fileOut, i, "True")
    elif online[k][1] < i < online[k+1][0]:
        write_in_file(fileOut, i, "False")
    else:
        if online[k + 1][0] != i:
            write_in_file(fileOut, online[k + 1][0], "True")
            write_in_file(fileOut, i, "True")
        else:
            write_in_file(fileOut, i, "True")

    if i + 5 > online[-1][1] != i:
        write_in_file(fileOut, online[-1][1], "True")

    if k < count-1 and i >= online[k+1][0]:
        k += 1
    i += 5

fileOut.close()
