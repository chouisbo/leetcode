class MyStack:

    def __init__(self):
        self.queues = [[], []]
        # 指向出队队列的索引位置
        self.q = 0

    def push(self, x: int) -> None:
        # 分别获取出队队列和入队队列
        de_queue = self.queues[self.q]
        en_queue = self.queues[1-self.q]

        # 将新元素存进入队队列，然后依次将所有出队队列中的元素存进入队队列
        en_queue.append(x)
        while de_queue:
            en_queue.append(de_queue.pop(0))
        
        # 切换索引，出队队列索引指向入队队列
        self.q = 1-self.q


    def pop(self) -> int:
        if not self.empty():
            return self.queues[self.q].pop(0)
        else:
            return None
        

    def top(self) -> int:
        if not self.empty():
            return self.queues[self.q][0]
        else:
            return None


    def empty(self) -> bool:
        if len(self.queues[self.q]) > 0:
            return False
        else:
            return True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()