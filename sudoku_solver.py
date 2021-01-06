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
						# We will always put a 1 for each blank square first.
						# Then, we'll check if 1 is valid. If it is, we move on. Otherwise, we increment it.
						possible_value = 1 
						self.check_valid_inputs(i, j, possible_value)
						

			self.completed_sudoku = True

	def check_valid_inputs(self, row, column, value):
		'''
		This function checks if the inputted value is valid or not.
		'''

		# Used to keep track if the inputted value is valid or not.
		is_valid = True

		# Checks if the inputted number is already in the row.
		if value in array[row]:
			is_valid = False

		# Checks if the inputted number is already in the column.
		if is_valid:
			for i in range(9):
				if value == self.array[i][column]:
					is_valid = False

		# Find all the filled in numbers in the 3 by 3 box.

		# This is for the first 3 squares in any row.
		if 0 <= row <= 2:
			if 0 <= column <= 2:
				lowest_block_index = 0

			elif 3 <= column <= 5:
				lowest_block_index = 3

			else:
				lowest_block_index = 6
			
			for i in range(3):
				for j in range(lowest_block_index, lowest_block_index + 3):
					if self.array[i][j] in valid_inputs:
						valid_inputs.remove(self.array[i][j])
				

		# This is for the second 3 squares in any row.
		elif 3 <= row <= 5:
			if 0 <= column <= 2:
				lowest_block_index = 0

			elif 3 <= column <= 5:
				lowest_block_index = 3

			else:
				lowest_block_index = 6
			
			for i in range(3, 6):
				for j in range(lowest_block_index, lowest_block_index + 3):
					if self.array[i][j] in valid_inputs:
						valid_inputs.remove(self.array[i][j])

		# This is for the last 3 squares in any row.
		else:
			if 0 <= column <= 2:
				lowest_block_index = 0

			elif 3 <= column <= 5:
				lowest_block_index = 3

			else:
				lowest_block_index = 6
			
			for i in range(6, 9):
				for j in range(lowest_block_index, lowest_block_index + 3):
					if self.array[i][j] in valid_inputs:
						valid_inputs.remove(self.array[i][j])

		return is_valid

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