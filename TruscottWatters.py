# I love you, My farher Mark William Watters
# Thank you Harvard University and Massachusetts Institute of Technology
# Charles Truscott Watters, Byron Bay Australia
# Certified in Computational Thinking using Python from MITx

class Unsolved_Rubiks:
	def __init__(self, state, moves, how_many):
		self.state = state.copy()
		self.moves = moves
		self.how_many = how_many
	def is_solved(self):
		solved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]
		if self.state == solved_state:
			return self.moves
	def R(self):
		pass
	def R_inv(self):
		pass
	def R2(self):
		pass
	def L(self):
		pass
	def L_inv(self):
		pass
	def L2(self):
		pass
	def F(self):
		pass
	def F_inv(self):
		pass
	def F2(self):
		pass
	def B(self):
		pass
	def B_inv(self):
		pass
	def B2(self):
		pass
	def U(self):
		pass
	def U2(self):
		pass
	def U_inv(self):
		pass
	def D(self):
		pass
	def D_inv(self):
		pass
	def D2(self):
		pass
		

def Charles_Rubiks():
	unsolved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]
	moves = [lambda C: C.R(), lambda C: C.R_inv(), lambda C: C.R2(), lambda C: C.L(), lambda C: C.L_inv(), lambda C: C.L2(), lambda C: C.F(), lambda C: C.F_inv(), lambda C: C.F2(), lambda C: C.B(), lambda C: C.B_inv(), lambda C: C.B2(), lambda C: C.U(), lambda C: C.U_inv(), lambda C: C.U2(), lambda C:C.D(), lambda C: C.D_inv(), lambda C: C.D2()]
	moved = []
	moved.append(Unsolved_Rubiks(unsolved_state, {}, 0))
	for n in range(len(moves)):
		moved.append(moves[n](moved[0]))
	print(moved)
	for e in moved:
		print(e.state)
		
	
Charles_Rubiks()