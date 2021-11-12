# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
import heapq

class Solution:
    def minimumEffortPath(self, heights) -> int:
        # Using Binary Min Heap 
        # With every Node, calculate weight and add it to Heap
        # choose Min weight using Heap Pop 	
        row_size = len(heights)
        col_size = len(heights[0])

        pq = [[0,0,0]]

        heapq.heappush([],(0,0,0))

        ans = 0

        directions= [(1,0),(-1,0),(0,1),(0,-1)]
        
        visited = set()

        while pq:

            pos = heapq.heappop(pq)
            
            weight = pos[0]
            
            ans = max(ans,weight)

            
            x = pos[1]
            y = pos[2]

            visited.add((x,y))

            if (x,y) == (row_size - 1, col_size - 1):
                return ans
            
            for k in range(4):

                new_x = x + directions[k][0]
                new_y = y + directions[k][1]

                if 0 <= new_x < row_size and 0 <= new_y < col_size and (new_x,new_y) not in visited:
                    heapq.heappush(pq,(abs(heights[new_x][new_y] - heights[x][y]),new_x,new_y))

        return ans



if __name__ == '__main__':
        X  = Solution()
        heights = [[1,2,2],[3,8,2],[5,3,5]]
        print(X.minimumEffortPath(heights))
        heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
        print(X.minimumEffortPath(heights))
        