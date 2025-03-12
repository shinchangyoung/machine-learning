## 주요 차이점 요약:

<table>
  <tr>
    <th>특징</th>
    <th>iloc</th>
    <th>loc</th>
  </tr>
  <tr>
    <td>인덱싱 기준</td>
    <td>정수 기반 인덱스 (0, 1, 2, ...)</td>
    <td>레이블 기반 인덱스 (행/열의 이름)</td>
  </tr>
  <tr>
    <td>슬라이싱 끝 인덱스</td>
    <td>끝 인덱스를 포함하지 않음</td>
    <td>끝 인덱스를 포함 (슬라이싱에서 범위 포함)</td>
  </tr>
  <tr>
    <td>사용 예시</td>
    <td>iloc[0], iloc[0:3]</td>
    <td>loc[0], loc[0:3]</td>
  </tr>
</table>

iloc: integer location의 약자


import pandas as pd

# 예시 DataFrame
data = {'col_1': [10, 20, 30, 40, 50],
        'col_2': [15, 25, 35, 45, 55]}
sample_df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# iloc: 정수 인덱스로 선택
print(sample_df.iloc[0])        # 첫 번째 행 (0번 인덱스)
print(sample_df.iloc[:, 0])     # 첫 번째 열 (0번 인덱스)
print(sample_df.iloc[0:3, 0:2]) # 0~2번 행, 0~1번 열

# loc: 레이블 인덱스로 선택
print(sample_df.loc['a'])       # 'a' 행
print(sample_df.loc[:, 'col_1'])# 'col_1' 열
print(sample_df.loc['a':'c', 'col_1':'col_2']) # 'a'~'c' 행, 'col_1'~'col_2' 열

