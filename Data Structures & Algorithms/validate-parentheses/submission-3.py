class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        for i in s:
            if i == "[" or i == "{" or i == "(":
                pilha.append(i)
                continue
            
            if not pilha:
                return False
            
            elif i == "]":
                if pilha.pop() != "[":
                    return False

            elif i == "}":
                if pilha.pop() != "{":
                    return False
                
            else:
                if pilha.pop() != "(":
                    return False

        if not pilha: 
            return True
        return False