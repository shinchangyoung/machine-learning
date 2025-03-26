
```py
### 1️⃣

```python
python
복사편집
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 
plt.______ (x, y, ______='o', ______='--', ______='b', label="Line Graph")

# x, y축 라벨 설정
plt.______ ("X축 라벨")
plt.______ ("Y축 라벨")

# 그래프 제목 추가
plt.______ ("간단한 선 그래프")

# 범례 추가
plt.______()

# 그래프 표시
plt.______ ()

```

---

### 2️⃣

```python
python
복사편집
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 15, 10, 20, 25]

# 
plt.______ (x, y, ______='red', ______='x', label="Scatter Plot")

# x, y축 라벨 설정
plt.______ ("X축 값")
plt.______ ("Y축 값")

# 제목 추가
plt.______ ("산점도 예제")

# 범례 추가
plt.______()

# 그래프 표시
plt.______ ()

```

---

### 3️⃣

```python
python
복사편집
import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

# 
plt.______ (categories, values, ______='blue')

# x, y축 라벨 설정
plt.______ ("카테고리")
plt.______ ("값")

# 제목 추가
plt.______ ("막대 그래프 예제")

# 그래프 표시
plt.______ ()

```

---

### 4️⃣

```python
python
복사편집
______ import matplotlib.pyplot as plt
______ import numpy as np

data = np.random.randn(1000)

# 
plt.______ (data, ______=20, ______='green', ______='black')

# 제목 추가
plt.______ ("히스토그램 예제")

# 그래프 표시
plt.______ ()

```

---

### 5️⃣

```python
python
복사편집
______ import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
sizes = [30, 20, 40, 10]

# 
plt.______ (sizes, labels=labels, autopct='%1.1f%%', ______=90)

# 제목 추가
plt.______ ("원형 차트 예제")

# 그래프 표시
plt.______ ()

```

---

### 6️⃣

```python
python
복사편집
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

# 
plt.______ (data)

# 제목 추가
plt.______ ("박스 플롯 예제")

# 그래프 표시
plt.______ ()

```

---

### 7️⃣

```python
python
복사편집
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = np.array([10, 20, 30, 25, 35])
errors = np.array([1, 2, 1, 2, 1])

# 
plt.______ (x, y, yerr=errors, fmt='o', ______='red', ______=5)

# 제목 추가
plt.______ ("오차 막대 그래프")

# 그래프 표시
plt.______ ()

```

---

### 8️⃣

```python
python
복사편집
import matplotlib.pyplot as plt
import numpy as np

#
plt.______ (figsize=(8, 6))

x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
plt.______ (x, y)

# 그래프 제목 추가
plt.______ ("Sine Wave")

# 그래프 표시
plt.______ ()

```

---

### 9️⃣

```python
python
복사편집
import matplotlib.pyplot as plt
import numpy as np

# 1행 2열의 서브플롯 생성
fig, ax = plt.______ (1, 2, figsize=(10, 4))

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 첫 번째 서브플롯에 그래프 그리기
ax[0].______ (x, y1, label="sin(x)")
ax[0].______ ("Sine Wave")

# 두 번째 서브플롯에 그래프 그리기
ax[1].______ (x, y2, label="cos(x)")
ax[1].______ ("Cosine Wave")

# 그래프 표시
plt.______ ()

```

---

### 🔟

```python
python
복사편집
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
plt.______ (x, y)

# 그래프 제목 추가
plt.______ ("Sine Wave")

# 그래프 저장하기
plt.______ ("sine_wave.png")

# 그래프 표시
plt.______ ()

```

---

### 1️⃣1️⃣

```python
python
복사편집
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

# 
plt.______ (data)

# 그래프 제목 추가
plt.______ ("Boxplot Example")

# 그래프 표시
plt.______ ()

```

---

### 1️⃣2️⃣

```python
python
복사편집
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
yerr = 0.1  # 오류 범위

# 
plt.______ (x, y, yerr=yerr)

# 그래프 제목 추가
plt.______ ("Error Bar Example")

# 그래프 표시
plt.______ ()

```
