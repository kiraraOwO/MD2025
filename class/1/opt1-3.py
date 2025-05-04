import json
import py5


with open("3DWeb_motion.json") as f:
    path_data = json.load(f)

insert_time = []
position = []
rotation = []

for i in path_data:
    insert_time.append(i["time"])
    position.append(i["position"])
    rotation.append(i["rotation"])
# print(rotation)

scale = 25  # 坐标倍率
canvas_width = 800
canvas_height = 600
offset_x = canvas_width / 2 + 100  # 原图有点偏所以加100偏移
offset_y = canvas_height / 2

flag = 0
blk_flag = 0
angle = 0


def setup():
    global main_layer, arrow_layer
    py5.size(canvas_width, canvas_height)
    py5.background(255)
    py5.frame_rate(30)
    # 下面这个是直接画完整个轨迹
    # for i in position:
    #     py5.circle(i["x"]*scale+offset_x, i["z"]*scale+offset_y, 5)
    main_layer = py5.create_graphics(canvas_width, canvas_height)
    arrow_layer = py5.create_graphics(40, 40)



def draw():
    global flag, blk_flag, angle
    # 逻辑：需要清除掉的东西画底层，因为image后的内容都会附到主图层上
    py5.background(255)
    # 换色
    if flag % 10 < 5:
        py5.fill(0, 255, 0)
    else:
        py5.fill(255, 0, 0)
    # 写字
    py5.text_size(20)
    py5.text(insert_time[flag].split(" ")[1], 30, 30)
    py5.text("Now", position[flag]["x"] * scale + offset_x + 15, position[flag]["z"] * scale + offset_y)

    # 画轨迹
    main_layer.begin_draw()
    main_layer.no_stroke()
    # 简单除一下，每50帧画一个时间
    if flag % 50 == 0:
        main_layer.fill(255, 0, 0)
        this_time = insert_time[flag].split(" ")[1]
        main_layer.text(this_time, position[flag]["x"] * scale + offset_x + 5, position[flag]["z"] * scale + offset_y + 5)
        main_layer.stroke(255, 0, 0)
        main_layer.stroke_weight(3)
    main_layer.fill(0, 102, 153)
    main_layer.circle(position[flag]["x"] * scale + offset_x, position[flag]["z"] * scale + offset_y, 5)
    main_layer.end_draw()

    # 叠图层
    py5.image(main_layer, 0, 0)

    if flag < len(position) - 1:
        flag = flag + 1
    else:
        # 结束
        py5.text_size(50)
        if blk_flag % 10 <= 5:
            py5.fill(0, 0, 255)
        else:
            py5.fill(255, 0, 0)
        blk_flag += 1
        if blk_flag >= 10:
            blk_flag = 0
        py5.text("Over", scale + offset_x, scale + offset_y)


if __name__ == '__main__':
    py5.run_sketch()
