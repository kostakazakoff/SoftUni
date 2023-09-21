def generate_expression(idx, end, words_by_idx, words_count, result):
    if idx >= end:
        print(*result, sep=' ')
        return
    
    if idx not in words_by_idx:
        return
    
    for word in words_by_idx[idx]:
        if words_count[word] == 0:
            continue

        result.append(word)
        words_count[word] -= 1

        generate_expression(idx + len(word), end, words_by_idx, words_count, result)

        result.pop()
        words_count[word] += 1


words = input().split(', ')
target_exp = input()
words_by_index = {}
words_count = {}
exp_end = len(target_exp)

for word in words:
    idx = 0

    while idx < len(target_exp):
        try:
            idx = target_exp.index(word, idx)
        except ValueError:
            break

        if idx not in words_by_index:
            words_by_index[idx] = set()

        words_by_index[idx].add(word)

        if word not in words_count:
            words_count[word] = words.count(word)

        idx += len(word)

        
generate_expression(0, exp_end, words_by_index, words_count, [])
