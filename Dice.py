# 라이브러리 불러오기

import random


#주사위 2개 던지기

die1 = random.randrange(1,12)
die2 = random.randrange(1,12)


# 각각의 눈과 합계 출력하기 

print("나온 눈은", die1, ",", die2, "이며 합은", die1 + die2, "입니다.")