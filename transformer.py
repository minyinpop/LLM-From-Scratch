import embedding
import random
import json

from pathlib import Path

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

VOCABULARY_TABLE: list[str] = []

EMBEDDING_TABLE: dict[str, list[float]] = {}

with open(file=Path(__file__).parent/"config.json", mode="r", encoding="utf-8") as f:
    config = json.load(f)

def get_random_point() -> list[float]:
    vector: list[float] = []

    for i in range(0, config["dimension_count"]):
        vector.append(random.uniform(-1, 1))

    return vector

def initialize():
    # 建立單辭表
    for data in DATASET:
        for question_word in data["question"]:
            if question_word in VOCABULARY_TABLE:
                continue

            VOCABULARY_TABLE.append(question_word)

        for answer_word in data["answer"]:
            if answer_word in VOCABULARY_TABLE:
                continue

            VOCABULARY_TABLE.append(answer_word)

    if config["debug_mode"]:
        print("")
        print(f"VOCABULARY_TABLE: {json.dumps(
            VOCABULARY_TABLE,
            ensure_ascii=False,
            indent=4
        )}")
    # ===

    # 建立向量表
    for vocabulary in VOCABULARY_TABLE:
        EMBEDDING_TABLE[vocabulary] = get_random_point()

    if config["debug_mode"]:
        print("")
        print(f"EMBEDDING_TABLE: {json.dumps(
            EMBEDDING_TABLE,
            ensure_ascii=False,
            indent=4
        )}")
    # ===

def main():
    initialize()

    embedding.forward(
        dataset=DATASET,
        vocabulary_table=VOCABULARY_TABLE,
        embedding_table=EMBEDDING_TABLE
    )

if __name__ == '__main__':
    main()