# 알파벳과 숫자 초기화
alphabet = 'a'
number = 1

# 4줄에 걸쳐 패턴 생성
for i in range(4):
    line = ""
    # 각 줄의 문자와 숫자 추가
    for j in range(4):
        if i + j < 4:  # 대각선 기준 왼쪽 위 부분
            line += alphabet + " "
            alphabet = chr(ord(alphabet) + 1)  # 다음 알파벳으로
        else:  # 대각선 기준 오른쪽 아래 부분
            line += str(number) + " "
            number += 1
    print(line.strip())  # 줄 끝의 공백 제거 후 출력
