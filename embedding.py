import random
import json
import math

DEBUG_MODE = False

CORRECT_LEARNING_RATE: float = .1
WRONG_LEARNING_RATE: float = .1

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

if DEBUG_MODE:
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

if DEBUG_MODE:
    print("")
    print(f"embedding_table: {json.dumps(
        embedding_table,
        ensure_ascii=False,
        indent=4
    )}")
# ===

for epoch in range(0, 20):
    print("")
    print(f"第 {epoch + 1} 次訓練")

    correct_count: int = 0
    accuracy: float = 0

    for subject in DATASET:
        question_vectors: list[list[float]] = []

        # 獲取問題的向量位置
        for word in subject["question"]:
            question_vectors.append(embedding_table[word])

        if DEBUG_MODE:
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

        if DEBUG_MODE:
            print("")
            print(f"average_question_vectors: {json.dumps(
                average_question_vectors,
                ensure_ascii=False,
                indent=4
            )}")
        # ===

        answer_vectors: list[list[float]] = []

        # 獲取答案的向量位置
        for word in vocabulary_table:
            answer_vectors.append(embedding_table[word])

        if DEBUG_MODE:
            print("")
            print(f"vocabulary_table: {json.dumps(
                vocabulary_table,
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

        if DEBUG_MODE:
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

        if DEBUG_MODE:
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

        if DEBUG_MODE:
            print("")
            print(f"distances: {json.dumps(
                distances,
                ensure_ascii=False,
                indent=4
            )}")
        # ===

        answer_distances: dict[str, float] = {}

        # 將答案與距離附值
        for i in range(0, len(vocabulary_table)):
            answer_distances[vocabulary_table[i]] = distances[i]

        if DEBUG_MODE:
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

        if DEBUG_MODE:
            print("")
            print(f"best_pair_word: {best_pair_word}")
            print(f"best_pair_distance: {best_pair_distance}")
        # ===

        print("")
        print(f"題目：{"".join(subject['question'])}")
        print(f"答案：{" / ".join(subject['answer'])}")
        print(f"選擇：{best_pair_word}")

        # 更新單辭的向量座標
        if best_pair_word in subject["answer"]:
            correct_count += 1
        else:
            # 把正確答案拉近題目中心點
            for answer_word in subject["answer"]:
                for i in range(0, len(embedding_table[answer_word])):
                    direction = average_question_vectors[i] - embedding_table[answer_word][i]
                    move_amount = direction * CORRECT_LEARNING_RATE
                    embedding_table[answer_word][i] += move_amount

                if DEBUG_MODE:
                    print("")
                    print("正確答案")

                    print("")
                    print(f"更新後的 {answer_word} 向量位置: {json.dumps(
                        embedding_table[answer_word],
                        ensure_ascii=False,
                        indent=4
                    )}")
            # ===

            # 把錯誤答案推離題目中心點
            for i in range(0, len(embedding_table[best_pair_word])):
                direction = embedding_table[best_pair_word][i] - average_question_vectors[i]
                move_amount = direction * WRONG_LEARNING_RATE
                embedding_table[best_pair_word][i] += move_amount
            # ===

            if DEBUG_MODE:
                print("")
                print("錯誤答案")

                print("")
                print(f"更新後的 {best_pair_word} 向量位置: {json.dumps(
                    embedding_table[best_pair_word],
                    ensure_ascii=False,
                    indent=4
                )}")
        # ===

    print("")
    print(f"第 {epoch + 1} 次訓練正確率: {(correct_count / len(DATASET)) * 100}%")