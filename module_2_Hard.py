import random
def one_cipher():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    cipher = random.choice(numbers)
    return cipher
def two_cipher(n):
    passcode = {}
    passcode.update({3: 12})
    passcode.update({4: 13})
    passcode.update({5: 1423})
    passcode.update({6: 121524})
    passcode.update({7: 162534})
    passcode.update({8: 13172635})
    passcode.update({9: 1218273645})
    passcode.update({10: 141923283746})
    passcode.update({11: 11029384756})
    passcode.update({12: 12131511124210394857})
    passcode.update({13: 112211310495867})
    passcode.update({14: 1611325212343114105968})
    passcode.update({15: 1214114232133124115106978})
    passcode.update({16: 1317115262143531341251161079})
    passcode.update({17: 11621531441351261171089})
    passcode.update({18: 12151811724272163631545414513612711810})
    passcode.update({19: 118217316415514613712811910})
    passcode.update({20: 13141911923282183731746416515614713812911})
    passresult = passcode.get(n)
    return passresult
n = one_cipher()
print('Шифр: ', n)
pair1 = list(range(1, n))
pair2 = list(range(1, n))
pairs = []
result = ""
for i in pair1:
    for j in pair2:
        p1 = i
        p2 = j
        if p1 >= p2:
            continue
        else:
            krat = n % (p1 + p2)
            if krat == 0:
                pairs.append([p1, p2])
                result = result + str(p1) + str(p2)
print('Пары чисел', *pairs)
print('Пароль', result,)
if int(result) == two_cipher(n):
    print('Ворота открыты')
