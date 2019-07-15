import re
opDict = ['', '*']
num = 1000

while num <= 9999:
    s = str(num)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ex = str(s[0]) + opDict[i] + str(s[1]) + opDict[j] + str(s[2]) + opDict[k] + str(s[3])
                ex = re.sub(r'\b0+(?!\b)', '', ex)
                res = 0
                try:
                    if len(ex) > 4:
                        res = eval(ex)
                        if str(num)[::-1] == str(res):
                            print(num)
                except ZeroDivisionError as error:
                    pass
    num += 1