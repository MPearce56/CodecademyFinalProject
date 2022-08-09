class Board:

	# each character size is 5 spaces by 5 lines and to make a board it requires 6 vertical lines
	# and it requires 6 horizontal lines. and lastly it requires 4 connectors
	X = ['X   X',
		 ' X X ',
		 '  X  ', 
		 ' X X ',
		 'X   X']

	O = [' OOO ',
		 'O   O',
		 'O   O',
		 'O   O',
		 ' OOO ']

	ONE = [' 11  ',
		   '111  ',
		   ' 11  ',
		   ' 11  ',
		   '1111 ']

	TWO = [' 22  ',
		   '2  2 ',
		   '  2  ',
		   ' 2   ',
		   '2222 ']

	THREE = ['333  ',
			 '   3 ',
			 ' 33  ',
			 '   3 ',
			 '333  ']

	FOUR = ['4  4 ',
			'4  4 ',
			'4444 ',
			'   4 ',
			'   4 ']

	FIVE = ['5555 ',
			'5    ',
			'555  ',
			'   5 ',
			'555  ']

	SIX = ['  6  ',
		   ' 6   ',
		   '6666 ',
		   '6   6',
		   ' 666 ']

	SEVEN = ['77777',
			 '   7 ',
			 '  7  ',
			 '  7  ',
			 '  7  ']

	EIGHT = [' 888 ',
			 '8   8',
			 ' 888 ',
			 '8   8',
			 ' 888 ']

	NINE = [' 9999',
			'9   9',
			' 9999',
			'   9 ',
			'  9  ']

	BLANK_LETTER = ['     ',
					'     ',
					'     ',
					'     ',
					'     ']

	VERTICAL_LINE = ['  |  ',
					 '  |  ',
					 '  |  ',
					 '  |  ',
					 '  |  ']

	HORIZONTAL_LINE = '-----'

	LINE_CONNECTOR = '  +  '
	LINE_MARGIN = '\n' * 2

	X_AND_O = {'X': X, 'O': O}

	numbers = [(1, ONE),
			   (2, TWO),
			   (3, THREE),
			   (4, FOUR),
			   (5, FIVE),
			   (6, SIX),
			   (7, SEVEN),
			   (8, EIGHT),
			   (9, NINE)]

	board = []
	tutorial_board = []

	# Tic tac toe boards are 3 by 3 this is a grid that represents that
	# each key represents either the top level, mid level, or bottom level of the board
	# each value is a list of options that correspond with each cell of a tic tac toe board
	# cells 1, 2, and 3 being in the top level of the board and so on
	# the second list is a multilevel list that corresponds with end index of where we need to place our letters line by line.

	grid = {
		1: [(1, 2, 3), [(0, 5, 10, 15, 20), (2, 7, 12, 17, 22), (4, 9, 14,19, 24)]],
		2: [(4, 5, 6), [(30, 35, 40, 45, 50), (32, 37, 42, 47, 52), (34, 39, 44, 49, 54)]],
		3: [(7, 8, 9), [(60, 65, 70, 75, 80), (62, 67, 72, 77, 82), (64, 69, 74, 79, 84)]]
	}


	def __init__(self):

		self.create_board()
		self.create_tutorial_board()

	def place_char(self, cell, char, tutorial_board=False):

		level = 0

		for i in range(3):
			if cell in self.grid[i+1][0]:
				level = i + 1

		cell_tuple, cell_range_list = self.grid[level]
		index_of_cell = cell_tuple.index(cell)
		cell_range = cell_range_list[index_of_cell]
		cell_start = cell_range[0]
		cell_end = cell_range[1]


		if tutorial_board:
			for index in cell_range:
				self.tutorial_board[index] = char[cell_range.index(index)]
		else:
			for index in cell_range:
				self.board[index] = char[cell_range.index(index)]



	def print_board(self, tutorial_board=False):

		if tutorial_board:
			board = self.tutorial_board
		else:
			board = self.board

		board_as_string = ""

		for i in range(0, len(board), 5):
			line = ""
			for x in range(5):
				line += board[i+x]

			board_as_string += line + '\n'

		print(board_as_string)


	def create_board(self):

		""" Creates blank game board """

		# The easiest way to create the board would be line by line.
		# We need a total of 17 lines. 15 lines for letters and 2 lines for horizontal lines
		index_counter = 0
		for i in range(17):

			# Because the list objects only have a max index of 4 we need to make an index counter that resets when at max range
			if index_counter > 4:
				index_counter = 0

			# On the 6th iteration we need to print our horizontal lines
			# so we adjust the value of i by 1 so that we dont run into any problems with the 0 index
			if (i+1) % 6 != 0:
				#print(i)
				self.board.extend([self.BLANK_LETTER[index_counter], self.VERTICAL_LINE[index_counter], self.BLANK_LETTER[index_counter], self.VERTICAL_LINE[index_counter], self.BLANK_LETTER[index_counter]])
			else:
				self.board.extend([self.HORIZONTAL_LINE, self.LINE_CONNECTOR, self.HORIZONTAL_LINE, self.LINE_CONNECTOR, self.HORIZONTAL_LINE])

		self.tutorial_board = [chunk for chunk in self.board]

	def create_tutorial_board(self):

		for i in range(len(self.numbers)):
			self.place_char(self.numbers[i][0], self.numbers[i][1], tutorial_board=True)

	def tutorial(self):

		print("Choose the number that corresponds with where you want to place your X or O.")
		print('\n' * 2)

		self.print_board(tutorial_board=True)