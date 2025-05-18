import py5

W, H = 600, 400
TOTAL_CIRCLES = 100

data = []
'''
[ [x,y], [dx, dy], [h, s, b], [size, change_speed] ]
    x : x坐标 1~width-1
    y : y坐标 1~height-1
    dx : x方向速度 random 1~-1  not 0
    dy : y方向速度 random 1~-1  not 0
    h : 颜色hue 0-360  0 ok
    s : 颜色saturation 50-100
    b : 亮度brightness 50-100
    size : 圆形初始大小 10-30  not 0
    change_speed : 圆形大小变化速度 -0.1~0.1  not 0
'''


def rd(start, end, type_, is_0_ok=False):
    """
    is_0_ok : 是否允许0

    is_0_ok=True, 允许0; is_0_ok=False, 不允许0
    """
    while True:
        if type_ == 'int':
            r = py5.random_int(start, end)
        elif type_ == 'float':
            r = py5.random(start, end)
        else:
            raise ValueError("type_ must be 'int' or 'float'")
        if not is_0_ok:
            if r != 0:
                return r
        else:
            return r


def setup():
    py5.size(W, H)
    py5.no_stroke()
    py5.color_mode(py5.HSB, 360, 100, 100)
    py5.frame_rate(60)
    # for i in range(TOTAL_CIRCLES):
    #     x = py5.random_int(1, py5.width - 1)
    #     y = py5.random_int(1, py5.height - 1)
    #     dx = py5.random(-1, 1)
    #     dy = py5.random(-1, 1)
    #     h = py5.random_int(0, 360)
    #     s = py5.random_int(50, 100)
    #     b = py5.random_int(50, 100)
    #     size = py5.random_int(0, 30)
    #     change_speed = py5.random(-0.1, 0.1)
    #     data.append([[x, y], [dx, dy], [h, s, b], [size, change_speed]])
    for i in range(TOTAL_CIRCLES):
        x = rd(1, py5.width - 1, 'int')
        y = rd(1, py5.height - 1, 'int')
        dx = rd(-1, 1, 'float')
        dy = rd(-1, 1, 'float')
        h = rd(0, 360, 'int', True)
        s = rd(50, 100, 'int')
        b = rd(50, 100, 'int')
        size = rd(10, 30, 'float')
        change_speed = rd(-0.1, 0.1, 'float')
        data.append([[x, y], [dx, dy], [h, s, b], [size, change_speed]])


def draw():
    py5.background(0)
    for i in range(TOTAL_CIRCLES):
        circle = data[i]
        x, y = circle[0]
        dx, dy = circle[1]
        h, s, b = circle[2]
        size, change_speed = circle[3]

        x += dx
        y += dy

        if size < 0:
            change_speed *= -1
        if size > 30:
            change_speed *= -1
        size += change_speed

        if x > py5.width - 1 or x < 1:
            dx *= -1
        if y > py5.height - 1 or y < 1:
            dy *= -1

        data[i] = [[x, y], [dx, dy], [h, s, b], [size, change_speed]]

        py5.fill(h, s, b)
        py5.circle(x, y, size)


if __name__ == '__main__':
    py5.run_sketch()
