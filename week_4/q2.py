class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for char in s:
            stack.append(char)
            if char == "]":
                repeat = ""
                letters = []
                stack.pop(-1)
                while stack[-1] != "[":
                    letters.append( stack[-1] )
                    stack.pop(-1)
                letters = letters[::-1]
                letters_str = "".join(letters)
                
                stack.pop(-1)
                repeat_num = ""
                while not stack[-1].isalpha() and stack[-1] != "[":
                    repeat_num += stack[-1]
                    stack.pop(-1)

                    if len(stack) == 0:
                        break
                repeat_num = repeat_num[::-1]

                for i in range(int(repeat_num)):
                    repeat += letters_str

                stack.append(repeat)

        return "".join(stack)

                
