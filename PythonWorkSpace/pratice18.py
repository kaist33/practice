from random import *
users = range(1,21)
users = list(users)
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에 1명은 치킨, 3명은 커피

print("--당첨자 발표")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하드립니다.--")
