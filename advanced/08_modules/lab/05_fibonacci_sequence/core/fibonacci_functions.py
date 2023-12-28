def create_fibonacci_seq(num):
    seq = [0, 1]
    for n in range(num - 2):
        seq.append(seq[-1] + seq[-2])
    return seq


def locate(num, seq_list):
    try:
        num_index = seq_list.index(num)
        print(f"The number - {num} is at index {num_index}")
    except ValueError:
        print(f"The number {num} is not in the sequence")