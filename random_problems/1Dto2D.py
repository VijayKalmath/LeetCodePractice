class Solution:
    def construct2DArray(self, original, m: int, n: int):
        # Checking for 2D Construction validity
        if not len(original) == m*n : 
            return []
        
        # Initializing List of Lists for 2D array
        output = [[]]
        
        counter = 0
        
        for i in range(len(original)):
            output[-1].append(original[i])
            counter+=1
        
            if counter == n : 
                counter = 0 
                output.append([])
        
        return output[:-1]