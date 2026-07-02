import random
import json
import math

DATASET: list[dict[str, list[str]]] = [
    {
        "question": ["我", "喜歡", "吃"],
        "answer": ["蘋果", "香蕉"]
    },
    {
        "question": ["電腦", "裡", "有"],
        "answer": ["CPU"]
    }
]

DIMENSION_COUNT: int = 3

def get_random_point() -> list[float]:
    vector: list[float] = []

    for i in range(0, DIMENSION_COUNT):
        vector.append(random.uniform(-1, 1))

    return vector

vocabulary_table: list[str] = []

# 建立單辭表
for data in DATASET:
    for question_word in data["question"]:
        if question_word in vocabulary_table:
            continue

        vocabulary_table.append(question_word)

    for answer_word in data["answer"]:
        if answer_word in vocabulary_table:
            continue

        vocabulary_table.append(answer_word)

print("")
print(f"vocabulary_table: {json.dumps(
    vocabulary_table,
    ensure_ascii=False,
    indent=4
)}")
# ===

embedding_table: dict[str, list[float]] = {}

# 建立向量表
for vocabulary in vocabulary_table:
    embedding_table[vocabulary] = get_random_point()

print("")
print(f"embedding_table: {json.dumps(
    embedding_table,
    ensure_ascii=False,
    indent=4
)}")
# ===

subject: dict[str, list[str]] = DATASET[random.randint(0, len(DATASET) - 1)]

question_vectors: list[list[float]] = []

# 獲取問題的向量位置
for word in subject["question"]:
    question_vectors.append(embedding_table[word])

print("")
print(f"subject: {json.dumps(
    subject,
    ensure_ascii=False,
    indent=4
)}")

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
print(f"answer: {json.dumps(
    answer,
    ensure_ascii=False,
    indent=4
)}")

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

print("")
print(f"題目：{"".join(subject['question'])}")
print(f"答案：{" / ".join(subject['answer'])}")
print(f"選擇：{best_pair_word}")