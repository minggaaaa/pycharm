r = range(1,11)

for i in r:
    print(i)

'''
    eval() -> 혁신적인 함수...
    
    int( 10.22) -> int로 바꿔주는 함수
    float(   )
    bool(  0   ) -> True, False
    str( 1.2 ) -> 문자열로  바꿔주는
    list(   ) ->list 로 바꿔
    tuple(   ) ->
    
    
    
    객체 밖에 있는 함수
    len([,1,2,3,4,5]), max('abcdef'), min ([1,2,3,4,5])
    객체 안에 있는 함수
    count, remove , pop, append, extend
    
    슬라이싱 문법
    a[0:4]
    a[:4]
    a[:]
    
'''

alist = {1,3,4,2,10,99,100,2,3,4}
cnt = alist.count()
alist.sort()