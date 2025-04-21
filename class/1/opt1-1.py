import py5

# 起点x，起点y，长，宽

def setup():
    py5.size(700, 700)
    py5.background(204, 204, 204)
    py5.no_stroke()

    angle = py5.radians(45)
    py5.translate(350, -150)
    py5.rotate(angle)

    # red
    py5.fill(193, 71, 97)
    py5.rect(150, 400, 400, 100)
    py5.ellipse(150, 450, 100, 100)
    py5.ellipse(550, 450, 100, 100)

    # green
    py5.fill(117, 179, 136)
    py5.rect(200, 150, 100, 400)
    py5.ellipse(250, 150, 100, 100)
    py5.ellipse(250, 550, 100, 100)

    # blue
    py5.fill(140, 193, 229)
    py5.rect(150, 200, 400, 100)
    py5.ellipse(150, 250, 100, 100)
    py5.ellipse(550, 250, 100, 100)

    # yellow
    py5.fill(222, 183, 98)
    py5.rect(400, 150, 100, 400)
    py5.ellipse(450, 150, 100, 100)
    py5.ellipse(450, 550, 100, 100)

    # cover red
    py5.fill(193, 71, 97)
    py5.rect(400, 400, 100, 100)


if __name__ == '__main__':
    py5.run_sketch()
