num = 11

while True:
   if format(num, 'b') == format(num, 'b')[::-1] and format(num, 'o') == format(num, 'o')[::-1] \
       and str(num) == str(num)[::-1]:
       print(num)
       break
   num += 2


 