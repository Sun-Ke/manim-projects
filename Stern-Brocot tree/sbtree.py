from manimlib.imports import *

lineScaleRatio = 0.85
fontScaleRatio = [0.7, 0.75]


class SBtreeScene(Scene):
    def construct(self):
        text = [TextMobject("什么是Stern–Brocot tree？"),
                TextMobject("话不多说，先来看一下构造过程")]
        self.play(ShowCreation(text[0]))
        self.wait(2)
        self.play(Uncreate(text[0]))
        self.play(ShowCreation(text[1]))
        self.wait()
        self.play(Uncreate(text[1]))

        text = VGroup(TextMobject(r"第一步在左边写下$\frac{0}{1}$，右边写$\frac{1}{0}$"),
                      TextMobject(r"分别代表$0$和$+\infty$"),
                      TextMobject(r"分子分母分别相加，得到$\frac{1}{1}$"),
                      TextMobject(r"并写在中间"),
                      TextMobject(r"继续构造下一层"),
                      TextMobject(r"先复制下来"),
                      TextMobject(r"还是分子分母分别相加写在中间"),
                      TextMobject(r"重复这个操作"))
        text.to_edge(DOWN)
        sbtree1 = [TexMobject("{0", "\\over", "1}"),
                   TexMobject("{1", "\\over", "1}"),
                   TexMobject("{1", "\\over", "0}")]
        sbtree1[0].move_to(4 * LEFT)
        sbtree1[2].move_to(4 * RIGHT)
        self.play(*[Write(sbtree1[0]),
                    Write(sbtree1[2]),
                    ShowCreation(text[0])],
                  run_time=2)
        self.wait()
        self.play(ReplacementTransform(text[0], text[1]))
        self.wait()
        # 第一层分子分母相加
        self.play(ReplacementTransform(VGroup(sbtree1[0][0], sbtree1[2][0]).copy(), sbtree1[1][0]),
                  ReplacementTransform(VGroup(sbtree1[2][2], sbtree1[0][2]).copy(), sbtree1[1][2]),
                  Write(sbtree1[1][1]),
                  ReplacementTransform(text[1], text[2]),
                  run_time=2)
        self.wait()
        self.play(ReplacementTransform(text[2], text[3]))
        self.wait()

        self.play(*[ApplyMethod(obj.shift, 2 * UP) for obj in sbtree1])
        self.play(*[ApplyMethod(obj.scale, fontScaleRatio[0]) for obj in sbtree1])
        self.play(ReplacementTransform(text[3], text[4]))
        self.wait()

        # second layer
        sbtree2 = [obj.copy().shift(-2 * UP) for obj in sbtree1]
        dashedLines1 = VGroup(
            *[
                DashedLine(start=sbtree1[i].get_bottom(), end=sbtree2[i].get_top(), positive_space_ratio=0.3)
                    .scale(lineScaleRatio)
                for i in range(len(sbtree1))
            ]
        )
        dashedLines1.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *[
                        DashedLine(start=sbtree1[i].get_bottom(), end=sbtree2[i].get_top(), positive_space_ratio=0.3)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree1))
                    ]
                ) if len(sbtree2) == len(sbtree1) else
                VGroup(
                    *[
                        DashedLine(start=sbtree1[i].get_bottom(), end=sbtree2[i * 2].get_top(),
                                   positive_space_ratio=0.3)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree1))
                    ]
                )
            )
        )
        self.play(ReplacementTransform(text[4], text[5]))
        self.wait()
        self.play(*([ReplacementTransform(A.copy(), B) for A, B in zip(sbtree1, sbtree2)]
                    + [ShowCreation(dashedLines1)]), run_time=3)
        self.wait()
        sbtree2.insert(2, TexMobject("{2", "\\over", "1}").move_to(2 * RIGHT).scale(fontScaleRatio[0]))
        sbtree2.insert(1, TexMobject("{1", "\\over", "2}").move_to(2 * LEFT).scale(fontScaleRatio[0]))
        # 第二层分子分母相加 0 1 2 3 4

        lines1 = VGroup(
            *([
                  Line(start=sbtree1[i].get_left(), end=sbtree2[i * 2 - 1].get_right()).scale(lineScaleRatio)
                  for i in range(1, len(sbtree1), 2)
              ] + [
                  Line(start=sbtree1[i].get_right(), end=sbtree2[i * 2 + 1].get_left()).scale(lineScaleRatio)
                  for i in range(1, len(sbtree1), 2)
              ])
        )
        lines1.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree1[i].get_left(), end=sbtree2[i * 2 - 1].get_right()).scale(lineScaleRatio)
                          for i in range(1, len(sbtree1), 2)
                      ] + [
                          Line(start=sbtree1[i].get_right(), end=sbtree2[i * 2 + 1].get_left()).scale(lineScaleRatio)
                          for i in range(1, len(sbtree1), 2)
                      ])
                )
            )
        )
        self.play(
            *([
                  TransformFromCopy(VGroup(sbtree2[i + 1][0], sbtree2[i - 1][0]), sbtree2[i][0])
                  for i in range(1, len(sbtree2), 2)
              ] + [
                  TransformFromCopy(VGroup(sbtree2[i - 1][2], sbtree2[i + 1][2]), sbtree2[i][2])
                  for i in range(1, len(sbtree2), 2)
              ] + [
                  Write(sbtree2[i][1])
                  for i in range(1, len(sbtree2), 2)
              ] + [
                  ReplacementTransform(text[5], text[6])
              ] + [
                  Write(lines1)
              ]), run_time=2)
        self.wait()

        self.play(ReplacementTransform(text[6], text[7]))
        self.wait()
        self.play(FadeOut(text[7]))
        # third layer
        sbtree3 = [obj.copy().shift(-2 * UP) for obj in sbtree2]

        dashedLines2 = VGroup(
            *[
                DashedLine(start=sbtree2[i].get_bottom(), end=sbtree3[i].get_top(), positive_space_ratio=0.3)
                    .scale(lineScaleRatio)
                for i in range(len(sbtree2))
            ]
        )
        dashedLines2.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *[
                        DashedLine(start=sbtree2[i].get_bottom(), end=sbtree3[i].get_top(), positive_space_ratio=0.3)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree2))
                    ]
                ) if len(sbtree3) == len(sbtree2) else
                VGroup(
                    *[
                        DashedLine(start=sbtree2[i].get_bottom(), end=sbtree3[i * 2].get_top(),
                                   positive_space_ratio=0.3)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree2))
                    ]
                )
            )
        )
        self.play(*([ReplacementTransform(A.copy(), B) for A, B in zip(sbtree2, sbtree3)]
                    + [ShowCreation(dashedLines2)]), run_time=3)
        self.wait()
        sbtree3.insert(4, TexMobject("{3", "\\over", "1}").move_to(2 * DOWN + 3 * RIGHT).scale(fontScaleRatio[0]))
        sbtree3.insert(3, TexMobject("{3", "\\over", "2}").move_to(2 * DOWN + 1 * RIGHT).scale(fontScaleRatio[0]))
        sbtree3.insert(2, TexMobject("{2", "\\over", "3}").move_to(2 * DOWN + 1 * LEFT).scale(fontScaleRatio[0]))
        sbtree3.insert(1, TexMobject("{1", "\\over", "3}").move_to(2 * DOWN + 3 * LEFT).scale(fontScaleRatio[0]))
        # 第三层分子分母相加 0 1 2 3 4 5 6 7 8

        lines2 = VGroup(
            *([
                  Line(start=sbtree2[i].get_left(), end=sbtree3[i * 2 - 1].get_right()).scale(lineScaleRatio)
                  for i in range(1, len(sbtree2), 2)
              ] + [
                  Line(start=sbtree2[i].get_right(), end=sbtree3[i * 2 + 1].get_left()).scale(lineScaleRatio)
                  for i in range(1, len(sbtree2), 2)
              ])
        )
        lines2.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree2[i].get_left(), end=sbtree3[i * 2 - 1].get_right()).scale(lineScaleRatio)
                          for i in range(1, len(sbtree2), 2)
                      ] + [
                          Line(start=sbtree2[i].get_right(), end=sbtree3[i * 2 + 1].get_left()).scale(lineScaleRatio)
                          for i in range(1, len(sbtree2), 2)
                      ])
                )
            )
        )
        self.play(
            *([
                  TransformFromCopy(VGroup(sbtree3[i + 1][0], sbtree3[i - 1][0]), sbtree3[i][0])
                  for i in range(1, len(sbtree3), 2)
              ] + [
                  TransformFromCopy(VGroup(sbtree3[i - 1][2], sbtree3[i + 1][2]), sbtree3[i][2])
                  for i in range(1, len(sbtree3), 2)
              ] + [
                  Write(sbtree3[i][1])
                  for i in range(1, len(sbtree3), 2)
              ] + [
                  Write(lines2)
              ]), run_time=2)
        self.wait()
        # 5 * 11
        H, W = 5, 11
        nsbtree1 = [obj.copy() for obj in sbtree1]
        nsbtree2 = [obj.copy() for obj in sbtree2]
        nsbtree3 = [obj.copy() for obj in sbtree3]
        for i in range(len(nsbtree1)):
            nsbtree1[i].scale(fontScaleRatio[1])
            nsbtree1[i].move_to(
                -0.25 * UP + H / 3 * 2 * UP + (i - len(nsbtree1) // 2) * (W / (len(nsbtree1) - 1)) * RIGHT)
        for i in range(len(nsbtree2)):
            nsbtree2[i].scale(fontScaleRatio[1])
            nsbtree2[i].move_to(-0.25 * UP + H / 3 * UP + (i - len(nsbtree2) // 2) * (W / (len(nsbtree2) - 1)) * RIGHT)
        for i in range(len(nsbtree3)):
            nsbtree3[i].scale(fontScaleRatio[1])
            nsbtree3[i].move_to(
                -0.25 * UP + H / 3 * 0 * UP + (i - len(nsbtree3) // 2) * (W / (len(nsbtree3) - 1)) * RIGHT)

        self.play(
            *([
                  Transform(A, B) for A, B in zip(sbtree1, nsbtree1)
              ] + [
                  Transform(A, B) for A, B in zip(sbtree2, nsbtree2)
              ] + [
                  Transform(A, B) for A, B in zip(sbtree3, nsbtree3)
              ]), run_time=2)
        self.wait()

        # fourth layer
        sbtree4 = [obj.copy().shift(H / 3 * DOWN) for obj in sbtree3]
        dashedLines3 = VGroup(
            *[
                DashedLine(start=sbtree3[i].get_bottom(), end=sbtree4[i].get_top(), positive_space_ratio=0.3)
                    .scale(lineScaleRatio)
                for i in range(len(sbtree3))
            ]
        )
        dashedLines3.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *[
                        DashedLine(start=sbtree3[i].get_bottom(), end=sbtree4[i].get_top(), positive_space_ratio=0.3)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree3))
                    ]
                ) if len(sbtree3) == len(sbtree4) else
                VGroup(
                    *[
                        DashedLine(start=sbtree3[i].get_bottom(), end=sbtree4[i * 2].get_top(),
                                   positive_space_ratio=0.3)
                            .scale(lineScaleRatio)
                        for i in range(len(sbtree3))
                    ]
                )
            )
        )

        self.play(*([ReplacementTransform(A.copy(), B) for A, B in zip(sbtree3, sbtree4)]
                    + [ShowCreation(dashedLines3)]), run_time=3)
        self.wait()
        sbtree4.insert(8, TexMobject("{4", "\\over", "1}")
                       .move_to(-0.25 * UP + H / 3 * DOWN + (15 - 17 // 2) * (W / (17 - 1)) * RIGHT)
                       .scale(fontScaleRatio[0] * fontScaleRatio[1]))
        sbtree4.insert(7, TexMobject("{5", "\\over", "2}")
                       .move_to(-0.25 * UP + H / 3 * DOWN + (13 - 17 // 2) * (W / (17 - 1)) * RIGHT)
                       .scale(fontScaleRatio[0] * fontScaleRatio[1]))
        sbtree4.insert(6, TexMobject("{5", "\\over", "3}")
                       .move_to(-0.25 * UP + H / 3 * DOWN + (11 - 17 // 2) * (W / (17 - 1)) * RIGHT)
                       .scale(fontScaleRatio[0] * fontScaleRatio[1]))
        sbtree4.insert(5, TexMobject("{4", "\\over", "3}")
                       .move_to(-0.25 * UP + H / 3 * DOWN + (9 - 17 // 2) * (W / (17 - 1)) * RIGHT)
                       .scale(fontScaleRatio[0] * fontScaleRatio[1]))
        sbtree4.insert(4, TexMobject("{3", "\\over", "4}")
                       .move_to(-0.25 * UP + H / 3 * DOWN + (7 - 17 // 2) * (W / (17 - 1)) * RIGHT)
                       .scale(fontScaleRatio[0] * fontScaleRatio[1]))
        sbtree4.insert(3, TexMobject("{3", "\\over", "5}")
                       .move_to(-0.25 * UP + H / 3 * DOWN + (5 - 17 // 2) * (W / (17 - 1)) * RIGHT)
                       .scale(fontScaleRatio[0] * fontScaleRatio[1]))
        sbtree4.insert(2, TexMobject("{2", "\\over", "5}")
                       .move_to(-0.25 * UP + H / 3 * DOWN + (3 - 17 // 2) * (W / (17 - 1)) * RIGHT)
                       .scale(fontScaleRatio[0] * fontScaleRatio[1]))
        sbtree4.insert(1, TexMobject("{1", "\\over", "4}")
                       .move_to(-0.25 * UP + H / 3 * DOWN + (1 - 17 // 2) * (W / (17 - 1)) * RIGHT)
                       .scale(fontScaleRatio[0] * fontScaleRatio[1]))

        lines3 = VGroup(
            *([
                  Line(start=sbtree3[i].get_left(), end=sbtree4[i * 2 - 1].get_right()).scale(lineScaleRatio)
                  for i in range(1, len(sbtree3), 2)
              ] + [
                  Line(start=sbtree3[i].get_right(), end=sbtree4[i * 2 + 1].get_left()).scale(lineScaleRatio)
                  for i in range(1, len(sbtree3), 2)
              ])
        )
        lines3.add_updater(
            lambda obj: obj.become(
                VGroup(
                    *([
                          Line(start=sbtree3[i].get_left(), end=sbtree4[i * 2 - 1].get_right()).scale(lineScaleRatio)
                          for i in range(1, len(sbtree3), 2)
                      ] + [
                          Line(start=sbtree3[i].get_right(), end=sbtree4[i * 2 + 1].get_left()).scale(lineScaleRatio)
                          for i in range(1, len(sbtree3), 2)
                      ])
                )
            )
        )
        self.play(
            *([
                  TransformFromCopy(VGroup(sbtree4[i + 1][0], sbtree4[i - 1][0]), sbtree4[i][0])
                  for i in range(1, len(sbtree4), 2)
              ] + [
                  TransformFromCopy(VGroup(sbtree4[i - 1][2], sbtree4[i + 1][2]), sbtree4[i][2])
                  for i in range(1, len(sbtree4), 2)
              ] + [
                  Write(sbtree4[i][1])
                  for i in range(1, len(sbtree4), 2)
              ] + [
                  Write(lines3)
              ]), run_time=2)

        explain = [TextMobject("观察下这棵树的结构"),
                   TextMobject("可以说Stern–Brocot tree是一个", r"\textbf{无限的完全二叉树}"),
                   TextMobject("再来看一下每个节点的权值大小"),
                   TextMobject("Stern–Brocot tree也是", r"\textbf{二叉排序树}"),
                   TextMobject("实际上，考虑其", r"\textbf{中序遍历}", "构成的序列"),
                   TextMobject(r"就从小到大的展示了", r"\textbf{所有的正有理数}", r"\\（注意到这个树是无限的）")
                   ]
        pause = [TextMobject("发现了么？"),
                 TextMobject("好，让我们看一些有意思的性质"),
                 TextMobject("可以发现"),
                 TextMobject("那么有以下性质...")]
        explain[1][1].set_color(color=GOLD_C)
        explain[3][1].set_color(color=GOLD_C)
        explain[4][1].set_color(color=RED)
        explain[5][1].set_color(color=RED)
        for obj in explain:
            obj.to_edge(DOWN)
        for obj in pause:
            obj.to_edge(DOWN)
        self.play(ShowCreation(explain[0]))
        self.wait(3)
        self.play(ReplacementTransform(explain[0], explain[1]))
        self.wait(3)
        self.play(ReplacementTransform(explain[1], explain[2]))
        self.wait(3)
        self.play(
            *([
                  ApplyMethod(sbtree1[i].set_color, ORANGE)
                  for i in range(1, len(sbtree1), 2)
              ] + [
                  ApplyMethod(sbtree2[i].set_color, ORANGE)
                  for i in range(1, len(sbtree2), 2)
              ] + [
                  ApplyMethod(sbtree3[i].set_color, ORANGE)
                  for i in range(1, len(sbtree3), 2)
              ] + [
                  ApplyMethod(sbtree4[i].set_color, ORANGE)
                  for i in range(1, len(sbtree4), 2)
              ] + [
                  ReplacementTransform(explain[2], pause[0])
              ]))
        self.wait(3)

        self.play(ReplacementTransform(pause[0], explain[3]))
        self.wait(3)
        self.play(
            *([
                  ApplyMethod(sbtree1[i].set_color, WHITE)
                  for i in range(1, len(sbtree1), 2)
              ] + [
                  ApplyMethod(sbtree2[i].set_color, WHITE)
                  for i in range(1, len(sbtree2), 2)
              ] + [
                  ApplyMethod(sbtree3[i].set_color, WHITE)
                  for i in range(1, len(sbtree3), 2)
              ] + [
                  ApplyMethod(sbtree4[i].set_color, WHITE)
                  for i in range(1, len(sbtree4), 2)
              ] + [
                  ReplacementTransform(explain[3], explain[4])
              ]))
        self.wait(2)
        self.play(*[
            ApplyMethod(sbtree4[i].set_color, ORANGE)
            for i in range(1, len(sbtree4) - 1)
        ])
        self.wait(2)
        self.play(ReplacementTransform(explain[4], explain[5]))
        self.wait(2)
        self.play(*([
                        ApplyMethod(sbtree4[i].set_color, WHITE)
                        for i in range(1, len(sbtree4) - 1)
                    ] + [
                        ReplacementTransform(explain[5], pause[1])
                    ]))
        self.wait(2)

        # add_updater用for循环会出错，会都绑到最后一个元素上
        sbtree1[2].add_updater(lambda obj: obj.move_to(2 * sbtree1[1].get_center() - sbtree1[0].get_center()))

        sbtree2[1].add_updater(lambda obj: obj.move_to(
            sbtree2[0].get_center() + 1 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (len(sbtree2) - 1)))

        sbtree2[2].add_updater(lambda obj: obj.move_to(
            sbtree2[0].get_center() + 2 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (len(sbtree2) - 1)))
        sbtree2[3].add_updater(lambda obj: obj.move_to(
            sbtree2[0].get_center() + 3 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (len(sbtree2) - 1)))
        sbtree2[4].add_updater(lambda obj: obj.move_to(
            sbtree2[0].get_center() + 4 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (len(sbtree2) - 1)))

        sbtree3[0].add_updater(lambda obj: obj.move_to(2 * sbtree2[0].get_center() - sbtree1[0].get_center()))
        sbtree3[1].add_updater(lambda obj:
                               obj.move_to(sbtree3[0].get_center() +
                                           1 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree3) - 1))
                               )
        sbtree3[2].add_updater(lambda obj:
                               obj.move_to(sbtree3[0].get_center() +
                                           2 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree3) - 1))
                               )
        sbtree3[3].add_updater(lambda obj:
                               obj.move_to(sbtree3[0].get_center() +
                                           3 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree3) - 1))
                               )
        sbtree3[4].add_updater(lambda obj:
                               obj.move_to(sbtree3[0].get_center() +
                                           4 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree3) - 1))
                               )
        sbtree3[5].add_updater(lambda obj:
                               obj.move_to(sbtree3[0].get_center() +
                                           5 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree3) - 1))
                               )
        sbtree3[6].add_updater(lambda obj:
                               obj.move_to(sbtree3[0].get_center() +
                                           6 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree3) - 1))
                               )
        sbtree3[7].add_updater(lambda obj:
                               obj.move_to(sbtree3[0].get_center() +
                                           7 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree3) - 1))
                               )
        sbtree3[8].add_updater(lambda obj:
                               obj.move_to(sbtree3[0].get_center() +
                                           8 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree3) - 1))
                               )
        sbtree4[0].add_updater(
            lambda obj: obj.move_to(sbtree3[0].get_center() + sbtree2[0].get_center() - sbtree1[0].get_center()))

        sbtree4[1].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           1 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[2].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           2 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[3].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           3 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[4].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           4 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[5].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           5 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[6].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           6 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[7].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           7 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[8].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           8 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[9].add_updater(lambda obj:
                               obj.move_to(sbtree4[0].get_center() +
                                           9 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                   len(sbtree4) - 1))
                               )
        sbtree4[10].add_updater(lambda obj:
                                obj.move_to(sbtree4[0].get_center() +
                                            10 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                    len(sbtree4) - 1))
                                )
        sbtree4[11].add_updater(lambda obj:
                                obj.move_to(sbtree4[0].get_center() +
                                            11 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                    len(sbtree4) - 1))
                                )
        sbtree4[12].add_updater(lambda obj:
                                obj.move_to(sbtree4[0].get_center() +
                                            12 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                    len(sbtree4) - 1))
                                )
        sbtree4[13].add_updater(lambda obj:
                                obj.move_to(sbtree4[0].get_center() +
                                            13 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                    len(sbtree4) - 1))
                                )
        sbtree4[14].add_updater(lambda obj:
                                obj.move_to(sbtree4[0].get_center() +
                                            14 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                    len(sbtree4) - 1))
                                )
        sbtree4[15].add_updater(lambda obj:
                                obj.move_to(sbtree4[0].get_center() +
                                            15 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                    len(sbtree4) - 1))
                                )
        sbtree4[16].add_updater(lambda obj:
                                obj.move_to(sbtree4[0].get_center() +
                                            16 * 2 * (sbtree1[1].get_center() - sbtree1[0].get_center()) / (
                                                    len(sbtree4) - 1))
                                )

        '''
        
        for i in range(1,len(sbtree4)):
            sbtree4[i].add_updater(lambda obj:
                obj.move_to(sbtree4[0].get_center() +
                            i*2*(sbtree1[1].get_center()-sbtree1[0].get_center())/(len(sbtree4)-1))
            )
        '''
        self.play(*[ApplyMethod(sbtree1[0].move_to, [-6, 4.5 / 2, 0]),
                    ApplyMethod(sbtree2[0].move_to, [-6, 4.5 / 3 / 2, 0]),
                    ApplyMethod(sbtree1[1].move_to, [-2.5, 4.5 / 2, 0])
                    ])
        self.wait()
        self.play(Uncreate(pause[1]))
        self.wait()
        final = [TextMobject(r"记树中的一个节点$\frac{y}{x}$"),
                 TextMobject(r"它是由$\frac{L_m}{L_n},\frac{R_m}{R_n}$这两个数产生的"),
                 TextMobject(r"$x$与$y$互质"),
                 TextMobject(r"$\frac{L_m}{L_n}$是位于左上方且离它最近的祖先"),
                 TextMobject(r"$\frac{R_m}{R_n}$是位于右上方且离它最近的祖先"),
                 TextMobject(r"$R_mL_n-L_mR_n=1$"),
                 TextMobject(r"以$\frac{y}{x}$为根的子树中的所有数"),
                 TextMobject(r"都落在区间$(\frac{L_m}{L_n},\frac{R_m}{R_n})$中")]
        right = [TextMobject(r"记树中的一个节点$\frac{y}{x}$"),
                 TextMobject(r"它是由$\frac{L_m}{L_n},\frac{R_m}{R_n}$这两个数产生的"),
                 TextMobject(r"$\bullet$ $gcd(x,y)=1$"),
                 TextMobject(r"$\bullet$ $\frac{L_m}{L_n}$是位于左上方且离它最近的祖先"),
                 TextMobject(r"$\bullet$ $\frac{R_m}{R_n}$是位于右上方且离它最近的祖先"),
                 TextMobject(r"$\bullet$ $R_mL_n-L_mR_n=1$"),
                 TextMobject(r"$\bullet$以$\frac{y}{x}$为根的子树中的所有数"),
                 TextMobject(r"都落在区间$(\frac{L_m}{L_n},\frac{R_m}{R_n})$中")]
        for obj in right:
            obj.scale(0.6)
        right[0].move_to([1.6, 2, 0] - right[0].get_left())
        for i in range(1, len(right)):
            right[i].move_to(right[i - 1].get_left() + 0.6 * DOWN - right[i].get_left())

        for obj in final:
            obj.to_edge(DOWN)

        for i in range(5):
            self.play(ShowCreation(final[i]))
            self.wait(2)
            self.play(ReplacementTransform(final[i], right[i]))
            self.wait()
            if i == 1:
                example = TextMobject(r"即$y=L_m+R_m,x=L_n+R_n$").to_edge(DOWN)
                self.play(ShowCreation(example))
                self.wait(2)
                self.play(Uncreate(example))
                self.wait()
                self.play(ShowCreation(pause[3]))
                self.wait(2)
                self.play(Uncreate(pause[3]))
                self.wait(2)

        framebox = SurroundingRectangle(sbtree4[11], buff=.1, color=ORANGE)
        frameboxL = SurroundingRectangle(sbtree4[10], buff=.1, color=ORANGE)
        frameboxR = SurroundingRectangle(sbtree4[12], buff=.1, color=ORANGE)
        frameboxLU = SurroundingRectangle(sbtree3[5], buff=.1, color=ORANGE)
        frameboxRU = SurroundingRectangle(sbtree2[3], buff=.1, color=ORANGE)
        self.play(ShowCreation(framebox))
        self.wait(2)
        self.play(*[
            ReplacementTransform(framebox.copy(), frameboxL),
            ReplacementTransform(framebox.copy(), frameboxR)
        ])
        self.play(*[
            ReplacementTransform(frameboxL, frameboxLU),
            ReplacementTransform(frameboxR, frameboxRU)
        ])
        self.wait(2)
        self.play(*[
            Uncreate(framebox),
            Uncreate(frameboxLU),
            Uncreate(frameboxRU),
        ])
        self.wait()

        self.play(ShowCreation(final[5]))
        self.wait(2)
        self.play(ReplacementTransform(final[5], right[5]))
        self.wait()
        self.play(
            *[
                ApplyMethod(sbtree2[3].scale, 3 / 2),
                ApplyMethod(sbtree3[5].scale, 3 / 2),
            ])
        self.play(
            *[
                ApplyMethod(sbtree2[3].scale, 2 / 3),
                ApplyMethod(sbtree3[5].scale, 2 / 3),
            ])
        self.wait()

        example = TextMobject("$2$", r"$\times$", "$2$", "$-$", "$3$", r"$\times$", "$1$", "$=1$").to_edge(DOWN)
        self.play(*[
            ReplacementTransform(sbtree2[3][0].copy(), example[0]),
            ReplacementTransform(sbtree3[5][2].copy(), example[2]),
            ReplacementTransform(sbtree3[5][0].copy(), example[4]),
            ReplacementTransform(sbtree2[3][2].copy(), example[6]),
            Write(example[1]),
            Write(example[3]),
            Write(example[5]),
            Write(example[7]),
        ], run_time=2)
        self.wait()
        self.play(Uncreate(example))
        self.wait()
        self.play(ShowCreation(final[6]))
        self.wait(2)
        self.play(ReplacementTransform(final[6], final[7]))
        self.wait(2)
        self.play(ReplacementTransform(final[7], VGroup(right[6], right[7])))
        self.wait(2)

        framebox = SurroundingRectangle(sbtree3[3], buff=.1, color=ORANGE)
        frameboxA = SurroundingRectangle(VGroup(sbtree3[3], sbtree4[5], sbtree4[7]), buff=.1, color=ORANGE)
        frameboxL = SurroundingRectangle(sbtree3[2], buff=.1, color=ORANGE)
        frameboxR = SurroundingRectangle(sbtree3[4], buff=.1, color=ORANGE)
        frameboxLU = SurroundingRectangle(sbtree2[1], buff=.1, color=ORANGE)
        frameboxRU = SurroundingRectangle(sbtree1[1], buff=.1, color=ORANGE)
        self.play(ShowCreation(framebox))
        self.wait()
        self.play(*[
            ReplacementTransform(framebox.copy(), frameboxL),
            ReplacementTransform(framebox.copy(), frameboxR),
        ])
        self.wait()
        self.play(*[
            ReplacementTransform(framebox, frameboxA),
            ReplacementTransform(frameboxL, frameboxLU),
            ReplacementTransform(frameboxR, frameboxRU)
        ])
        self.wait(2)

        example = TextMobject(r"$\forall x \in T(\frac{2}{3})$,", r"$\frac{1}{2}$", r"$<$", r"$x$", r"$<$",
                              r"$\frac{1}{1}$").to_edge(DOWN)
        self.play(*[
            ReplacementTransform(sbtree2[1].copy(), example[1]),
            ReplacementTransform(VGroup(sbtree3[3], sbtree4[5], sbtree4[7]).copy(), example[3]),
            ReplacementTransform(sbtree1[1].copy(), example[5]),
            Write(example[0]),
            Write(example[2]),
            Write(example[4]),
        ], run_time=2)
        self.wait(2)

        self.play(*[
            Uncreate(frameboxA),
            Uncreate(frameboxLU),
            Uncreate(frameboxRU),
        ])
        self.wait()
        self.play(Uncreate(example))
        self.wait()

        endword = [TextMobject("ok，这期视频先介绍到这里"),
                   TextMobject("下期讲讲竞赛中Stern–Brocot tree的应用"),
                   TextMobject(r"See you\textasciitilde")]
        for obj in endword:
            obj.to_edge(DOWN)
            self.play(ShowCreation(obj))
            self.wait(2)
            self.play(Uncreate(obj))
            self.wait()

        self.play(FadeOut(VGroup(*right)))
        self.wait()

        self.play(*[ApplyMethod(sbtree1[0].move_to, [-5, 5 / 2, 0]),
                    ApplyMethod(sbtree2[0].move_to, [-5, 5 / 3 / 2, 0]),
                    ApplyMethod(sbtree1[1].move_to, [0, 5 / 2, 0])
                    ])
        self.wait(5)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python -m manim -p -n 135 " + module_name + " SBtreeScene"
    os.system(command)
