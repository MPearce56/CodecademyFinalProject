class Board:

	# each letter size is 5x5 and to make a board it requires 6 vertical lines
	# and it requires 6 horizontal lines. and lastly it requires 4 connectors
	X = ['X     X',
		 ' X   X ',
		 '   X   ', 
		 ' X   X ',
		 'X     X']

	O = [' OOO ',
		 'O   O',
		 'O   O',
		 'O   O',
		 ' OOO ']

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

	board = []

	def __init__(self):

		self.create()

	def create(self):

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
				self.board.append(self.BLANK_LETTER[index_counter] + self.VERTICAL_LINE[index_counter] + self.BLANK_LETTER[index_counter] + self.VERTICAL_LINE[index_counter] + self.BLANK_LETTER[index_counter])
			else:
				self.board.append(self.HORIZONTAL_LINE + self.LINE_CONNECTOR + self.HORIZONTAL_LINE + self.LINE_CONNECTOR + self.HORIZONTAL_LINE)
		print('\n'.join(self.board))


board = Board()