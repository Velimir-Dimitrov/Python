from core.fibonacci_functions import create_fibonacci_seq, locate


def play_fibonacci():
    some_command_string = input()

    while some_command_string != "Stop":
        some_command_string = some_command_string.split()
        if some_command_string[0] == "Create":
            fib_seq = create_fibonacci_seq(int(some_command_string[-1]))
            print(' '.join([str(n) for n in fib_seq]))
        elif some_command_string[0] == "Locate":
            locate(int(some_command_string[-1]), fib_seq)
        else:
            print("Provide valid command.")
        some_command_string = input()



