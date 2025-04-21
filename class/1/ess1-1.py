import py5


def setup():
    py5.size(700, 700)
    py5.background(204, 204, 204)
    py5.no_stroke()

    # red
    py5.fill(193, 71, 97)
    py5.rect(100, 400, 500, 100)

    # green
    py5.fill(117, 179, 136)
    py5.rect(200, 100, 100, 500)

    # blue
    py5.fill(140, 193, 229)
    py5.rect(100, 200, 500, 100)

    # yellow
    py5.fill(222, 183, 98)
    py5.rect(400, 100, 100, 500)

    # cover red
    py5.fill(193, 71, 97)
    py5.rect(400, 400, 100, 100)


if __name__ == '__main__':
    py5.run_sketch()
