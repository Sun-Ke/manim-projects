from manimlib.imports import *

lineScaleRatio = 0.85
fontScaleRatio = 0.7 * 0.75
LINESTROKE = 3
SLICE=0.2

class PointAndText(VGroup):
    def __init__(self, pos, text, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = Dot(pos)
        t = TextMobject(text).move_to(p.get_center() + 0.5 * UP)
        self.add(t)
        self.add(p)


def calc_pos(len, x):
    lm, ln = 0, 1
    rm, rn = 1, 0
    ans = 0
    for i in range(30):
        len /= 2
        p, q = lm + rm, ln + rn
        if x * q < p:
            rm, rn = p, q
        else:
            ans += len
            lm, ln = p, q
    return np.array([ans, 0, 0])


class SBtreeScene(Scene):
    def construct(self):
        # d1,d2,d3 for position
        d1 = Dot([-100, 0, 0])
        d2 = Dot([-100, 0, 0])
        d3 = Dot([-100, 0, 0])
        sbtree1 = VGroup(TexMobject("{0", "\\over", "1}"),
                         TexMobject("{1", "\\over", "1}"),
                         TexMobject("{1", "\\over", "0}"))
        sbtree2 = VGroup(TexMobject("{0", "\\over", "1}"),
                         TexMobject("{1", "\\over", "2}"),
                         TexMobject("{1", "\\over", "1}"),
                         TexMobject("{2", "\\over", "1}"),
                         TexMobject("{1", "\\over", "0}"))
        sbtree3 = VGroup(TexMobject("{0", "\\over", "1}"),
                         TexMobject("{1", "\\over", "3}"),
                         TexMobject("{1", "\\over", "2}"),
                         TexMobject("{2", "\\over", "3}"),
                         TexMobject("{1", "\\over", "1}"),
                         TexMobject("{3", "\\over", "2}"),
                         TexMobject("{2", "\\over", "1}"),
                         TexMobject("{3", "\\over", "1}"),
                         TexMobject("{1", "\\over", "0}"))
        sbtree4 = VGroup(TexMobject("{0", "\\over", "1}"),
                         TexMobject("{1", "\\over", "4}"),
                         TexMobject("{1", "\\over", "3}"),
                         TexMobject("{2", "\\over", "5}"),
                         TexMobject("{1", "\\over", "2}"),
                         TexMobject("{3", "\\over", "5}"),
                         TexMobject("{2", "\\over", "3}"),
                         TexMobject("{3", "\\over", "4}"),
                         TexMobject("{1", "\\over", "1}"),
                         TexMobject("{4", "\\over", "3}"),
                         TexMobject("{3", "\\over", "2}"),
                         TexMobject("{5", "\\over", "3}"),
                         TexMobject("{2", "\\over", "1}"),
                         TexMobject("{5", "\\over", "2}"),
                         TexMobject("{3", "\\over", "1}"),
                         TexMobject("{4", "\\over", "1}"),
                         TexMobject("{1", "\\over", "0}"))
        sbtree5 = VGroup(TexMobject("{0", "\\over", "1}"),
                         TexMobject("{1", "\\over", "5}"),
                         TexMobject("{1", "\\over", "4}"),
                         TexMobject("{2", "\\over", "7}"),
                         TexMobject("{1", "\\over", "3}"),
                         TexMobject("{3", "\\over", "8}"),
                         TexMobject("{2", "\\over", "5}"),
                         TexMobject("{3", "\\over", "7}"),
                         TexMobject("{1", "\\over", "2}"),
                         TexMobject("{4", "\\over", "7}"),
                         TexMobject("{3", "\\over", "5}"),
                         TexMobject("{5", "\\over", "8}"),
                         TexMobject("{2", "\\over", "3}"),
                         TexMobject("{5", "\\over", "7}"),
                         TexMobject("{3", "\\over", "4}"),
                         TexMobject("{4", "\\over", "5}"),
                         TexMobject("{1", "\\over", "1}"),
                         TexMobject("{5", "\\over", "4}"),
                         TexMobject("{4", "\\over", "3}"),
                         TexMobject("{7", "\\over", "5}"),
                         TexMobject("{3", "\\over", "2}"),
                         TexMobject("{8", "\\over", "5}"),
                         TexMobject("{5", "\\over", "3}"),
                         TexMobject("{7", "\\over", "4}"),
                         TexMobject("{2", "\\over", "1}"),
                         TexMobject("{7", "\\over", "3}"),
                         TexMobject("{5", "\\over", "2}"),
                         TexMobject("{8", "\\over", "3}"),
                         TexMobject("{3", "\\over", "1}"),
                         TexMobject("{7", "\\over", "2}"),
                         TexMobject("{4", "\\over", "1}"),
                         TexMobject("{5", "\\over", "1}"),
                         TexMobject("{1", "\\over", "0}"))
        sbtree1.scale(fontScaleRatio)
        sbtree2.scale(fontScaleRatio)
        sbtree3.scale(fontScaleRatio)
        sbtree4.scale(fontScaleRatio)
        sbtree5.scale(fontScaleRatio)
        dashedLines1 = VGroup(
            *[
                DashedLine(start=sbtree1[i].get_bottom(), end=sbtree2[i].get_top(), positive_space_ratio=0.3,
                           stroke_width=LINESTROKE)
                    .scale(lineScaleRatio)
                for i in range(len(sbtree1))
            ]
        )
        dashedLines1.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *[
                        DashedLine(start=sbtree1[i].get_bottom(), end=sbtree2[i * 2].get_top(),
                                   positive_space_ratio=0.3, stroke_width=LINESTROKE)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree1))
                    ]
                )
            )
        )
        lines1 = VGroup(
            *([
                  Line(start=sbtree1[i].get_left(), end=sbtree2[i * 2 - 1].get_right(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(1, len(sbtree1), 2)
              ] + [
                  Line(start=sbtree1[i].get_right(), end=sbtree2[i * 2 + 1].get_left(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(1, len(sbtree1), 2)
              ])
        )
        lines1.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree1[i].get_left(), end=sbtree2[i * 2 - 1].get_right(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(1, len(sbtree1), 2)
                      ] + [
                          Line(start=sbtree1[i].get_right(), end=sbtree2[i * 2 + 1].get_left(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(1, len(sbtree1), 2)
                      ])
                )
            )
        )
        dashedLines2 = VGroup(
            *[
                DashedLine(start=sbtree2[i].get_bottom(), end=sbtree3[i].get_top(), positive_space_ratio=0.3,
                           stroke_width=LINESTROKE)
                    .scale(lineScaleRatio)
                for i in range(len(sbtree2))
            ]
        )
        dashedLines2.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *[
                        DashedLine(start=sbtree2[i].get_bottom(), end=sbtree3[i * 2].get_top(),
                                   positive_space_ratio=0.3, stroke_width=LINESTROKE)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree2))
                    ]
                )
            )
        )
        lines2 = VGroup(
            *([
                  Line(start=sbtree2[i].get_left(), end=sbtree3[i * 2 - 1].get_right(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(1, len(sbtree2), 2)
              ] + [
                  Line(start=sbtree2[i].get_right(), end=sbtree3[i * 2 + 1].get_left(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(1, len(sbtree2), 2)
              ])
        )
        lines2.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree2[i].get_left(), end=sbtree3[i * 2 - 1].get_right(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(1, len(sbtree2), 2)
                      ] + [
                          Line(start=sbtree2[i].get_right(), end=sbtree3[i * 2 + 1].get_left(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(1, len(sbtree2), 2)
                      ])
                )
            )
        )
        dashedLines3 = VGroup(
            *[
                DashedLine(start=sbtree3[i].get_bottom(), end=sbtree4[i].get_top(), positive_space_ratio=0.3,
                           stroke_width=LINESTROKE)
                    .scale(lineScaleRatio)
                for i in range(len(sbtree3))
            ]
        )
        dashedLines3.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *[
                        DashedLine(start=sbtree3[i].get_bottom(), end=sbtree4[i * 2].get_top(),
                                   positive_space_ratio=0.3, stroke_width=LINESTROKE)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree3))
                    ]
                )
            )
        )
        lines3 = VGroup(
            *([
                  Line(start=sbtree3[i].get_left(), end=sbtree4[i * 2 - 1].get_right(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(1, len(sbtree3), 2)
              ] + [
                  Line(start=sbtree3[i].get_right(), end=sbtree4[i * 2 + 1].get_left(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(1, len(sbtree3), 2)
              ])
        )
        lines3.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree3[i].get_left(), end=sbtree4[i * 2 - 1].get_right(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(1, len(sbtree3), 2)
                      ] + [
                          Line(start=sbtree3[i].get_right(), end=sbtree4[i * 2 + 1].get_left(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(1, len(sbtree3), 2)
                      ])
                )
            )
        )

        def update_1(obj):
            obj[0].move_to(d1.get_center())
            obj[1].move_to(d2.get_center())
            obj[2].move_to(2 * d2.get_center() - d1.get_center())

        def update_2(obj):
            obj[0].move_to(d3.get_center())
            for i in range(1, len(obj)):
                obj[i].move_to(obj[0].get_center() + i * 2 * (d2.get_center() - d1.get_center()) / (len(obj) - 1))

        def update_3(obj):
            obj[0].move_to(d1.get_center() + 2 * (d3.get_center() - d1.get_center()))
            for i in range(1, len(obj)):
                obj[i].move_to(obj[0].get_center() + i * 2 * (d2.get_center() - d1.get_center()) / (len(obj) - 1))

        def update_4(obj):
            obj[0].move_to(d1.get_center() + 3 * (d3.get_center() - d1.get_center()))
            for i in range(1, len(obj)):
                obj[i].move_to(obj[0].get_center() + i * 2 * (d2.get_center() - d1.get_center()) / (len(obj) - 1))

        sbtree1.add_updater(update_1)
        sbtree2.add_updater(update_2)
        sbtree3.add_updater(update_3)
        sbtree4.add_updater(update_4)

        self.play(ShowCreation(d1), ShowCreation(d2), ShowCreation(d3))
        self.play(Uncreate(d1), Uncreate(d2), Uncreate(d3))
        H, W = 4, 10
        d1.move_to([-W / 2, H / 2, 0])
        d3.move_to([-W / 2, H / 3 / 2, 0])
        d2.move_to([0, H / 2, 0])
        self.play(
            *[
                ShowCreation(sbtree1),
                ShowCreation(sbtree2),
                ShowCreation(sbtree3),
                ShowCreation(sbtree4),
                ShowCreation(dashedLines1),
                ShowCreation(dashedLines2),
                ShowCreation(dashedLines3),
                ShowCreation(lines1),
                ShowCreation(lines2),
                ShowCreation(lines3)
            ]
        )
        self.wait(2+SLICE)

        text = VGroup(
            TextMobject("上期视频讲了Stern–Brocot tree的构造方法"),
            TextMobject("可以发现每个正有理数会在树中出现且仅出现一次"),
            TextMobject("更形象一点"),
            TextMobject(r"这个树挂在$0$到$+\infty$之间的连线上"),
            TextMobject(r"试着找找", "$\displaystyle \sqrt{2}$", ",", "$e$", ",", "$\pi$", "的位置"),
            TextMobject("这启发着我们在树上去做无理数的有理逼近"),
            TextMobject("你也可以寻找Stern–Brocot tree与法雷序列，连分数的联系"),
            TextMobject("不过这期视频我们要先解决一个更简单的问题"),
            TextMobject(r"如何在树上找到有理数$\displaystyle \frac{p}{q}$的位置？"),
        )
        text.to_edge(DOWN)
        dashedLines0 = VGroup(
            DashedLine(start=sbtree1[0].get_right(), end=sbtree1[1].get_left(), positive_space_ratio=0.3,
                       stroke_width=LINESTROKE)
                .scale(lineScaleRatio),
            DashedLine(start=sbtree1[2].get_left(), end=sbtree1[1].get_right(), positive_space_ratio=0.3,
                       stroke_width=LINESTROKE)
                .scale(lineScaleRatio)
        )
        self.play(ShowCreation(text[0]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(text[0], text[1]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(text[1], text[2]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(text[2], text[3]))
        self.wait(1+SLICE)
        dashedLines1.clear_updaters()
        dashedLines2.clear_updaters()
        dashedLines3.clear_updaters()
        '''
        self.play(
            FadeOut(dashedLines1),
            FadeOut(dashedLines2),
            FadeOut(dashedLines3)
        )
        '''
        self.play(
            *([
                  FadeOut(sbtree2[i]) for i in range(0, len(sbtree2), 2)
              ] + [
                  FadeOut(sbtree3[i]) for i in range(0, len(sbtree3), 2)
              ] + [
                  FadeOut(sbtree4[i]) for i in range(0, len(sbtree4), 2)
              ] + [
                  FadeOut(dashedLines1)
              ] + [
                  FadeOut(dashedLines2)
              ] + [
                  FadeOut(dashedLines3)
              ] + [
                  ShowCreation(dashedLines0)
              ])
        )
        self.wait(3+SLICE)

        # \sqrt{2},e,\pi在虚线上的位置
        # TextMobject(r"你可以试着找找","$\displaystyle \sqrt{2}$",",","$e$",",","$\pi$","的位置")
        self.play(ReplacementTransform(text[3], text[4]))
        self.wait(3+SLICE)

        points = VGroup(
            PointAndText(sbtree1[0].get_center() + calc_pos(W, math.sqrt(2)), r"$\sqrt{2}$"),
            PointAndText(sbtree1[0].get_center() + calc_pos(W, math.e), r"$e$"),
            PointAndText(sbtree1[0].get_center() + calc_pos(W, PI), r"$\pi$")
        )
        self.play(*([
                        ReplacementTransform(text[4][1], points[0]),
                        ReplacementTransform(text[4][3], points[1]),
                        ReplacementTransform(text[4][5], points[2])
                    ] + [
                        FadeOut(text[4][i]) for i in range(0, 7, 2)
                    ]))
        self.wait(3+SLICE)
        self.play(ShowCreation(text[5]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(text[5], text[6]))
        self.wait(3+SLICE)
        self.play(*[
            ReplacementTransform(text[6], text[7]),
            Uncreate(points)
        ])
        self.wait(3+SLICE)
        self.play(ReplacementTransform(text[7], text[8]))
        self.wait(3+SLICE)
        explain = VGroup(
            TextMobject("为了描述位置信息，我们需要一个好的表示方法"),
            TextMobject("从上往下看从根到该点的路径"),
            TextMobject("如果当前是往左走，则记为$L$"),
            TextMobject("如果当前是往右走，则记为$R$"),
            TextMobject(r"这样我们就用包含L和R的字符串表示了该有理数"),
            TextMobject("反过来，给出一个LR字符串"),
            TextMobject(r"也就定位了树中对应的有理数"),
            TextMobject(r"为了方便，也可以将字符串记为$\uparrow$")
        )
        explain.to_edge(DOWN)
        self.play(ReplacementTransform(text[8], explain[0]))
        self.wait(2+SLICE)

        # 移到左边，updater影响效果，先去掉
        lines1.clear_updaters()
        lines2.clear_updaters()
        lines3.clear_updaters()
        # 整个树消失，字幕消失
        self.play(
            *([
                  FadeOut(sbtree1),
                  FadeOut(dashedLines0),
                  FadeOut(lines1),
                  FadeOut(lines2),
                  FadeOut(lines3),
              ] + [
                  FadeOut(sbtree2[i]) for i in range(1, len(sbtree2), 2)
              ] + [
                  FadeOut(sbtree3[i]) for i in range(1, len(sbtree3), 2)
              ] + [
                  FadeOut(sbtree4[i]) for i in range(1, len(sbtree4), 2)
              ] + [
                  FadeOut(explain[0])
              ])
        )

        # 重做树的效果
        sbtree1 = VGroup(TexMobject("{0", "\\over", "1}"),
                         TexMobject("{1", "\\over", "1}"),
                         TexMobject("{1", "\\over", "0}"))
        sbtree2 = VGroup(TexMobject("{1", "\\over", "2}"),
                         TexMobject("{2", "\\over", "1}"))
        sbtree3 = VGroup(TexMobject("{1", "\\over", "3}"),
                         TexMobject("{2", "\\over", "3}"),
                         TexMobject("{3", "\\over", "2}"),
                         TexMobject("{3", "\\over", "1}"))
        sbtree4 = VGroup(TexMobject("{1", "\\over", "4}"),
                         TexMobject("{2", "\\over", "5}"),
                         TexMobject("{3", "\\over", "5}"),
                         TexMobject("{3", "\\over", "4}"),
                         TexMobject("{4", "\\over", "3}"),
                         TexMobject("{5", "\\over", "3}"),
                         TexMobject("{5", "\\over", "2}"),
                         TexMobject("{4", "\\over", "1}"))
        sbtree5 = VGroup(TexMobject("{1", "\\over", "5}"),
                         TexMobject("{2", "\\over", "7}"),
                         TexMobject("{3", "\\over", "8}"),
                         TexMobject("{3", "\\over", "7}"),
                         TexMobject("{4", "\\over", "7}"),
                         TexMobject("{5", "\\over", "8}"),
                         TexMobject("{5", "\\over", "7}"),
                         TexMobject("{4", "\\over", "5}"),
                         TexMobject("{5", "\\over", "4}"),
                         TexMobject("{7", "\\over", "5}"),
                         TexMobject("{8", "\\over", "5}"),
                         TexMobject("{7", "\\over", "4}"),
                         TexMobject("{7", "\\over", "3}"),
                         TexMobject("{8", "\\over", "3}"),
                         TexMobject("{7", "\\over", "2}"),
                         TexMobject("{5", "\\over", "1}"))
        sbtree1.scale(fontScaleRatio * 0.9)
        sbtree2.scale(fontScaleRatio * 0.9)
        sbtree3.scale(fontScaleRatio * 0.9)
        sbtree4.scale(fontScaleRatio * 0.9)
        sbtree5.scale(fontScaleRatio * 0.9)

        def new_update_2(obj):
            for i in range(0, len(obj)):
                obj[i].move_to(d3.get_center() + (2 * i + 1) * (d2.get_center() - d1.get_center()) / len(obj))

        def new_update_3(obj):
            for i in range(0, len(obj)):
                obj[i].move_to(d1.get_center() + 2 * (d3.get_center() - d1.get_center())
                               + (2 * i + 1) * (d2.get_center() - d1.get_center()) / len(obj))

        def new_update_4(obj):
            for i in range(0, len(obj)):
                obj[i].move_to(d1.get_center() + 3 * (d3.get_center() - d1.get_center())
                               + (2 * i + 1) * (d2.get_center() - d1.get_center()) / len(obj))

        def new_update_5(obj):
            for i in range(0, len(obj)):
                obj[i].move_to(d1.get_center() + 4 * (d3.get_center() - d1.get_center())
                               + (2 * i + 1) * (d2.get_center() - d1.get_center()) / len(obj))

        sbtree1.add_updater(update_1)
        sbtree2.add_updater(new_update_2)
        sbtree3.add_updater(new_update_3)
        sbtree4.add_updater(new_update_4)
        sbtree5.add_updater(new_update_5)

        dashedLines0 = VGroup(
            DashedLine(start=sbtree1[0].get_right(), end=sbtree1[1].get_left(), positive_space_ratio=0.3,
                       stroke_width=LINESTROKE)
                .scale(lineScaleRatio),
            DashedLine(start=sbtree1[2].get_left(), end=sbtree1[1].get_right(), positive_space_ratio=0.3,
                       stroke_width=LINESTROKE)
                .scale(lineScaleRatio)
        )
        dashedLines0.add_updater(
            lambda obj: obj.become(
                VGroup(
                    DashedLine(start=sbtree1[0].get_right(), end=sbtree1[1].get_left(), positive_space_ratio=0.3,
                               stroke_width=LINESTROKE)
                        .scale(lineScaleRatio),
                    DashedLine(start=sbtree1[2].get_left(), end=sbtree1[1].get_right(), positive_space_ratio=0.3,
                               stroke_width=LINESTROKE)
                        .scale(lineScaleRatio)
                )
            )
        )
        lines1 = VGroup(
            Line(start=sbtree1[1].get_left(), end=sbtree2[0].get_right(), stroke_width=LINESTROKE).scale(
                lineScaleRatio),
            Line(start=sbtree1[1].get_right(), end=sbtree2[1].get_left(), stroke_width=LINESTROKE).scale(lineScaleRatio)
        )
        lines1.add_updater(
            lambda obj: obj.become(
                VGroup(
                    Line(start=sbtree1[1].get_left(), end=sbtree2[0].get_right(), stroke_width=LINESTROKE).scale(
                        lineScaleRatio),
                    Line(start=sbtree1[1].get_right(), end=sbtree2[1].get_left(), stroke_width=LINESTROKE).scale(
                        lineScaleRatio)
                )
            )
        )
        lines2 = VGroup(
            *([
                  Line(start=sbtree2[i].get_left(), end=sbtree3[i * 2].get_right(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(len(sbtree2))
              ] + [
                  Line(start=sbtree2[i].get_right(), end=sbtree3[i * 2 + 1].get_left(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(len(sbtree2))
              ])
        )
        lines2.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree2[i].get_left(), end=sbtree3[i * 2].get_right(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(len(sbtree2))
                      ] + [
                          Line(start=sbtree2[i].get_right(), end=sbtree3[i * 2 + 1].get_left(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(len(sbtree2))
                      ])
                )
            )
        )
        lines3 = VGroup(
            *([
                  Line(start=sbtree3[i].get_left(), end=sbtree4[i * 2].get_right(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(len(sbtree3))
              ] + [
                  Line(start=sbtree3[i].get_right(), end=sbtree4[i * 2 + 1].get_left(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(len(sbtree3))
              ])
        )
        lines3.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree3[i].get_left(), end=sbtree4[i * 2].get_right(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(len(sbtree3))
                      ] + [
                          Line(start=sbtree3[i].get_right(), end=sbtree4[i * 2 + 1].get_left(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(len(sbtree3))
                      ])
                )
            )
        )
        lines4 = VGroup(
            *([
                  Line(start=sbtree4[i].get_left(), end=sbtree5[i * 2].get_right(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(len(sbtree4))
              ] + [
                  Line(start=sbtree4[i].get_right(), end=sbtree5[i * 2 + 1].get_left(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(len(sbtree4))
              ])
        )
        lines4.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree4[i].get_left(), end=sbtree5[i * 2].get_right(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(len(sbtree4))
                      ] + [
                          Line(start=sbtree4[i].get_right(), end=sbtree5[i * 2 + 1].get_left(),
                               stroke_width=LINESTROKE).scale(lineScaleRatio)
                          for i in range(len(sbtree4))
                      ])
                )
            )
        )

        #
        d1.move_to([-6 - 0.3, 5 / 2 + 0.5 -10, 0])
        d3.move_to([-6 - 0.3, 5 / 2 / 2 + 0.5-10, 0])
        d2.move_to([-2.5 - 0.3, 5 / 2 + 0.5-10, 0])

        self.play(
            *[
                ApplyMethod(d1.move_to,[-6 - 0.3, 5 / 2 + 0.5, 0],run_time=2),
                ApplyMethod(d3.move_to,[-6 - 0.3, 5 / 2 / 2 + 0.5, 0],run_time=2),
                ApplyMethod(d2.move_to,[-2.5 - 0.3, 5 / 2 + 0.5, 0],run_time=2),
                FadeIn(sbtree1,run_time=2),
                FadeIn(sbtree2,run_time=2),
                FadeIn(sbtree3,run_time=2),
                FadeIn(sbtree4,run_time=2),
                FadeIn(sbtree5,run_time=2),
                FadeIn(lines1,run_time=2),
                FadeIn(lines2,run_time=2),
                FadeIn(lines3,run_time=2),
                FadeIn(lines4,run_time=2),
                FadeIn(dashedLines0,run_time=2)
            ]
        )
        self.wait(2+SLICE)

        # 其他边透明0.5,显出样例路径
        # 必须先清除updater
        lines1.clear_updaters()
        lines2.clear_updaters()
        lines3.clear_updaters()
        lines4.clear_updaters()
        sbtree1.clear_updaters()
        sbtree2.clear_updaters()
        sbtree3.clear_updaters()
        sbtree4.clear_updaters()
        sbtree5.clear_updaters()
        dashedLines0.clear_updaters()

        pause = TextMobject(r"举个栗子，比如$\frac{5}{7}$")
        pause.to_edge(DOWN)
        self.play(ShowCreation(pause))
        self.wait(2+SLICE)


        example = TexMobject(r"\frac{5}{7}", r"\Longrightarrow", "L", "R", "R", "L").move_to([3, 0, 0])
        example_later = TexMobject(r"\frac{5}{7}", r"\Longleftrightarrow", "L^1", "R^2", "L^1").move_to([3, 0, 0])
        example[0].set_color(ORANGE)
        example[2].set_color(BLUE)
        example[3].set_color(RED)
        example[4].set_color(RED)
        example[5].set_color(BLUE)
        example_later[0].set_color(ORANGE)
        example_later[2].set_color(BLUE)
        example_later[3].set_color(RED)
        example_later[4].set_color(BLUE)

        self.play(ReplacementTransform(sbtree5[6].copy(), example[0]),
                  ReplacementTransform(sbtree5[6].copy(), example[1]))
        self.wait(2+SLICE)

        self.play(ReplacementTransform(pause,explain[1]))
        self.wait(2+SLICE)

        self.play(*([
                        ApplyMethod(lines1[i].set_opacity, 0.4) for i in range(len(lines1)) if i != 0
                    ] + [
                        ApplyMethod(lines2[i].set_opacity, 0.4) for i in range(len(lines2)) if i != 2
                    ] + [
                        ApplyMethod(lines3[i].set_opacity, 0.4) for i in range(len(lines3)) if i != 5
                    ] + [
                        ApplyMethod(lines4[i].set_opacity, 0.4) for i in range(len(lines4)) if i != 3
                    ] + [
                        ApplyMethod(sbtree1[i].set_opacity, 0.4) for i in range(len(sbtree1)) if i != 1
                    ] + [
                        ApplyMethod(sbtree2[i].set_opacity, 0.4) for i in range(len(sbtree2)) if i != 0
                    ] + [
                        ApplyMethod(sbtree3[i].set_opacity, 0.4) for i in range(len(sbtree3)) if i != 1
                    ] + [
                        ApplyMethod(sbtree4[i].set_opacity, 0.4) for i in range(len(sbtree4)) if i != 3
                    ] + [
                        ApplyMethod(sbtree5[i].set_opacity, 0.4) for i in range(len(sbtree5)) if i != 6
                    ] + [
                        ApplyMethod(obj.set_opacity, 0.4) for obj in dashedLines0
                    ]))
        self.wait(1+SLICE)
        self.play(ReplacementTransform(explain[1], explain[2]))
        self.wait(3+SLICE)

        '''
        explain = VGroup(
            TextMobject("为了描述位置信息，我们需要一个好的表示方法"),
            TextMobject("从上往下看从根到该点的路径"),
            TextMobject("如果当前是往左走，则记为$L$"),
            TextMobject("如果当前是往右走，则记为$R$"),
            TextMobject(r"这样我们就用包含L和R的字符串表示了该有理数"),
            TextMobject("反过来，给出一个LR字符串"),
            TextMobject(r"也就定位了树中对应的有理数"),
            TextMobject(r"为了方便，也可以将字符串记为$uparrow$")
        )
        '''

        self.play(ReplacementTransform(lines1[0].copy(), example[2]))
        self.play(ReplacementTransform(explain[2], explain[3]))
        self.wait(2+SLICE)
        self.play(ReplacementTransform(lines2[2].copy(), example[3]))
        self.play(ReplacementTransform(explain[3], explain[4]))
        self.play(ReplacementTransform(lines3[5].copy(), example[4]))
        self.play(ReplacementTransform(lines4[3].copy(), example[5]))
        self.wait(2+SLICE)
        self.play(
            *([
                  ReplacementTransform(explain[4], explain[5])
              ] + [
                  ApplyMethod(example[i].scale, 5 / 4) for i in range(2, 6)
              ])
        )
        self.wait(1+SLICE)
        self.play(*[
            ApplyMethod(example[i].scale, 4 / 5) for i in range(2, 6)
        ])
        self.wait(1+SLICE)
        self.play(ReplacementTransform(explain[5], explain[6]),
                  Transform(example[1], example_later[1]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(explain[6], explain[7]))
        self.play(Transform(example, example_later))
        self.wait(3+SLICE)
        # 复原
        self.play(*([
                        ApplyMethod(lines1[i].set_opacity, 1) for i in range(len(lines1)) if i != 0
                    ] + [
                        ApplyMethod(lines2[i].set_opacity, 1) for i in range(len(lines2)) if i != 2
                    ] + [
                        ApplyMethod(lines3[i].set_opacity, 1) for i in range(len(lines3)) if i != 5
                    ] + [
                        ApplyMethod(lines4[i].set_opacity, 1) for i in range(len(lines4)) if i != 3
                    ] + [
                        ApplyMethod(sbtree1[i].set_opacity, 1) for i in range(len(sbtree1)) if i != 1
                    ] + [
                        ApplyMethod(sbtree2[i].set_opacity, 1) for i in range(len(sbtree2)) if i != 0
                    ] + [
                        ApplyMethod(sbtree3[i].set_opacity, 1) for i in range(len(sbtree3)) if i != 1
                    ] + [
                        ApplyMethod(sbtree4[i].set_opacity, 1) for i in range(len(sbtree4)) if i != 3
                    ] + [
                        ApplyMethod(sbtree5[i].set_opacity, 1) for i in range(len(sbtree5)) if i != 6
                    ] + [
                        ApplyMethod(obj.set_opacity, 1) for obj in dashedLines0
                    ] + [
                        Uncreate(example)
                    ] + [
                        Uncreate(explain[7])
                    ]))
        # 介绍二分
        algo = VGroup(
            TextMobject("好，可以再重新描述一下我们的问题了"),
            TextMobject(r"给一个既约分数$\displaystyle p/q \;(p,q\le 10^9)$ \\求该分数对应的LR字符串表示"),
            TextMobject(r"之前说过Stern–Brocot tree是二叉排序树"),
            TextMobject(r"天然的具有二分性质！"),
            TextMobject(r"我们每次二分记录区间左右端点"),
            TextMobject(r"然后求出mediant，即当前节点的值"),
            TextMobject(r"与$p/q$比较大小"),
            TextMobject(r"还是刚才的例子，我们演示一下"),
            TextMobject(r"$p=5,\;q=7$")
        )
        algo.to_edge(DOWN)
        algo[1].scale(0.7)
        problem = VGroup(
            TextMobject(r"给一个既约分数$\displaystyle p/q \;(p,q\le 10^9)$"),
            TextMobject(r"求该分数对应的LR字符串表示")
        )
        problem.scale(0.7)
        problem[0].move_to([1.5, 2.5 + 0.25, 0] - problem[0].get_left())
        problem[1].move_to([1.5, 2 + 0.25, 0] - problem[1].get_left())
        nodes = VGroup(
            TexMobject("{L_m", "\\over", "L_n}"),
            TexMobject("{L_m+R_m", "\\over", "L_n+R_n}"),
            TexMobject("{R_m", "\\over", "R_n}")
        )
        nodes_later = VGroup(
            TexMobject("{L_m", "\\over", "L_n}"),
            TexMobject("{x", "\\over", "y}", "=", "{L_m+R_m", "\\over", "L_n+R_n}"),
            TexMobject("{R_m", "\\over", "R_n}")
        )
        nodes.scale(0.8)
        nodes[0].move_to([2 - 0.25, 0.8 + 0.25, 0])
        nodes[1].move_to([4.25 - 0.25, 0.8 + 0.25, 0])
        nodes[2].move_to([6.5 - 0.25, 0.8 + 0.25, 0])
        nodes_later.scale(0.8)
        nodes_later[0].move_to([2 - 0.25, 0.8 + 0.25, 0])
        nodes_later[1].move_to([4.25 - 0.25, 0.8 + 0.25, 0])
        nodes_later[2].move_to([6.5 - 0.25, 0.8 + 0.25, 0])
        eq = TexMobject(
            r"\begin{cases} \text{Left}& \frac{p}{q}<\frac{x}{y} \\ \text{Right} & \frac{p}{q}>\frac{x}{y} \\ \text{End} & \frac{p}{q}=\frac{x}{y} \end{cases}")
        eq.move_to([1.5, -1.5 + 0.35, 0] - eq.get_left())
        self.play(ShowCreation(algo[0]))
        self.wait(2+SLICE)
        self.play(ReplacementTransform(algo[0], algo[1]))
        self.wait(2+SLICE)
        self.play(ReplacementTransform(algo[1], problem));
        self.wait(2+SLICE)
        self.play(ShowCreation(algo[2]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(algo[2], algo[3]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(algo[3], algo[4]))
        self.wait(2+SLICE)

        self.play(ShowCreation(VGroup(nodes[0], nodes[2])))
        self.wait(2+SLICE)

        self.play(ReplacementTransform(algo[4], algo[5]))
        self.wait(2+SLICE)
        self.play(*[
            ReplacementTransform(VGroup(nodes[0][0], nodes[2][0]).copy(), nodes[1][0]),
            ReplacementTransform(VGroup(nodes[0][1], nodes[2][1]).copy(), nodes[1][1]),
            ReplacementTransform(VGroup(nodes[0][2], nodes[2][2]).copy(), nodes[1][2])
        ])
        self.wait(2+SLICE)
        self.play(Transform(nodes, nodes_later))
        self.wait(2+SLICE)
        self.play(ReplacementTransform(algo[5], algo[6]))
        self.wait(2+SLICE)
        self.play(ReplacementTransform(algo[6], eq))
        self.wait(3+SLICE)
        self.play(ShowCreation(algo[7]))
        self.wait(3+SLICE)
        frameboxL = SurroundingRectangle(nodes[0], buff=.1, color=BLUE)
        frameboxR = SurroundingRectangle(nodes[2], buff=.1, color=RED)
        frameboxM = SurroundingRectangle(nodes[1], buff=.1, color=WHITE)
        self.play(*[
            ShowCreation(frameboxL),
            ShowCreation(frameboxR),
            ShowCreation(frameboxM),
            ReplacementTransform(algo[7], algo[8])
        ])
        self.wait(2+SLICE)
        frameboxL2 = SurroundingRectangle(sbtree1[0], buff=.1, color=BLUE, plot_depth=3)
        frameboxR2 = SurroundingRectangle(sbtree1[2], buff=.1, color=RED, plot_depth=2)
        frameboxM2 = SurroundingRectangle(sbtree1[1], buff=.1, color=WHITE, plot_depth=1)

        arrow = Arrow(sbtree5[6].get_bottom() + np.array([0, -1, 0]), sbtree5[6].get_bottom())
        self.play(
            ReplacementTransform(frameboxL.copy(), frameboxL2),
            ReplacementTransform(frameboxR.copy(), frameboxR2),
            ReplacementTransform(algo[8], arrow)
        )
        self.wait(1+SLICE)
        self.play(
            ReplacementTransform(frameboxM.copy(), frameboxM2)
        )
        self.wait(2+SLICE)
        ans = TexMobject("L^1", "R^1", "L^1").to_edge(DOWN)
        ans_later = TexMobject("L^1", "R^2", "L^1").to_edge(DOWN)
        self.play(
            ApplyMethod(frameboxR2.move_to, frameboxM2.get_center()),
            ShowCreation(ans[0])
        )
        self.wait(1+SLICE)
        self.play(ApplyMethod(frameboxM2.move_to, sbtree2[0].get_center()))
        self.wait(1+SLICE)
        self.play(
            ApplyMethod(frameboxL2.move_to, frameboxM2.get_center()),
            ShowCreation(ans[1])
        )
        self.wait(1+SLICE)
        self.play(ApplyMethod(frameboxM2.move_to, sbtree3[1].get_center()))
        self.wait(1+SLICE)
        self.play(
            ApplyMethod(frameboxL2.move_to, frameboxM2.get_center()),
            Transform(ans[1], ans_later[1])
        )
        self.wait(1+SLICE)
        self.play(ApplyMethod(frameboxM2.move_to, sbtree4[3].get_center()))
        self.wait(1+SLICE)
        self.play(
            ApplyMethod(frameboxR2.move_to, frameboxM2.get_center()),
            ShowCreation(ans[2])
        )
        self.wait(1+SLICE)
        self.play(ApplyMethod(frameboxM2.move_to, sbtree5[6].get_center()))
        self.wait(1+SLICE)

        final = VGroup(
            TextMobject(r"我们成功用二分的方法解决了这个问题"),
            TextMobject(r"然而，这个算法的时间复杂度是$O(\log{(p+q)})$吗？"),
            TextMobject(r"显然不是，刚才模拟的是一步一步往下走"),
            TextMobject(r"考虑一个极端的输入：$p=1,q=10^9$"),
            TextMobject(r"此时答案是$L^{999999999}$"),
            TextMobject(r"所以尽管用了二分，这里的时间复杂度仍然是线性$O(p+q)$"),
            TextMobject(r"如何优化呢？我们下期再说"),
            TextMobject(r"See you\textasciitilde")
        ).to_edge(DOWN)
        self.play(
            ReplacementTransform(ans, final[0]),
            Uncreate(arrow),
            Uncreate(frameboxL2),
            Uncreate(frameboxM2),
            Uncreate(frameboxR2)
        )
        self.wait(2+SLICE)
        self.play(ReplacementTransform(final[0], final[1]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(final[1], final[2]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(final[2], final[3]))
        self.wait(3+SLICE)

        dots=TextMobject("$\dots$").move_to(sbtree5[0].get_bottom()+np.array([0,-0.25,0])).scale(0.6)
        self.play(ReplacementTransform(final[3], final[4]))
        self.wait(2+SLICE)
        self.play(*([
                        ApplyMethod(lines1[i].set_opacity, 0.4) for i in range(len(lines1)) if i != 0
                    ] + [
                        ApplyMethod(lines2[i].set_opacity, 0.4) for i in range(len(lines2)) if i != 0
                    ] + [
                        ApplyMethod(lines3[i].set_opacity, 0.4) for i in range(len(lines3)) if i != 0
                    ] + [
                        ApplyMethod(lines4[i].set_opacity, 0.4) for i in range(len(lines4)) if i != 0
                    ] + [
                        ApplyMethod(sbtree1[i].set_opacity, 0.4) for i in range(len(sbtree1)) if i != 1
                    ] + [
                        ApplyMethod(sbtree2[i].set_opacity, 0.4) for i in range(len(sbtree2)) if i != 0
                    ] + [
                        ApplyMethod(sbtree3[i].set_opacity, 0.4) for i in range(len(sbtree3)) if i != 0
                    ] + [
                        ApplyMethod(sbtree4[i].set_opacity, 0.4) for i in range(len(sbtree4)) if i != 0
                    ] + [
                        ApplyMethod(sbtree5[i].set_opacity, 0.4) for i in range(len(sbtree5)) if i != 0
                    ] + [
                        ApplyMethod(obj.set_opacity, 0.4) for obj in dashedLines0
                    ] + [
                        ShowCreation(dots)
                    ]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(final[4], final[5]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(final[5], final[6]))
        self.wait(3+SLICE)
        self.play(ReplacementTransform(final[6], final[7]))
        self.wait(5)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python -m manim -p " + module_name + " SBtreeScene"
    os.system(command)
