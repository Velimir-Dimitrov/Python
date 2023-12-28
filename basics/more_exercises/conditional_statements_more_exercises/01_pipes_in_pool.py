v_volume_in_litres = int(input())
p1_litres_per_hour = int(input())
p2_litres_per_hour = int(input())
n_hours = float(input())

p1_pipe_in_litres = p1_litres_per_hour * n_hours
p2_pipe_in_litres = p2_litres_per_hour * n_hours
both_pipes_litres = p1_pipe_in_litres + p2_pipe_in_litres
both_pipes_percentage = (both_pipes_litres / v_volume_in_litres) * 100
p1_pipe_in_percentage = (p1_pipe_in_litres / both_pipes_litres) * 100
p2_pipe_in_percentage = (p2_pipe_in_litres / both_pipes_litres) * 100

if v_volume_in_litres >= both_pipes_litres:
    print(f'The pool is {both_pipes_percentage:.2f}% full. Pipe 1: {p1_pipe_in_percentage:.2f}%. Pipe 2: '
          f'{p2_pipe_in_percentage:.2f}%.')
elif v_volume_in_litres < both_pipes_litres:
    print(f'For {n_hours} hours the pool overflows with {(both_pipes_litres - v_volume_in_litres):.2f} liters.')
