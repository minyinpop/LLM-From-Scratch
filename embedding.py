import random

def get_random_value() -> float:
    return random.uniform(-1, 1)

tokens: list[str] = [
    "我",
    "喜歡",
    "吃",
    "香蕉",
    "蘋果",
    "CPU"
]

embedding_table: dict[str, float] = {}

# 把 Token 轉為 Embedding 列表
for token in tokens:
    embedding_table[token] = get_random_value()
# ===

question: list[str] = [
    "我",
    "喜歡",
    "吃"
]

total_question_point: float = 0

# 出題目
for word in question:
    total_question_point += embedding_table[word]
# ===

probably_answer: list[str] = [
    "香蕉",
    "蘋果",
    "CPU"
]

answer_distance: dict[str, float] = {}

average_question_point: float = total_question_point / len(question)

# 計算答案的權重
for word in probably_answer:
    answer_distance[word] = abs(average_question_point - embedding_table[word])
# ===

best_pair_word: str = ""
best_pair_word_point: float = 0

# 獲取權重最小的值
for word, point in answer_distance.items():
    if best_pair_word == "":
        best_pair_word = word
        best_pair_word_point = point
        continue

    if point < best_pair_word_point:
        best_pair_word = word
        best_pair_word_point = point
        continue
# ===

print(f"answer_distance: {answer_distance}")
print(f"best_pair_word: {best_pair_word}")