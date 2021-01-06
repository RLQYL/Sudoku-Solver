class sudoku_solver:

	def __init__(self, array):
		self.completed_sudoku = False
		self.array = array
		self.blank_squares = []

	def solve_sudoku(self):
		'''
		This function uses backtracking to solve a sudoku puzzle.
		'''
		if (not self.completed_sudoku):
			for i in range(len(self.array)):
				for j in range(len(self.array[i])):
					if self.array[i][j] == 0:
						self.blank_squares.append((i, j))
						x = self.find_valid_inputs(i, j)
						print(x)

			self.completed_sudoku = True

	def find_valid_inputs(self, row, column):
		'''
		This function is used to find all the possible valid inputs.
		'''

		# This is used to store the possible values.
		possible_values = [1,2,3,4,5,6,7,8,9]

		# Removes all the numbers that are already in the given row.
		for number in self.array[row]:
			if number in possible_values:
				possible_values.remove(number)

		# Removes all the numbers that are already in the given column.
		for row_value in range(9):
			if self.array[row_value][column] in possible_values:
				possible_values.remove(self.array[row_value][column])

		# Removes all the numbers that are already in that block.
		# This finds the row section the element is in.
		if (row >= 0 and row <= 2):
			row_index = 0
		elif (row >= 3 and row <= 5):
			row_index = 3
		else:
			row_index = 6
			
		# This finds the columnumn section the element is in.
		if (column >= 0 and column <= 2):
			column_index = 0
		elif (column >= 3 and column <= 5):
			column_index = 3
		else:
			column_index = 6
		
		# This for loop goes through each 3*3 section to check if there's a
		# number there already.
		for i in range(row_index, row_index + 3):
			for j in range(column_index, column_index + 3):
				if self.array[i][j] in possible_values:
					possible_values.remove(self.array[i][j])    
			
		return possible_values

	def print_array(self):
		'''
		This function prints the completed sudoku array, if possible.
		'''
		if (not self.completed_sudoku):
			print("The sudoku puzzle has not been completed.")
			return

		for i in self.array:
			for j in i:
				print(str(j) + " ", end='')
			print("")

if (__name__ == "__main__"):
	# 0's represent an empty space.
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
	sudoku.solve_sudoku()
	sudoku.print_array()