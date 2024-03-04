class MyQueue:

    def __init__(self):
        self.en_stack = list()
        self.de_stack = list()
        self.en_stack_head = None

    def push(self, x: int) -> None:
        if len(self.en_stack) <= 0:
            self.en_stack_head = x
        self.en_stack.append(x)

    def pop(self) -> int:
        if len(self.de_stack) > 0:
            return self.de_stack.pop(-1)
        else:
            while self.en_stack:
                self.de_stack.append(self.en_stack.pop(-1))
            self.en_stack_head = None
            if len(self.de_stack) > 0:
                return self.de_stack.pop(-1)
        return None

    def peek(self) -> int:
        if len(self.de_stack) > 0:
            return self.de_stack[-1]
        else:
            return self.en_stack_head

    def empty(self) -> bool:
        if len(self.de_stack) <= 0 and len(self.en_stack) <= 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

