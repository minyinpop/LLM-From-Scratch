import json

text = "ABABABC"

pairs = {}

# 排序
for i in range(len(text) - 1):
    new_text = text[i:i+2]

    if new_text in pairs:
        pairs[new_text] += 1
    else:
        pairs[new_text] = 1
    continue
# ===

best_pair = {
    "appear_number": 0,
    "best_word": ""
}

# 排序，大到小，取最大
for key, value in pairs.items():
    if value > best_pair["appear_number"]:
        best_pair["appear_number"] = value
        best_pair["best_word"] = key
        continue
# ===

temp_tokens = []
new_tokens = []
pointer = 0

# TODO 記得取名
for current_text_01 in text:
    current_text_02 = best_pair["best_word"][pointer]

    if current_text_01 == current_text_02:
        if pointer == len(best_pair["best_word"]) - 1:
            temp_tokens.append(current_text_02)
            new_tokens.append("".join(temp_tokens))

            temp_tokens = []
            pointer = 0
        elif pointer < len(best_pair["best_word"]) - 1:
            temp_tokens.append(current_text_02)
            pointer += 1
        else:
            print("【🥳】恭喜程式碼出問題！")
        continue
    else:
        if pointer == len(best_pair["best_word"]) - 1:
            print("【🥳】恭喜程式碼出問題！")
        elif pointer < len(best_pair["best_word"]) - 1:
            temp_tokens.append(current_text_01)
            new_tokens.append("".join(temp_tokens))

            pointer = 0
        else:
            print("【🥳】恭喜程式碼出問題！")
# ===

# 顯示結果
print("".join(new_tokens))
# ===