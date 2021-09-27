#My original solution.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1lc = name1.lower()
name2lc = name2.lower()

T = name1lc.count('t') + name2lc.count('t')
R = name1lc.count('r') + name2lc.count('r')
U = name1lc.count('u') + name2lc.count('u')
E = name1lc.count('e') + name2lc.count('e')

true = T + R + U + E

L = name1lc.count('l') + name2lc.count('l')
O = name1lc.count('o') + name2lc.count('o')
V = name1lc.count('v') + name2lc.count('v')
E2 = name1lc.count('e') + name2lc.count('e')

love = L + O + V + E2

tls = str(true) + str(love)

tl = int(tls)

if tl <= 10 or tl >= 90:
  print(f'Your score is {tl}%, you go together like coke and mentos.')
if tl >= 40 and tl <= 50:
  print(f'Your score is {tl}%, you are alright together.')
else:
  print(f'Your score is {tl}%.')

#More optimized solution.

names = name1 + name2
nameslc = names.lower()

T = nameslc.count('t')
R = nameslc.count('r')
U = nameslc.count('u')
E = nameslc.count('e')

true = T + R + U + E

L = nameslc.count('l')
O = nameslc.count('o')
V = nameslc.count('v')
E = nameslc.count('e')

love = L + O + V + E

tl = int(str(true) + str(love))

if tl <= 10 or tl >= 90:
  print(f'Your score is {tl}%, you go together like coke and mentos.')
if tl >= 40 and tl <= 50:
  print(f'Your score is {tl}%, you are alright together.')
else:
  print(f'Your score is {tl}%.')