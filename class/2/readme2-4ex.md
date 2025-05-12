# 4

締切に間に合わないかもしれないと思って、自分で作ったプログラムの説明を書きました。

これはグループで話し合った最終的な結果ではないかもしれません。

[Video Recording ( Google Drive )](https://drive.google.com/file/d/1AQgchidfjt_0ok0zV1XX-rPh2Pv9X1M1/view?usp=drive_link)

```python
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
    py5.size(600, 300)
    py5.color_mode(py5.HSB, 360, 100, 100)
    py5.background(0, 0, 0)
    py5.text_size(text_size)
    py5.frame_rate(PLAY_SPEED)
    for i in range(py5.width // text_size):
        y_list.append(random.randint(-100, 0))

def draw():
    global lock, locked_x
    py5.background(0, 0, 0)
		#  part 1
    py5.fill(0, 100, 100, 255)
    py5.text(''.join(random.choice(chars) for chars in special_list2), py5.mouse_x, py5.mouse_y)
    #  part 1 end
    #  part 2
    if random.random() > 0.975:
        py5.text("press to pause", random.randint(1, int(py5.width/2)), py5.height-text_size)
    else:
        py5.text("press to pause", 5, py5.height-text_size)
		#  part 2 end
		#  part 3
    for i in range(len(y_list)):
		    #  part 3.1
        x = i * text_size
        y = y_list[i] * text_size
        #  part 3.1 end
        #  part 3.2
        if random.random() > 0.975 and lock == False and y < 0:
            lock = True
            locked_x = x
            # x是在列表里的位置，y是在锁定时的位置
            print(f"Locked at {locked_x/text_size}, {y/text_size}")
        #  part 3.2 half
        if lock and x == locked_x:
            for j in range(len(special_list)):
                py5.fill(0, 100, 100, 255)
                # t = random.choice(special_list[j])
                t = random.choice(special_list[len(special_list) - 1 - j])
                py5.text(t, x, y + (text_size + OFFSET) * j)
				#  part 3.2 end
				#  part 3.3
        else:
            for j in range(TEXT_LENS):
                alpha = 255 * j / TEXT_LENS
                if flag:
                    py5.fill(120, 100, 100, alpha)
                else:
                    # 加了暂停后这一步其实是没用的
                    py5.fill(0, 100, 100, alpha)
                py5.text(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'), x, y + (text_size + OFFSET) * j)
				#  part 3.3 end
				#  part 3.4
        if y > py5.height and random.random() > 0.975:
            if x == locked_x:
                print(f"Unlocked at {locked_x/text_size}, {y/text_size}")
                lock = False
                locked_x = 0
            y_list[i] = -20
        else:
            y_list[i] += 1
        #  part 3.4 end
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
```

[Github Raw File Link](https://github.com/kiraraOwO/MD2025/raw/refs/heads/main/class/2/ess2-4_EX.py)

これはコードレインのプログラムです。

最初にパッケージをインポートします。

その後、いくつかのグローバル変数を設定します。最初の2つはユーザーがカスタマイズできます。

- PLAY_SPEED：再生速度。実際にはプログラム内ではフレームレートです。
- TEXT_LENS：1行のコードレインの長さ。
- OFFSET：文字間のオフセット。大きくしすぎると別のものになります。

以下の変数はカスタマイズできません：

- y_list：文字サイズとウィンドウサイズに基づいて、重ならないように各列のY座標をランダムに格納するためのリスト。
- text_size：コードレインの文字サイズ。変更は推奨されません。見た目が悪くなります。
- flag：再生・一時停止状態の切り替え判断。
- lock：特殊配列が場に存在するかどうかを判断し、重複を防止します。
- locked_x：ロックされた列の位置（座標）を記録します。
- special_list：特殊文字リスト1。
- special_list2：特殊文字リスト2。

---

## setup関数

まず、py5の設定を行います。例えばキャンバスサイズ、カラーモード、初期背景、フォントサイズ、フレームレートなどを設定します。

このプログラムではremap関数による色変換を使用していないため、カラーモードの変更は実質的な意味はありません。

最後のforループでは、フォントサイズに基づいてキャンバスを分割し、コードレインの文字が重ならないようにし、各列に -100〜0 の初期位置を設定します。

---

## draw関数

まず、`lock`と`locked_x`はグローバル変数なので、関数内で変更するには先に`global`でグローバルとして明示する必要があります。そうでないと読み取り専用になります。

次に画面をリフレッシュします。`draw`関数が実行されるたびにキャンバスをクリアします。

### part 1

マウス座標上に特殊な文字列を生成するための部分です。

まずは空文字列を用意し、`join`を使って後続の内容を挿入します。

`random.choice`とforループを使用して、特殊文字リスト内の各サブリストから1つずつ文字を選び、先ほどの空文字列に挿入します。この書き方はシンタックスシュガーで、少し読みづらいかもしれません。

最後に、この文字列をマウス座標上に表示します。

### part 2

これはユーザーに画面をクリックして一時停止できることを伝えるためのメッセージです。

`random`は、この文字列がランダムに揺れるようにするために使われており、プログラム全体のスタイルに合わせています。

`if`ブロックでは、乱数が0.975より大きいときに、ランダムな開始位置で文字列を表示します。

`else`では、通常の固定位置で表示します。

### part 3

以下のforループは、コードレインの主な構造を実現する部分です。

このループは、`setup`関数で得られたリストの長さに応じて回数を設定します。

### 3.1

この部分では開始座標を取得します。

- x：開始のx座標はリストのインデックスとフォントサイズを掛けて算出されます。
- yも同様ですが、`setup`で初期化された相対位置とフォントサイズを掛けて算出します（この時点ではyは非常に大きな負の値になっているはずです）。

### 3.2

このコードは、1列を特殊文字列としてロックするためのものです。

- 前半部分：以下の3つの条件をすべて満たすと発動します。
    - 乱数が0.975より大きい
    - ロックが解除状態である
    - 現在の列のy座標が画面外にある
    
    条件を満たすと、
    
    - まずロックし、後続のループでこのyが更新されるのを防ぎます。
    - 現在のx座標をロックします。このx座標の列が特殊文字列列であることを識別するためです。
- 後半部分：
    - ロックされていて、現在のループのx座標がロックされたx座標と一致するときに特殊文字列を描画します。
    - このforループの処理は、マウス座標付近に生成する特殊文字列の方法とほぼ同じです。
    - リストの長さ分だけループし、リストを逆順にして文字を描画します。`offset`は文字間の間隔調整用です。

（この部分は直感的には分かりづらいかもしれません。というのも、py5のキャンバスは直交座標系で言う第2象限のような構造で、y座標が上下逆になっています。コードを書く際に少し混乱しやすいです）

### 3.3

ロックされていない列にはランダムな文字を生成して描画します。

- この部分のロジックは比較的単純で、ランダムに生成した文字を画面に描画するだけです。
- 透明度は、逆順で描画しているため、現在の文字のインデックスに応じて不透明度を調整します。
- 中間の`if…else`は現在は意味がありません（後述します）。
- 最後に`random.choice`を使って、文字列からランダムに1文字を選んで描画します。

### 3.4

現在の列が画面外に出たかどうかを判定します。

列が画面外に出た場合、すぐに元の位置に戻るのではなく、少しランダム性を持たせて自然に見えるようにしています。

条件を満たすと、その列の相対位置を画面上方（画面外）に戻します。

中間のif文では、この列が特殊列かどうかを判定し、そうであればロックを解除し、`locked_x`の値をリセットします（実はリセットしなくても動作には問題ありません）。

列がまだ画面外に出ていない場合は、相対位置に1を加えて、1ステップ（文字サイズ分）だけ下に移動させます。

---

## mouse_pressed関数

これは[イベントリスナー](https://py5coding.org/reference/summary.html#mouse-event-functions)で、定義されていればマウスクリック時にその内容が実行されます。

まずは`flag`を切り替えます。`flag`がFalseの場合は、画面中央に"paused"と表示し、描画ループを一時停止します。

Trueであればループを継続します。

---

最後の最後はpy5の実行関数です。

- 原版中文说明
    
    这是一个代码雨的程序
    
    最开始先导入包
    
    然后设定一些全局变量，前两个是用户可以自定义的
    
    - PLAY_SPEED 播放速度，其实在程序里这个是帧率
    - TEXT_LENS 单条代码雨的长度
    - OFFSET 字符间距偏移，加的太大就变成另一种东西了
    
    下面这些是不能自定义的
    
    - y_list 用于存放根据字符大小和窗口大小计算后得出的不重叠情况下每列的y轴随机坐标
    - text_size 代码雨字符大小，不推荐改，改了不好看
    - flag 播放暂停状态切换判断
    - lock 判断场上是否有特殊配列，防止重复
    - locked_x 记录被锁的列的位置（坐标）
    - special_list 特殊字符列表1
    - pecial_list2 特殊字符列表2
    
    ---
    
    ## setup函数
    
    先做一些py5的settings，比如设置画布大小，颜色模式，初始背景，字体大小，帧率等
    
    本程序因为没有用到remap函数进行颜色变换，所以调整颜色模式在此没有实际性意义
    
    在最后的for循环是对画布按照字体大小进行拆分，以保证代码雨字符不重叠，以及给每一列设置一个-100到0直接的初始位置
    
    ---
    
    ## draw函数
    
    首先因为lock和locked_x因为是全局变量，在函数块里修改时需要先用global定位到全局，否则为只读
    
    然后是刷新页面，在每次执行draw函数时将画布清空
    
    ### part 1
    
    用于在鼠标坐标上生成一个特殊字符串
    
    首先是一个空字符串，使用join将后面的内容插入进去
    
    使用random.choice和for循环依次在特殊字符列表中的每个子列表中抽选一个字符插入到前面的空字符串，这个写法是一个语法糖，我觉得可读性有点差
    
    最后 是将这个字符串打印在鼠标的坐标上
    
    ### part 2
    
    这是一行提示，告诉用户可以点击屏幕暂停
    
    使用random只是为了让这行字符串随机抖动，用来配合程序的整体风格
    
    if块是当随机数大于0.975时执行下面这行带有随机起始坐标的文字打印
    
    else是一般情况，也就是固定位置
    
    ### part 3
    
    下面的for循环是实现代码雨的主要结构
    
    此循环是根据setup函数中获得的列表长度配置循环次数
    
    3.1 
    
    这一部分是获得起始坐标
    
    - x是起始x轴坐标，列表的index和字体大小相乘后获得，
        
        y同理，只不过需要从setup中初始到的相对位置相乘后获得（此时这个负值应该很大）
        
    
    3.2
    
    这段代码是为了用于锁定一列作为特殊字符串
    
    - 前半部分需要同时满足三个条件时才能触发
        
        需要随机数大于0.975，锁为释放状态，当前列的y位于画面外
        
        满足条件后
        
        先锁定，防止后续循环时选到的y被刷新
        
        锁定当前x坐标，用于在输出时判断该列是否为特殊字符列
        
    - 后半部分
        
        当锁被锁时且当前循环到的x坐标是当时锁定的x坐标时执行打印
        
        后面这部分for循环的意思和上面在鼠标坐标旁边生成特殊字符串的方法差不多
        
        按列表长度循环，然后按列表倒序将字符打印到画布上，offset用于调整字符间距
        
        （这部分写的有点反直觉，主要是py5的画布按平面直角坐标系来说的话是第二象限，也就是y是反过来的，写的时候有点写晕了）
        
    
    3.3
    
    当列没有匹配上锁时生成随机字符
    
    - 这一段的逻辑比上面简单，因为只是随便生成后打印到画布上而已
        
        透明度因为是反向打印的，所以使用不透明乘当前字符的index
        
        中间的if…else已经没有实际意义了，后面会讲
        
        最后就是使用random.choice随机在字符串中选一个字符打印到画布上
        
    
    3.4
    
    判断当前列是否已经到屏幕外
    
    为了使到屏幕外的列表不要很机械的直接回到开头就加了个随机，当两个条件同时成立时才会把列表中的相对位置拉回到上方的屏幕外
    
    中间的if语句用于判断这个列是不是特殊列，如果是的话就解锁，并清空locked_x的值（其实不清空也没关系）
    
    如果当前列还没到屏幕外就使当前列的相对位置加一，也就是往下移动一格（一格就是一个字符大小的像素）
    
    ---
    
    ## mouse_pressed函数
    
    这是一个[[事件监听器](https://py5coding.org/reference/summary.html#mouse-event-functions)]，如果被定义了会在鼠标点击时执行里面的内容
    
    首先是转换flag，当flag为False时在屏幕中间打印一行paused，并且暂停打印循环
    
    如果是true就继续循环
    
    ---
    
    最后的最后就是py5的执行函数