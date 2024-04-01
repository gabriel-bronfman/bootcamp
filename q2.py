class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for char in s:
            stack.append(char)
            if char == "]":
                repeat = ""
                letter = []
                stack.pop(-1)
                while stack[-1] != "[":
                    letter.append( stack[-1] )
                    stack.pop(-1)
                letter = letter[::-1]
                letter_str = "".join(letter)
                print(letter)
                stack.pop(-1)
                numb = ""
                while not stack[-1].isalpha() and stack[-1] != "[":
                    numb += stack[-1]
                    stack.pop(-1)

                    if len(stack) == 0:
                        break
                numb = numb[::-1]

                for i in range(int(numb)):
                    repeat += letter_str

                stack.append(repeat)

        return "".join(stack)
