import py5
import random

PLAY_SPEED = 25  # recommend 15-25
TEXT_LENS = 10  # recommend 5-10
OFFSET = 0

y_list = []
text_size = 20
flag = True
lock = False
locked_x = 0
special_list = [["p", "P"], ["a", "A", "@"], ["s", "S", "$"], ["s", "S", "$"], ["w", "W"], ["d", "D"]]
special_list2 = [["h", "H", "#"], ["a", "A", "@"], ["c", "C", "("], ["k", "K"], ["e", "E", "3"], ["r", "R"]]


def setup():
    py5.size(600, 800)
    py5.color_mode(py5.HSB, 360, 100, 100)
    py5.background(0, 0, 0)
    py5.text_size(text_size)
    py5.frame_rate(PLAY_SPEED)
    for i in range(py5.width // text_size):
        y_list.append(random.randint(-100, 0))


def draw():
    global lock, locked_x
    py5.background(0, 0, 0)

    py5.fill(0, 100, 100, 255)
    py5.text(''.join(random.choice(chars) for chars in special_list2), py5.mouse_x, py5.mouse_y)
    if random.random() > 0.975:
        py5.text("press to pause", random.randint(1, int(py5.width/2)), py5.height-text_size)
    else:
        py5.text("press to pause", 5, py5.height-text_size)

    for i in range(len(y_list)):
        x = i * text_size
        y = y_list[i] * text_size
        if random.random() > 0.975 and lock == False and y < 0:
            lock = True
            locked_x = x
            # x是在列表里的位置，y是在锁定时的位置
            print(f"Locked at {locked_x/text_size}, {y/text_size}")
        if lock and x == locked_x:
            for j in range(len(special_list)):
                py5.fill(0, 100, 100, 255)
                # t = random.choice(special_list[j])
                t = random.choice(special_list[len(special_list) - 1 - j])
                py5.text(t, x, y + (text_size + OFFSET) * j)

        else:
            for j in range(TEXT_LENS):
                alpha = 255 * j / TEXT_LENS
                if flag:
                    py5.fill(120, 100, 100, alpha)
                else:
                    # 加了暂停后这一步其实是没用的
                    py5.fill(0, 100, 100, alpha)
                py5.text(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'), x, y + (text_size + OFFSET) * j)

        if y > py5.height and random.random() > 0.975:
            if x == locked_x:
                print(f"Unlocked at {locked_x/text_size}, {y/text_size}")
                lock = False
                locked_x = 0
            y_list[i] = -20
        else:
            y_list[i] += 1
    # print("Debug:", y_list)


def mouse_pressed():
    global flag
    flag = not flag
    if not flag:
        text_size_temp = text_size
        py5.text_size(100)
        py5.fill(0, 100, 100, 255)
        py5.text("Paused", py5.width / 4, py5.height / 2)
        py5.text_size(text_size_temp)
        py5.no_loop()
    else:
        py5.loop()


if __name__ == '__main__':
    py5.run_sketch()
