class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ans=0
        for c in tokens:
            if c in "+-*/":
                a=stack.pop()
                b=stack.pop()
                stack.append(self.expression(c,b,a))
            else:
                stack.append(int(c))
        return stack[-1]

    def expression(self,c,b,a):
        if c=="+":
            return b+a
        elif c=="-":
            return b-a
        elif c=="*":
            return b*a
        else:
            return int(b/a)



        