length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

volume_sm = length * width * height
volume_litres = volume_sm / 1000
required_litres = volume_litres * (1 - percentage)
print(required_litres)

