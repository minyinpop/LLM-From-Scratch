input_text: str = "ABABABCACABAC"

sorted_text: list[str] = []

# 分解所有文字
for word in input_text:
    sorted_text.append(word)
# ===

while True:
    temp_pairs: list[str] = []

    # 與下一個相鄰的參數做合併
    for i in range(0, len(sorted_text) - 1):
        temp_pairs.append("".join(sorted_text[i:i+2]))
    # ===

    pair_counts: dict[str, int] = {}

    # 計算各別單詞的出現次數
    for word in temp_pairs:
        if word in pair_counts:
            pair_counts[word] += 1
        else:
            pair_counts[word] = 1
    # ===

    can_merge: bool = False

    # TODO 記得改名 - 檢查還有沒有 Merge 的必要
    for appear_count in pair_counts.values():
        if appear_count > 1:
            can_merge = True

    if not can_merge:
        break
    # ===

    best_pair: str = ""
    best_pair_appear_count: int = 0

    # 取出最常出現的值
    for word, appear_count in pair_counts.items():
        if appear_count <= best_pair_appear_count:
            continue

        best_pair = word
        best_pair_appear_count = appear_count
    # ===

    pointer: int = 0
    new_sorted_text: list[str] = []

    # 組合新的 Token
    while pointer < len(sorted_text):
        text: list[str] = sorted_text[pointer: pointer + 2]
        merged_text: str = "".join(text)

        if merged_text == best_pair:
            new_sorted_text.append(merged_text)
            pointer += 2
        else:
            new_sorted_text.append(text[0])
            pointer += 1


    # ===

    print("")
    print("===")
    print(f"sorted_text: {sorted_text}")
    print(f"temp_pairs: {temp_pairs}")
    print(f"pair_counts: {pair_counts}")
    print(f"best_pair: {best_pair}")
    print(f"new_sorted_text: {new_sorted_text}")
    print("===")

    # 更新 Token
    sorted_text = new_sorted_text
    #

print("")
print("===")
print(f"合併結束: {sorted_text}")
print("===")