# 第一节上的py5画图主要函数

[notion link](https://www.notion.so/Lecture-1-Materials-1d7919598f2680408ac1f6f5a8146409)

**init&run**

- `size(width, height)` - 画布大小
- `run_sketch()` - run

**基本図形**

- `ellipse(x, y, width, height)` - 楕円を描画する。円を描く場合はwidthとheightを同じ値にする
- `rect(x, y, width, height)` - 矩形
- `line(x1, y1, x2, y2)` - 2点間に直線を描画する
- `triangle(x1, y1, x2, y2, x3, y3)` - 3点を指定して三角形を描画する
- `quad(x1, y1, x2, y2, x3, y3, x4, y4)` - 4点を指定して四角形を描画する

**色と塗りつぶし**

- `fill(r, g, b)` - 図形の塗りつぶし色をRGB値で指定する
- `stroke(r, g, b)` - 図形の輪郭線の色をRGB値で指定する
- `no_fill()` - 塗りつぶしを無効化する
- `no_stroke()` - 輪郭線を無効化する

**スタイル設定**

- `stroke_weight(weight)` - 線の太さを指定する
- `background(r, g, b)` - 背景色をRGB値で指定する

---
基本格式

```python
import py5


def setup():
   py5.size(700, 700)
   py5.background(204, 204, 204)
   py5.no_stroke()

   py5.fill(193, 71, 97)
   py5.rect(100, 400, 500, 100)


if __name__ == '__main__':
   py5.run_sketch()

```
注意点：

* 设定画布之类的初始化设定必须在`setup`函数的最开始
* py5需要调用java，注意配置JAVA_HOME
