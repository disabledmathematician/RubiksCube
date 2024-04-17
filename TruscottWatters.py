# I love you, My farher Mark William Watters
# Thank you Harvard University and Massachusetts Institute of Technology
# Charles Truscott Watters, Byron Bay Australia
# Certified in Computational Thinking using Python from MITx
# Love you high rollin Dad, Mark William Watters
# Until tommorrow
class Unsolved_Rubiks:
	def __init__(self, state, moves):
		self.state = state.copy()
		self.moves = moves
	def is_solved(self):
		pass
		solved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]
		if self.state == solved_state:
			return self.moves
	def R(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy()
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()
		tR[0], tR[1], tR[2], tR[3] = prev_R[2], prev_R[0], prev_R[3], prev_R[1]
		tU[1], tU[3] = prev_F[1], prev_F[3]
		tF[1], tF[3] = prev_D[1], prev_D[3]
		tD[1], tD[3] = prev_B[0], prev_B[1]
		tB[0], tB[2] = prev_U[3], prev_U[1]
		self.moves.append("R")
		new_state = Unsolved_Rubiks(self.state.copy(), self.moves.copy())
		return new_state
	def R_inv(self):
		for n in range(0, 3, 1):
			new_state = self.R()
		return new_state
	def R2(self):
		for n in range(0, 2, 1):
			new_state = self.R()
		return new_state
	def L(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()
		tL[0], tL[1], tL[2], tL[3] = prev_L[1], prev_L[3], prev_L[0], prev_L[2]
		tF[0], tF[2] = prev_D[0], prev_D[2]
		tB[1], tB[3] = prev_U[2], prev_U[0]
		tU[0], tU[2] = prev_F[0], prev_F[2]
		tD[0], tD[2] = prev_B[3], prev_B[1]
		self.moves.append("L")
		new_state = Unsolved_Rubiks(self.state.copy(), self.moves.copy())
		return new_state
	def L_inv(self):
		for n in range(0, 3, 1):
			new_state = self.L()
		return new_state
	def L2(self):
		for n in range(0, 2):
			new_state = self.L()
		return new_state
	def F(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()
		tF[0], tF[1], tF[2], tF[3] = prev_F[2], prev_F[0], prev_F[3], prev_F[1]
		pass
	def F_inv(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def F2(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def B(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
	
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def B_inv(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def B2(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()
		pass
	def U(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def U2(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def U_inv(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]

		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def D(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
		
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def D_inv(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]

		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def D2(self):
		tL = self.state[0]
		tF = self.state[1]
		tR = self.state[2]
		tB = self.state[3]
		tU = self.state[4]
		tD = self.state[5]
	
		prev_L = tL.copy()
		prev_R = tR.copy
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()

		pass
	def __str__(self):
		return str(self.state)

def Charles_Rubiks():
	unsolved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]
#	moves = [lambda C: C.R(), lambda C: C.R_inv(), lambda C: C.R2(), lambda C: C.L(), lambda C: C.L_inv(), lambda C: C.L2(), lambda C: C.F(), lambda C: C.F_inv(), lambda C: C.F2(), lambda C: C.B(), lambda C: C.B_inv(), lambda C: C.B2(), lambda C: C.U(), lambda C: C.U_inv(), lambda C: C.U2(), lambda C:C.D(), lambda C: C.D_inv(), lambda C: C.D2()]
#	moved = []
#	moved.append(Unsolved_Rubiks(unsolved_state, {}, 0))
#	for n in range(len(moves)):
#		moved.append(moves[n](moved[0]))
#	print(moved)
#	for e in moved:
#		print(e.state)
	cube = Unsolved_Rubiks(unsolved_state, [])
	yet_moves = [lambda cube: cube.R(), lambda cube: cube.L()]
	moved = []
	moved.append(cube)
	for l in yet_moves:
		n = l(moved[0])
		print("State: {} Moves: {}".format(n.state, n.moves))
"""
State: [['R', 'R', 'R', 'R'], ['G', 'W', 'G', 'W'], ['O', 'O', 'O', 'O'], ['Y', 'B', 'Y', 'B'], ['Y', 'G', 'Y', 'G'], ['W', 'B', 'W', 'B']] Moves: ['R']
State: [['R', 'R', 'R', 'R'], ['W', 'W', 'W', 'W'], ['O', 'O', 'O', 'O'], ['Y', 'Y', 'Y', 'Y'], ['G', 'G', 'G', 'G'], ['B', 'B', 'B', 'B']] Moves: ['R', 'L']

[Program finished]
"""
Charles_Rubiks()
