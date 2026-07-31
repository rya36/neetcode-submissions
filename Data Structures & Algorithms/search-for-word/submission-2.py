class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(x, y, i):


            if (x, y) in visited or grid[x][y] != word[i]:
                return False

            
            if i == len(word) - 1:
                return True 
                
            visited.add((x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if dfs(nx, ny, i + 1):
                        visited.remove((x, y))
                        return True

            visited.remove((x, y))
            return False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c, 0):
                    return True
        
        return False
                
                