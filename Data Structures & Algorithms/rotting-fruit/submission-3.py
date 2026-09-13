class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1

        while queue and fresh>0:
            size = len(queue)
            print(queue)
            minutes+=1
            for i in range(size):
                r,c = queue.popleft()
                if 0<=r-1 and 0<=c and r-1<rows and c<cols and grid[r-1][c]==1:
                    grid[r-1][c] = 2
                    queue.append((r-1,c))
                    fresh-=1
                    print((r-1,c))
                if 0<=r+1 and 0<=c and r+1<rows and c<cols and grid[r+1][c]==1:
                    grid[r+1][c] = 2
                    queue.append((r+1,c))
                    fresh-=1
                    print((r+1,c))
                if 0<=r and 0<=c-1 and r<rows and c-1<cols and grid[r][c-1]==1:
                    grid[r][c-1] = 2
                    queue.append((r,c-1))
                    fresh-=1
                    print((r,c-1))
                if 0<=r and 0<=c+1 and r<rows and c+1<cols and grid[r][c+1]==1:
                    grid[r][c+1] = 2
                    queue.append((r,c+1))
                    fresh-=1
                    print((r,c+1))


        return -1 if fresh>0 else minutes
                    



        






        