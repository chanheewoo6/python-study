print("안녕하세요!\n당신의 상상 속 세상, 드레고타운 입니다.")
print("어느 세계를 가실 건가요??")
place = ""
time = ""

while place == "조선" or "고려":
  place = input("오늘은 대한민국 입니다.\n고려와 조선 중 선택하세요: ")
  print("-------------------------------------------------------")
  if place == "조선":
    break
  if place == "고려":
    break
  else:
      print("알맞은 장소를 선택하세요")

print("{}로 가신다고요? 알겠습니다. {}까지 안전하게 모셔 드리겠습니다.".format(place, place))
print("-------------------------------------------------------")
if place == "고려":
  print("고려에서 어느 시대로 여행을 떠나실 건가요?")
  time = input("고려의 어느 시대에 가실지 선택하세요. 이름으로 정확하게 말해주세요!!\n1. 고려건국\n2. 고려거란전쟁\n3. 고려여진전쟁\n4. 고려의 하이라이트, 원나라와의 긴 전쟁!!\n: ")

if place == "조선":
  print("조선에서 어느 시대로 여행을 떠나실 건가요?")
  time = input("조선의 어느 시대에 가실지 선택하세요. 이름으로 정확하게 말해주세요!!\n1. 조선건국\n2. 조선의 초기 왕들과 사건들\n3. 조선vs명나라 전쟁\n4. 조선의 하이라이트, 왜와의 긴 전쟁과이순신 장군의 이야기!!\n: ")


while time == "고려건국" or "고려거란전쟁" or "고려여진전쟁" or "고려의 하이라이트, 원나라와의 긴 전쟁!!":
  if time == "고려건국" or "고려거란전쟁" or "고려여진전쟁" or "고려의 하이라이트, 원나라와의 긴 전쟁!!":
    break
  else:
    print("알맞은 시대를 선택하세요")
while time == "조선건국" or "조선의 초기 왕들과 사건들" or"조선vs명나라 전쟁" or "왜와의 긴 전쟁과이순신 장군의 이야기!!":
  if time == "조선건국" or "조선의 초기 왕들과 사건들" or"조선vs명나라 전쟁" or "왜와의 긴 전쟁과이순신 장군의 이야기!!":
    break
  else: 
    print("알맞은 시대를 선택하세요")

print("알겠습니다. {}의 {}시대로 가시는군요!!".format(place, time))
while 
  if time not in "고려건국" or "고려거란전쟁" or "고려여진전쟁" or "고려의 하이라이트, 원나라와의 긴 전쟁!!" or "조선건국" or "조선의 초기 왕들과 사건들" or"조선vs명나라 전쟁" or "왜와의 긴 전쟁과이순신 장군의 이야기!!":
    print("그런데 {}에는 {}시대가 없군요!!\n다시 선텍하세요.")
  
  
print("그럼 본격적으로 여행을 출발 하겠습니다.")
print("-------------------------------------------------------")
print("**여행은 시간여행이 끝나면 다음 시간으로 넘어갑니다.**")
print("**또, 여행이 다 끝나면 나오는 상도 있으니 열심히 해 주십시오.**")
print("당신이 살아 돌아온다면...")
print("시작합니다!!")