#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def reachableNodes(
        self, n: int, edges: list[list[int]], restricted: list[int]
    ) -> int:
        matrix = dict()
        restrictedNodeSet = set()
        for node in restricted:
            restrictedNodeSet.add(node)
        for edge in edges:
            if edge[0] not in restrictedNodeSet and edge[1] not in restrictedNodeSet:
                if edge[0] not in matrix:
                    matrix[edge[0]] = set()
                if edge[1] not in matrix:
                    matrix[edge[1]] = set()
                matrix[edge[0]].add(edge[1])
                matrix[edge[1]].add(edge[0])
        toBeVisitedNodeList = [0]
        visitedNodeSet = set()
        while len(toBeVisitedNodeList) > 0:
            curNode = toBeVisitedNodeList.pop(0)
            visitedNodeSet.add(curNode)
            if curNode in matrix:
                for expandNode in matrix[curNode]:
                    if expandNode not in visitedNodeSet:
                        toBeVisitedNodeList.append(expandNode)
        return len(visitedNodeSet)


if __name__ == '__main__':
    s = Solution()
    print(s.reachableNodes(n=7, edges=[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted=[4,5]))
