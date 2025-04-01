📌 예제: 학생의 시험 합격 여부 예측 (KNN 활용)
📌 문제 정의: 학생의 공부 시간과 수업 참여율을 바탕으로 시험 합격 여부(합격=1, 불합격=0)를 예측하는 문제

1️⃣ 문제 정의
학생의 공부 시간과 수업 참여율을 기반으로 시험 합격 여부(0 or 1)를 예측하는 것이 목표

K-최근접 이웃(KNN) 모델을 사용하여 학습

2️⃣ 라이브러리 및 데이터 불러오기
필요한 라이브러리를 불러와!

```py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
```

py```
df = pd.read_csv("student_data.csv")  # 가상의 학생 데이터
```

md```
3️⃣ 데이터 확인하기
데이터가 어떻게 생겼는지 확인!
````

py```
print(df.head())  # 처음 5개 데이터 확인
print(df.info())  # 데이터 타입 및 결측치 확인
print(df.describe())  # 기초 통계 정보 확인
```
📌 예제 데이터 (student_data.csv)

공부시간(hours)	수업 참여율(%)	시험 합격 여부(target)
3	50	0
5	60	0
7	80	1
8	85	1
2	40	0
4️⃣ 목표값에서 고윳값 확인하기
py```
print(df['target'].value_counts())  # 합격(1), 불합격(0) 개수 확인
```
📌 예제 출력
1    200  # 합격한 학생 200명
0    200  # 불합격한 학생 200명

✅ 합격(1)과 불합격(0)이 균형적으로 분포됨!

5️⃣ 전처리: 결측치 처리하기
py```
print(df.isnull().sum())  # 결측치 개수 확인
df = df.dropna()  # 결측치 제거
```

✅ 결측치가 있다면 평균값으로 채우기

py```
df.fillna(df.mean(), inplace=True)
```

6️⃣ 스케일링 (정규화/표준화)
KNN은 거리 기반 알고리즘이므로 데이터 크기를 맞춰야 해!

py```
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['공부시간(hours)', '수업 참여율(%)']])
```

➡️ 모든 값이 평균 0, 표준편차 1로 변환됨!

7️⃣ 모델링 및 예측, 평가하기
📌 데이터 분리 (80% 학습, 20% 테스트)

py```
X_train, X_test, y_train, y_test = train_test_split(X_scaled, df["target"], test_size=0.2, random_state=42)
```

📌 모델 학습

py```
knn = KNeighborsClassifier(n_neighbors=5)  # K=5 설정
knn.fit(X_train, y_train)  # 모델 학습
```

📌 예측 및 평가 (정확도 확인)

py```
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"KNN 모델 정확도: {accuracy:.2f}")
```

✅ 모델 정확도 예제 출력
KNN 모델 정확도: 0.87
8️⃣ 하이퍼파라미터 튜닝 (K값 조정)
K값을 조정해서 최적의 값을 찾자!

py```
accuracies = []
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

plt.plot(range(1, 21), accuracies)
plt.xlabel("K 값")
plt.ylabel("정확도")
plt.title("K 값에 따른 정확도 변화")
plt.show()
```

📌 K 값에 따른 정확도 변화를 보고 최적의 k를 선택!
✅ 보통 적절한 K값은 3~7 사이에서 결정됨!

9️⃣ KNN 원리 이해하기
📌 KNN 작동 방식
1️⃣ 새로운 학생 데이터(공부 시간, 수업 참여율)가 들어옴
2️⃣ 기존 학생 데이터와의 거리를 계산
3️⃣ 가장 가까운 K개의 데이터를 찾음
4️⃣ 그 데이터의 다수결을 통해 합격 여부 예측

📌 예제: 새로운 학생 예측

python
복사
편집
new_student = [[6, 75]]  # 공부시간 6시간, 참여율 75%
new_student_scaled = scaler.transform(new_student)  # 스케일링 적용
prediction = knn.predict(new_student_scaled)
print("예측 결과:", "합격" if prediction[0] == 1 else "불합격")
✅ 예측 결과 예제 출력

복사
편집
예측 결과: 합격
🎯 정리 (전체 과정)
1️⃣ 문제 정의: 시험 합격 여부 예측
2️⃣ 라이브러리 및 데이터 불러오기
3️⃣ 데이터 확인: 크기, 컬럼, 통계 정보 확인
4️⃣ 목표값 고윳값 확인: 0(불합격), 1(합격) 개수 확인
5️⃣ 전처리: 결측치 제거 또는 채우기
6️⃣ 스케일링: 거리 기반 알고리즘이므로 표준화
7️⃣ 모델링: KNN 학습 및 평가 (기본 K=5 설정)
8️⃣ 하이퍼파라미터 튜닝: 최적의 K 찾기
9️⃣ 이해하기: 새로운 데이터 예측 실습

✅ KNN 모델을 활용하여 학생이 시험에 합격할 확률을 예측할 수 있음! 🚀







나의 말:
여기서 결측치 처리는 어떯


ChatGPT의 말:
✅ 결측치 처리 방법
데이터에 **결측치(NaN)**가 있으면 모델의 학습에 방해가 될 수 있어. 따라서 결측치를 적절히 처리해야 해!

1️⃣ 결측치 확인
먼저 데이터에서 어떤 컬럼에 결측치가 있는지 확인해야 해.

py```
print(df.isnull().sum())  # 각 컬럼별 결측치 개수 확인
```

📌 예제 출력

공부시간(hours)     3  
수업 참여율(%)      2  
target            0  
➡️ "공부시간"과 "수업 참여율"에 결측치가 있음을 확인
```
