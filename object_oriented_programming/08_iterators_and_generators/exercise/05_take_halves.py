def solution():
    def integers():
        current_num = 1
        while True:
            yield current_num
            current_num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]
    return (take, halves, integers)


# Test codes:
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))

