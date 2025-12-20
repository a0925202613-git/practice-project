# 📚 Python 專案學習指南：虛擬寵物收容所

## 專案簡介

透過實作寵物管理系統，學習 Python 基礎語法和**物件導向程式設計（OOP）**。

### 🎯 學習目標

| 類別 | 概念 |
|------|------|
| **OOP** | 類別、物件、繼承、**多型** |
| **語法** | List、for / while 迴圈、if / elif / else、input() |

---

## 📌 專案結構

```
python-test/
├── art_data.py        # ASCII Art 資料
├── animal_models.py   # OOP 類別定義（重點！）
├── shelter_app.py     # 主程式、互動選單
└── readme.md
```

---

## 🔑 核心概念：多型

> 不同類型的物件，用相同方式呼叫，但有不同的行為。

```python
pets = [Cat("小花"), Dog("旺財"), Turtle("龜龜")]

for pet in pets:
    pet.make_sound()  # 同樣呼叫，不同輸出！
```

---

## 🎯 任務清單

找到所有 `#### [任務] ####` 的地方，補上程式碼。

### `animal_models.py`

| 任務 | 概念 |
|------|------|
| `get_info()` | 回傳字串 |
| Cat/Dog/Turtle 建構式 | `super().__init__()` |
| Cat/Dog/Turtle 的 `make_sound()` | 多型 |
| `introduce_all_animals()` | for 迴圈 |

### `shelter_app.py`

| 任務 | 概念 |
|------|------|
| 初始寵物列表 | 建立物件 |
| `show_all_pets()` | for 迴圈、計數器 |
| `add_pet_interactive()` | input()、if/elif、append() |
| `remove_pet_interactive()` | int()、pop() |
| `let_pets_interact()` | isinstance() |
| `count_by_species()` | for + isinstance |
| `interactive_menu()` | while、break |

---

## 📖 概念速查

### 繼承與 super()
```python
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")
```

### 多型
```python
class Cat(Animal):
    def make_sound(self):
        print("喵！")

class Dog(Animal):
    def make_sound(self):
        print("汪！")
```

### isinstance
```python
if isinstance(pet, Cat):
    pet.climb_tree()
```

### List 操作
```python
pets.append(Cat("小花"))  # 新增
pets.pop(0)               # 移除
```

---

## ▶️ 執行方式

```bash
python shelter_app.py
```

祝學習愉快！🐾
