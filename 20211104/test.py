# 1. 튜플을 인자로 전달하면, 이를 리스트로 바꿔주는 함수를 만들어보자.
# 예를 들어서 to_list 라는 이름으로 함수를 만들었다면 다음과 같이 동작해야 한다.
# ds = (1,2,3)
# ds = to_list(ds)
# print(ds)
# [1,2,3]
#
# 만약에 함수를 제대로 만들었다면, 다음과 같이 이 함수는 문자열을 대상으로도 잘
# 동작할 것이다.
# ds = "hello"
# ds = to_list(ds)
# print(ds)
# ['h','e','l','l','o']

# 2.
# 구구단의 7단을 거꾸로 출력하는  for루프와 range를 기반으로 만들어보자. 단 출력 내용
# 으로는 다음과 같이 결과만 보이기로 하자
# 63 56 49 42 35 28 21 14 7

# 3.
# 다음 튜플을 만들어보자. 이 튜플은 1부터 시작해서 100까지 증가한다. 그리고 다시 1씩
# 줄어들어서 마지막에 1로 끝난다
# (1,2,3,4,5,6,7,...97,98,99,100,99,98,97,96,95...5,4,3,2,1)
#
# 물론 위의 숫자를 모두 입력해서 만들라는 뜻이 아니다. 레인지와 이를 튜플로 바꿔주는
# 함수를 사용해서 한 줄에 입력 가능한 수준으로 만들어보라는 의미이다.
# 참고로 이러한 튜플을 만들려면 값이 증가하는 튜플과 감소하는 튜플을 각각
# 생성해서 이를 하나로 묶는 과정을 격어야 한다.
