class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        prev_op="+"

        for i in range(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
            if s[i] in '+-/*' or i==len(s)-1:
                if prev_op=="+":
                    stack.append(num)
                elif prev_op=="-":
                    stack.append(-num)
                elif prev_op=="*":
                    stack.append(stack.pop()*num)
                elif prev_op=="/":
                    stack.append(int(stack.pop()/num))
                prev_op=s[i]
                num=0

        return sum(stack)
                
                

        