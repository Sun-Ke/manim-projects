from manimlib.imports import *

table_opacity=0.7
dash_color="#436EEE"

class Problem(Scene):
    def Path(self,st,edges,colors):
        lst=[]
        now=np.array(st,dtype='float64')
        for dir,col in zip(edges,colors):
            lst.append(Line(now,now+dir,color=col).set_stroke(width=10))
            now+=dir
        return VGroup(*lst)

    def construct(self):
        #组合数学P195
        text=VGroup(
            TextMobject("\yahei 今天我们来分析一道经典的组合题目",stroke_width=1.5),
            TextMobject("\yahei 考虑如果没有找零钱这个限制",stroke_width=1.5),
            TextMobject(r"\yahei 没错，答案就是$C_5^2$",stroke_width=1.5),
            TextMobject(r"\yahei 现在加上零钱限制，需要减去一些情况",stroke_width=1.5),
            TextMobject(r"\yahei 也就是说所有前缀中100元出现的次数不能超过50元出现次数",stroke_width=1.5),
            TextMobject(r"\yahei 换一个等价的模型看看",stroke_width=1.5),
            TextMobject(r"\yahei 在$m\times n$的网格图上从左下角$A$走到右上角$B$",stroke_width=1.5),
            TextMobject(r"\yahei 每次只能向上或者向右走",stroke_width=1.5),
            TextMobject(r"\yahei 把向右当成","50元",",向上当成","100元",stroke_width=1.5),
            TextMobject(r"\yahei 那么之前的限制就转换成了不能越过如图所示的白线",stroke_width=1.5)
        ).scale(0.6).to_edge(DOWN)
        text[8][1].set_color(RED)
        text[8][3].set_color(BLUE)

        #今天我们来分析一道经典的组合题目
        self.play(FadeIn(text[0]))
        self.wait(3)
        self.play(FadeOut(text[0]))
        problem=TextMobject(r"""
            问题：有$m+n$个人站成一排要进入剧院，门票是$50$元。\\
            其中有$n$个人有50元，而$m$个人只有一张整的$100$元。\\
            售票处一开始没有零钱，这些人需要以某种方式排队\\
            使得售票处总有零钱可找，求合法的方案数。
        """).scale(0.8)

        self.play(ShowCreation(problem,rate_func=linear),run_time=11)
        self.wait(6)
        self.play(Uncreate(problem))
        self.wait()

        balls=VGroup(
            VGroup(
                Circle(color=RED,radius=0.7,fill_opacity=1,stroke_width=0),
                #TextMobject("50",background_stroke_color=WHITE)
            ),
            VGroup(
                Circle(color=RED, radius=0.7, fill_opacity=1,stroke_width=0),
                #TextMobject("50", background_stroke_color=WHITE)
            ),
            VGroup(
                Circle(color=RED, radius=0.7, fill_opacity=1,stroke_width=0),
                #TextMobject("50", background_stroke_color=WHITE)
            ),
            VGroup(
                Circle(color=BLUE, radius=0.7, fill_opacity=1,stroke_width=0),
                #TextMobject("100", background_stroke_color=WHITE)
            ),
            VGroup(
                Circle(color=BLUE, radius=0.7, fill_opacity=1,stroke_width=0),
                #TextMobject("100", background_stroke_color=WHITE)
            )
        )
        for i in range(0,5):
            balls[i].move_to([(i-2)*1.7,0.5,0])

        self.play(*[FadeIn(balls[i][0]) for i in range(5)],run_time=2)
        self.wait(2)
        #考虑如果没有找零钱这个限制
        self.play(FadeIn(text[1]))

        self.wait(2)

        number = TexMobject("1").move_to([0, -1, 0])
        self.play(
            FadeOut(text[1]),
            FadeIn(number)
        )
        self.wait()

        lst=[(3,2),(3,1),(3,0),(4,2),(3,0),(3,1),(4,1),(4,0),(3,0)]
        num=1
        for a,b in lst:
            num+=1
            self.play(
                MoveAlongPath(balls[a], ArcBetweenPoints(balls[a].get_center(), balls[b].get_center())),
                MoveAlongPath(balls[b], ArcBetweenPoints(balls[b].get_center(), balls[a].get_center())),
                Transform(number,TexMobject(str(num)).move_to([0,-1,0]))
            )
        #43012
        self.wait()
        self.play(FadeIn(text[2]))
        self.wait(2)
        self.play(
            Transform(number,TexMobject("C_5^2=10").move_to([0,-1,0])),
            FadeOut(text[2])
        )
        self.wait(2)
        self.play(FadeOut(number))
        self.play(FadeIn(text[3]))
        self.wait(2)
        self.play(FadeOut(text[3]))

        for i in range(len(balls)):
            if i<3:
                balls[i].add(TextMobject("50", background_stroke_color=WHITE).move_to(balls[i][0].get_center()))
            else:
                balls[i].add(TextMobject("100", background_stroke_color=WHITE).move_to(balls[i][0].get_center()))

        self.play(*[ShowCreation(balls[i][1]) for i in range(len(balls))])
        wrong = ImageMobject(r"C:\Users\sk\Pictures\素材\错").shift(DOWN)
        right = ImageMobject(r"C:\Users\sk\Pictures\素材\对").shift(DOWN)
        self.wait(0.5)
        self.play(FadeInFromLarge(wrong))
        self.wait(0.5)
        self.play(FadeOut(wrong))
        self.wait(0.5)
        self.play(
            MoveAlongPath(balls[4], ArcBetweenPoints(balls[4].get_center(), balls[0].get_center())),
            MoveAlongPath(balls[0], ArcBetweenPoints(balls[0].get_center(), balls[4].get_center())),
        )
        self.wait(0.5)
        self.play(FadeInFromLarge(wrong))
        self.wait(0.5)
        self.play(FadeOut(wrong))
        self.wait(0.5)
        self.play(
            MoveAlongPath(balls[3], ArcBetweenPoints(balls[3].get_center(), balls[1].get_center())),
            MoveAlongPath(balls[1], ArcBetweenPoints(balls[1].get_center(), balls[3].get_center())),
        )
        self.wait(0.5)
        self.play(FadeInFromLarge(right))
        self.wait(0.5)
        self.play(FadeOut(right))
        self.wait(0.5)
        self.play(FadeIn(text[4]))
        self.wait(4)
        self.play(ReplacementTransform(text[4],text[5]))
        self.wait(2)
        lst = []
        for i in range(0, 5):
            if i % 2 == 1:
                lst.append(Line([0, i, 0], [6, i, 0]).set_opacity(table_opacity))
            else:
                lst.append(Line([6, i, 0], [0, i, 0]).set_opacity(table_opacity))
        for i in range(0, 7):
            if i % 2 == 1:
                lst.append(Line([i, 0, 0], [i, 4, 0]).set_opacity(table_opacity))
            else:
                lst.append(Line([i, 4, 0], [i, 0, 0]).set_opacity(table_opacity))
        table = VGroup(*lst)
        table.shift(-table.get_center_of_mass())

        self.play(
            FadeOut(balls),
            FadeOut(text[5]),
        )
        self.play(
            ShowCreation(table),
            run_time=4
        )
        self.wait()
        st = Dot([-3, -2, 0], radius=0.12)
        ed = Dot([3, 2, 0], radius=0.12)
        A = TexMobject("A").next_to(st,DL)
        B = TexMobject("B").next_to(ed,UR)
        M = TexMobject("m").shift(4.5 * RIGHT)
        N = TexMobject("n").shift(3 * UP)

        self.play(
            FadeIn(text[6]),
            ShowCreation(M),
            ShowCreation(N),
            ShowCreation(A),
            ShowCreation(B),
            ShowCreation(st),
            ShowCreation(ed),
        )
        self.wait(4)
        self.play(ReplacementTransform(text[6],text[7]))
        self.wait(2)
        path=self.Path([-3,-2,0],
            [RIGHT,RIGHT,UP,RIGHT,UP,RIGHT,UP,UP,RIGHT,RIGHT],
            ["#ff3333" for i in range(10)])
        self.play(ShowCreation(path),FadeOut(text[7]),run_time=2)
        self.wait()
        path2=self.Path([-3,-2,0],
            [RIGHT,RIGHT,UP,RIGHT,UP,RIGHT,UP,UP,RIGHT,RIGHT],
            [RED,RED,BLUE,RED,BLUE,RED,BLUE,BLUE,RED,RED]
        )
        self.play(FadeIn(text[8]))
        self.wait()
        self.play(
            ReplacementTransform(path,path2)
        )
        balls = VGroup(
            Circle(color=RED, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=RED, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=BLUE, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=RED, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=BLUE, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=RED, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=BLUE, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=BLUE, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=RED, radius=0.3, fill_opacity=1,stroke_width=0),
            Circle(color=RED, radius=0.3, fill_opacity=1,stroke_width=0),
        )
        for i in range(10):
            balls[i].move_to([-7/9*4.5+i*7/9,-3.3,0])
        self.wait()
        self.play(FadeOut(text[8]))
        self.wait()
        self.play(*[
            ReplacementTransform(path2[i].copy(),balls[i]) for i in range(10)
        ])
        self.wait(3)
        self.play(FadeOut(balls))
        self.wait()
        self.play(FadeIn(text[9]))
        self.wait()

        barrier=Line([-3,-2,0],[1,2,0]).set_stroke(width=6)
        self.play(ShowCreation(barrier))
        self.wait()
        path3 = self.Path([-3, -2, 0],
                          [RIGHT,  UP, UP,RIGHT, RIGHT, RIGHT, UP, UP, RIGHT, RIGHT],
                          [RED, BLUE, BLUE, RED, RED, RED, BLUE, BLUE, RED, RED])
        self.play(ReplacementTransform(path2,path3))
        self.wait()
        self.play(FadeInFromLarge(wrong))
        self.wait()
        self.play(
            FadeOut(wrong),
            FadeOut(text[9]),
            FadeOut(path3),
        )
        self.wait()
        solution=VGroup(
            TextMobject("\yahei 如何求解合法的路径数呢", stroke_width=1.5),
            TextMobject("\yahei $n$和$m$较小时，可以用动态规划", stroke_width=1.5),
            TextMobject("\yahei 就像这样，求出$n=6,m=4$的答案是$90$", stroke_width=1.5),
            TextMobject("\yahei 后面讲一下用折线法求通项公式", stroke_width=1.5),
            TextMobject("\yahei 对于不合法的路径，一定与图中的","蓝线","有交点", stroke_width=1.5),
            TextMobject("\yahei 找到第一次相交的地方", stroke_width=1.5),
            TextMobject("\yahei 将路径前半段沿","蓝线","对称过去", stroke_width=1.5),
            TextMobject("\yahei 会发现非法路径和从$A^{\prime}$到$B$的路径一一对应", stroke_width=1.5),
            TextMobject("\yahei 这样我们就可以用总数减去不合法的情况了", stroke_width=1.5),
            TextMobject("\yahei 得到最终的答案", stroke_width=1.5),
            TextMobject("\yahei 当我们把$n=m$代入式子", stroke_width=1.5),
            TextMobject("\yahei 就求出了卡特兰数的通项公式", stroke_width=1.5)
        ).scale(0.6).to_edge(DOWN)
        solution[4][1].set_color(dash_color)
        solution[6][1].set_color(dash_color)
        self.play(FadeIn(solution[0]))
        self.wait(2.5)
        self.play(ReplacementTransform(solution[0],solution[1]))
        self.wait(2.5)
        self.play(FadeOut(solution[1]))
        dp=[[0 for j in range(5)]for i in range(7)]

        for i in range(7):
            for j in range(5):
                if j>i:
                    continue
                if j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        mp={}
        circles=[]
        slice=0.50
        num=0
        for j in range(5):
            for i in range(7):
                if j>i:
                    continue
                num += 1
                if num<=12:
                    slice-=0.02
                elif num>13:
                    slice+=0.02
                mp[(i,j)]=VGroup(
                    TexMobject(str(dp[i][j]),stroke_width=2,color=BLACK,fill_color=BLACK).scale(0.78).move_to([i - 3, j - 2, 0]),
                )
                circles.append(Circle(radius=0.26, stroke_width=0, fill_color=WHITE, fill_opacity=0.90).move_to([i - 3, j - 2, 0]))
                if j==0:
                    self.play(
                        ShowCreation(VGroup(circles[-1],mp[(i,j)])),
                        run_time=slice
                    )
                    continue
                if i==j:
                    self.play(
                        ShowCreation(circles[-1]),
                        ReplacementTransform(mp[(i, j-1)].copy(), mp[(i, j)]),
                        run_time=slice)
                    continue
                self.play(
                    ShowCreation(circles[-1]),
                    ReplacementTransform(VGroup(mp[(i, j - 1)],mp[(i-1, j)]).copy(), mp[(i, j)]),
                    run_time=slice)
        self.wait()
        self.play(
            ApplyMethod(circles[-1].scale,1.4),
            ApplyMethod(mp[(6,4)].scale,1.4),
        )
        self.play(FadeIn(solution[2]))
        self.wait(2)
        self.play(*([
            FadeOut(obj) for obj in circles
        ] + [
            FadeOut(obj) for obj in mp.values()
        ]))
        self.wait()
        self.play(ReplacementTransform(solution[2],solution[3]))
        self.wait(2)
        self.play(FadeOut(solution[3]))
        self.wait()
        path3=self.Path([-3, -2, 0],
                          [RIGHT,  UP, UP,RIGHT, RIGHT, RIGHT, UP, UP, RIGHT, RIGHT],
                          ["#ff3333" for i in range(10)])

        dashedline=DashedLine([-4.5,-2.5,0],[1.5,3.5,0],color=dash_color, positive_space_ratio=0.5,dash_length=0.1).set_stroke(width=6)
        self.play(ShowCreation(dashedline))
        self.wait()
        self.play(ShowCreation(path3))
        self.wait()
        self.play(FadeIn(solution[4]))
        self.wait(3)
        self.play(FadeOut(solution[4]))
        self.wait()
        dot=Dot([-2, 0, 0], radius=0.12)
        C = TexMobject("C").next_to(dot,UL)
        self.play(
            ShowCreation(dot),
            ShowCreation(C),
            FadeIn(solution[5])
        )
        self.wait()
        self.play(FadeOut(solution[5]))
        self.wait()
        path_sym=self.Path([-4,-1,0],[UP,RIGHT,RIGHT],["#FFEC8B" for i in range(3)])
        st_sym=Dot([-4, -1, 0], radius=0.12)
        AA = TexMobject(r"A^{\prime}").next_to(st_sym, DL)
        self.play(
            ReplacementTransform(
                VGroup(A,st,path3[0],path3[1],path3[2]).copy(),
                VGroup(AA,st_sym,path_sym[0],path_sym[1],path_sym[2])
            ),
            FadeIn(solution[6]),
        )
        self.wait(3)

        table.add(Line([-4,2,0],[-4,-1,0]).set_opacity(table_opacity))
        self.play(
            ApplyMethod(table[1].become,Line([-4, -1, 0], [3, -1, 0]).set_opacity(table_opacity)),
            ApplyMethod(table[2].become,Line([3, 0, 0],[-4, 0, 0]).set_opacity(table_opacity)),
            ApplyMethod(table[3].become,Line([-4, 1, 0], [3, 1, 0]).set_opacity(table_opacity)),
            ApplyMethod(table[4].become,Line( [3, 2, 0],[-4, 2, 0]).set_opacity(table_opacity)),
            ShowCreation(table[-1])
        )
        self.wait()
        self.play(*([
            ReplacementTransform(solution[6], solution[7])
        ] + [
            ApplyMethod(path3[i].set_color,"#ff6600") for i in range(3,10)
        ]))

        self.wait(2.5)
        self.play(ReplacementTransform(solution[7],solution[8]))
        self.wait(2.5)
        self.play(
            ApplyMethod(path_sym.shift,2.5*LEFT),
            ApplyMethod(path3.shift,2.5*LEFT),
            ApplyMethod(table.shift,2.5*LEFT),
            ApplyMethod(barrier.shift,2.5*LEFT),
            ApplyMethod(dashedline.shift,2.5*LEFT),
            ApplyMethod(VGroup(dot,st,ed,st_sym).shift,2.5*LEFT),
            FadeOutAndShift(VGroup(N,M,A,B,AA,C),2.5*LEFT),
            FadeOut(solution[8])
        )
        form=VGroup(
            TextMobject(r"$C_{n+m}^{m}-C_{n+1+m-1}^{n+1}$"),
            TextMobject(r"$=C_{n+m}^{m}-C_{n+m}^{m-1}$"),
            TextMobject(r"$=C_{n+m}^{m}-\frac{m}{n+1}C_{n+m}^{m}$"),
            TextMobject(r"$=$",r"$\frac{n+1-m}{n+1}C_{n+m}^{m}$")
        )
        form[0].move_to([1.55,2,0]-form[0].get_left())
        form[1].move_to([1,0.7,0]-form[1].get_left())
        form[2].move_to([1,-0.6,0]-form[2].get_left())
        form[3].move_to([1,-1-0.9,0]-form[3].get_left())
        self.wait()
        self.play(ShowCreation(form,rate_func=linear),run_time=6)
        self.wait(2)
        final=VGroup(
            TextMobject(r"$\frac{n+1-m}{n+1}C_{n+m}^{m}$"),
            TextMobject(r"$\frac{C_{2n}^{n}}{n+1}$"),
            TextMobject(r"$1, 1, 2, 5, 14, 42, 132\dots $").shift(DOWN),
        ).scale(1.8)
        self.play(
            FadeOut(path_sym),
            FadeOut(path3),
            FadeOut(table),
            FadeOut(barrier),
            FadeOut(dashedline),
            FadeOut(VGroup(dot, st, ed, st_sym)),
            FadeOut(form[0]),
            FadeOut(form[1]),
            FadeOut(form[2]),
            FadeOut(form[3][0]),
            ReplacementTransform(form[3][1],final[0])
        )
        self.play(FadeIn(solution[9]))
        self.wait(2)
        self.play(ReplacementTransform(solution[9],solution[10]))
        self.wait()
        self.play(ReplacementTransform(final[0],final[1]))
        self.wait()
        self.play(ReplacementTransform(solution[10],solution[11]))
        self.wait(2)
        self.wait(5)


class Picture(Scene):
    def construct(self):
        title=Text("折线法求卡特兰数",font="黑体",stroke_width=2).scale(1.4)
        title[0:3].set_color(ORANGE)
        title[4:].set_color(BLUE)
        self.add(title)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python -m manim -p " + module_name + " Picture"
    os.system(command)
