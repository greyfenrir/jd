from sys import argv


def minimal_distance(word1, word2):
    def get_dp(i, j):
        if i < 0 and j < 0:  # both words are finished
            return 0
        if i < 0:           # word1 is finished, deletion of j+1 (rest of word2) chars
            return j + 1
        if j < 0:           # word2 is finished, insertion of i+1 (rest of word1) chars
            return i + 1
        return dp[i][j]     # check in progress..

    lines = len(word1)
    rows = len(word2)
    dp = [[0 for _ in range(rows)] for _ in range(lines)]

    for i in range(lines):
        for j in range(rows):
            dp[i][j] = min(
                get_dp(i - 1, j) + 1,   # remove last char from w1 (deletion)
                get_dp(i, j - 1) + 1,   # remove last char from w2 (insertion)
                get_dp(i - 1, j - 1) + (0 if word1[i] == word2[j] else 1)   # replacement or just moving forward
            )

    distance = get_dp(lines - 1, rows - 1)

    result = distance
    cur_i = lines - 1
    cur_j = rows - 1
    cur_word = list(word2)

    print(''.join(cur_word))
    while distance > 0:
        deletion = get_dp(cur_i, cur_j - 1)
        insertion = get_dp(cur_i - 1, cur_j)
        substitution = get_dp(cur_i - 1, cur_j - 1)
        if deletion < distance:
            del cur_word[cur_j]
            cur_j -= 1
            distance = deletion
            print(''.join(cur_word))
        elif insertion < distance:
            cur_word.insert(cur_j + 1, word1[cur_i])
            cur_i -= 1
            distance = insertion
            print(''.join(cur_word))
        elif substitution < distance:
            cur_word[cur_j] = word1[cur_i]
            cur_i -= 1
            cur_j -= 1
            distance = substitution
            print(''.join(cur_word))
        else:
            cur_i -= 1
            cur_j -= 1

    return result


def min_dist(w1, w2):
    # todo: don't calculate min_dist several times for the same input words, for that save results in cache table
    if w1 == w2:
        return 0
    elif not w1:
        return len(w2)
    elif not w2:
        return len(w1)
    elif w1[0] == w2[0]:
        return min_dist(w1[1:], w2[1:])
    else:
        deletion = min_dist(w1[1:], w2)
        replacement = min_dist(w1[1:], w2[1:])
        insertion = min_dist(w1, w2[1:])
        return 1 + min(deletion, replacement, insertion)


if __name__ == '__main__':
    if len(argv) != 3:
        print('Usage format: \n\t distance <word1> <word2>')
        exit(1)
    else:
        min_d = minimal_distance(argv[1], argv[2])
        print(f'Min distance: {min_d}')

