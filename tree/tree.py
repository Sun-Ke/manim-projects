from cyaron import *
from cyaron import Graph as cyaGraph
from manimlib.imports import *


class LineLinkCircles(Line):
    def __init__(self, cirA=Circle(), cirB=Circle(),**kwargs):
        if not isinstance(cirA,Circle) or not isinstance(cirB,Circle):
            raise Exception('TypeError, need Circle')
        vec = cirB.get_center()-cirA.get_center()
        dis = get_norm(vec)
        if dis<cirA.radius+cirB.radius:
            raise Exception('Two circles intersect')
        vec = normalize(vec)
        super().__init__(start=cirA.get_center()+vec*cirA.radius,
                         end=cirB.get_center()-vec*cirB.radius,
                         **kwargs)

class Tree(VGroup):
    CONFIG = {
        'node_size': 0.2,
        'node_color': WHITE
    }

    def dfs_pre(self, u):
        if not self.edges[u]:
            self.leaves[u] += 1
            return
        for edge in self.edges[u]:
            v = edge.end
            self.dfs_pre(v)
            self.leaves[u] += self.leaves[v]

    def dfs(self, u):
        sum = self.alpha[u]
        for edge in self.edges[u]:
            v = edge.end
            self.angle[v] = self.leaves[v] / self.leaves[0] * PI
            self.alpha[v] = sum
            alpha_uv = self.alpha[v] + self.angle[v] / 2
            self.pos[v] = self.pos[u] + edge.weight * (np.array([np.cos(alpha_uv), np.sin(alpha_uv), 0]))
            sum += self.angle[v]
            self.dfs(v)

    def __init__(self, n=1, chain=0, flower=0, **kwargs):
        if not isinstance(n, int) or n <= 0:
            raise Exception("illegal number of nodes")
        VGroup.__init__(self, **kwargs)
        self.leaves = [0 for i in range(n )]
        self.pos = [np.array([0, 0, 0]) for i in range(n)]
        self.angle = [0.0 for i in range(n)]
        self.alpha = [0.0 for i in range(n)]
        tree = cyaGraph.tree(n, directed=True)
        print(tree)
        self.edges = tree.edges
        del self.edges[0]
        for vedge in self.edges:
            for edge in vedge:
                edge.start-=1
                edge.end-=1
        self.dfs_pre(0)
        self.angle[0] = PI
        self.dfs(0)

        nodes = [Circle(radius=self.node_size / 2,
                        color=self.node_color) for i in range(n)]
        for i in range(n):
            nodes[i].move_to(-self.pos[i])
        lines = []
        for vedge in self.edges:
            for edge in vedge:
                lines.append(LineLinkCircles(cirA=nodes[edge.start],cirB=nodes[edge.end]))
        self.add(*nodes)
        self.add(*lines)
        self.move_to([0,1,0])

    def get_center_of_mass(self,nodes,lines):
        mass=np.array([TAU*circle.radius for circle in nodes]+[line.get_length() for line in lines])
        vx=np.array([circle.get_center()[0] for circle in nodes]+[line.get_center()[0] for line in lines])
        vy=np.array([circle.get_center()[1] for circle in nodes]+[line.get_center()[1] for line in lines])
        x=np.dot(vx,mass)/np.sum(mass)
        y=np.dot(vy,mass)/np.sum(mass)
        return np.array([x,y,0])

class Test_Tree(Scene):
    def construct(self):
        tree=Tree(8,0,0)
        #tree2=Tree(8,0.3,0.7)
        self.play(ShowCreation(tree),run_time=4)
        #self.play(Transform(tree,tree2),run_time=2)
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python -m manim -pm " + module_name + " Test_Tree"
    os.system(command)

'''
0 1 1
0 2 1
2 3 1
3 4 1
3 5 1
4 6 1
4 7 1
'''