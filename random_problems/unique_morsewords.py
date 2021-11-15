class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_Code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_list = []
        for word in words : 
            morse_list .append(''.join([morse_Code[ord(x) - 97] for x in word]))
            
        return len(set(morse_list))