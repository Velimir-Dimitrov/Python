def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    ract_area = length * width
    rect_perim = 2 * length + 2 * width

    return f"Rectangle area: {ract_area}\nRectangle perimeter: {rect_perim}"


print(rectangle(2, 10))
print(rectangle('2', 10))

