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
