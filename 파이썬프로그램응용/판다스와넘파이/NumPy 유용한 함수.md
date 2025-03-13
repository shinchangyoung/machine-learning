NumPy 유용한 함수
```py
arr = np.array([1, 2, 3, 4, 5])

print(np.mean(arr))   # 평균
print(np.median(arr)) # 중앙값
print(np.std(arr))    # 표준 편차
print(np.sum(arr))    # 합계
print(np.max(arr))    # 최대값
print(np.min(arr))    # 최소값

```
정렬 및 유니크 값
```py
arr = np.array([3, 1, 2, 4, 2, 3, 1])

print(np.sort(arr))     # [1 1 2 2 3 3 4] (정렬)
print(np.unique(arr))   # [1 2 3 4] (유니크 값)

```

랜덤 숫자 생성
```py
np.random.rand(3, 3)       # 0~1 사이의 난수 (3x3 행렬)
np.random.randint(1, 10, (2, 2)) # 1~9 사이의 정수 (2x2 행렬)
np.random.normal(0, 1, 5)  # 평균 0, 표준편차 1의 정규분포 (5개)

``
