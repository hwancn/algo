# -*- coding: utf-8 -*-
"""
图的深度遍历和广度遍历算法
时间复杂度为O(E),空间复杂度为O(V), E表示边数，V表示顶点数
visited用来记录顶点的是否访问情况，如果q被访问过，则visited[q]会被设置为True
queue为一个队列，用来存储已经被访问、但是相连的顶点还没有被访问的顶点
prev用来记录搜索路径，不过这个路径是反向的，prev[w]表示的是，顶点w是从哪个前驱顶点遍历过来的
"""

from typing import List, Optional, Generator, IO
from collections import deque


class Graph:
    """无向图"""
    def __init__(self, num_verties: int):
        """
        :param num_verties: 定点个数
        """
        self._num_verties = num_verties
        self._adjacency = [[] for _ in range(num_verties)]    # 邻接表

    def add_edge(self, s: int, t: int) -> None:
        """
        :param s:  顶点下标，本例中顶点里面存储的是整数，下标为0等同于定点0
        :param t:  顶点下标
        :return:
        """
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s: int, t: int, prev: List[Optional[int]]) -> Generator[str, None, None]:
        if prev[t] is not None and s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s: int, t: int) -> IO[str]:
        """
        广度优先遍历
        """
        if s == t:
            return
        visited = [False] * self._num_verties   # 访问顶点列表，True表示访问过，False表示没有访问过
        visited[s] = True
        queue = deque()   # queue为一个队列，用来存储已经被访问、但是相连的顶点还没有被访问的顶点
        queue.append(s)
        prev = [None] * self._num_verties   # prev用来记录搜索路径，不过这个路径是反向的，prev[w]表示的是，顶点w是从哪个前驱顶点遍历过来的

        while queue:
            v = queue.popleft()
            for neighbour in self._adjacency[v]:
                # 遍历q顶点的邻接顶点
                if not visited[neighbour]:
                    # 如果该邻接顶点没有访问过
                    prev[neighbour] = v  # 加入路径
                    if neighbour == t:
                        # 找到目标顶点
                        print("->".join(self._generate_path(s, t, prev)))
                        return
                    else:
                        visited[neighbour] = True
                        queue.append(neighbour)

    def dfs(self, s: int, t: int) -> IO[str]:
        """
        深度优先遍历
        """
        found = False
        visited = [False] * self._num_verties   # 访问顶点列表，True表示访问过，False表示没有访问过
        prev = [None] * self._num_verties   # prev用来记录搜索路径，不过这个路径是反向的，prev[w]表示的是，顶点w是从哪个前驱顶点遍历过来的

        def _dfs(from_vertex: int) -> None:
            nonlocal found
            if found:
                return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbour in self._adjacency[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)
        _dfs(s)
        print("->".join(self._generate_path(s, t, prev)))


if __name__ == "__main__":
    graph = Graph(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    graph.bfs(0, 7)
    graph.dfs(0, 7)

    graph.bfs(3, 7)
    graph.dfs(3, 7)

"""
0->1->2->5->7
0->1->2->5->4->6->7
3->4->5->7
3->0->1->2->5->4->6->7
"""