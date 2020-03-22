from manimlib.imports import *

colorA = "#ff6600"
colorB = "#3366ff"


def num(ch):
    return ord(ch) - ord("A")

class Picture(Scene):
    def construct(self):
        text = Text("博弈游戏互动", font="华文中宋", stroke_width=4).scale(1.6)
        title = Text("Alice & Bob",font="华文中宋", stroke_width=2).scale(0.5).shift(DOWN*1.3)
        text[:2].set_color(colorB)
        text[2:4].set_color(colorA)
        title[:5].set_color(colorA)
        title[7:].set_color(colorB)
        self.add(text,title)
        self.wait()


class Begin(Scene):
    def construct(self):
        text = Text("来玩一局博弈游戏吧！", font="华文中宋", stroke_width=2)
        self.play(ShowCreation(text))
        self.wait(2)
        self.play(Uncreate(text))
        self.wait()
        text = TextMobject(r"""
        \begin{itemize}
        \item 平面上给出某正$n$边形的$n$个顶点，一开始没有边相连 
        \item 你和对手轮流行动，每一轮，玩家需选择其中两个点并连边
        \item 新连的边不能与之前任何一条边规范相交（除了端点）
        \item 第一个画出凸多边形的玩家获胜
        \end{itemize}
        """, stroke_width=2).scale(0.8)
        title = TextMobject(r"游戏规则\&获胜条件", stroke_width=2).to_edge(UP)
        line = Rectangle(width=500, height=0)
        line.shift(2.8 * UP)
        self.play(
            GrowFromCenter(line),
            FadeIn(title, direction=DOWN),
            run_time=2
        )
        self.play(ShowCreation(text, rate_func=linear), run_time=8)
        self.wait(8)
        self.play(
            Uncreate(text),
            Uncreate(line),
            Uncreate(title),
            run_time=2
        )
        self.wait()
        exa = Text("下面演示一局游戏的过程", font="华文中宋", stroke_width=2)
        self.play(ShowCreation(exa))
        self.wait(2)
        self.play(Uncreate(exa))
        self.wait()

        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / 5 + PI / 2), dist * np.sin(i * TAU / 5 + PI / 2), 0]) for i in range(5)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)
        self.play(
            FadeIn(VGroup(points)),
            FadeIn(VGroup(txt)),
        )
        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.wait(2)
        self.play(
            ShowCreation(first),
            ShowCreation(second),
        )
        self.wait(2)
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.play(FadeIn(star))
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        self.wait()
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("C")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(*lines[1:]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        # 后手win，显示在中间
        self.wait()
        rec=Rectangle(height=1.5,width=14,color=colorB,fill_opacity=0.7, stroke_width=0)
        gameover=Text("后手获胜", font="华文中宋", stroke_width=2)
        self.play(
            GrowFromCenter(rec),
            GrowFromCenter(gameover),
        )
        self.wait(2)
        self.play(
            FadeOut(star),
            FadeOut(points),
            FadeOut(txt),
            FadeOut(rec),
            FadeOut(gameover),
            FadeOut(first),
            FadeOut(second),
            FadeOut(VGroup(*lines)),
        )
        self.wait()
        text = Text("游戏开始！", font="华文中宋", stroke_width=2)
        self.play(ShowCreation(text))
        self.wait()


class easy0(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)
        self.play(
            FadeIn(VGroup(points)),
            FadeIn(VGroup(txt)),
        )
        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.wait(2)
        self.play(
            ShowCreation(first),
            ShowCreation(second),
        )
        self.wait(2)

class easy00(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.add(VGroup(points), VGroup(txt), first, second)
        self.wait()
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.play(GrowFromCenter(star))
        self.wait()

class easy000(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.add(VGroup(points), VGroup(txt), first, second ,star)
        self.wait()
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy0000(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("G")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 lines[0],lines[1])
        self.wait()
        lines.append(Line(points[num("C")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("E")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy0001(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("G")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 lines[0],lines[1])
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("C")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       points[num("G")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1], lines[2], lines[3]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy0002(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("G")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 lines[0],lines[1])
        self.wait()
        lines.append(Line(points[num("E")], points[num("F")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("C")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy00020(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("G")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("F")], color=colorA).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 lines[0],lines[1],lines[2],lines[3])
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("H")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       points[num("G")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2],lines[1],lines[5],lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy00000(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("G")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("H")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("F")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 lines[0],lines[1],lines[2],lines[3])
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("H")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       points[num("G")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2],lines[1],lines[5],lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy001(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.add(VGroup(points), VGroup(txt), first, second ,star)
        self.wait()
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy0010(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy00100(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("H")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("E")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 *lines)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("E")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("F")].get_center(),
                       points[num("G")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1],lines[2], lines[3], lines[4], lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy00101(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("H")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("E")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("E")], points[num("H")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[3], lines[4]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy0011(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 lines[0],lines[1])
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy00110(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 *lines)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("E")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("F")].get_center(),
                       points[num("G")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1],lines[2], lines[3], lines[4], lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy00111(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("E")], points[num("H")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[3], lines[4]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy0012(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,
                 lines[0],lines[1])
        self.wait()
        lines.append(Line(points[num("E")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy00120(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("H")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[3], lines[4]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy0013(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("H")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("F")].get_center(),
                       points[num("G")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1], lines[2], lines[3]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy002(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.add(VGroup(points), VGroup(txt), first, second ,star)
        self.wait()
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy0020(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("F")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy0021(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("F")], points[num("G")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy0022(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("D")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("D")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0], lines[2], lines[3]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy0023(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(*lines).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy00200(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("G")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0],lines[1],lines[4],lines[5]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy00210(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("G")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0],lines[1],lines[4],lines[5]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy003(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.add(VGroup(points), VGroup(txt), first, second ,star)
        self.wait()
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("D")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy0030(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("D")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1], lines[2], lines[3]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy0031(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("D")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("F")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class easy00310(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("D")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("H")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1], lines[3], lines[4]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy01(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.add(VGroup(points), VGroup(txt), first, second)
        self.wait()
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.play(FadeIn(star))
        lines = []
        lines.append(Line(points[num("C")], points[num("G")], color=colorA).set_stroke(width=5))
        self.wait()
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class easy010(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("C")], points[num("G")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class easy0100(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("C")], points[num("G")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("B")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("B")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1], lines[3], lines[4]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy011(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("C")], points[num("G")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("D")], points[num("F")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class easy0110(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("C")], points[num("G")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("F")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1], lines[3], lines[4]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class easy012(Scene):
    def construct(self):
        N = 8
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("C")], points[num("G")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("B")], points[num("G")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       points[num("G")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0], lines[1], lines[2]).set_color, WHITE,
                        rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)
        self.play(
            FadeIn(VGroup(points)),
            FadeIn(VGroup(txt)),
        )
        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.wait(2)
        self.play(
            ShowCreation(first),
            ShowCreation(second),
        )
        self.wait(2)

class diff00(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.add(VGroup(points), VGroup(txt), first, second)
        self.wait()
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.play(GrowFromCenter(star))
        self.wait()

class diff000(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.add(VGroup(points), VGroup(txt), first, second ,star)
        self.wait()
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("C")], points[num("I")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff0000(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("H")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("E")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00000(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("H")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("G")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("E")], points[num("F")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("F")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("E")].get_center(),
                       points[num("F")].get_center(),
                       points[num("G")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(*lines[3:]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0001(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("G")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("E")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00010(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("G")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("F")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("H")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("G")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2],lines[4],lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff00020(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("F")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("H")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("F")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("F")].get_center(),
                       points[num("G")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(*lines[2:]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0003(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("H")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00030(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("C")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("H")], points[num("F")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("H")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("E")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("F")].get_center(),
                       points[num("H")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(*lines[2:]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0010(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0],lines[2],lines[3]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0011(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("F")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00110(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("G")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0],lines[4],lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0012(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("F")], points[num("G")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("D")], points[num("I")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00120(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("D")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("G")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))

        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0],lines[4],lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff002(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.add(VGroup(points), VGroup(txt), first, second ,star)
        self.wait()
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff0020(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00200(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("A")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0], lines[4], lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0021(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00210(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("H")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("A")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0], lines[4], lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0022(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("A")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0], lines[2], lines[3]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff003(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.add(VGroup(points), VGroup(txt), first, second ,star)
        self.wait()
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff0030(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00300(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("D")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[4], lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0031(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00310(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("D")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[4], lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0032(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("D")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()

class diff00320(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("A")], points[num("E")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("F")], points[num("I")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("D")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("H")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("C")], points[num("D")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       points[num("D")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[4], lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff01(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.add(VGroup(points), VGroup(txt), first, second)
        self.wait()
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            first[0].get_right() + RIGHT * 0.35)
        self.play(GrowFromCenter(star))
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        self.wait()
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class diff010(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("H")], points[num("F")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class diff0100(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("B")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("H")], points[num("F")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1], lines[3], lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff011(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("E")], points[num("G")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class diff0110(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("G")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[3], lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff012(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class diff0120(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[3], lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0121(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class diff01210(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("E")], points[num("H")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("C")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("G")], points[num("F")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("B")], points[num("C")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[4], lines[5]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff013(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("A")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("H")], points[num("F")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * DOWN)
        self.wait()

class diff0130(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("C")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("H")], points[num("F")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("B")], points[num("C")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("A")], points[num("B")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("A")].get_center(),
                       points[num("B")].get_center(),
                       points[num("C")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[1], lines[3], lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0131(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("C")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("H")], points[num("F")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("D")], points[num("E")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("E")], points[num("I")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("E")].get_center(),
                       points[num("I")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0], lines[3], lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0132(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("C")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("H")], points[num("F")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("G")], points[num("H")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("F")], points[num("G")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("H")].get_center(),
                       points[num("G")].get_center(),
                       points[num("F")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[2], lines[3], lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class diff0133(Scene):
    def construct(self):
        N = 9
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)

        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        star = Pentagram(dist=0.26, color=WHITE, fill_opacity=1, stroke_width=0).move_to(
            second[0].get_right() + RIGHT * 0.35)
        lines = []
        lines.append(Line(points[num("D")], points[num("I")], color=colorA).set_stroke(width=5))
        lines.append(Line(points[num("A")], points[num("C")], color=colorB).set_stroke(width=5))
        lines.append(Line(points[num("H")], points[num("F")], color=colorA).set_stroke(width=5))

        self.add(VGroup(points), VGroup(txt), first, second ,star,*lines)
        self.wait()
        lines.append(Line(points[num("H")], points[num("I")], color=colorB).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        self.play(star.shift, 0.7 * UP)
        self.wait()
        lines.append(Line(points[num("D")], points[num("F")], color=colorA).set_stroke(width=5))
        self.play(ShowCreation(lines[-1]))
        self.wait()
        # 显示凸包
        poly = Polygon(points[num("D")].get_center(),
                       points[num("F")].get_center(),
                       points[num("H")].get_center(),
                       points[num("I")].get_center(),
                       color=WHITE, fill_opacity=0.8, stroke_width=0)
        self.play(
            ApplyMethod(VGroup(lines[0], lines[2], lines[3],lines[4]).set_color, WHITE, rate_func=there_and_back),
            FadeIn(poly, rate_func=there_and_back),
            run_time=2)
        self.wait()

class hard(Scene):
    def construct(self):
        N = 12
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)
        self.play(
            FadeIn(VGroup(points)),
            FadeIn(VGroup(txt)),
        )
        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.wait(2)
        self.play(
            ShowCreation(first),
            ShowCreation(second),
        )
        self.wait(2)

class nightmare(Scene):
    def construct(self):
        N = 13
        dist = 2.5
        points = VGroup(
            *[Dot([dist * np.cos(i * TAU / N + PI / 2 + PI / N),
                   dist * np.sin(i * TAU / N + PI / 2 + PI / N), 0]) for i in range(N)])
        txt = []
        for i in range(len(points)):
            pos = normalize(points[i].get_center() - ORIGIN) * 0.8 + points[i].get_center()
            txt.append(TextMobject(chr(65 + i)).move_to(pos))
        txt = VGroup(*txt)
        self.play(
            FadeIn(VGroup(points)),
            FadeIn(VGroup(txt)),
        )
        first = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorA, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("先手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        second = VGroup(
            RoundedRectangle(height=0.62, width=1.1, color=colorB, corner_radius=0.2, fill_opacity=1, stroke_width=0),
            Text("后手", font="华文中宋", stroke_width=2).scale(0.4)
        )
        first[0].to_corner(UL)
        first[1].move_to(first[0].get_center())
        second[0].to_corner(UL).shift(0.7 * DOWN)
        second[1].move_to(second[0].get_center())
        self.wait(2)
        self.play(
            ShowCreation(first),
            ShowCreation(second),
        )
        self.wait(2)



class FLose(Scene):
    def construct(self):
        rec = Rectangle(height=1.5, width=14, color=colorA, fill_opacity=0.7, stroke_width=0)
        gameover = Text("挑战失败", font="华文中宋", stroke_width=2)
        self.play(
            GrowFromCenter(rec),
            GrowFromCenter(gameover),
        )
        self.wait(2)

class SLose(Scene):
    def construct(self):
        rec = Rectangle(height=1.5, width=14, color=colorB, fill_opacity=0.7, stroke_width=0)
        gameover = Text("挑战失败", font="华文中宋", stroke_width=2)
        self.play(
            GrowFromCenter(rec),
            GrowFromCenter(gameover),
        )
        self.wait(2)

class FWin(Scene):
    def construct(self):
        rec = Rectangle(height=1.5, width=14, color=colorA, fill_opacity=0.7, stroke_width=0)
        gameover = Text("挑战成功", font="华文中宋", stroke_width=2)
        self.play(
            GrowFromCenter(rec),
            GrowFromCenter(gameover),
        )
        self.wait(2)

class SWin(Scene):
    def construct(self):
        rec = Rectangle(height=1.5, width=14, color=colorB, fill_opacity=0.7, stroke_width=0)
        gameover = Text("挑战成功", font="华文中宋", stroke_width=2)
        self.play(
            GrowFromCenter(rec),
            GrowFromCenter(gameover),
        )
        self.wait(2)

class Right(Scene):
    def construct(self):
        rec = Rectangle(height=1.5, width=14, color=colorB, fill_opacity=0.7, stroke_width=0)
        gameover = Text("回答正确", font="华文中宋", stroke_width=2)
        self.play(
            GrowFromCenter(rec),
            GrowFromCenter(gameover),
        )
        self.wait(2)
class Wrong(Scene):
    def construct(self):
        rec = Rectangle(height=1.5, width=14, color=colorB, fill_opacity=0.7, stroke_width=0)
        gameover = Text("回答错误", font="华文中宋", stroke_width=2)
        self.play(
            GrowFromCenter(rec),
            GrowFromCenter(gameover),
        )
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python -m manim -p " + module_name + " Picture"
    os.system(command)
