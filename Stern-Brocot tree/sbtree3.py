from manimlib.imports import *

lineScaleRatio = 0.85
fontScaleRatio = 0.7 * 0.75 * 0.9
d1 = Dot([-100, 0, 0])
d2 = Dot([-100, 0, 0])
d3 = Dot([-100, 0, 0])
LINESTROKE = 3


class SBtreeScene(Scene):
    def construct(self):
        # d1,d2,d3 for position
        d1 = Dot([-100, 0, 0])
        d2 = Dot([-100, 0, 0])
        d3 = Dot([-100, 0, 0])

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
        sbtree1.scale(fontScaleRatio)
        sbtree2.scale(fontScaleRatio)
        sbtree3.scale(fontScaleRatio)
        sbtree4.scale(fontScaleRatio)
        sbtree5.scale(fontScaleRatio)

        def update_1(obj):
            obj[0].move_to(d1.get_center())
            obj[1].move_to(d2.get_center())
            obj[2].move_to(2 * d2.get_center() - d1.get_center())

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
        # 空白2秒
        self.play(ShowCreation(d1), ShowCreation(d2), ShowCreation(d3))
        self.play(Uncreate(d1), Uncreate(d2), Uncreate(d3))

        d1.move_to([-6 - 0.3, 5 / 2 + 0.5 - 10, 0])
        d3.move_to([-6 - 0.3, 5 / 2 / 2 + 0.5 - 10, 0])
        d2.move_to([-2.5 - 0.3, 5 / 2 + 0.5 - 10, 0])

        self.play(
                FadeIn(sbtree1),
                FadeIn(sbtree2),
                FadeIn(sbtree3),
                FadeIn(sbtree4),
                FadeIn(sbtree5),
                FadeIn(lines1),
                FadeIn(lines2),
                FadeIn(lines3),
                FadeIn(lines4),
                FadeIn(dashedLines0)
        )
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
        # 整个树从下往上出现在左边
        self.play(
                ApplyMethod(sbtree1.shift, 10*UP, run_time=3),
                ApplyMethod(sbtree2.shift, 10*UP, run_time=3),
                ApplyMethod(sbtree3.shift, 10*UP, run_time=3),
                ApplyMethod(sbtree4.shift, 10*UP, run_time=3),
                ApplyMethod(sbtree5.shift, 10*UP, run_time=3),
                ApplyMethod(lines1.shift, 10*UP, run_time=3),
                ApplyMethod(lines2.shift, 10*UP, run_time=3),
                ApplyMethod(lines3.shift, 10*UP, run_time=3),
                ApplyMethod(lines4.shift, 10*UP, run_time=3),
                ApplyMethod(dashedLines0.shift, 10*UP, run_time=3)
        )


        
        problem = VGroup(
            TextMobject(r"给一个既约分数$\displaystyle p/q \;(p,q\le 10^9)$"),
            TextMobject(r"求该分数对应的LR字符串表示")
        )
        problem.scale(0.7)
        problem[0].move_to([1.5, 2.5 + 0.25, 0] - problem[0].get_left())
        problem[1].move_to([1.5, 2 + 0.25, 0] - problem[1].get_left())

        text = VGroup(
            TextMobject("继续考虑之前的问题"),
            TextMobject("为了改进一步一步的暴力二分"),
            TextMobject("考虑能否一段一段的走"),
            TextMobject("即每次直接走到下一个拐点"),
            TextMobject(r"就像这样求出$5/7$的答案"),
            TextMobject(r"后面会证明拐点个数是$O(\log N)$级别的"),
            TextMobject(r"那么如何快速找到拐点呢？"),
        ).to_edge(DOWN)

        self.play(ShowCreation(text[0]))
        self.wait(2.5)
        self.play(ShowCreation(problem))
        self.wait(2.5)
        self.play(ReplacementTransform(text[0], text[1]))
        self.wait(2.5)
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
        self.wait(2.5)
        self.play(ReplacementTransform(text[1], text[2]))
        self.wait(1.5)
        self.play(ApplyMethod(lines1[0].set_color, BLUE), run_time=2 / 3)
        self.play(
            ApplyMethod(lines2[2].set_color, RED),
            ApplyMethod(lines3[5].set_color, RED),
            run_time=2 / 3
        )
        self.play(ApplyMethod(lines4[3].set_color, BLUE), run_time=2 / 3)
        self.play(ReplacementTransform(text[2], text[3]))
        self.wait(1.5)
        arrows = VGroup(
            CurvedArrow(sbtree1[1].get_left(), sbtree2[0].get_right(), color=BLUE, angle=PI / 5),
            CurvedArrow(sbtree2[0].get_left(), sbtree4[3].get_left(), color=RED, angle=PI / 5),
            CurvedArrow(sbtree4[3].get_left(), sbtree5[6].get_left(), color=BLUE, angle=PI / 5)
        )
        for obj in arrows:
            self.play(ShowCreation(obj), run_time=2 / 3)
        self.wait(1.5)
        self.play(ReplacementTransform(text[3], text[4]))
        self.wait(1.5)
        ans = TexMobject("L^1", "R^2", "L^1")
        ans.move_to(problem[1].get_center() + 2.5 * DOWN)
        ans[0].set_color(color=BLUE)
        ans[1].set_color(color=RED)
        ans[2].set_color(color=BLUE)
        self.play(
            ReplacementTransform(arrows, ans)
        )
        self.wait(2.5)
        self.play(ReplacementTransform(text[4], text[5]))
        self.wait(2.5)
        self.play(ReplacementTransform(text[5], text[6]))
        self.wait(2.5)
        # 复原
        self.play(FadeOut(ans))
        self.wait(1.5)
        remind = VGroup(
            TextMobject("很简单，回顾之前的二分过程"),
            TextMobject(r"我们需要记录代表当前子树范围的区间端点"),
            TextMobject("通过分子分母分别相加得到当前节点的值"),
            TextMobject("然后判断和p/q的大小关系选择左或者右"),
            TextMobject("那么如果我需要连续往左走呢？")
        )
        remind.to_edge(DOWN)
        self.play(ReplacementTransform(text[6], remind[0]))
        self.wait(2.5)
        nodes = VGroup(
            TexMobject("{L_m", "\\over", "L_n}"),
            TexMobject("{L_m+R_m", "\\over", "L_n+R_n}"),
            TexMobject("{R_m", "\\over", "R_n}")
        )
        nodes.scale(0.65)
        nodes[0].move_to([2 - 0.25, 0.8 + 0.25, 0])
        nodes[1].move_to([4.25 - 0.25, 0.8 + 0.25, 0])
        nodes[2].move_to([6.5 - 0.25, 0.8 + 0.25, 0])
        lnode = TexMobject(r"({L_m \over L_n},{L_m+R_m \over L_n+R_n})").scale(0.65)
        rnode = TexMobject(r"({L_m+R_m \over L_n+R_n},{R_m \over R_n})").scale(0.65)
        lnode.move_to([4 - 1.2 - 0.25, 0.8 + 0.25 - 1.6, 0])
        rnode.move_to([4 + 1.2 + 0.25, 0.8 + 0.25 - 1.6, 0])
        node = TexMobject(r"({L_m \over L_n},{R_m \over R_n})").scale(0.65)
        node.move_to([4, 0.8 + 0.25, 0])

        self.play(
            ReplacementTransform(sbtree1[0].copy(), nodes[0]),
            ReplacementTransform(sbtree1[2].copy(), nodes[2])
        )
        self.wait(2.5)
        self.play(ReplacementTransform(remind[0], remind[1]))
        self.wait(2.5)
        self.play(*[
            ReplacementTransform(VGroup(nodes[0][0], nodes[2][0]).copy(), nodes[1][0]),
            ReplacementTransform(VGroup(nodes[0][1], nodes[2][1]).copy(), nodes[1][1]),
            ReplacementTransform(VGroup(nodes[0][2], nodes[2][2]).copy(), nodes[1][2])
        ])
        self.wait(2.5)
        self.play(ReplacementTransform(remind[1], remind[2]))
        self.wait(2.5)
        self.play(
            ReplacementTransform(VGroup(nodes[0], nodes[1]).copy(), lnode),
            ReplacementTransform(VGroup(nodes[2], nodes[1]).copy(), rnode)
        )
        self.wait(1.5)
        self.play(ReplacementTransform(nodes, node))
        self.wait(2.5)
        self.play(ReplacementTransform(remind[2], remind[3]))
        self.wait(2.5)
        self.play(ReplacementTransform(remind[3], remind[4]))
        self.wait(2.5)

        # 树往左移
        self.play(
            *[
                FadeOutAndShift(sbtree1, direction=3 * LEFT),
                FadeOutAndShift(sbtree2, direction=3 * LEFT),
                FadeOutAndShift(sbtree3, direction=3 * LEFT),
                FadeOutAndShift(sbtree4, direction=3 * LEFT),
                FadeOutAndShift(sbtree5, direction=3 * LEFT),
                FadeOutAndShift(lines1, direction=3 * LEFT),
                FadeOutAndShift(lines2, direction=3 * LEFT),
                FadeOutAndShift(lines3, direction=3 * LEFT),
                FadeOutAndShift(lines4, direction=3 * LEFT),
                FadeOutAndShift(dashedLines0, direction=3 * LEFT),
                ApplyMethod(problem[0].shift, problem[0].get_center()[0] * LEFT),
                ApplyMethod(problem[1].shift, problem[1].get_center()[0] * LEFT),
                ApplyMethod(node.shift, 4 * LEFT),
                ApplyMethod(lnode.move_to, [-2.5, 0.8 + 0.25 - 1.6, 0]),
                ApplyMethod(rnode.move_to, [2.5, 0.8 + 0.25 - 1.6, 0]),
            ]
        )
        # 偷偷复原
        sbtree1.set_opacity(1)
        sbtree2.set_opacity(1)
        sbtree3.set_opacity(1)
        sbtree4.set_opacity(1)
        sbtree5.set_opacity(1)
        lines1.set_opacity(1).set_color(WHITE)
        lines2.set_opacity(1).set_color(WHITE)
        lines3.set_opacity(1).set_color(WHITE)
        lines4.set_opacity(1).set_color(WHITE)
        dashedLines0.set_opacity(1)

        self.wait(2.5)

        frame = SurroundingRectangle(lnode, buff=0.3, color=BLUE)
        self.play(ShowCreation(frame))
        self.wait(1.5)
        # 往左递归走
        point_mid = node.get_center()
        point_l = lnode.get_center()
        point_r = rnode.get_center()
        new_lnode = TexMobject(r"({L_m \over L_n},{2L_m+R_m \over 2L_n+R_n})").scale(0.65)
        new_rnode = TexMobject(r"({2L_m+R_m \over 2L_n+R_n},{L_m+R_m \over L_n+R_n})").scale(0.65)
        new_lnode.move_to(point_l)
        new_rnode.move_to(point_r)
        # 还需调整缩放大小
        time_slice = 1.0
        time_wait = 0.2
        for i in range(7):
            node.generate_target()
            node.target.scale(1.3).shift(1.5*(point_l - [-2.5 - 1.5, 0.8 + 0.25 - 1.6 - 1, 0])).fade(1)
            rnode.generate_target()
            rnode.target.scale(1.3).shift(1.5*(point_r - [-2.5 + 1.5 + 0.25, 0.8 + 0.25 - 1.6 - 1, 0])).fade(1)
            self.play(
                MoveToTarget(node,run_time=time_slice),
                MoveToTarget(rnode,run_time=time_slice),
                #FadeOutAndShift(node, direction=point_l - [-2.5 - 1.5, 0.8 + 0.25 - 1.6 - 1, 0], run_time=time_slice),
                #FadeOutAndShift(rnode, direction=point_r - [-2.5 + 1.5 + 0.25, 0.8 + 0.25 - 1.6 - 1, 0],run_time=time_slice),
                ApplyMethod(lnode.move_to, point_mid, run_time=time_slice),
                FadeInFromPoint(new_lnode, [-2.5 - 1.5, 0.8 + 0.25 - 1.6 - 1, 0] , run_time=time_slice),
                FadeInFromPoint(new_rnode, [-2.5 + 1.5 + 0.25, 0.8 + 0.25 - 1.6 - 1, 0],
                           run_time=time_slice),
            )
            self.wait(time_wait)
            if i < 3:
                time_wait *= 0.8
                time_slice *= 0.8
            else:
                time_wait /= 0.8
                time_slice /= 0.8
            if i == 6:
                break
            node = lnode
            rnode = new_rnode
            lnode = new_lnode
            new_lnode = TexMobject(
                r"({L_m \over L_n},{" + str(i + 3) + r"L_m+R_m \over " + str(i + 3) + r"L_n+R_n})").scale(0.65)
            new_rnode = TexMobject(r"({" + str(i + 3) + r"L_m+R_m \over " + str(i + 3) + r"L_n+R_n},{" + str(
                i + 2) + r"L_m+R_m \over " + str(i + 2) + r"L_n+R_n})").scale(0.65)
            new_lnode.move_to(point_l)
            new_rnode.move_to(point_r)

        self.wait(1.5)


        proof = VGroup(
            TextMobject("发现规律了吧，那直接设往左走了$k$步"),
            TextMobject("开始推导..."),
            TextMobject("正的除过去，不等号方向不变"),
            TextMobject(r"这样我们就$O(1)$求出了往左能迈出的最大步数"),
            TextMobject("往右的话也是同理，优化完成"),
            TextMobject("我们来证明一下这样的复杂度为什么是$O(\log N)$"),
        )
        proof.to_edge(DOWN)
        self.play(ReplacementTransform(remind[4], proof[0]))
        self.wait(2.5)
        knode = TexMobject(r"({L_m \over L_n},{kL_m+R_m \over kL_n+R_n})").scale(0.65)
        knode.move_to([0, 0.8 + 0.25 - 1.6, 0])
        self.play(
            FadeOut(lnode),
            FadeOut(new_rnode),
            ApplyMethod(frame.move_to, [0, 0.8 + 0.25 - 1.6, 0]),
            ReplacementTransform(new_lnode, knode)
        )
        self.wait(2.5)
        self.play(
            ApplyMethod(VGroup(problem, frame, knode).shift, 4 * LEFT),
            ReplacementTransform(proof[0], proof[1])
        )
        self.wait(1.5)

        midline = Line([-1, 2.8, 0], [-1, -2.8, 0])
        self.play(ShowCreation(midline))

        form = VGroup(
            TexMobject(r"\frac{L_m}{L_n}< \frac{p}{q} ", r"\le \frac{kL_m+R_m}{kL_n+R_n}"),
            TexMobject(r"\frac{p}{q}\le \frac{kL_m+R_m}{kL_n+R_n}"),
            TexMobject(r"pkL_n+pR_n\le qkL_m+qR_m"),
            TexMobject(r"k(", r"pL_n-qL_m", r")\le qR_m-pR_n"),
            TexMobject(r"k\le \frac{qR_m-pR_n}{pL_n-qL_m}"),
            TexMobject(r"k\le", r"\lfloor \frac{qR_m-pR_n}{pL_n-qL_m}\rfloor"),
        ).scale(0.8)
        form[0].move_to([3, 2, 0])
        form[1].move_to([3, 2, 0])
        form[2].move_to([3, 1, 0])
        form[3].move_to([3, 0, 0])
        form[4].move_to([3, -1, 0])
        form[5].move_to([3, -1, 0])
        self.play(Write(form[0]))
        self.wait(0.5)
        condition = TexMobject(r"pL_n-qL_m>0").scale(0.65).move_to([-4, -1.6, 0])
        self.play(
            ApplyMethod(knode.move_to, [-4, 0.3, 0]),
            ApplyMethod(frame.move_to, [-4, 0.3, 0]),
            ReplacementTransform(form[0][0].copy(), condition)
        )
        self.wait(0.5)
        self.play(ReplacementTransform(form[0], form[1]))
        self.wait(0.5)
        self.play(Write(form[2]))
        self.wait(0.5)
        self.play(Write(form[3]))
        self.wait(0.5)
        self.play(FadeOutAndShift(condition, direction=form[3][1].get_center() - condition.get_center()))
        self.wait(0.5)
        self.play(ReplacementTransform(proof[1], proof[2]))
        self.wait(0.5)
        self.play(Write(form[4]))
        self.wait(0.5)
        self.play(ReplacementTransform(form[4], form[5]))
        self.wait(0.5)
        self.play(ReplacementTransform(proof[2], proof[3]))
        self.wait(1.5)
        self.play(Transform(frame, SurroundingRectangle(form[5][1], buff=0.2, color=BLUE)))
        self.wait(1.5)
        self.play(ReplacementTransform(proof[3], proof[4]))
        self.wait(2.5)
        self.play(ReplacementTransform(proof[4], proof[5]))
        self.wait(2.5)
        # 往右，树出现
        self.play(
            ApplyMethod(problem[0].move_to, [4.0067504, 2.75, 0]),
            ApplyMethod(problem[1].move_to, [4.06095093, 2 + 0.25, 0]),
            FadeInFrom(sbtree1, direction=3 * LEFT),
            FadeInFrom(sbtree2, direction=3 * LEFT),
            FadeInFrom(sbtree3, direction=3 * LEFT),
            FadeInFrom(sbtree4, direction=3 * LEFT),
            FadeInFrom(sbtree5, direction=3 * LEFT),
            FadeInFrom(lines1, direction=3 * LEFT),
            FadeInFrom(lines2, direction=3 * LEFT),
            FadeInFrom(lines3, direction=3 * LEFT),
            FadeInFrom(lines4, direction=3 * LEFT),
            FadeInFrom(dashedLines0, direction=3 * LEFT),
            FadeOutAndShift(knode, direction=8 * RIGHT),
            FadeOutAndShift(midline, direction=8 * RIGHT),
            FadeOutAndShift(frame, direction=8 * RIGHT),
            FadeOutAndShift(form, direction=4 * RIGHT)
        )

        self.wait(2.5)

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

        matproof = VGroup(
            TextMobject("再看一下二分过程中记录的形式"),
            TextMobject(r"这里将区间记录成$2\times 2$的矩阵会非常合适"),
            TextMobject(r"那么根节点$\frac{1}{1}$就是..."),
            TextMobject(r"咦？不太完美，上下交换一下吧"),
            TextMobject(r"这样根节点就是单位矩阵了"),
            TextMobject("注意，现在是分母在上，分子在下"),
            TextMobject("第二层的节点对应的矩阵也可以写出来"),
            TextMobject("再进一步，你会发现..."),
            TextMobject("节点对应的矩阵可以写成一系列LR矩阵乘积形式"),
            TextMobject("举个例子"),
        )
        matproof.to_edge(DOWN)
        self.play(ReplacementTransform(proof[5], matproof[0]))
        self.wait(2.5)
        lnode = TexMobject(r"({L_m \over L_n},{L_m+R_m \over L_n+R_n})").scale(0.65)
        rnode = TexMobject(r"({L_m+R_m \over L_n+R_n},{R_m \over R_n})").scale(0.65)
        lnode.move_to([4.25 - 0.25 - 1.2 - 0.25, 0.8 + 0.25 - 1.6, 0])
        rnode.move_to([4.25 - 0.25 + 1.2 + 0.25, 0.8 + 0.25 - 1.6, 0])
        node = TexMobject(r"({L_m \over L_n},{R_m \over R_n})").scale(0.65)
        node.move_to([4.25 - 0.25, 0.8 + 0.25, 0])
        self.play(
            FadeIn(node),
            FadeIn(lnode),
            FadeIn(rnode),
        )
        self.wait(2.5)
        self.play(ReplacementTransform(matproof[0], matproof[1]))
        self.wait(2.5)
        matnode = TexMobject(r"""  
                \begin{pmatrix} 
                    L_m & R_m \\
                    L_n & R_n
                \end{pmatrix} 
                """).scale(0.65).move_to(node.get_center())
        matlnode = TexMobject(r"""  
                \begin{pmatrix} 
                    L_m & L_m+R_m \\
                    L_n & L_n+R_n
                \end{pmatrix} 
                """).scale(0.65).move_to(lnode.get_center())
        matrnode = TexMobject(r"""  
                \begin{pmatrix} 
                    L_m+R_m & R_m\\
                    L_n+R_n & R_n
                \end{pmatrix} 
                """).scale(0.65).move_to(rnode.get_center())

        self.play(
            ReplacementTransform(node, matnode),
            ReplacementTransform(lnode, matlnode),
            ReplacementTransform(rnode, matrnode),
        )
        self.wait(2.5)
        self.play(ReplacementTransform(matproof[1], matproof[2]))
        self.wait(2.5)
        matsbtreeroot = TexMobject(r"""  
                        \begin{pmatrix} 
                            0 & 1\\
                            1 & 0
                        \end{pmatrix} 
                        """).scale(fontScaleRatio).move_to(sbtree1[1].get_center())
        self.play(Transform(sbtree1[1], matsbtreeroot))
        self.wait(1.5)
        self.play(ReplacementTransform(matproof[2], matproof[3]))
        self.wait(1.5)
        frames = VGroup(
            SurroundingRectangle(sbtree1[1], buff=0.1, color=ORANGE),
            SurroundingRectangle(matnode, buff=0.1, color=ORANGE),
            SurroundingRectangle(matlnode, buff=0.1, color=ORANGE),
            SurroundingRectangle(matrnode, buff=0.1, color=ORANGE),
        )
        self.play(
            ShowCreation(frames[0]),
            ShowCreation(frames[1]),
            ShowCreation(frames[2]),
            ShowCreation(frames[3]),
        )
        self.wait(1.5)
        matsbtreeroot = TexMobject(r"""  
                        \begin{pmatrix} 
                            1 & 0\\
                            0 & 1
                        \end{pmatrix} 
                        """).scale(fontScaleRatio).move_to(sbtree1[1].get_center())
        matnode_later = TexMobject(r"""  
                                \begin{pmatrix} 
                                    L_n & R_n \\
                                    L_m & R_m
                                \end{pmatrix} 
                                """).scale(0.65).move_to(matnode.get_center())
        matlnode_later = TexMobject(r"""  
                                \begin{pmatrix} 
                                    L_n & L_n+R_n \\
                                    L_m & L_m+R_m
                                \end{pmatrix} 
                                """).scale(0.65).move_to(matlnode.get_center())
        matrnode_later = TexMobject(r"""  
                                \begin{pmatrix} 
                                    L_n+R_n & R_n\\
                                    L_m+R_m & R_m
                                \end{pmatrix} 
                                """).scale(0.65).move_to(matrnode.get_center())
        self.play(
            Transform(sbtree1[1], matsbtreeroot),
            Transform(matnode, matnode_later),
            Transform(matlnode, matlnode_later),
            Transform(matrnode, matrnode_later)
        )
        self.wait(2.5)
        self.play(ReplacementTransform(matproof[3], matproof[4]))
        self.wait(2.5)
        self.play(ReplacementTransform(matproof[4], matproof[5]))
        self.wait(2.5)
        self.play(ReplacementTransform(matproof[5], matproof[6]))
        self.wait(2.5)
        matsbtree2 = VGroup(
            TexMobject(r"""  
                                \begin{pmatrix} 
                                    1 & 1\\
                                    0 & 1
                                \end{pmatrix} 
                                """).scale(fontScaleRatio).move_to(sbtree2[0].get_center()),
            TexMobject(r"""  
                                \begin{pmatrix} 
                                1 & 0\\
                                1 & 1
                                \end{pmatrix} 
                                """).scale(fontScaleRatio).move_to(sbtree2[1].get_center()),

        )
        self.play(Uncreate(frames))
        self.wait(1.5)
        self.play(
            Transform(sbtree2[0], matsbtree2[0]),
            Transform(sbtree2[1], matsbtree2[1])
        )
        self.wait(2,5)
        lines1.clear_updaters()
        lines2.clear_updaters()
        dashedLines0.clear_updaters()

        textL = TexMobject("L").scale(fontScaleRatio).move_to(sbtree2[0].get_center() + UP * 0.5).set_color(BLUE)
        textR = TexMobject("R").scale(fontScaleRatio).move_to(sbtree2[1].get_center() + UP * 0.5).set_color(RED)

        self.play(
            ApplyMethod(sbtree2[0].set_color, BLUE),
            ApplyMethod(sbtree2[1].set_color, RED),
            FadeIn(textL),
            FadeIn(textR),
        )
        self.play(ReplacementTransform(matproof[6], matproof[7]))
        self.wait(2.5)
        formular = VGroup(
            TexMobject(r"""  
                    \begin{pmatrix} 
                    L_n & L_n+R_n \\
                    L_m & L_m+R_m
                    \end{pmatrix}
                    """, r"""
                    =
                    """, r""" 
                    \begin{pmatrix} 
                    L_n & R_n \\
                    L_m & R_m
                    \end{pmatrix}
                    """, r"""
                    \begin{pmatrix} 
                    1 & 1\\
                    0 & 1
                    \end{pmatrix} 
                    """
                       , stroke_width=2).scale(0.65).move_to([2, 0.2, 0]),
            TexMobject(r"""  
                            \begin{pmatrix} 
                            L_n+R_n & R_n\\
                            L_m+R_m & R_m
                            \end{pmatrix}
                            """, r"""
                            =
                            """, r""" 
                            \begin{pmatrix} 
                            L_n & R_n \\
                            L_m & R_m
                            \end{pmatrix}
                            """, r"""
                            \begin{pmatrix} 
                            1 & 0\\
                            1 & 1
                            \end{pmatrix} 
                            """
                       , stroke_width=2).scale(0.65).move_to([2, -1.3, 0])
        )
        formular[0][3].set_color(BLUE)
        formular[1][3].set_color(RED)
        self.play(*[
            ApplyMethod(VGroup(*sbtree3[2:]).set_opacity, 0.2),
            ApplyMethod(VGroup(*sbtree4[4:]).set_opacity, 0.2),
            ApplyMethod(VGroup(*sbtree5[8:]).set_opacity, 0.2),
            ApplyMethod(VGroup(lines2[1], lines2[3]).set_opacity, 0.2),
            ApplyMethod(VGroup(lines3[2], lines3[3], lines3[6], lines3[7]).set_opacity, 0.2),
            ApplyMethod(VGroup(*lines4[4:8]).set_opacity, 0.2),
            ApplyMethod(VGroup(*lines4[12:16]).set_opacity, 0.2),
        ])
        self.wait(1.5)
        self.play(
            ReplacementTransform(matlnode, formular[0][0]),
            ReplacementTransform(matrnode, formular[1][0]),
            ReplacementTransform(matnode.copy(), formular[0][2]),
            ReplacementTransform(matnode, formular[1][2]),
        )
        self.wait(1.5)
        self.play(
            Write(formular[0][1]),
            Write(formular[1][1]),
            ReplacementTransform(sbtree2[0].copy(), formular[0][3]),
            ReplacementTransform(sbtree2[1].copy(), formular[1][3]),
        )
        self.wait(2.5)
        self.play(ReplacementTransform(matproof[7], matproof[8]))
        self.wait(3)

        self.play(ReplacementTransform(matproof[8], matproof[9]))
        self.wait(1.5)
        self.play(FadeOut(formular))
        self.wait(1.5)
        example = VGroup(
            TextMobject(r"设$f(S)$表示与矩阵$S$对应的分数"),
            TextMobject(r"""
            \begin{align*}
            f(LRRL) & = 
            f\left(
            \begin{pmatrix} 
            1 & 1\\
            0 & 1
            \end{pmatrix} 
            \begin{pmatrix} 
            1 & 0\\
            1 & 1
            \end{pmatrix} 
            \begin{pmatrix} 
            1 & 0\\
            1 & 1
            \end{pmatrix} 
            \begin{pmatrix} 
            1 & 1\\
            0 & 1
            \end{pmatrix}
            \right)
             \\
            & = 
            f\left(
            \begin{pmatrix} 
            3 & 4\\
            2 & 3
            \end{pmatrix}
            \right) = \frac{5}{7}
            \end{align*}
            """)
        ).scale(0.7)
        example[0].move_to([-1.7, 0.5, 0] - example[0].get_left())
        example[1].move_to([-1.7, -1, 0] - example[1].get_left())
        self.play(ShowCreation(example[0]))
        self.wait(2.5)
        self.play(ShowCreation(example[1]))
        self.wait(2.5)
        proof = VGroup(
            TextMobject(r"这样L和R既可以表示字符，又可以表示$2\times 2$矩阵"),
            TextMobject(r"那么现在往左走一步，相当于当前矩阵右边乘L"),
            TextMobject(r"往右走一步，相当于当前矩阵右边乘R"),
            TextMobject(r"如果是左边乘上L或R呢？"),
            TextMobject(r"试着推导一下..."),
        ).to_edge(DOWN)
        self.play(ReplacementTransform(matproof[-1], proof[0]))
        self.wait(2.5)
        self.play(Uncreate(example))
        self.wait(2.5)
        self.play(
            FadeIn(formular),
            ReplacementTransform(proof[0], proof[1])
        )
        self.wait(2.5)
        self.play(ReplacementTransform(proof[1], proof[2]))
        self.wait(2.5)
        self.play(ReplacementTransform(proof[2], proof[3]))
        self.wait(2.5)
        self.play(ReplacementTransform(proof[3], proof[4]))
        self.wait(2.5)
        # 全部消失
        self.play(
            FadeOut(sbtree1),
            FadeOut(sbtree2),
            FadeOut(sbtree3),
            FadeOut(sbtree4),
            FadeOut(sbtree5),
            FadeOut(lines1),
            FadeOut(lines2),
            FadeOut(lines3),
            FadeOut(lines4),
            FadeOut(dashedLines0),
            FadeOut(problem),
            FadeOut(proof[4]),
            FadeOut(formular),
            FadeOut(textL),
            FadeOut(textR),
        )
        self.wait(2.5)
        formular = VGroup(
            TexMobject(r"""  
                L=\begin{pmatrix} 
                    1 & 1\\
                    0 & 1
                    \end{pmatrix},
                S=\begin{pmatrix} 
                    L_n & R_n \\
                    L_m & R_m
                \end{pmatrix}
                """
                       , ),
            TexMobject(r"""LS=""",r"""\begin{pmatrix} 
                            L_n+L_m & R_n+R_m \\
                            L_m & R_m
                        \end{pmatrix}
                        """
                       ),
            TexMobject(r"f(S)=\frac{L_m+R_m}{L_n+R_n}"),
            TexMobject(r"f(LS)=\frac{L_m+R_m}{L_n+R_n+L_m+R_m}"),
        ).scale(0.7)
        formular[0].move_to([0, 2, 0])
        formular[1].move_to([0, 4/6, 0])
        formular[2].move_to([0, -4/6, 0])
        formular[3].move_to([0, -2, 0])

        self.play(ShowCreation(formular[0]))
        self.wait(1.5)
        self.play(ShowCreation(formular[1][0]))
        self.wait(1.5)
        self.play(ShowCreation(formular[1][1]))
        self.wait(1.5)
        self.play(ShowCreation(formular[2]))
        self.wait(1.5)
        self.play(ShowCreation(formular[3]))
        self.wait(3.5)
        # formular左移，
        self.play(
            ApplyMethod(formular[0].shift, [-5.5, 2, 0] - formular[0].get_left()),
            ApplyMethod(formular[1].shift, [-5.5, 4/6, 0] - formular[1].get_left()),
            ApplyMethod(formular[2].shift, [-5.5, -4/6, 0] - formular[2].get_left()),
            ApplyMethod(formular[3].shift, [-5.5, -2, 0] - formular[3].get_left()),
        )

        self.wait(2.5)
        explain = VGroup(
            TextMobject(r"设$n=L_n+R_n,\, m=L_m+R_m$"),
            TextMobject(r"$f(S)=\frac{m}{n},\, f(LS)=\frac{m}{n+m}$"),
            TextMobject(r"倒着考虑，设有分数$\frac{m^{\prime}}{n^{\prime}}(m^{\prime}<n^{\prime})$"),
            TextMobject(r"第一步一定是L，剩下的走法同$\frac{m^{\prime}}{n^{\prime} - m^{\prime}}$"),
            TextMobject(r"问题就递归下去了，直到$m^{\prime} =n^{\prime} = 1$"),
        ).scale(0.7)
        explain[0].move_to([0.5, 2, 0] - explain[0].get_left())
        explain[1].move_to([0.5, 1, 0] - explain[1].get_left())
        explain[2].move_to([0.5, 0, 0] - explain[2].get_left())
        explain[3].move_to([0.5, -1, 0] - explain[3].get_left())
        explain[4].move_to([0.5, -2, 0] - explain[4].get_left())
        self.play(ShowCreation(explain[0]))
        self.wait(2.5)
        self.play(ShowCreation(explain[1]))
        self.wait(2.5)
        self.play(ShowCreation(explain[2]))
        self.wait(2.5)
        self.play(ShowCreation(explain[3]))
        self.wait(2.5)
        self.play(ShowCreation(explain[4]))
        self.wait(2.5)
        final = VGroup(
            TextMobject("把L换成R推导是类似的，不再赘述"),
            TextMobject("直接来看一下结果~"),
            TextMobject("这一段的推导在《具体数学》中可以找到"),
            TextMobject("代码的话非常简洁"),
            TextMobject("仔细观察一下，这不就是","辗转相减","吗？"),
            TextMobject("把减法换成取模，就是","辗转相除","了"),
            TextMobject("就像这样"),
            TextMobject(r"我们知道",r"欧几里得算法",r"的时间复杂度是$O(\log N)$"),
            TextMobject("因此这也就说明了路径拐点的个数是$O(\log N)$级别的"),
            TextMobject(r"我们也就完成了最终的优化"),
            TextMobject("那本期视频就到这里了"),
            TextMobject("评论区有两道练习题目，大家不妨挑战一下"),
            TextMobject(r"See you\textasciitilde"),
        ).to_edge(DOWN)
        final[4][1].set_color(BLUE)
        final[5][1].set_color(ORANGE)
        final[7][1].set_color(ORANGE)
        con = VGroup(
            TexMobject(r"""
            \frac{m}{n}=f(LS)\qquad \Leftrightarrow \qquad \frac{m-n}{n}=f(S) \qquad m>n 
        """), TexMobject(r"""
            \frac{m}{n}=f(RS)\qquad \Leftrightarrow \qquad \frac{m}{n-m}=f(S) \qquad m<n
        """)
        ).scale(0.8)
        con[0].shift(0.6 * UP)
        con[1].shift(0.6 * DOWN)
        self.play(ShowCreation(final[0]))
        self.wait(2.5)
        self.play(ReplacementTransform(final[0], final[1]))
        self.wait(1.5)
        self.play(
            FadeOutAndShift(formular, 4 * LEFT),
            FadeOutAndShift(explain, 4 * RIGHT)
        )
        self.wait(1.5)
        self.play(ShowCreation(con))
        self.wait(2.5)
        self.play(ReplacementTransform(final[1], final[2]))
        self.wait(2.5)
        self.play(ReplacementTransform(final[2], final[3]))
        self.wait(2.5)
        self.play(FadeOut(con))
        code = VGroup(
            TextMobject(r"""
\begin{lstlisting}[language=python,basicstyle=\con]
m, n = p, q
while m != n:
    if m < n:
        n = n - m
        print('L')
    else:
        m = m - n
        print('R')
\end{lstlisting}    
            """),
            TextMobject(r"""
\begin{lstlisting}[language=python,basicstyle=\con]
m, n = p, q
while m != n:
    if m < n:
        step = (n - 1) // m
        n -= step * m
        print('L', step)
    else:
        step = (m - 1) // n
        m -= step * n
        print('R', step)
\end{lstlisting}
            """

                        )
        ).scale(0.6)
        code[0].move_to([2.2, -0.1, 0] - code[0].get_left())
        code[1].move_to([1.2, -0.4, 0] - code[1].get_left())
        sbtree1[1].become(TexMobject("{1", "\\over", "1}").scale(fontScaleRatio).move_to(sbtree1[1].get_center()))
        sbtree2[0].become(TexMobject("{1", "\\over", "2}").scale(fontScaleRatio).move_to(sbtree2[0].get_center()))
        sbtree2[1].become(TexMobject("{2", "\\over", "1}").scale(fontScaleRatio).move_to(sbtree2[1].get_center()))
        sbtree3.set_opacity(1)
        sbtree4.set_opacity(1)
        sbtree5.set_opacity(1)
        lines2.set_opacity(1)
        lines3.set_opacity(1)
        lines4.set_opacity(1)
        lines1.become(VGroup(
            Line(start=sbtree1[1].get_left(), end=sbtree2[0].get_right(), stroke_width=LINESTROKE).scale(
                lineScaleRatio),
            Line(start=sbtree1[1].get_right(), end=sbtree2[1].get_left(), stroke_width=LINESTROKE).scale(lineScaleRatio)
        ))
        lines2.become(VGroup(
            *([
                  Line(start=sbtree2[i].get_left(), end=sbtree3[i * 2].get_right(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(len(sbtree2))
              ] + [
                  Line(start=sbtree2[i].get_right(), end=sbtree3[i * 2 + 1].get_left(), stroke_width=LINESTROKE).scale(
                      lineScaleRatio)
                  for i in range(len(sbtree2))
              ])
        ))
        self.play(
            FadeIn(sbtree1),
            FadeIn(sbtree2),
            FadeIn(sbtree3),
            FadeIn(sbtree4),
            FadeIn(sbtree5),
            FadeIn(lines1),
            FadeIn(lines2),
            FadeIn(lines3),
            FadeIn(lines4),
            FadeIn(dashedLines0),
            FadeIn(problem),
        )
        self.wait(1.5)
        self.play(ShowCreation(code[0]))
        self.wait(2.5)
        self.play(ReplacementTransform(final[3], final[4]))
        self.wait(2.5)
        self.play(ReplacementTransform(final[4], final[5]))
        self.wait(2.5)
        self.play(ReplacementTransform(code[0], code[1]))
        self.wait(2.5)
        for i in range(5, len(final) - 1):
            self.play(ReplacementTransform(final[i], final[i + 1]))
            self.wait(2.5)
        self.wait(6)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python -m manim -p " + module_name + " SBtreeScene"
    os.system(command)
