def parallelogram_area(height, side_len):
    area = height * side_len
    return area

s, h = map(int, input().split())
print(parallelogram_area(h, s))

