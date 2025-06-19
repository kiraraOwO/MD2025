import csv
import py5

now = 0
flag_autoplay = True
play_speed = 1
play_speed_tick = 0
page_of_now = "daily"  # daily, weekly, monthly
page_selector_color = 0
page_load = 0


def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def raw_csv_format(data, start_at_line=1):
    r = []
    # data = read_csv('slack_time.csv')[2:]
    data = data[start_at_line:]
    for i in range(len(data)):
        # print(data[i])
        date = data[i][0]
        # 1-11是int型， 12-17是float型， 18-30是int型
        active_premium_member = int(data[i][1])
        active_normal_member = int(data[i][2])
        active_guest = int(data[i][3])
        daily_member = int(data[i][4])
        daily_comment = int(data[i][5])
        weekly_member = int(data[i][6])
        weekly_comment = int(data[i][7])
        comment_public_channel = int(data[i][8])
        comment_private_channel = int(data[i][9])
        comment_sharing_channel = int(data[i][10])
        comment_dm = int(data[i][11])
        percent_comment_public_channel = float(data[i][12])
        percent_comment_private_channel = float(data[i][13])
        percent_comment_dm_channel = float(data[i][14])
        percent_view_public_channel = float(data[i][15])
        percent_view_private_channel = float(data[i][16])
        percent_view_dm_channel = float(data[i][17])
        count_normal_member = int(data[i][18])
        count_guest = int(data[i][19])
        count_all_member = int(data[i][20])
        req_all_normal_member = int(data[i][21])
        req_all_guest = int(data[i][22])
        req_all_member = int(data[i][23])
        upload_files = int(data[i][24])
        msg_member = int(data[i][25])
        workspace_public = int(data[i][26])
        msg_send = int(data[i][27])
        app_msg_send = int(data[i][28])
        monthly_member = int(data[i][29])
        monthly_msg_send = int(data[i][30])
        this_dict = {"date": date,
                     "active_premium_member": active_premium_member,
                     "active_normal_member": active_normal_member,
                     "active_guest": active_guest,
                     "daily_member": daily_member,
                     "daily_comment": daily_comment,
                     "weekly_member": weekly_member,
                     "weekly_comment": weekly_comment,
                     "comment_public_channel": comment_public_channel,
                     "comment_private_channel": comment_private_channel,
                     "comment_sharing_channel": comment_sharing_channel,
                     "comment_dm": comment_dm,
                     "percent_comment_public_channel": percent_comment_public_channel,
                     "percent_comment_private_channel": percent_comment_private_channel,
                     "percent_comment_dm_channel": percent_comment_dm_channel,
                     "view_public_channel": percent_view_public_channel,
                     "view_private_channel": percent_view_private_channel,
                     "view_dm_channel": percent_view_dm_channel,
                     "count_normal_member": count_normal_member,
                     "count_guest": count_guest,
                     "count_all_member": count_all_member,
                     "req_all_normal_member": req_all_normal_member,
                     "req_all_guest": req_all_guest,
                     "req_all_member": req_all_member,
                     "upload_files": upload_files,
                     "msg_member": msg_member,
                     "workspace_public": workspace_public,
                     "msg_send": msg_send,
                     "app_msg_send": app_msg_send,
                     "monthly_member": monthly_member,
                     "monthly_msg_send": monthly_msg_send}
        r.append(this_dict)
    return r


def menu_bar():
    global page_selector_color
    py5.fill("#00ffff")
    py5.no_stroke()
    py5.rect(0, 0, py5.width, 50)
    py5.fill(0)
    py5.text_size(20)
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.text("Home", 20, 25)
    py5.text_align(py5.RIGHT, py5.CENTER)
    py5.color_mode(py5.HSB, 360, 100, 100)  # 临时切换，记得切回来
    if page_of_now == "monthly":
        py5.fill(page_selector_color, 100, 100)
        py5.text("Monthly", py5.width-20, 25)
        py5.fill(0)
        py5.text("Weekly", py5.width-120, 25)
        py5.text("Daily", py5.width-215, 25)
    elif page_of_now == "weekly":
        py5.fill(page_selector_color, 100, 100)
        py5.text("Weekly", py5.width-120, 25)
        py5.fill(0)
        py5.text("Monthly", py5.width-20, 25)
        py5.text("Daily", py5.width-215, 25)
    elif page_of_now == "daily":
        py5.fill(page_selector_color, 100, 95)
        py5.text("Daily", py5.width-215, 25)
        py5.fill(0)
        py5.text("Monthly", py5.width-20, 25)
        py5.text("Weekly", py5.width-120, 25)
    page_selector_color += 1
    if page_selector_color > 360:
        page_selector_color = 0
    py5.color_mode(py5.RGB, 255)  # 切回RGB模式


def menu_bar_underline():
    # print(py5.mouse_x)
    if 5 < py5.mouse_y < 48:
        # Home
        if 15 < py5.mouse_x < 75:
            py5.stroke(0)
            py5.line(20, 40, 70, 40)
        # Monthly
        if 1107 < py5.mouse_x < 1187:
            py5.stroke(0)
            py5.line(1112, 40, 1180, 40)
        # Weekly
        if 1015 < py5.mouse_x < 1085:
            py5.stroke(0)
            py5.line(1020, 40, 1080, 40)
        # Daily
        if 938 < py5.mouse_x < 988:
            py5.stroke(0)
            py5.line(944, 40, 985, 40)


def control_bar():
    py5.fill("#ffcccc")
    py5.no_stroke()
    py5.rect(0, 50, py5.width, 50)
    py5.fill(0)
    py5.text_size(20)
    py5.text_align(py5.LEFT, py5.CENTER)
    if flag_autoplay:
        py5.text("Click to PAUSE", 865, 75)
    else:
        py5.text("Click to PLAY", 865, 75)

    py5.text("PlaySpeed: ", 1020, 75)
    py5.text_align(py5.RIGHT, py5.CENTER)
    if play_speed == 0:
        py5.text("Original", py5.width-20, 75)
    elif play_speed == 1:
        py5.text("Faster", py5.width-20, 75)
    elif play_speed == 2:
        py5.text("Normal", py5.width-20, 75)
    elif play_speed == 3:
        py5.text("Slower", py5.width-20, 75)
    else:
        py5.text("Unknown", py5.width-20, 75)


def control_bar_underline():
    if 55 < py5.mouse_y < 98:
        if 860 < py5.mouse_x < 990:
            py5.stroke(0)
            if flag_autoplay:
                py5.line(865, 90, 985, 90)
            else:
                py5.line(865, 90, 972, 90)
        if 1015 < py5.mouse_x < 1185:
            py5.stroke(0)
            py5.line(1020, 90, 1180, 90)


def footer_bar():
    py5.fill("#ccccff")
    py5.no_stroke()
    py5.rect(0, py5.height - 50, py5.width, 50)

    py5.fill(0)
    py5.text_size(20)
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.text("Date Selector", 20, py5.height - 25)

    py5.text("UP", 680, py5.height - 25)
    py5.text("DOWN", 720, py5.height - 25)
    py5.text_align(py5.RIGHT, py5.CENTER)

    py5.stroke(0)
    py5.line(165, py5.height - 50 / 2, 165 + 500, py5.height - 50 / 2)
    py5.text("Design by 2522017", py5.width - 20, py5.height - 25)
    py5.text("Powered by py5", py5.width - 220, py5.height - 25)


def footer_bar_underline():
    if 760 < py5.mouse_y < 795:
        if 675 < py5.mouse_x < 710:
            py5.stroke(0)
            py5.line(680, py5.height - 10, 705, py5.height - 10)
        if 715 < py5.mouse_x < 780:
            py5.stroke(0)
            py5.line(720, py5.height - 10, 775, py5.height - 10)


def draw_pie(x, y, data, r_size, single_data=False):
    """
    画饼图，从圆中心
    when single_data, value should between 0-1
    :param single_data:
    :param x: center x
    :param y: center y
    :param data: [{value: int, color: [r, g ,b], label: str}, ...]
    :param r_size:
    :return:
    """
    if single_data:
        total = 1
        data.append({"value": 1 - data[0]["value"], "color": [220, 220, 220], "label": ""})
    else:
        total = sum(i["value"] for i in data)
    angle = 0
    for i in data:
        slice_angle = py5.TWO_PI * (i["value"] / total)  # 当前切片比例计算
        py5.fill(i["color"][0], i["color"][1], i["color"][2])  # 设置切片颜色
        py5.no_stroke()
        py5.arc(x, y, r_size * 2, r_size * 2, angle, angle + slice_angle)  # 画圆弧
        angle += slice_angle  # 更新角度计数


def draw_label(x, y, data, single_data=False):
    """
    绘制标签，从左上角
    :param x:
    :param y:
    :param data:
    :return:
    """
    if single_data:
        data.pop(-1)
    box_size = 20
    text_offset = box_size + 10
    for i in range(len(data)):
        this_y = i * (box_size + 10) + y
        py5.fill(data[i]["color"][0], data[i]["color"][1], data[i]["color"][2])
        py5.rect(x, this_y, box_size, box_size)  # 绘制颜色方块
        py5.fill(0)
        py5.text_align(py5.LEFT, py5.CENTER)
        if single_data:
            py5.text(f"{data[i]['value']}", x + text_offset, this_y + box_size / 2)
        else:
            py5.text(f"{data[i]['label']}: {data[i]['value']}", x + text_offset, this_y + box_size / 2)


def together_to_make_a_pie(x, y, title, data, r_size, border=10, label_zone=200, single_data=False):
    """
    组合函数，绘制饼图和标签
    :param x: center x
    :param y: center y
    :param data: [{value: int, color: [r, g ,b], label: str}, ...]
    :param r_size:
    :return:
    """
    title_zone = 10  # 标题区域高度
    py5.fill(0)
    py5.text_align(py5.CENTER, py5.TOP)
    py5.text(title, x + (r_size * 2 + border * 2 + label_zone) / 2, y + border)

    py5.stroke(0)
    py5.no_fill()
    py5.rect(x, y, r_size * 2 + border * 2 + label_zone, r_size * 2 + border * 2 + (title_zone + border * 2))  # 绘制一个矩形框，作为饼图的背景

    draw_pie(x + r_size + border, y + r_size + border + (title_zone + border * 2), data, r_size, single_data)
    draw_label(x + r_size * 2 + border * 2, y + border + (title_zone + border * 2), data, single_data)


def draw_arrow(x, y, direction="up", size=10):
    py5.no_stroke()
    if direction == "up":
        py5.fill(255, 0, 0)
        py5.triangle(x, y - size, x - size / 2, y + size / 2, x + size / 2, y + size / 2)
    elif direction == "down":
        py5.fill(0, 255, 0)
        py5.triangle(x, y + size, x - size / 2, y - size / 2, x + size / 2, y - size / 2)
    else:
        py5.stroke(0, 0, 255)
        py5.stroke_weight(3)
        py5.line(x-5, y, x + 5, y)
        py5.stroke(0)
        py5.stroke_weight(1)
    py5.fill(0)


def date_selector():
    # not in use
    offset = 70
    py5.fill(200)
    py5.stroke(0)
    py5.rect(py5.width/2-300/2, py5.height/2-150/2-offset, 300, 150)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(20)
    py5.fill(0)
    py5.text("Date Selector", py5.width/2, py5.height/2 - 50 - offset)
    # mouth
    py5.text("11", py5.width/2, py5.height/2 + 5 - offset)


def data_selector_4_daily():
    py5.no_stroke()
    py5.fill(255)
    now_x = py5.remap(now, 0, len(formatted_data), 165, 165 + 500)
    py5.circle(now_x, py5.height - 50/2, 20)


def data_selector_4_weekly():
    py5.no_stroke()
    py5.fill(255)
    now_x = py5.remap(now, 0, len(formatted_data), 165, 165 + 500)
    py5.circle(now_x, py5.height - 50/2, 20)
    now_x_after_7 = py5.remap(now+7, 0, len(formatted_data), 165, 165 + 500)
    py5.circle(now_x_after_7, py5.height - 50 / 2, 20)
    py5.rect(now_x, py5.height - 50 / 2 - 10, now_x_after_7 - now_x, 20)


def page_daily():
    py5.fill(0)
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.text(f"{formatted_data[now]['date']} {now}/{len(formatted_data) - 1}", 20, 75)

    d1 = [
        {"value": formatted_data[now]['active_premium_member'], "color": [113, 181, 220], "label": "Premium"},
        {"value": formatted_data[now]['active_normal_member'], "color": [166, 222, 107], "label": "Normal"},
        {"value": formatted_data[now]['active_guest'], "color": [197, 95, 217], "label": "Guest"}
    ]
    d2 = [
        {"value": formatted_data[now]['daily_member'], "color": [255, 100, 100], "label": "Member"},
        {"value": formatted_data[now]['daily_comment'], "color": [100, 255, 100], "label": "Comment"}
    ]
    d3 = [
        {"value": formatted_data[now]['comment_public_channel'], "color": [255, 180, 50], "label": "Public Channel"},
        {"value": formatted_data[now]['comment_private_channel'], "color": [150, 200, 255], "label": "Private Channel"},
        {"value": formatted_data[now]['comment_sharing_channel'], "color": [180, 100, 255], "label": "Sharing Channel"},
        {"value": formatted_data[now]['comment_dm'], "color": [100, 150, 200], "label": "DM"}
    ]

    lbz = 210
    bd = 10
    rs = 70
    offset = 20
    next_ = bd * 2 + rs * 2 + lbz + offset
    # for i in range(3):
    #     together_to_make_a_pie(50+i*next, 100, d, rs)
    together_to_make_a_pie(25, 125, "Users", d1, r_size=rs, border=bd, label_zone=lbz)
    together_to_make_a_pie(25 + next_, 125, "Daily of", d2, r_size=rs, border=bd, label_zone=lbz)
    together_to_make_a_pie(25 + next_ * 2, 125, "Comment", d3, r_size=rs, border=bd, label_zone=lbz)

    d4_1 = [
        {"value": formatted_data[now]['percent_comment_public_channel'], "color": [255, 100, 100], "label": "Public Channel"}
    ]
    d4_2 = [
        {"value": formatted_data[now]['percent_comment_private_channel'], "color": [150, 200, 255], "label": "Private Channel"}
    ]
    d4_3 = [
        {"value": formatted_data[now]['percent_comment_dm_channel'], "color": [180, 100, 255], "label": "DM"}
    ]

    py5.fill(0)
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.text("Percent of channel_comment", 25, 345)

    lbz = 95
    bd = 10
    rs = 30
    offset = 20
    next_ = bd * 2 + rs * 2 + lbz + offset
    together_to_make_a_pie(25, 370, "public", d4_1, r_size=rs, border=bd, label_zone=lbz, single_data=True)
    together_to_make_a_pie(25 + next_, 370, "private", d4_2, r_size=rs, border=bd, label_zone=lbz, single_data=True)
    together_to_make_a_pie(25 + next_ * 2, 370, "dm", d4_3, r_size=rs, border=bd, label_zone=lbz, single_data=True)

    d5_1 = [
        {"value": formatted_data[now]['view_public_channel'], "color": [207, 83, 57], "label": "Public Channel"}
    ]
    d5_2 = [
        {"value": formatted_data[now]['view_private_channel'], "color": [221, 205, 80], "label": "Private Channel"}
    ]
    d5_3 = [
        {"value": formatted_data[now]['view_dm_channel'], "color": [131, 87, 76], "label": "DM"}
    ]

    py5.text("Percent of channel_view", 610, 345)

    together_to_make_a_pie(25 + next_ * 3, 370, "public", d5_1, r_size=rs, border=bd, label_zone=lbz, single_data=True)
    together_to_make_a_pie(25 + next_ * 4, 370, "private", d5_2, r_size=rs, border=bd, label_zone=lbz, single_data=True)
    together_to_make_a_pie(25 + next_ * 5, 370, "dm", d5_3, r_size=rs, border=bd, label_zone=lbz, single_data=True)

    py5.text("Count of Member", 25, 510)
    py5.text("Requests of Member", 320, 510)

    py5.stroke(0)
    py5.no_fill()
    py5.rect(25, 535, 270, 120)
    py5.rect(320, 535, 270, 120)
    py5.line(50, 610, 270, 610)
    py5.line(340, 610, 570, 610)

    py5.no_stroke()
    py5.fill(0)
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.text("Normal", 50, 560)
    py5.text(formatted_data[now]['count_normal_member'], 190, 560)
    py5.text("Guest", 50, 590)
    py5.text(formatted_data[now]['count_guest'], 190, 590)
    py5.text("ALL Member", 50, 630)
    py5.text(formatted_data[now]['count_all_member'], 190, 630)
    try:
        if formatted_data[now-1]['count_normal_member'] < formatted_data[now]['count_normal_member']:
            draw_arrow(250, 560, "up", 10)
        elif formatted_data[now-1]['count_normal_member'] > formatted_data[now]['count_normal_member']:
            draw_arrow(250, 560, "down", 10)
        else:
            draw_arrow(250, 560, "middle", 10)

        if formatted_data[now-1]['count_guest'] < formatted_data[now]['count_guest']:
            draw_arrow(250, 590, "up", 10)
        elif formatted_data[now-1]['count_guest'] > formatted_data[now]['count_guest']:
            draw_arrow(250, 590, "down", 10)
        else:
            draw_arrow(250, 590, "middle", 10)

        if formatted_data[now-1]['count_all_member'] < formatted_data[now]['count_all_member']:
            draw_arrow(250, 630, "up", 10)
        elif formatted_data[now-1]['count_all_member'] > formatted_data[now]['count_all_member']:
            draw_arrow(250, 630, "down", 10)
        else:
            draw_arrow(250, 630, "middle", 10)
    except IndexError:
        pass

    py5.text("Normal", 340, 560)
    py5.text(formatted_data[now]['req_all_normal_member'], 490, 560)
    py5.text("Guest", 340, 590)
    py5.text(formatted_data[now]['req_all_guest'], 490, 590)
    py5.text("ALL Member", 340, 630)
    py5.text(formatted_data[now]['req_all_member'], 490, 630)
    try:
        if formatted_data[now-1]['req_all_normal_member'] < formatted_data[now]['req_all_normal_member']:
            draw_arrow(550, 560, "up", 10)
        elif formatted_data[now-1]['req_all_normal_member'] > formatted_data[now]['req_all_normal_member']:
            draw_arrow(550, 560, "down", 10)
        else:
            draw_arrow(550, 560, "middle", 10)

        if formatted_data[now-1]['req_all_guest'] < formatted_data[now]['req_all_guest']:
            draw_arrow(550, 590, "up", 10)
        elif formatted_data[now-1]['req_all_guest'] > formatted_data[now]['req_all_guest']:
            draw_arrow(550, 590, "down", 10)
        else:
            draw_arrow(550, 590, "middle", 10)

        if formatted_data[now-1]['req_all_member'] < formatted_data[now]['req_all_member']:
            draw_arrow(550, 630, "up", 10)
        elif formatted_data[now-1]['req_all_member'] > formatted_data[now]['req_all_member']:
            draw_arrow(550, 630, "down", 10)
        else:
            draw_arrow(550, 630, "middle", 10)
    except IndexError:
        pass

    py5.no_fill()
    py5.stroke(0)
    py5.rect(25, 675, 270, 55)
    py5.rect(320, 675, 270, 55)
    py5.text("Upload Files", 50, 700)
    py5.text("Workspace", 340, 700)
    py5.text(formatted_data[now]['upload_files'], 190, 700)
    py5.text(formatted_data[now]['workspace_public'], 490, 700)
    try:
        if formatted_data[now-1]['upload_files'] < formatted_data[now]['upload_files']:
            draw_arrow(250, 700, "up", 10)
        elif formatted_data[now-1]['upload_files'] > formatted_data[now]['upload_files']:
            draw_arrow(250, 700, "down", 10)
        else:
            draw_arrow(250, 700, "middle", 10)

        if formatted_data[now-1]['workspace_public'] < formatted_data[now]['workspace_public']:
            draw_arrow(550, 700, "up", 10)
        elif formatted_data[now-1]['workspace_public'] > formatted_data[now]['workspace_public']:
            draw_arrow(550, 700, "down", 10)
        else:
            draw_arrow(550, 700, "middle", 10)
    except IndexError:
        pass

    py5.no_fill()
    py5.stroke(0)
    py5.rect(610, 535, 565, 195)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text("No data", 610 + 565 / 2, 535 + 195 / 2)


def draw_week_l3(start_x=20, y_offset=0, data_key=[], label=[]):
    """
    :param start_x:
    :param y_offset: need -120
    :param data_key: len == 3
    :param label: len == 3
    :return:
    """
    py5.no_fill()
    py5.stroke(0)
    py5.rect(start_x, 120 + y_offset, 560, 200)
    py5.line(start_x + 20, 220 + y_offset, start_x + 60, 220 + y_offset)

    left_text_start_x = start_x + 40
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.fill(0)
    py5.text("max", left_text_start_x, 145 + y_offset)
    py5.text("min", left_text_start_x, 295 + y_offset)

    # x -> 130-555, y -> 145-295
    max_1 = max(formatted_data[now + all_][data_key[0]] for all_ in range(7))
    max_2 = max(formatted_data[now + all_][data_key[1]] for all_ in range(7))
    max_3 = max(formatted_data[now + all_][data_key[2]] for all_ in range(7))
    min_1 = min(formatted_data[now + all_][data_key[0]] for all_ in range(7))
    min_2 = min(formatted_data[now + all_][data_key[1]] for all_ in range(7))
    min_3 = min(formatted_data[now + all_][data_key[2]] for all_ in range(7))

    box_size = 20
    box_start_x = start_x + 430
    py5.no_stroke()
    py5.fill(113, 181, 220)
    py5.text(f"{max_1}", left_text_start_x, 165 + y_offset)
    py5.text(f"{min_1}", left_text_start_x, 275 + y_offset)
    py5.rect(box_start_x, 160 + y_offset, box_size, box_size)
    py5.fill(166, 222, 107)
    py5.text(f"{max_2}", left_text_start_x, 185 + y_offset)
    py5.text(f"{min_2}", left_text_start_x, 255 + y_offset)
    py5.rect(box_start_x, 210 + y_offset, box_size, box_size)
    py5.fill(197, 95, 217)
    py5.text(f"{max_3}", left_text_start_x, 205 + y_offset)
    py5.text(f"{min_3}", left_text_start_x, 235 + y_offset)
    py5.rect(box_start_x, 260 + y_offset, box_size, box_size)

    label_text_start_x = box_start_x + 30
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.fill(0)
    py5.text(label[0], label_text_start_x, 170 + y_offset)
    py5.text(label[1], label_text_start_x, 220 + y_offset)
    py5.text(label[2], label_text_start_x, 270 + y_offset)

    point_y_1 = []
    point_y_2 = []
    point_y_3 = []
    for i in range(7):
        point_y_1.append(py5.remap(formatted_data[now + i][data_key[0]], min_1 - 1, max_1 + 1, 145, 295))
        point_y_2.append(py5.remap(formatted_data[now + i][data_key[1]], min_2 - 1, max_2 + 1, 145, 295))
        point_y_3.append(py5.remap(formatted_data[now + i][data_key[2]], min_3 - 1, max_3 + 1, 145, 295))
    offset_x = 50
    point_start_x = start_x + 95
    for j in range(7):
        py5.no_stroke()
        py5.fill(113, 181, 220)
        py5.ellipse(point_start_x + offset_x * j, point_y_1[j] + y_offset, 10, 10)
        try:
            py5.stroke(113, 181, 220)
            py5.line(point_start_x + offset_x * j, point_y_1[j] + y_offset, point_start_x + offset_x * (j+1), point_y_1[j+1] + y_offset)
        except IndexError:
            pass
        py5.no_stroke()
        py5.fill(166, 222, 107)
        py5.ellipse(point_start_x + offset_x * j, point_y_2[j] + y_offset, 10, 10)
        try:
            py5.stroke(166, 222, 107)
            py5.line(point_start_x + offset_x * j, point_y_2[j] + y_offset, point_start_x + offset_x * (j+1), point_y_2[j+1] + y_offset)
        except IndexError:
            pass
        py5.no_stroke()
        py5.fill(197, 95, 217)
        py5.ellipse(point_start_x + offset_x * j, point_y_3[j] + y_offset, 10, 10)
        try:
            py5.stroke(197, 95, 217)
            py5.line(point_start_x + offset_x * j, point_y_3[j] + y_offset, point_start_x + offset_x * (j+1), point_y_3[j+1] + y_offset)
        except IndexError:
            pass
        py5.no_stroke()


def draw_week_l2(start_x=20, y_offset=0, data_key=[], label=[]):
    """
    :param start_x:
    :param y_offset: need -120
    :param data_key: len == 2
    :param label: len == 2
    :return:
    """
    py5.no_fill()
    py5.stroke(0)
    py5.rect(start_x, 120 + y_offset, 560, 160)
    py5.line(start_x + 20, 200 + y_offset, start_x + 60, 200 + y_offset)

    left_text_start_x = start_x + 40
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.fill(0)
    py5.text("max", left_text_start_x, 145 + y_offset)
    py5.text("min", left_text_start_x, 255 + y_offset)

    max_1 = max(formatted_data[now + all_][data_key[0]] for all_ in range(7))
    max_2 = max(formatted_data[now + all_][data_key[1]] for all_ in range(7))
    min_1 = min(formatted_data[now + all_][data_key[0]] for all_ in range(7))
    min_2 = min(formatted_data[now + all_][data_key[1]] for all_ in range(7))

    box_size = 20
    box_start_x = start_x + 430
    py5.no_stroke()
    py5.fill(255, 100, 100)
    py5.text(f"{max_1}", left_text_start_x, 165 + y_offset)
    py5.text(f"{min_1}", left_text_start_x, 235 + y_offset)
    py5.rect(box_start_x, 165 + y_offset, box_size, box_size)
    py5.fill(100, 255, 100)
    py5.text(f"{max_2}", left_text_start_x, 185 + y_offset)
    py5.text(f"{min_2}", left_text_start_x, 215 + y_offset)
    py5.rect(box_start_x, 215 + y_offset, box_size, box_size)

    label_text_start_x = box_start_x + 30
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.fill(0)
    py5.text(label[0], label_text_start_x, 175 + y_offset)
    py5.text(label[1], label_text_start_x, 225 + y_offset)

    point_y_1 = []
    point_y_2 = []
    for i in range(7):
        point_y_1.append(py5.remap(formatted_data[now + i][data_key[0]], min_1 - 1, max_1 + 1, 145, 255))
        point_y_2.append(py5.remap(formatted_data[now + i][data_key[1]], min_2 - 1, max_2 + 1, 145, 255))
    offset_x = 50
    point_start_x = start_x + 95
    for j in range(7):
        py5.no_stroke()
        py5.fill(255, 100, 100)
        py5.ellipse(point_start_x + offset_x * j, point_y_1[j] + y_offset, 10, 10)
        try:
            py5.stroke(255, 100, 100)
            py5.line(point_start_x + offset_x * j, point_y_1[j] + y_offset, point_start_x + offset_x * (j+1), point_y_1[j+1] + y_offset)
        except IndexError:
            pass
        py5.no_stroke()
        py5.fill(100, 255, 100)
        py5.ellipse(point_start_x + offset_x * j, point_y_2[j] + y_offset, 10, 10)
        try:
            py5.stroke(100, 255, 100)
            py5.line(point_start_x + offset_x * j, point_y_2[j] + y_offset, point_start_x + offset_x * (j+1), point_y_2[j+1] + y_offset)
        except IndexError:
            pass


def draw_week_l1(start_x=20, y_offset=0, data_key=[], label=[]):
    """
    :param start_x:
    :param y_offset: need -120
    :param data_key: len == 1
    :param label: len == 1
    :return:
    """
    py5.no_fill()
    py5.stroke(0)
    py5.rect(start_x, 120 + y_offset, 560, 120)
    py5.line(start_x + 20, 180 + y_offset, start_x + 60, 180 + y_offset)

    left_text_start_x = start_x + 40
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.fill(0)
    py5.text("max", left_text_start_x, 145 + y_offset)
    py5.text("min", left_text_start_x, 215 + y_offset)

    max_1 = max(formatted_data[now + all_][data_key[0]] for all_ in range(7))
    min_1 = min(formatted_data[now + all_][data_key[0]] for all_ in range(7))

    box_size = 20
    box_start_x = start_x + 430
    py5.no_stroke()
    py5.fill(255, 180, 50)
    py5.text(f"{max_1}", left_text_start_x, 165 + y_offset)
    py5.text(f"{min_1}", left_text_start_x, 195 + y_offset)
    py5.rect(box_start_x, 170 + y_offset, box_size, box_size)

    label_text_start_x = box_start_x + 30
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.fill(0)
    py5.text(label[0], label_text_start_x, 180 + y_offset)

    point_y_1 = []
    for i in range(7):
        point_y_1.append(py5.remap(formatted_data[now + i][data_key[0]], min_1 - 1, max_1 + 1, 145, 215))
    offset_x = 50
    point_start_x = start_x + 95
    for j in range(7):
        py5.no_stroke()
        py5.fill(255, 180, 50)
        py5.ellipse(point_start_x + offset_x * j, point_y_1[j] + y_offset, 10, 10)
        try:
            py5.stroke(255, 180, 50)
            py5.line(point_start_x + offset_x * j, point_y_1[j] + y_offset, point_start_x + offset_x * (j+1), point_y_1[j+1] + y_offset)
        except IndexError:
            pass


def page_weekly():
    global now
    if now + 7 >= len(formatted_data):
        now = 0

    py5.fill(0)
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.text(f"START:{formatted_data[now]['date']} END:{formatted_data[now+6]['date']} {now}-{now+6}/{len(formatted_data) - 1}", 20, 75)

    py5.text("Active Member", 20, 125)
    py5.text("Channel Comment", 20+600, 125)
    draw_week_l3(start_x=20, y_offset=30, data_key=["active_premium_member", "active_normal_member", "active_guest"], label=["Premium", "Normal", "Guest"])
    draw_week_l3(start_x=20+600, y_offset=30, data_key=["comment_public_channel", "comment_private_channel", "comment_sharing_channel"], label=["Public", "Private", "Sharing"])
    py5.fill(0)
    py5.text("Daily", 20, 375)
    py5.text("Send Messages", 20+600, 375)
    draw_week_l2(start_x=20, y_offset=395-120, data_key=["daily_member", "daily_comment"], label=["Member", "Comment"])
    draw_week_l2(start_x=20+600, y_offset=395-120, data_key=["msg_send", "app_msg_send"], label=["Web", "App"])
    py5.fill(0)
    py5.text("Upload files", 20, 580)
    py5.text("Workspace", 20+600, 580)
    draw_week_l1(start_x=20, y_offset=600-120, data_key=["upload_files"], label=["Files"])
    draw_week_l1(start_x=20+600, y_offset=600-120, data_key=["workspace_public"], label=["Public"])


def page_monthly():
    global page_load
    py5.fill(0)
    py5.text_align(py5.LEFT, py5.CENTER)
    py5.text("Monthly data is not available yet.", 20, 75)

    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(30)
    if 0 <= page_load < 10:
        py5.text("Loading...-", py5.width/2, py5.height/2)
    elif 10 <= page_load < 20:
        py5.text("Loading...\\", py5.width/2, py5.height/2)
    elif 20 <= page_load < 30:
        py5.text("Loading...|", py5.width/2, py5.height/2)
    elif 30 <= page_load < 40:
        py5.text("Loading.../", py5.width/2, py5.height/2)
    py5.text_size(12)
    page_load += 1
    if page_load >= 40:
        page_load = 0


def setup():
    global formatted_data
    py5.size(1200, 800)
    py5.window_title("Tichu")
    py5.background(255)
    formatted_data = raw_csv_format(read_csv('slack_time.csv'), 2)


def draw():
    global formatted_data, now, play_speed_tick, flag_autoplay
    print(f"x: {py5.mouse_x}, y: {py5.mouse_y}")
    py5.background(255)
    menu_bar()
    menu_bar_underline()
    control_bar()
    control_bar_underline()
    footer_bar()
    footer_bar_underline()
    if page_of_now == "daily":
        page_daily()
        data_selector_4_daily()
    elif page_of_now == "weekly":
        page_weekly()
        data_selector_4_weekly()
    elif page_of_now == "monthly":
        page_monthly()

    if flag_autoplay:
        play_speed_tick += 1
        if play_speed == 0:
            play_speed_tick = 0
            now += 1
        elif play_speed == 1:
            if play_speed_tick > 5:
                play_speed_tick = 0
                now += 1
        elif play_speed == 2:
            if play_speed_tick > 15:
                play_speed_tick = 0
                now += 1
        elif play_speed == 3:
            if play_speed_tick > 30:
                play_speed_tick = 0
                now += 1
    else:
        pass

    if py5.is_mouse_pressed:
        if 760 < py5.mouse_y < 795:
            if 165 < py5.mouse_x < 665:
                flag_autoplay = False
                if page_of_now == "daily":
                    now = int(py5.remap(py5.mouse_x, 165, 665, 0, len(formatted_data) - 1))
                elif page_of_now == "weekly":
                    now = int(py5.remap(py5.mouse_x, 165, 665, 0, len(formatted_data) - 7))

    if now >= len(formatted_data):
        now = 0


def mouse_pressed():
    global flag_autoplay, play_speed, now, page_of_now
    if 5 < py5.mouse_y < 48:
        # now = 0
        # Monthly
        if 1107 < py5.mouse_x < 1187:
            page_of_now = "monthly"
        # Weekly
        if 1015 < py5.mouse_x < 1085:
            page_of_now = "weekly"
        # Daily
        if 938 < py5.mouse_x < 988:
            page_of_now = "daily"

    if 55 < py5.mouse_y < 98:
        if 860 < py5.mouse_x < 990:
            flag_autoplay = not flag_autoplay
        if 1015 < py5.mouse_x < 1185:
            play_speed += 1
            if play_speed > 3:
                play_speed = 0

    if 760 < py5.mouse_y < 795:
        if 675 < py5.mouse_x < 710:
            flag_autoplay = False
            now += 1
        if 715 < py5.mouse_x < 780:
            flag_autoplay = False
            now -= 1
        if now < 0:
            now = 0
        if now >= len(formatted_data):
            now = len(formatted_data) - 1


if __name__ == '__main__':
    py5.run_sketch()
