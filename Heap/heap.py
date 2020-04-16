from manimlib.imports import *
import layered

BLUE = "#00CCFF"


class LineLinkCircles(Line):
    def __init__(self, cirA=Circle(), cirB=Circle(), **kwargs):
        if not isinstance(cirA, Circle) or not isinstance(cirB, Circle):
            raise Exception('TypeError, need Circle')
        vec = cirB.get_center() - cirA.get_center()
        dis = get_norm(vec)
        if dis < cirA.radius + cirB.radius:
            raise Exception('Two circles intersect')
        vec = normalize(vec)
        super().__init__(start=cirA.get_center() + vec * cirA.radius,
                         end=cirB.get_center() - vec * cirB.radius,
                         **kwargs)


def swap(x, y):
    return y, x


def gen_tree(edges, **kwargs):
    gen = layered.Gen(edges, **kwargs)
    n = len(edges)
    nodes = [Circle(radius=layered.node_size / 2, color=WHITE) for i in range(n)]
    pos = gen.getCoor()
    l, r, u, d = 1e10, -1e10, -1e10, 1e10
    for i in range(n):
        pos[i][1] = -pos[i][1]
        nodes[i].move_to(pos[i])
        l = min(l, pos[i][0])
        r = max(r, pos[i][0])
        u = max(u, pos[i][1])
        d = min(d, pos[i][1])
    lines = [LineLinkCircles(cirA=nodes[x], cirB=nodes[y])
             for x in range(len(edges)) for y in edges[x]]
    res = VGroup(VGroup(*nodes), VGroup(*lines))
    res.shift((l + r) / 2 * LEFT + (u + d) / 2 * DOWN)
    return res


def mix_order(tree):
    lst = []
    lst.append(tree[0][0])
    for i in range(len(tree[1])):
        lst.append(tree[1][i])
        lst.append(tree[0][i + 1])
    return VGroup(*lst)


def gen_ncb(n):
    edges = []
    for i in range(n):
        if i + 1 < n // 2:
            edges.append([2 * (i + 1) - 1, 2 * (i + 1) + 1 - 1])
        elif i + 1 == n // 2:
            if 2 * (i + 1) + 1 <= n:
                edges.append([2 * (i + 1) - 1, 2 * (i + 1) + 1 - 1])
            else:
                edges.append([2 * (i + 1) - 1])
        else:
            edges.append([])
    return edges


class Tree(Scene):
    def construct(self):
        edges = gen_ncb(11)
        tree = gen_tree(edges)
        values = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 3]
        vals = [TexMobject(str(x)) for x in values]
        for i in range(len(tree[0])):
            vals[i].move_to(tree[0][i].get_center())
        self.play(ShowCreation(tree), run_time=5)
        self.wait(2)
        self.play(FadeIn(VGroup(*vals)), run_time=2)
        self.wait(2)


PART_WIDTH = 1.5
PART_HEIGHT = 1
PART_RADIUS = 0.4
PART_SPACEY = 2
PART_SPACEX = 7
PART_SCALE = 0.5
STROKE_WIDTH = 1.4
OPACITY = 0.2

class Begin(Scene):
    def construct(self):
        leftprofile = ImageMobject(r"C:\Users\sk\Pictures\Saved Pictures\faraway.png").shift(3*LEFT+1*UP).scale(0.01)
        rightprofile = ImageMobject(r"C:\Users\sk\Pictures\Saved Pictures\mao.png").shift(3*RIGHT+1*UP).scale(0.01)
        anim1=ApplyMethod(leftprofile.scale,160,run_time=2)
        anim2=ApplyMethod(rightprofile.scale,160,run_time=2)
        self.add(turn_animation_into_updater(anim1))
        self.add(turn_animation_into_updater(anim2))
        self.wait(1)
        faraway=TextMobject("@法拉薇").set_stroke(width=1.5).scale(0.8).move_to(leftprofile.get_center()+2.5*DOWN)
        mao=TextMobject("@笨手笨脚oO").set_stroke(width=1.5).scale(0.8).move_to(rightprofile.get_center()+2.5*DOWN)
        anim3=ShowCreation(faraway,run_time=2)
        anim4=ShowCreation(mao,run_time=2)
        self.add(turn_animation_into_updater(anim3))
        self.add(turn_animation_into_updater(anim4))
        self.wait(3)

class One(Scene):
    def construct(self):
        title = Text("堆排序算法", font="华文中宋", stroke_width=2).to_edge(UP).scale(0.7)
        titleline = Rectangle(width=500, height=0)
        titleline.shift(2.5 * UP)
        cons = VGroup(
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("定义", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("存储", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("建堆", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("排序", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
        )
        cons[0].move_to([-PART_SPACEX / 2 + 0 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        cons[1].move_to([-PART_SPACEX / 2 + 1 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        cons[2].move_to([-PART_SPACEX / 2 + 2 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        cons[3].move_to([-PART_SPACEX / 2 + 3 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        cons.shift(0.2 * DOWN)

        darkcons = VGroup(
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("定义", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("存储", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("建堆", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("排序", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
        )
        darkcons[0].move_to([-PART_SPACEX / 2 + 0 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        darkcons[1].move_to([-PART_SPACEX / 2 + 1 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        darkcons[2].move_to([-PART_SPACEX / 2 + 2 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        darkcons[3].move_to([-PART_SPACEX / 2 + 3 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        darkcons.shift(0.2 * DOWN)

        dashedlines = VGroup(
            DashedLine(cons[0].get_center(), cons[1].get_center()).scale(0.55),
            DashedLine(cons[1].get_center(), cons[2].get_center()).scale(0.55),
            DashedLine(cons[2].get_center(), cons[3].get_center()).scale(0.55),
        )
        self.play(
            FadeIn(title),
            FadeIn(titleline),
            FadeIn(cons),
            FadeIn(dashedlines),
        )
        self.wait(5.5)
        self.play(
            ApplyMethod(title.set_opacity, OPACITY),
            ApplyMethod(titleline.set_opacity, OPACITY),
            ApplyMethod(dashedlines.set_opacity, OPACITY),
            Transform(cons[1], darkcons[1]),
            Transform(cons[2], darkcons[2]),
            Transform(cons[3], darkcons[3]),
        )
        self.wait(2)


class Two(Scene):
    def construct(self):
        title = Text("堆排序算法", font="华文中宋", stroke_width=2).to_edge(UP).scale(0.7)
        titleline = Rectangle(width=500, height=0)
        titleline.shift(2.5 * UP)
        cons = VGroup(
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("定义", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("存储", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("建堆", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("排序", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
        )
        cons[0].move_to([-PART_SPACEX / 2 + 0 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        cons[1].move_to([-PART_SPACEX / 2 + 1 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        cons[2].move_to([-PART_SPACEX / 2 + 2 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        cons[3].move_to([-PART_SPACEX / 2 + 3 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        cons.shift(0.2 * DOWN)

        darkcons = VGroup(
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("定义", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("存储", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("建堆", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("排序", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
        )
        darkcons[0].move_to([-PART_SPACEX / 2 + 0 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        darkcons[1].move_to([-PART_SPACEX / 2 + 1 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        darkcons[2].move_to([-PART_SPACEX / 2 + 2 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        darkcons[3].move_to([-PART_SPACEX / 2 + 3 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        darkcons.shift(0.2 * DOWN)

        dashedlines = VGroup(
            DashedLine(cons[0].get_center(), cons[1].get_center()).scale(0.55),
            DashedLine(cons[1].get_center(), cons[2].get_center()).scale(0.55),
            DashedLine(cons[2].get_center(), cons[3].get_center()).scale(0.55),
        )
        self.play(
            FadeIn(title),
            FadeIn(titleline),
            FadeIn(cons),
            FadeIn(dashedlines),
        )
        self.wait(1.5)
        self.play(
            ApplyMethod(title.set_opacity, OPACITY),
            ApplyMethod(titleline.set_opacity, OPACITY),
            ApplyMethod(dashedlines.set_opacity, OPACITY),
            Transform(cons[0], darkcons[0]),
            Transform(cons[2], darkcons[2]),
            Transform(cons[3], darkcons[3]),
        )
        self.wait(2)


class Three(Scene):
    def construct(self):
        title = Text("堆排序算法", font="华文中宋", stroke_width=2).to_edge(UP).scale(0.7)
        titleline = Rectangle(width=500, height=0)
        titleline.shift(2.5 * UP)
        cons = VGroup(
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("定义", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("存储", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("建堆", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("排序", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
        )
        cons[0].move_to([-PART_SPACEX / 2 + 0 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        cons[1].move_to([-PART_SPACEX / 2 + 1 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        cons[2].move_to([-PART_SPACEX / 2 + 2 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        cons[3].move_to([-PART_SPACEX / 2 + 3 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        cons.shift(0.2 * DOWN)

        darkcons = VGroup(
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("定义", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("存储", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("建堆", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("排序", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
        )
        darkcons[0].move_to([-PART_SPACEX / 2 + 0 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        darkcons[1].move_to([-PART_SPACEX / 2 + 1 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        darkcons[2].move_to([-PART_SPACEX / 2 + 2 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        darkcons[3].move_to([-PART_SPACEX / 2 + 3 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        darkcons.shift(0.2 * DOWN)

        dashedlines = VGroup(
            DashedLine(cons[0].get_center(), cons[1].get_center()).scale(0.55),
            DashedLine(cons[1].get_center(), cons[2].get_center()).scale(0.55),
            DashedLine(cons[2].get_center(), cons[3].get_center()).scale(0.55),
        )
        self.play(
            FadeIn(title),
            FadeIn(titleline),
            FadeIn(cons),
            FadeIn(dashedlines),
        )
        self.wait(1.5)
        self.play(
            ApplyMethod(title.set_opacity, OPACITY),
            ApplyMethod(titleline.set_opacity, OPACITY),
            ApplyMethod(dashedlines.set_opacity, OPACITY),
            Transform(cons[0], darkcons[0]),
            Transform(cons[1], darkcons[1]),
            Transform(cons[3], darkcons[3]),
        )
        self.wait(2)


class Four(Scene):
    def construct(self):
        title = Text("堆排序算法", font="华文中宋", stroke_width=2).to_edge(UP).scale(0.7)
        titleline = Rectangle(width=500, height=0)
        titleline.shift(2.5 * UP)
        cons = VGroup(
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("定义", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("存储", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("建堆", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS),
                   Text("排序", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE)),
        )
        cons[0].move_to([-PART_SPACEX / 2 + 0 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        cons[1].move_to([-PART_SPACEX / 2 + 1 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        cons[2].move_to([-PART_SPACEX / 2 + 2 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        cons[3].move_to([-PART_SPACEX / 2 + 3 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        cons.shift(0.2 * DOWN)

        darkcons = VGroup(
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("定义", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("存储", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("建堆", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
            VGroup(RoundedRectangle(width=PART_WIDTH, height=PART_HEIGHT, corner_radius=PART_RADIUS,
                                    stroke_opacity=OPACITY),
                   Text("排序", font="华文中宋", stroke_width=STROKE_WIDTH).scale(PART_SCALE).set_opacity(opacity=OPACITY)),
        )
        darkcons[0].move_to([-PART_SPACEX / 2 + 0 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        darkcons[1].move_to([-PART_SPACEX / 2 + 1 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        darkcons[2].move_to([-PART_SPACEX / 2 + 2 * PART_SPACEX / 3, -PART_SPACEY / 2, 0])
        darkcons[3].move_to([-PART_SPACEX / 2 + 3 * PART_SPACEX / 3, PART_SPACEY / 2, 0])
        darkcons.shift(0.2 * DOWN)

        dashedlines = VGroup(
            DashedLine(cons[0].get_center(), cons[1].get_center()).scale(0.55),
            DashedLine(cons[1].get_center(), cons[2].get_center()).scale(0.55),
            DashedLine(cons[2].get_center(), cons[3].get_center()).scale(0.55),
        )
        self.play(
            FadeIn(title),
            FadeIn(titleline),
            FadeIn(cons),
            FadeIn(dashedlines),
        )
        self.wait(1.5)
        self.play(
            ApplyMethod(title.set_opacity, OPACITY),
            ApplyMethod(titleline.set_opacity, OPACITY),
            ApplyMethod(dashedlines.set_opacity, OPACITY),
            Transform(cons[0], darkcons[0]),
            Transform(cons[1], darkcons[1]),
            Transform(cons[2], darkcons[2]),
        )
        self.wait(2)


class PartOne(Scene):
    def construct(self):
        edges1 = gen_ncb(7)
        tree1 = mix_order(gen_tree(edges1))

        edges2 = gen_ncb(11)
        tree2 = mix_order(gen_tree(edges2))
        self.play(ShowCreation(tree1), run_time=7)
        self.play(ReplacementTransform(tree1, VGroup(*tree2[:13])))
        self.play(ShowCreation(VGroup(*tree2[13:])), run_time=4.5)
        self.wait()

        frame = SurroundingRectangle(VGroup(tree2[14::2]), buff=0.16, color=ORANGE, stroke_width=4).round_corners(
            radius=0.35)
        self.play(ShowCreation(frame))
        self.wait(3)
        self.play(Uncreate(frame))
        self.wait(3)
        tree3 = mix_order(gen_tree(edges2, node_size=0.7, level_separation=1.4))

        self.play(ReplacementTransform(tree2, tree3))
        self.wait()
        values = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 5]
        vals = [TexMobject(str(-x + 17)) for x in values]
        for i in range(len(vals)):
            vals[i].move_to(tree3[i * 2].get_center())
        self.play(FadeIn(VGroup(*vals)))
        self.wait()

        explain = VGroup(
            TextMobject("Min Heap"),
            TexMobject(r"A[\text{PARENT}(i)]\le A[i]").scale(0.85)
        ).arrange(direction=0.8 * DOWN).shift(4 * LEFT + 1.5 * UP)
        explain[1].shift(explain[0].get_left() - explain[1].get_left() + DOWN)
        self.play(
            ApplyMethod(tree3.shift, 0.1 * UP + 2 * RIGHT),
            ApplyMethod(VGroup(*vals).shift, 0.1 * UP + 2 * RIGHT),
            FadeInFrom(explain, direction=DOWN)
        )
        self.wait(7)

        vals2 = [TexMobject(str(x)) for x in values]
        for i in range(len(vals)):
            vals2[i].move_to(tree3[i * 2].get_center())
        explain2 = VGroup(
            TextMobject("Max Heap"),
            TexMobject(r"A[\text{PARENT}(i)]\ge A[i]").scale(0.85)
        ).arrange(direction=0.8 * DOWN).shift(4.5 * LEFT + 1.5 * UP)
        explain2[1].shift(explain2[0].get_left() - explain2[1].get_left() + DOWN)
        self.play(
            ReplacementTransform(VGroup(*vals), VGroup(*vals2)),
            ReplacementTransform(explain, explain2),
        )
        self.wait(14)


LEN = 0.75


class PartTwo(Scene):
    def construct(self):
        values = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 5]
        edges = gen_ncb(11)
        tree = gen_tree(edges, node_size=0.7, level_separation=1.4).shift(0.1 * UP + 2 * RIGHT)
        array = VGroup(*[Rectangle(height=LEN, width=LEN) for i in range(11)]).arrange(
            direction=0.000001 * RIGHT).to_corner(UL)
        arrayvalue = VGroup(*[TexMobject(str(values[i])).move_to(array[i].get_center()) for i in range(11)])
        arraynumber = VGroup(
            *[TexMobject(str(i + 1)).set_color("#11C2EE").scale(0.7).move_to(array[i].get_center() + 0.8 * DOWN) for i
              in range(11)])
        heapnumber = VGroup(
            *[TexMobject(str(i + 1)).set_color("#11C2EE").scale(0.7).move_to(tree[0][i].get_center() + 0.6 * UP) for i
              in range(11)])
        heapvalue = VGroup(*[TexMobject(str(values[i])).move_to(tree[0][i].get_center()) for i in range(11)])
        self.play(
            FadeIn(tree),
            FadeIn(heapvalue),
            FadeIn(array),
            FadeIn(arrayvalue),
        )
        self.wait(5)
        self.play(
            ShowCreation(arraynumber),
            run_time=2
        )
        self.wait(5)
        self.play(
            ShowCreation(heapnumber),
            run_time=2
        )
        self.wait(3)
        explain = VGroup(
            TextMobject(r"Node $i$").set_stroke(width=1.8),
            TextMobject(r"parent $\lfloor i/2\rfloor$").set_stroke(width=1.8),
            TextMobject(r"left child $2i$").set_stroke(width=1.8),
            TextMobject(r"right child $2i+1$").set_stroke(width=1.8),
            TextMobject(r"leaves $\lfloor n/2\rfloor +1$\ \textasciitilde\  $n$").set_stroke(width=1.8),
        ).scale(0.75)
        explain[0].move_to([-5.5, 1.2, 0])
        explain[1].move_to(explain[0].get_left() + 0.6 * DOWN - explain[1].get_left())
        explain[2].move_to(explain[1].get_left() + 0.6 * DOWN - explain[2].get_left())
        explain[3].move_to(explain[2].get_left() + 0.6 * DOWN - explain[3].get_left())
        explain[4].move_to(explain[3].get_left() + 0.6 * DOWN - explain[4].get_left())
        self.play(ShowCreation(explain[0]), run_time=1)
        self.wait(1.5)
        self.play(ShowCreation(explain[1]), run_time=1)
        self.wait(0.5)
        self.play(ShowCreation(explain[2]), run_time=1)
        self.wait(0.5)
        self.play(ShowCreation(explain[3]), run_time=1)
        self.wait(5)
        self.play(ShowCreation(explain[4]))
        self.wait(8)


class PartThree(Scene):
    def construct(self):
        values = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 5]
        array = VGroup(*[Rectangle(height=LEN, width=LEN) for i in range(11)]).arrange(
            direction=0.000001 * RIGHT).to_corner(UL)
        arrayvalue = VGroup(*[TexMobject(str(values[i])).move_to(array[i].get_center()) for i in range(11)])
        values_shuffle = values[:]
        random.shuffle(values_shuffle)
        array_shuffle = array.copy()
        arrayvalue_shuffle = [TexMobject(str(values_shuffle[i])).move_to(array[i].get_center()) for i in range(11)]
        self.play(
            FadeIn(array),
            FadeIn(arrayvalue)
        )
        self.wait(1)
        np.random.seed(2)
        pos = [[np.random.random() * 8 - 4, np.random.random() * 6 - 3, 0] for i in range(11)]
        self.play(*[
            ApplyMethod(VGroup(array[i], arrayvalue[i]).move_to, pos[i]) for i in range(11)
        ], run_time=1.5)
        self.wait(0.5)
        tmp = [values_shuffle.index(values[i]) for i in range(11)]
        self.play(*([
                        ReplacementTransform(array[i], array_shuffle[tmp[i]]) for i in range(11)
                    ] + [
                        ReplacementTransform(arrayvalue[i], arrayvalue_shuffle[tmp[i]]) for i in range(11)
                    ]), run_time=1.5)
        self.wait(20)

        frame = SurroundingRectangle(array_shuffle[0], buff=0.12, color=ORANGE, stroke_width=4).round_corners(
            radius=0.1)
        self.play(ShowCreation(frame))

        self.wait(2)
        tree = mix_order(gen_tree(gen_ncb(1), node_size=0.7, level_separation=1.4))
        heapvalue = [arrayvalue_shuffle[0].copy().set_stroke(width=2.5).move_to(tree[0].get_center())]
        heapvalue[0].add_updater(lambda obj: obj.move_to(tree[0].get_center()))
        self.play(
            ReplacementTransform(array_shuffle[0].copy(), tree[0]),
            ReplacementTransform(arrayvalue_shuffle[0].copy(), heapvalue[0])
        )
        self.wait()
        for i in range(1, 11, 2):
            tree_new = mix_order(gen_tree(gen_ncb(i + 2), node_size=0.7, level_separation=1.4))
            self.play(*([
                            Transform(tree[i], tree_new[i]) for i in range(len(tree_new) - 4)
                        ] + [
                            ApplyMethod(frame.move_to, array_shuffle[i].get_center())
                        ]))
            self.wait()
            tree.add(*tree_new[-4:])
            heapvalue.append(arrayvalue_shuffle[i].copy().set_stroke(width=2.5).move_to(tree[i * 2].get_center()))
            heapvalue[-1].add_updater(lambda obj, i=i: obj.move_to(tree[i * 2].get_center()))

            self.play(
                ShowCreation(tree[-4]),
                ReplacementTransform(array_shuffle[i].copy(), tree[-3]),
                ReplacementTransform(arrayvalue_shuffle[i].copy(), heapvalue[-1])
            )
            self.wait()
            # up
            x = i + 1
            lst = []
            while x > 0:
                lst.append(heapvalue[x - 1])
                lst.append(tree[(x - 1) * 2])
                if (x - 1) * 2 - 1 >= 0:
                    lst.append(tree[(x - 1) * 2 - 1])
                x //= 2
            lst = VGroup(*lst)
            self.play(ApplyMethod(lst.set_color, ORANGE))
            self.play(ApplyMethod(lst.set_color, WHITE))
            x = i + 1
            while x > 1:
                if values_shuffle[x - 1] > values_shuffle[x // 2 - 1]:
                    values_shuffle[x - 1], values_shuffle[x // 2 - 1] = swap(values_shuffle[x - 1],
                                                                             values_shuffle[x // 2 - 1])
                    heapvalue[x - 1].clear_updaters()
                    heapvalue[x // 2 - 1].clear_updaters()
                    self.play(
                        MoveAlongPath(arrayvalue_shuffle[x - 1],
                                      ArcBetweenPoints(arrayvalue_shuffle[x - 1].get_center(),
                                                       arrayvalue_shuffle[x // 2 - 1].get_center())),
                        MoveAlongPath(arrayvalue_shuffle[x // 2 - 1],
                                      ArcBetweenPoints(arrayvalue_shuffle[x // 2 - 1].get_center(),
                                                       arrayvalue_shuffle[x - 1].get_center())),
                        MoveAlongPath(heapvalue[x - 1],
                                      ArcBetweenPoints(heapvalue[x - 1].get_center(),
                                                       heapvalue[x // 2 - 1].get_center())),
                        MoveAlongPath(heapvalue[x // 2 - 1],
                                      ArcBetweenPoints(heapvalue[x // 2 - 1].get_center(),
                                                       heapvalue[x - 1].get_center())),

                    )
                    self.wait()
                    arrayvalue_shuffle[x - 1], arrayvalue_shuffle[x // 2 - 1] = swap(arrayvalue_shuffle[x - 1],
                                                                                     arrayvalue_shuffle[x // 2 - 1])
                    heapvalue[x - 1], heapvalue[x // 2 - 1] = swap(heapvalue[x - 1], heapvalue[x // 2 - 1])
                    heapvalue[x - 1].add_updater(lambda obj, x=x: obj.move_to(tree[(x - 1) * 2].get_center()))
                    heapvalue[x // 2 - 1].add_updater(lambda obj, x=x: obj.move_to(tree[(x // 2 - 1) * 2].get_center()))
                else:
                    break
                x //= 2

            self.play(frame.move_to, array_shuffle[i + 1].get_center())
            self.wait()
            heapvalue.append(
                arrayvalue_shuffle[i + 1].copy().set_stroke(width=2.5).move_to(tree[(i + 1) * 2].get_center()))
            heapvalue[-1].add_updater(lambda obj, i=i: obj.move_to(tree[(i + 1) * 2].get_center()))

            self.play(
                ShowCreation(tree[-2]),
                ReplacementTransform(array_shuffle[i + 1].copy(), tree[-1]),
                ReplacementTransform(arrayvalue_shuffle[i + 1].copy(), heapvalue[-1])
            )
            self.wait()

            x = i + 1 + 1
            lst = []
            while x > 0:
                lst.append(heapvalue[x - 1])
                lst.append(tree[(x - 1) * 2])
                if (x - 1) * 2 - 1 >= 0:
                    lst.append(tree[(x - 1) * 2 - 1])
                x //= 2
            lst = VGroup(*lst)
            self.play(ApplyMethod(lst.set_color, ORANGE))
            self.play(ApplyMethod(lst.set_color, WHITE))
            x = i + 1 + 1
            while x > 1:
                if values_shuffle[x - 1] > values_shuffle[x // 2 - 1]:
                    values_shuffle[x - 1], values_shuffle[x // 2 - 1] = swap(values_shuffle[x - 1],
                                                                             values_shuffle[x // 2 - 1])
                    heapvalue[x - 1].clear_updaters()
                    heapvalue[x // 2 - 1].clear_updaters()
                    self.play(
                        MoveAlongPath(arrayvalue_shuffle[x - 1],
                                      ArcBetweenPoints(arrayvalue_shuffle[x - 1].get_center(),
                                                       arrayvalue_shuffle[x // 2 - 1].get_center())),
                        MoveAlongPath(arrayvalue_shuffle[x // 2 - 1],
                                      ArcBetweenPoints(arrayvalue_shuffle[x // 2 - 1].get_center(),
                                                       arrayvalue_shuffle[x - 1].get_center())),
                        MoveAlongPath(heapvalue[x - 1],
                                      ArcBetweenPoints(heapvalue[x - 1].get_center(),
                                                       heapvalue[x // 2 - 1].get_center())),
                        MoveAlongPath(heapvalue[x // 2 - 1],
                                      ArcBetweenPoints(heapvalue[x // 2 - 1].get_center(),
                                                       heapvalue[x - 1].get_center())),

                    )
                    self.wait()
                    arrayvalue_shuffle[x - 1], arrayvalue_shuffle[x // 2 - 1] = swap(arrayvalue_shuffle[x - 1],
                                                                                     arrayvalue_shuffle[x // 2 - 1])
                    heapvalue[x - 1], heapvalue[x // 2 - 1] = swap(heapvalue[x - 1], heapvalue[x // 2 - 1])
                    heapvalue[x - 1].add_updater(lambda obj, x=x: obj.move_to(tree[(x - 1) * 2].get_center()))
                    heapvalue[x // 2 - 1].add_updater(lambda obj, x=x: obj.move_to(tree[(x // 2 - 1) * 2].get_center()))
                else:
                    break
                x //= 2

        self.wait()
        self.play(
            FadeOut(VGroup(*self.mobjects))
        )
        self.wait()
        code = TextMobject(r"""
\begin{algorithmic}[1]
\Procedure{MaxHeapInsert}{$A,key$}
\State $\textit{A.heap-size}  \gets \textit{A.heap-size}  + 1$
\State $i \gets \textit{A.heap-size} $
\State $A[i] \gets key $
\While{$i>1 \AND A[i]>A[\lfloor i/2 \rfloor]$}
\State \Call{Swap}{$A[i],A[\lfloor i/2 \rfloor]$}
\State $i \gets \lfloor i/2 \rfloor$
\EndWhile
\EndProcedure

\Procedure{BuildMaxHeap}{$A$}
\State $\textit{A.heap-size} \gets 0$
\For{$i \gets 1$ \textbf{to} $\textit{A.length}$} 
\State \Call{MaxHeapInsert}{$A,A[i]$}
\EndFor
\EndProcedure
\end{algorithmic}
        """).scale(0.8)
        frame = SurroundingRectangle(code, buff=0.1, color=WHITE, stroke_width=4)
        self.play(
            FadeIn(code),
            FadeIn(frame),
        )
        self.wait(5)
        self.play(
            ApplyMethod(code.shift, 2.5 * LEFT),
            ApplyMethod(frame.shift, 2.5 * LEFT),
        )
        #self.wait()
        explain = VGroup(
            TextMobject(r"Time complexity"),
            TexMobject(r"O(n\log{n})"),
        ).scale(1.1).arrange(direction=1.5 * DOWN).shift((7.2 * RIGHT + frame.get_right()) / 2)
        # explain[0].move_to([2.5,2.5,0]-explain[0].get_left())
        # explain[1].move_to(explain[0].get_center()+1.5*DOWN)
        timec = VGroup(
            TexMobject(r"O(n)"),
            TexMobject(r"O(\log{n})"),
        ).scale(0.9)
        timec[0].move_to([2.2, -2.1, 0] - timec[0].get_left())
        timec[1].move_to([2.2, -2.65, 0] - timec[1].get_left())

        dashedlines = VGroup(
            DashedLine(timec[0].get_left() + 2.7 * LEFT, timec[0].get_left()).scale(0.98),
            DashedLine(timec[1].get_left() + 1.9 * LEFT, timec[1].get_left()).scale(0.98),
        )
        self.play(
            FadeInFrom(explain[0], direction=DOWN)
        )
        self.wait(4)
        self.play(
            FadeInFrom(timec, direction=0.5 * LEFT),
            ShowCreation(dashedlines)
        )
        self.wait(4)
        self.play(
            ReplacementTransform(timec, explain[1]),
            Uncreate(dashedlines)
        )
        self.wait(2)


class PartThree2(Scene):
    def construct(self):
        values = [7, 1, 4, 3, 10, 2, 16, 9, 5, 8, 14]
        random.shuffle(values)
        array = VGroup(*[Rectangle(height=LEN, width=LEN) for i in range(11)]).arrange(
            direction=0.000001 * RIGHT).to_corner(UL)
        arrayvalue = [TexMobject(str(values[i])).move_to(array[i].get_center()) for i in range(11)]
        self.play(
            FadeIn(array),
            FadeIn(VGroup(*arrayvalue))
        )
        self.wait(4)
        tree = mix_order(gen_tree(gen_ncb(11), node_size=0.7, level_separation=1.4))
        heapvalue = [TexMobject(str(values[i]), stroke_width=2.5).move_to(tree[i * 2]) for i in range(11)]
        self.play(
            FadeIn(tree),
            FadeIn(VGroup(*heapvalue)),
        )
        self.wait(3)
        frame = SurroundingRectangle(array[11 // 2 - 1], buff=0.12, color=ORANGE, stroke_width=4).round_corners(
            radius=0.1)
        self.play(
            ShowCreation(frame),
            ApplyMethod(VGroup(*heapvalue[11 // 2 + 1 - 1:]).set_color, BLUE),
        )
        self.wait()
        i = 11 // 2
        while i >= 1:
            x = i
            self.play(
                ApplyMethod(heapvalue[x - 1].set_color, ORANGE),
            )
            self.wait()
            while 2 * x <= 11:
                y = 2 * x
                if y + 1 <= 11 and values[y - 1] < values[y]:
                    y += 1
                if values[y - 1] <= values[x - 1]:
                    break
                values[y - 1], values[x - 1] = swap(values[y - 1], values[x - 1])
                self.play(
                    MoveAlongPath(arrayvalue[x - 1],
                                  ArcBetweenPoints(arrayvalue[x - 1].get_center(),
                                                   arrayvalue[y - 1].get_center())),
                    MoveAlongPath(arrayvalue[y - 1],
                                  ArcBetweenPoints(arrayvalue[y - 1].get_center(),
                                                   arrayvalue[x - 1].get_center())),
                    MoveAlongPath(heapvalue[x - 1],
                                  ArcBetweenPoints(heapvalue[x - 1].get_center(),
                                                   heapvalue[y - 1].get_center())),
                    MoveAlongPath(heapvalue[y - 1],
                                  ArcBetweenPoints(heapvalue[y - 1].get_center(),
                                                   heapvalue[x - 1].get_center())),
                )
                self.wait()
                arrayvalue[x - 1], arrayvalue[y - 1] = swap(arrayvalue[x - 1], arrayvalue[y - 1])
                heapvalue[x - 1], heapvalue[y - 1] = swap(heapvalue[x - 1], heapvalue[y - 1])
                x = y
            self.play(
                ApplyMethod(heapvalue[x - 1].set_color, BLUE),
            )
            self.wait()
            i -= 1
            if i >= 1:
                self.play(frame.move_to, array[i - 1].get_center())
                self.wait()
        self.wait()
        self.play(VGroup(*heapvalue).set_color, WHITE)
        self.wait(2)
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait()
        code = TextMobject(r"""
\begin{algorithmic}[1]
\Procedure{MaxHeapify}{$A,i$}
\While{$2i\le \textit{A.heap-size}$}
\State $j \gets 2i $
\If{$j+1\le \textit{A.heap-size} \AND A[j]<A[j+1]$}
\State $j\gets j+1$
\EndIf
\If{$A[j]\le A[i]$}
$\Break$
\EndIf
\State \Call{Swap}{$A[i],A[j]$}
\State $i \gets j$
\EndWhile
\EndProcedure

\Procedure{BuildMaxHeap}{$A$}
\State $\textit{A.heap-size} \gets \textit{A.length}$
\For{$i \gets \lfloor\textit{A.heap-size}/2\rfloor$ \textbf{downto} $1$} 
\State \Call{MaxHeapify}{$A,i$}
\EndFor
\EndProcedure
\end{algorithmic}
                """).scale(0.65)
        frame = SurroundingRectangle(code, buff=0.1, color=WHITE, stroke_width=4)
        self.play(
            FadeIn(code),
            FadeIn(frame),
        )
        self.wait(5)
        self.play(
            ApplyMethod(code.shift, 2.5 * LEFT),
            ApplyMethod(frame.shift, 2.5 * LEFT),
        )
        explain = VGroup(
            TextMobject(r"Time complexity"),
            TexMobject(r"O(n\log{n})"),
        ).scale(1.1).arrange(direction=1.5 * DOWN).shift((7.2 * RIGHT + frame.get_right()) / 2)
        # explain[0].move_to([2.5,2.5,0]-explain[0].get_left())
        # explain[1].move_to(explain[0].get_center()+1.5*DOWN)
        timec = VGroup(
            TexMobject(r"O(n)"),
            TexMobject(r"O(\log{n})"),
        ).scale(0.75)
        timec[0].move_to([2.3, -1.95, 0] - timec[0].get_left())
        timec[1].move_to([2.3, -2.39, 0] - timec[1].get_left())

        dashedlines = VGroup(
            DashedLine(timec[0].get_left() + 2.45 * LEFT, timec[0].get_left()).scale(0.98),
            DashedLine(timec[1].get_left() + 4.8 * LEFT, timec[1].get_left()).scale(0.98),
        )
        self.play(
            FadeInFrom(explain[0], direction=DOWN)
        )
        self.wait(4)
        self.play(
            FadeInFrom(timec, direction=0.5 * LEFT),
            ShowCreation(dashedlines[0]),
            ShowCreation(dashedlines[1]),
        )
        self.wait(4)
        self.play(
            ReplacementTransform(timec, explain[1]),
            Uncreate(dashedlines)
        )
        self.wait(2)
        explain2 = VGroup(
            TextMobject(r"Time complexity"),
            TextMobject(r"\sout{$O(n\log{n})$}"),
        ).scale(1.1).arrange(direction=1.5 * DOWN).shift((7.2 * RIGHT + frame.get_right()) / 2)
        self.play(
            Transform(explain, explain2)
        )
        self.wait()
        explain3 = VGroup(
            TextMobject(r"Time complexity"),
            TextMobject(r"\sout{$O(n\log{n})$}"),
            TextMobject(r"Tighter analysis"),
            TextMobject(r"$O(n)$"),
        ).scale(1.1).arrange(direction=1.5 * DOWN).shift((7.2 * RIGHT + frame.get_right()) / 2)
        self.play(
            ApplyMethod(explain.move_to, VGroup(explain3[0], explain3[1]).get_center()),
            FadeInFrom(explain3[2], direction=DOWN),
            FadeInFrom(explain3[3], direction=DOWN),
        )
        self.wait()


class PartThree3(Scene):
    def construct(self):
        tree = mix_order(gen_tree(gen_ncb(11), node_size=0.7, level_separation=1.4))
        number = [i+1 for i in range(11)]
        def calc(i):
            now = 0
            while (i << now) <= 11:
                now += 1
            return now - 1

        value = [calc(i + 1) for i in range(11)]
        heapnumber = VGroup(
            *[TexMobject(str(i + 1)).set_color("#11C2EE").scale(0.7).move_to(tree[i*2].get_center() + 0.6 * UP) for i in range(11)])
        height = VGroup(
            *[TexMobject("h="+str(value[i]), stroke_width=1.2).scale(0.5).move_to(tree[i * 2].get_center() + 0.7 * RIGHT+0.23*UP) for i in range(11)])
        self.play(
            FadeIn(tree),
            FadeIn(heapnumber),
        )
        self.wait(3)
        self.play(
            FadeIn(height)
        )
        self.wait(3)
        self.play(
            ApplyMethod(VGroup(height, tree,heapnumber).shift, 2.8 * LEFT)
        )
        question=TextMobject(r"There are at most \underline{ }\underline{ ? }\underline{ } \\ nodes of height $h$ in any \\ $n$-element heap").scale(0.9).move_to((7.2 * RIGHT + tree.get_right()) / 2)
        self.wait(2)
        self.play(ShowCreation(question))
        self.wait(4)
        self.play(Uncreate(question))
        self.wait(10)
        formular = VGroup(
            TexMobject(r"2^{h}i",r"\le n", r"<2^{h+1}i"),
            TexMobject(r"n/2^{h+1}<i\le n/2^{h}"),
            TexMobject(r"\lfloor n/2^{h+1}\rfloor<i\le \lfloor n/2^{h}\rfloor"),
            Line([-2.6,0,0],[2.6,0,0]),
            TexMobject(r"\lfloor n/2^{h}\rfloor - \lfloor n/2^{h+1}\rfloor"),
            TexMobject(r"\le \lceil n/2^{h+1}\rceil"),
        ).scale(0.95).arrange(0.95 * DOWN).move_to((7.2 * RIGHT + tree.get_right()) / 2)
        self.play(ShowCreation(formular[0][0]),run_time=3)
        self.wait(5.5)
        self.play(ShowCreation(formular[0][1]), run_time=1.5)
        self.wait(3)
        self.play(ShowCreation(formular[0][2]), run_time=2)
        self.wait(6)
        self.play(ShowCreation(formular[1:3]),run_time=4)
        self.wait(4)
        self.play(ShowCreation(formular[3:]),run_time=3)
        self.wait(28)
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait()
        '''
        explain=VGroup(
            TextMobject(r"$n$个元素的堆中，至多有$\lceil n/2^{h+1}\rceil$个高度为$h$的结点"),
            TextMobject(r"在一个高度为$h$的结点上运行MAX-HEAPIFY的代价是$O(h)$"),
        ).arrange(direction=DOWN)
        '''
        final = TexMobject(r"""
            \begin{aligned}
            \textit{Total cost} = & \sum_{h=0}^{\lfloor\log{n}\rfloor}\lceil\frac{n}{2^{h+1}}\rceil O(h) \\ 
            = &  O(n\sum_{h=0}^{\lfloor\log{n}\rfloor}\lceil\frac{h}{2^{h}}\rceil) \\
            = & O(n\sum_{h=0}^{\infty}\lceil\frac{h}{2^{h}}\rceil) \\
            = & O(2n) = O(n)
            \end{aligned}
            """)
        '''
        self.play(ShowCreation(explain[0]))
        self.wait()
        self.play(ShowCreation(explain[1]))
        self.wait()
        self.play(Uncreate(explain))
        self.wait()
        '''
        self.play(ShowCreation(final,rate_func=linear), run_time=20)
        self.wait(5)
        self.play(FadeOut(VGroup(*self.mobjects)))
        self.wait()


class PartFour(Scene):
    def construct(self):
        values = [16, 14, 9, 10, 8, 3, 1, 4, 7, 5, 2]
        array = VGroup(*[Rectangle(height=LEN, width=LEN) for i in range(11)]).arrange(
            direction=0.000001 * RIGHT).to_corner(UL)
        arrayvalue = [TexMobject(str(values[i])).move_to(array[i].get_center()) for i in range(11)]
        tree = mix_order(gen_tree(gen_ncb(11), node_size=0.7, level_separation=1.4))
        heapvalue = [arrayvalue[i].copy().set_stroke(width=2.5).move_to(tree[2*i].get_center()) for i in range(11)]

        self.play(
            FadeIn(array),
            FadeIn(VGroup(*arrayvalue)),
            FadeIn(tree),
            FadeIn(VGroup(*heapvalue)),
        )
        self.wait(2)

        size = 11
        while size>1:
            x,y=1,size
            values[y - 1], values[x - 1] = swap(values[y - 1], values[x - 1])
            self.play(
                MoveAlongPath(arrayvalue[x - 1],
                              ArcBetweenPoints(arrayvalue[x - 1].get_center(),
                                               arrayvalue[y - 1].get_center())),
                MoveAlongPath(arrayvalue[y - 1],
                              ArcBetweenPoints(arrayvalue[y - 1].get_center(),
                                               arrayvalue[x - 1].get_center())),
                MoveAlongPath(heapvalue[x - 1],
                              ArcBetweenPoints(heapvalue[x - 1].get_center(),
                                               heapvalue[y - 1].get_center())),
                MoveAlongPath(heapvalue[y - 1],
                              ArcBetweenPoints(heapvalue[y - 1].get_center(),
                                               heapvalue[x - 1].get_center()))
            )
            self.wait()
            arrayvalue[x - 1], arrayvalue[y - 1] = swap(arrayvalue[x - 1], arrayvalue[y - 1])
            heapvalue[x - 1], heapvalue[y - 1] = swap(heapvalue[x - 1], heapvalue[y - 1])
            self.play(
                ApplyMethod(arrayvalue[x - 1].set_color, ORANGE),
                ApplyMethod(heapvalue[x - 1].set_color, ORANGE),
                ApplyMethod(heapvalue[size-1].set_color,BLUE),
                ApplyMethod(tree[2*(size-1)].set_color,BLUE),
                ApplyMethod(arrayvalue[size-1].set_color, BLUE),
                FadeOut(tree[2*(size-1)-1])
            )
            self.wait()
            size-=1
            x=1
            while 2 * x <= size:
                y = 2 * x
                if y + 1 <= size and values[y - 1] < values[y]:
                    y += 1
                if values[y - 1] <= values[x - 1]:
                    break
                values[y - 1], values[x - 1] = swap(values[y - 1], values[x - 1])
                self.play(
                    MoveAlongPath(arrayvalue[x - 1],
                                  ArcBetweenPoints(arrayvalue[x - 1].get_center(),
                                                   arrayvalue[y - 1].get_center())),
                    MoveAlongPath(arrayvalue[y - 1],
                                  ArcBetweenPoints(arrayvalue[y - 1].get_center(),
                                                   arrayvalue[x - 1].get_center())),
                    MoveAlongPath(heapvalue[x - 1],
                                  ArcBetweenPoints(heapvalue[x - 1].get_center(),
                                                   heapvalue[y - 1].get_center())),
                    MoveAlongPath(heapvalue[y - 1],
                                  ArcBetweenPoints(heapvalue[y - 1].get_center(),
                                                   heapvalue[x - 1].get_center())),
                )
                self.wait()
                arrayvalue[x - 1], arrayvalue[y - 1] = swap(arrayvalue[x - 1], arrayvalue[y - 1])
                heapvalue[x - 1], heapvalue[y - 1] = swap(heapvalue[x - 1], heapvalue[y - 1])
                x = y
            if size==1:
                self.play(
                    ApplyMethod(tree[x - 1].set_color, BLUE),
                    ApplyMethod(heapvalue[x - 1].set_color, BLUE),
                    ApplyMethod(arrayvalue[x - 1].set_color, BLUE),
                )
            else:
                self.play(
                    ApplyMethod(heapvalue[x-1].set_color,WHITE),
                    ApplyMethod(arrayvalue[x-1].set_color,WHITE),
                )
            self.wait()
        self.wait(5)

colorA = "#ff6600"
colorB = "#3366ff"

class Picture(Scene):
    def construct(self):
        tree = mix_order(gen_tree(gen_ncb(11), node_size=0.7, level_separation=1.4))
        values = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 5]
        vals = VGroup(*[TexMobject(str(values[i])).move_to(tree[2*i].get_center()) for i in range(11)])
        tree.shift(2.7*RIGHT+0.2*DOWN)
        vals.shift(2.7*RIGHT+0.2*DOWN)
        bg = ImageMobject(r"C:\Users\sk\Desktop\manim\1.png").scale(4).set_opacity(0.32)
        title2=Text("算法可视化",font="华文中宋",stroke_width=5.5).scale(1.3).set_stroke(color=colorA).move_to(2.75*LEFT+0.95*UP)
        title = Text("堆 排 序", font="华文中宋",stroke_width=4.8).scale(1.5).set_stroke(color=colorB)
        title.move_to(title2.get_left()+1.8 * UP-title.get_left())
        title[:].set_color(colorA)
        title2[:].set_color([BLUE,colorB])
        self.add(tree,vals,bg,title,title2)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python -m manim -p " + module_name + " Picture"
    os.system(command)
