# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X



class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m,n = self.get_board_size(board)
        if m == 0 or n == 0:
        	return []
        #check the 1 and last rows, with 1 and last cols, and save all the O s; and then flip all the other 'X'	

        res = []
        queue = []
        queue = queue + [(0,i) for i in range(n)]
        queue = queue + [(m-1,i) for i in range(n)]
        queue = queue + [(j,0) for j in range(1,m-1)]
        queue = queue + [(j,n-1) for j in range(1,m-1)]
        
        while len(queue) > 0:
        	idx = queue[0]
        	if board[idx[0]][idx[1]] == 'O' and idx not in res:
        		res.append(idx)
        		neight_lst = self.get_neight(idx[0],idx[1],m,n, board)
        		add_lst = filter(lambda x: x not in res, neight_lst)
        		queue = queue + add_lst

        	queue.pop(0)
        new_board = [['X']*n	for i in range(m)]
        for idx in res:
        	new_board[idx[0]][idx[1]] = 'O'
        return new_board

    def get_board_size(self, board):
    	#m is the # of rows
    	m = len(board)
    	if m == 0:
    		n = 0
    		return m,n
    	#n is the # of cols
    	n = len(board[0])
    	return m,n
    
    def get_neight(self, i,j,m,n, board):
    	res= []
    	if i-1 >= 0 and board[i-1][j] == 'O':
    		res.append((i-1,j))
    	if i+1 <= m-1 and board[i+1][j] == 'O':
    		res.append((i+1,j))
    	if j-1 >= 0 and board[i][j-1] == 'O':
    		res.append((i,j-1))
    	if j+1 <= n-1 and board[i][j+1] == 'O':
    		res.append((i, j+1))
    	return res



if __name__ == '__main__':
	test = Solution()
	input1 = [['X','X','O'],['X','O','X'],['X','X','X']]
	input2 = [['X','X','O','O'],['X','X','X','X'],['X','X','O','X'],['X','X','X','X']]
	print test.solve(input1)
	print test.solve(input2)


