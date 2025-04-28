import json
import time

import py5

PIXEL_SIZE = 15
BORDER_X = 10
BORDER_Y = 10
SPEED = 20

# 太大的图片按行画会很慢
with open("extra/creeper_head.json") as f:
    data: list = json.load(f)
print(data)

# 根据像素数量自动调整画布大小
max_y = len(data)
max_x = len(data[0])
canvas_size_x = max_x * PIXEL_SIZE + BORDER_X * 2
canvas_size_y = max_y * PIXEL_SIZE + BORDER_Y * 2

flag_x = 0
flag_y = 0


def setup():
    py5.size(canvas_size_x, canvas_size_y)
    py5.frame_rate(SPEED)
    py5.background(204, 204, 204)
    py5.no_stroke()


def draw():
    global flag_x, flag_y

    if flag_y >= len(data):
        flag_x = 0
        flag_y = 0
        print("finish")
        time.sleep(1)
        py5.background(204)

    py5.fill(data[flag_y][flag_x][0], data[flag_y][flag_x][1], data[flag_y][flag_x][2])
    py5.rect(BORDER_X + PIXEL_SIZE * flag_x, BORDER_Y + PIXEL_SIZE * flag_y, PIXEL_SIZE, PIXEL_SIZE)
    print(flag_x, flag_y)
    flag_x += 1
    if flag_x >= len(data):
        flag_x = 0
        flag_y += 1


if __name__ == '__main__':
    py5.run_sketch()
