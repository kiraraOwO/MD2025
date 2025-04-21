import json
import py5

with open("extra/creeper_head.json") as f:
    data: list = json.load(f)
print(data)


def setup():
    py5.size(100, 100)
    py5.no_stroke()
    x_start_at = 10
    y_start_at = 10
    # py5.rect(start_X, start_Y, width, height)
    for y in range(len(data)):
        for x in range(len(data[y])):
            print(x, y, data[y][x])
            py5.fill(data[y][x][0], data[y][x][1], data[y][x][2])
            py5.rect(x_start_at * (x + 1), y_start_at * (y + 1), 10, 10)


if __name__ == '__main__':
    py5.run_sketch()
