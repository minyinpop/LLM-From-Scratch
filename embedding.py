import random
import json
import math

DATASET: list[dict[str, list[str]]] = [
    {
        "question": ["我", "喜歡", "吃"],
        "answer": "蘋果"
    },
    {
        "question": ["電腦", "裡", "有"],
        "answer": "CPU"
    }
]

DIMENSION_COUNT: int = 3

def get_random_point() -> list[float]:
    vector: list[float] = []

    for i in range(0, DIMENSION_COUNT):
        vector.append(random.uniform(-1, 1))

    return vector

input_tokens: list[str] = [
    "我",
    "喜歡",
    "吃",
    "蘋果",
    "香蕉",
    "CPU"
]

embedding_table: dict[str, list[float]] = {}

# 使 token 隨機分布在向量空間
for token in input_tokens:
    embedding_table[token] = get_random_point()

print("")
print(f"embedding_table: {json.dumps(
    embedding_table,
    ensure_ascii=False,
    indent=4
)}")
# ===

question: list[str] = [
    "我",
    "喜歡",
    "吃"
]

question_vectors: list[list[float]] = []

# 獲取問題的向量位置
for word in question:
    question_vectors.append(embedding_table[word])

print("")
print(f"question_vector: {json.dumps(
    question_vectors,
    ensure_ascii=False,
    indent=4
)}")
# ===

average_question_vectors: list[float] = []

# 平均問題的向量位置
for i in range(0, DIMENSION_COUNT):
    total_point: float = 0

    for vector in question_vectors:
        total_point += vector[i]

    average_question_vectors.append(total_point / len(question_vectors))

print("")
print(f"average_question_vectors: {json.dumps(
    average_question_vectors,
    ensure_ascii=False,
    indent=4
)}")
# ===

answer: list[str] = [
    "蘋果",
    "香蕉",
    "CPU"
]

answer_vectors: list[list[float]] = []

# 獲取答案的向量位置
for word in answer:
    answer_vectors.append(embedding_table[word])

print("")
print(f"answer_vectors: {json.dumps(
    answer_vectors,
    ensure_ascii=False,
    indent=4
)}")
# ===

differences: list[list[float]] = []

# 計算自身與目標的向量差值
for vector in answer_vectors:
    difference: list[float] = []

    for i in range(0, len(vector)):
        difference.append(vector[i] - average_question_vectors[i])

    differences.append(difference)

print("")
print(f"differences: {json.dumps(
    differences,
    ensure_ascii=False,
    indent=4
)}")
# ===

squared_differences: list[list[float]] = []

# 計算向量的差值平方
for difference in differences:
    squared_difference: list[float] = []

    for point in difference:
        squared_difference.append(point * point)

    squared_differences.append(squared_difference)

print("")
print(f"squared_differences: {json.dumps(
    squared_differences,
    ensure_ascii=False,
    indent=4
)}")
# ===

distances: list[float] = []

# 將差值平方開根號
for squared_difference in squared_differences:
    distance: float = 0

    for point in squared_difference:
        distance += point

    distances.append(math.sqrt(distance))

print("")
print(f"distances: {json.dumps(
    distances,
    ensure_ascii=False,
    indent=4
)}")
# ===

answer_distances: dict[str, float] = {}

# 將答案與距離附值
for i in range(0, len(answer)):
    answer_distances[answer[i]] = distances[i]

print("")
print(f"answer_distances: {json.dumps(
    answer_distances,
    ensure_ascii=False,
    indent=4
)}")
# ===

best_pair_word: str = ""
best_pair_distance: float | None = None

# 找尋距離最靠近 0 的答案
for word, distance in answer_distances.items():
    if best_pair_distance is None:
        best_pair_word = word
        best_pair_distance = distance

    elif best_pair_distance > distance:
        best_pair_word = word
        best_pair_distance = distance

print("")
print(f"best_pair_word: {best_pair_word}")
print(f"best_pair_distance: {best_pair_distance}")
# ===