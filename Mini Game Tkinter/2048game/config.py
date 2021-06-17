
class Config:

	def __init__(self):

		#GAME CONFIG
		self.title = "2048"
		self.row = 4
		self.column = 4


		#WINDOW CONFIG
		base  = 120
		ratio = 3.9
		self.width = int(base*ratio)
		self.height = int(base*ratio + 17)
		self.screen = f"{self.width}x{self.height}"

		#cell settings
		self.cell_bg = {  #background cell color
		'2': '#eee4da',
		'4': '#ede0c8',
 		'8': '#f2b179',
		'16': '#f59563',
		'32': '#f67c5f',
		'64': '#f65e3b',
		'128': '#edcf72',
		'256': '#edcc61',
		'512': '#edc850',
		'1024': '#edc53f',
		'2048': '#edc22e',
		'beyond': '#3c3a32'
		}

		self.cell_color = { # font color
		'2': '#776e65',
		'4': '#776e65',
		'8': '#f9f6f2',
		'16': '#f9f6f2',
		'32': '#f9f6f2',
		'64': '#f9f6f2',
		'128': '#f9f6f2',
		'256': '#f9f6f2',
		'512': '#f9f6f2',
		'1024': '#f9f6f2',
		'2048': '#f9f6f2',
		'beyond': '#f9f6f2'
		}


		# key pressed list
		self.up_keys = ('w', 'W', 'Up')
		self.left_keys = ('a', 'A', 'Left')
		self.down_keys = ('s', 'S', 'Down')
		self.right_keys = ('d', 'D', 'Right')
