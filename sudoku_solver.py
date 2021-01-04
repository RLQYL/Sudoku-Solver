class sudoku_solver:

	def __init__(self, array):
		self.array = array

	def solve_sudoku(self):
		pass

	def print_array(self):
		for i in self.array:
			for j in i:
				print(str(j) + " ", end='')
			print("")

if (__name__ == "__main__"):
	array = [
			 [0, 0, 0, 0, 0, 0, 9, 4, 0],
			 [6, 0, 0, 0, 0, 0, 2, 7, 0],
			 [8, 2, 0, 0, 4, 9, 6, 0, 0],
			 [0, 7, 4, 0, 0, 0, 0, 0, 0],
			 [1, 0, 0, 7, 6, 0, 0, 0, 0],
			 [0, 6, 2, 0, 0, 5, 0, 8, 0],
			 [0, 0, 0, 0, 5, 7, 0, 2, 3],
			 [0, 0, 0, 0, 0, 0, 0, 0, 0],
			 [7, 5, 3, 2, 0, 4, 0, 0, 0]
			]

	sudoku = sudoku_solver(array)
	sudoku.print_array()