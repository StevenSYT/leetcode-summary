class Solution:
    def __init__(self):
        self.pos = 0

    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"
        n = len(s)
        while self.pos < n:
            ch = s[self.pos]
            self.pos += 1
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch == "(":
                # 这里因为pos算是全局变量，calculate会继续把pos往后移动
                num = self.calculate(s)
            # 决定要不要进栈
            if self.pos == n or ch in ["+", "-", "*", "/", ")"]:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    stack.append(int(stack.pop() / num))
                # 更新op和num
                op = ch
                num = 0
            if ch == ")":
                break
        return sum(stack)