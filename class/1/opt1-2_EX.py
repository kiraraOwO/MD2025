import json
import py5

PIXEL_SIZE = 1
BORDER_X = 10
BORDER_Y = 10

with open("extra/mihoyo_logo.json") as f:
    data: list = json.load(f)
print(data)

# 根据像素数量自动调整画布大小
max_y = len(data)
max_x = len(data[0])
canvas_size_x = max_x * PIXEL_SIZE + BORDER_X * 2
canvas_size_y = max_y * PIXEL_SIZE + BORDER_Y * 2


def setup():
    # py5.size(100, 100)
    py5.size(canvas_size_x, canvas_size_y)
    py5.background(204, 204, 204)
    py5.no_stroke()
    x_start_at = BORDER_X
    y_start_at = BORDER_Y
    # py5.rect(start_X, start_Y, width, height)
    for y in range(len(data)):
        for x in range(len(data[y])):
            print(x, y, data[y][x])
            py5.fill(data[y][x][0], data[y][x][1], data[y][x][2])
            # py5.rect(x_start_at*(x+1), y_start_at*(y+1), PIXEL_SIZE, PIXEL_SIZE)
            py5.rect(x_start_at+PIXEL_SIZE*x, y_start_at+PIXEL_SIZE*y, PIXEL_SIZE, PIXEL_SIZE)


if __name__ == '__main__':
    py5.run_sketch()
