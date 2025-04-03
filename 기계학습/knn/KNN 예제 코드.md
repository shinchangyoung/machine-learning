KNN 예제 코드
```py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 2. 훈련 데이터와 테스트 데이터로 분리 (8:2 비율)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 데이터 표준화 (KNN은 거리 기반이므로 스케일 조정 필요)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. KNN 모델 생성 및 학습 (K=5)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 5. 예측 수행
y_pred = knn.predict(X_test)

# 6. 모델 평가 (정확도)
accuracy = accuracy_score(y_test, y_pred)
print(f"KNN 정확도: {accuracy:.2f}")

```
코드 설명 정리
데이터 로드
load_iris()를 사용해 붓꽃 데이터셋을 불러오고, 특징(X)과 정답(y) 데이터를 분리.

훈련 데이터와 테스트 데이터 분리
train_test_split()을 사용하여 80%를 훈련 데이터, 20%를 테스트 데이터로 나눔.

데이터 표준화 (정규화)
KNN은 거리(유클리드 거리)를 기반으로 하기 때문에, StandardScaler()를 이용하여 데이터를 표준화(평균 0, 분산 1)함.
KNN 모델 생성 및 학습
KNeighborsClassifier(n_neighbors=5)을 사용하여 k=5인 KNN 모델을 생성하고 fit() 함수로 학습.

예측 수행
predict() 함수로 테스트 데이터를 입력하여 예측 수행.

모델 평가
accuracy_score()로 실제 값과 예측 값을 비교하여 정확도를 출력.


KNN의 특징
✅ 비모수 모델: 데이터 분포를 가정하지 않고 학습.
✅ 간단한 개념: 거리를 기반으로 다수결 투표를 통해 예측.
✅ 훈련 속도 빠름: 학습 과정에서 데이터 저장만 수행.
⚠️ 예측 속도 느림: 새로운 데이터가 들어오면 거리 계산을 수행해야 해서 느릴 수 있음.
⚠️ 고차원 데이터에 취약: 차원이 커질수록 거리 계산이 어려워지고 성능이 떨어질 수 있음.

K 값 선택(K=?)은 중요한 하이퍼파라미터로, 보통 홀수 + 교차 검증을 통해 최적값을 찾는 것이 일반적



