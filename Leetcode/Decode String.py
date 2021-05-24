class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                tmp = ""
                while stack:
                    x = stack.pop()
                    if x == '[':
                        cnt = stack.pop()
                        stack.append(int(cnt) * tmp)
                        break
                    else:
                        tmp = x + tmp
                i += 1
            elif s[i].isdigit():
                cnt_tmp = ""
                while s[i].isdigit():
                    cnt_tmp += s[i]
                    i += 1
                stack.append(cnt_tmp)
            else:
                stack.append(s[i])
                i += 1
        return "".join(stack)