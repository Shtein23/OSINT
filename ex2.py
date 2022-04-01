# Перевести даты из одного формата в другой

fileIn = open('files/ex2_user_1.log', 'r')

old_split_date = []
start_date = 0
end_date = 0

dates = fileIn.read().split("\n")
flag = False

fileOut = open('files/ex2_output.txt', 'w', encoding='utf-8')
fileOut.write('User_1 был онлайн в следующие промежутки времени:\n')

for date in dates:

    if date != '':
        old_split_date.append(date.split(" "))
        if old_split_date[-1][2] == "True" and not flag:
            flag = True
            start_date = old_split_date[-1][0] + " " + old_split_date[-1][1]
        elif old_split_date[-1][2] == "False" and flag:
            flag = False
            end_date = old_split_date[-2][0] + " " + old_split_date[-2][1] + "\n"
            fileOut.write(start_date + " - " + end_date)
if old_split_date[-1][2] == "True" and flag:
    end_date = old_split_date[-1][0] + " " + old_split_date[-1][1] + "\n"
    fileOut.write(start_date + " - " + end_date)

fileOut.close()
