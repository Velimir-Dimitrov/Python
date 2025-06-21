def construct(index, target, words, used, path, results):
    if index == len(target):
        results.add(' '.join(path))
        return

    for i in range(len(words)):
        if used[i]:
            continue
        word = words[i]
        if target.startswith(word, index):
            used[i] = True
            construct(index + len(word), target, words, used, path + [word], results)
            used[i] = False


words = input().split(', ')
target = input()

used_flags = [False] * len(words)
results = set()

construct(0, target, words, used_flags, [], results)

for res in results:
    print(res)


# # Input
# text, me, so, do, m, ran
# somerandomtext

# Word, cruncher, cr, h, unch, c, r, un, ch, er
# Wordcruncher

# tu, stu, p, i, d, pi, pid, s, pi
# stupid

