import py5
import random

PLAY_SPEED = 20

y_list = []
text_size = 20
offset = 20
flag = True


def setup():
    py5.size(400, 600)
    py5.background(0)
    py5.text_size(text_size)
    py5.frame_rate(PLAY_SPEED)
    for i in range(py5.width // text_size):
        y_list.append(random.randint(-100, 0))


def draw():
    py5.background(0)
    for i in range(len(y_list)):
        x = i * text_size
        y = y_list[i] * text_size
        for j in range(5):
            if flag:
                py5.fill(0, 255, 70, 255/(5-j))
            else:
                py5.fill(255, 0, 70, 255/(5-j))
            py5.text(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'), x, y+offset*j)
        if y > py5.height and random.random() > 0.975:
            y_list[i] = -10
        else:
            y_list[i] += 1
    # print("Debug:", y_list)


def mouse_pressed():
    global flag
    flag = not flag


if __name__ == '__main__':
    py5.run_sketch()
