import numpy as np
level_separation = 1.5
sibling_separation = 0.8
subtree_separation = 0.8
node_size = 0.6

class Gen:
    def __init__(self, edges, **kwargs):
        global level_separation,sibling_separation,subtree_separation,node_size
        if "level_separation" in kwargs:
            level_separation=kwargs["level_separation"]
        if "sibling_separation" in kwargs:
            sibling_separation=kwargs["sibling_separation"]
        if "subtree_separation" in kwargs:
            subtree_separation=kwargs["subtree_separation"]
        if "node_size" in kwargs:
            node_size=kwargs["node_size"]
        n = len(edges)
        dep = [0 for i in range(n)]
        size = [0 for i in range(n)]
        parent = [-1 for i in range(n)]
        coorX = [0.0 for i in range(n)]
        coorY = [0.0 for i in range(n)]
        prelim = [0.0 for i in range(n)]
        modifier = [0.0 for i in range(n)]
        leftSibling = [-1 for i in range(n)]
        rightSibling = [-1 for i in range(n)]
        tmp = [-1 for i in range(n)]
        leftNeighbor = [-1 for i in range(n)]

        def dfs(x, level):
            size[x] += 1
            dep[x] = level
            leftNeighbor[x] = tmp[level]
            tmp[level] = x
            for i in range(len(edges[x])):
                y = edges[x][i]
                dfs(y, level + 1)
                size[x] += size[y]
                parent[y] = x
                if i > 0:
                    leftSibling[y] = edges[x][i - 1]
                if i + 1 < len(edges[x]):
                    rightSibling[y] = edges[x][i + 1]

        dfs(0, 0)

        self.n = n
        self.edges = edges
        self.dep = dep
        self.size = size
        self.parent = parent
        self.coorX = coorX
        self.coorY = coorY
        self.prelim = prelim
        self.modifier = modifier
        self.leftSibling = leftSibling
        self.rightSibling = rightSibling
        self.leftNeighbor = leftNeighbor

        self.firstWalk(0, 0)
        self.xTopAdjustment = self.coorX[0] - self.prelim[0]
        self.yTopAdjustment = self.coorY[0]
        self.secondWalk(0, 0, 0)

    def getCoor(self):
        lst = [np.array([x, y, 0]) for x, y in zip(self.coorX, self.coorY)]
        return lst

    def getLeftMost(self, cur, level, depth):
        size = self.size
        edges = self.edges
        if level >= depth:
            return cur
        if size[cur] == 1:
            return -1
        for child in edges[cur]:
            tmp = self.getLeftMost(child, level + 1, depth)
            if tmp != -1:
                return tmp
        return -1

    def apportion(self, cur):
        edges = self.edges
        size = self.size
        parent = self.parent
        leftNeighbor = self.leftNeighbor
        leftSibling = self.leftSibling
        modifier = self.modifier
        prelim = self.prelim
        leftmost = edges[cur][0]
        neighbor = leftNeighbor[leftmost]
        compareDepth = 1
        while leftmost != -1 and neighbor != -1:
            leftModsum, rightModsum = 0, 0
            ancestorLeftmost = leftmost
            ancestorNeighbor = neighbor
            for i in range(compareDepth):
                ancestorLeftmost = parent[ancestorLeftmost]
                ancestorNeighbor = parent[ancestorNeighbor]
                assert ancestorLeftmost != -1 and ancestorNeighbor != -1
                rightModsum += modifier[ancestorLeftmost]
                leftModsum += modifier[ancestorNeighbor]
            moveDistance = prelim[neighbor] + leftModsum + subtree_separation + node_size - (
                    prelim[leftmost] + rightModsum)
            if moveDistance > 0.0:
                tmp = cur
                leftSiblings = 0
                while tmp != -1 and tmp != ancestorNeighbor:
                    leftSiblings += 1
                    tmp = leftSibling[tmp]
                if tmp != -1:
                    portion = moveDistance / leftSiblings
                    tmp = cur
                    while tmp != ancestorNeighbor:
                        prelim[tmp] += moveDistance
                        modifier[tmp] += moveDistance
                        moveDistance -= portion
                        tmp = leftSibling[tmp]
                else:
                    return
            compareDepth += 1
            if size[leftmost] == 1:
                leftmost = self.getLeftMost(cur, 0, compareDepth)
            else:
                leftmost = edges[leftmost][0]
            neighbor = leftNeighbor[leftmost]

    def firstWalk(self, cur, level):
        size = self.size
        edges = self.edges
        leftSibling = self.leftSibling
        prelim = self.prelim
        modifier = self.modifier
        # 叶子结点
        if size[cur] == 1:
            if leftSibling[cur] == -1:
                prelim[cur] = 0
            else:
                prelim[cur] = prelim[leftSibling[cur]] + sibling_separation + node_size
        # 非叶节点
        else:
            for child in edges[cur]:
                self.firstWalk(child, level + 1)
            midpos = (prelim[edges[cur][0]] + prelim[edges[cur][-1]]) / 2
            if leftSibling[cur] != -1:
                prelim[cur] = prelim[leftSibling[cur]] + sibling_separation + node_size
                modifier[cur] = prelim[cur] - midpos
                self.apportion(cur)
            else:
                prelim[cur] = midpos

    def secondWalk(self, cur, level, modsum):
        size = self.size
        coorX = self.coorX
        coorY = self.coorY
        prelim = self.prelim
        modifier = self.modifier
        edges = self.edges
        coorX[cur] = self.xTopAdjustment + prelim[cur] + modsum
        coorY[cur] = self.yTopAdjustment + level * level_separation
        for child in edges[cur]:
            self.secondWalk(child, level + 1, modsum + modifier[cur])
