# 한줄이 넘어갈 때 \를 주면 됨

alist = [['동수',103020],
         ['진우',102030],
         ['길동',112233]]

print(alist)
alist[0] [0] = '수진'
print(alist)

btuple = [('동수',102030),
          ('진우',102030),
          ('길동',112233)]

print(btuple)
btuple[0][0] = '수진'
print(btuple)