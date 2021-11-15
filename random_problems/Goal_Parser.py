class Solution:
    def interpret(self, command: str) -> str:
        out = ''
        i = 0 
        while(i < len(command)):
            if command[i] == "G" :
                out += "G"
                i += 1
            elif command[i] == "(" and command[i+1] == ")" : 
                out +="o"
                i +=2
            else : 
                out +="al"
                i +=4  
        return out