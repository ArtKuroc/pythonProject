my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
s = 0
while s < len(my_list):
    num = my_list[s]
    s = s + 1
    if num == 0:
        continue
    elif num < 0:
        break
    print(num)