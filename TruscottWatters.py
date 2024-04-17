# I love you, My father Mark William Watters
# Thank you Harvard University and Massachusetts Institute of Technology
# Charles Truscott Watters, Byron Bay Australia
# Certified in Computational Thinking using Python from MITx
# Certified in Data Science in Using Python for Research PH556 (Harvard Centre for Continuing Education, Harvard Extension School)
# Love you high rollin Dad, Mark William Watters
import sys
class Unsolved_Rubiks:
	def __init__(self, state, moves):
		self.state = state.copy()
		self.moves = moves
	def is_solved(self):
		solved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]
		if self.state == solved_state:
			print("State: {} Solved by: {}".format(self.state, self.moves))
			sys.exit()
			
	def R(self):
		tL = self.state[0].copy()
		tF = self.state[1].copy()
		tR = self.state[2].copy()
		tB = self.state[3].copy()
		tU = self.state[4].copy()
		tD = self.state[5].copy()
		
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
		new_matrix = [tL, tF, tR, tB, tU, tD]
		n = self.moves.copy()
		n.append("R")
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def R_inv(self):
		for n in range(0, 3, 1):
			new_state = self.R()
		return new_state
	def R2(self):
		pass
		new_state.moves.append("R2")
		return new_state
	def L(self):
		tL = self.state[0].copy()
		tF = self.state[1].copy()
		tR = self.state[2].copy()
		tB = self.state[3].copy()
		tU = self.state[4].copy()
		tD = self.state[5].copy()
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
		new_matrix = [tL, tF, tR, tB, tU, tD]
		n = self.moves.copy()
		n.append("L")
#		self.moves.append("L")
		new_state = Unsolved_Rubiks(new_matrix, n)
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
		tL = self.state[0].copy()
		tF = self.state[1].copy()
		tR = self.state[2].copy()
		tB = self.state[3].copy()
		tU = self.state[4].copy()
		tD = self.state[5].copy()
		
		prev_L = tL.copy()
		prev_R = tR.copy()
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()
		tF[0], tF[1], tF[2], tF[3] = prev_F[2], prev_F[0], prev_F[3], prev_F[1]
		tU[2], tU[3] = prev_L[3], prev_L[1]
		tL[1], tL[3] = prev_D[0], prev_D[1]
		tD[0], tD[1] = prev_R[2], prev_R[0]
		tR[2], tR[0] = prev_U[3], prev_U[2]
		new_matrix = [tL, tF, tR, tB, tU, tD]
		n = self.moves.copy()
		n.append("F")
#		self.moves.append("F")
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def F_inv(self):
		for n in range(0, 3):
			new_state = self.F()
		return new_state
	def F2(self):
		for n in range(0, 2):
			new_state = self.F()
		return new_state
	def B(self):
		tL = self.state[0].copy()
		tF = self.state[1].copy()
		tR = self.state[2].copy()
		tB = self.state[3].copy()
		tU = self.state[4].copy()
		tD = self.state[5].copy()
	
		prev_L = tL.copy()
		prev_R = tR.copy()
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()
		tB[0], tB[1], tB[2], tB[3] = prev_B[2], prev_B[0], prev_B[3], prev_B[1]
		tU[0], tU[1] = prev_L[2], prev_L[0]
		tL[0], tL[2] = prev_D[2], prev_D[3]
		tD[2], tD[3] = prev_R[3], prev_R[1]
		tR[1], tR[3] = prev_U[0], prev_U[1]
		new_matrix = [tL, tF, tR, tB, tU, tD]
		n = self.moves.copy()
		n.append("B")
#		self.moves.append("B")
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def B_inv(self):
		for n in range(0, 3, 1):
			new_state = self.B()
		return new_state
	def B2(self):
		for n in range(0, 2):
			new_state = self.B()
		return new_state
	def U(self):
		tL = self.state[0].copy()
		tF = self.state[1].copy()
		tR = self.state[2].copy()
		tB = self.state[3].copy()
		tU = self.state[4].copy()
		tD = self.state[5].copy()
		
		prev_L = tL.copy()
		prev_R = tR.copy()
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()
		tU[0], tU[1], tU[2], tU[3] = prev_U[2], prev_U[0], prev_U[3], prev_U[1]
		tL[0], tL[1] = prev_B[0], prev_B[1]
		tB[0], tB[1] = prev_R[0], prev_R[1]
		tR[0], tR[1] = prev_F[0], prev_F[1]
		tF[0], tF[1] = prev_L[0], prev_L[1]
		new_matrix = [tL, tF, tR, tB, tU, tD]
		n = self.moves.copy()
		n.append("U")
#		self.moves.append("U")
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def U2(self):
		for n in range(0, 2):
			new_state = self.U()
		return new_state
	def U_inv(self):
		for n in range(0, 3, 1):
			new_state = self.U()
		return new_state
	def D(self):
		tL = self.state[0].copy()
		tF = self.state[1].copy()
		tR = self.state[2].copy()
		tB = self.state[3].copy()
		tU = self.state[4].copy()
		tD = self.state[5].copy()
		
		prev_L = tL.copy()
		prev_R = tR.copy()
		prev_F = tF.copy()
		prev_B = tB.copy()
		prev_U = tU.copy()
		prev_D = tD.copy()
		tD[0], tD[1], tD[2], tD[3] = prev_D[2], prev_D[0], prev_D[3], prev_D[1]
		tL[2], tL[3] = prev_B[2], prev_B[3]
		tB[2], tB[3] = prev_R[2], prev_R[3]
		tR[2], tR[3] = prev_F[2], prev_F[3]
		tF[2], tF[3] = prev_L[2], prev_L[3]
		new_matrix = [tL, tF, tR, tB, tU, tD]
		n = self.moves.copy()
		n.append("D")
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def D_inv(self):
		for n in range(0, 3, 1):
			new_state = self.D()
		return new_state
	def D2(self):
		for n in range(0, 2):
			new_state = self.D()
		return new_state
	def __str__(self):
		return str("Left: {} Front: {} Right: {} Back: {} Up: {} Down: {}".format(self.state[0], self.state[1], self.state[2], self.state[3], self.state[4], self.state[5]))

def Charles_Rubiks():
#	unsolved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]
	unsolved_state = [["Y", "R", "R", "R"], ["G", "Y", "G", "G"], ["G", "B", "O", "O"], ["R", "B", "B", "B"], ["O", "Y", "Y", "O"], ["W", "W", "W", "W"]]
#	yet_moves = [lambda cube: cube.R(), lambda cube: cube.R2(), lambda cube: cube.R_inv(), lambda cube: cube.L(), lambda cube: cube.L2(), lambda cube: cube.L_inv(), lambda cube: cube.F(), lambda cube: cube.F2(), lambda cube: cube.F_inv(), lambda cube: cube.B(), lambda cube: cube.B2(), lambda cube: cube.B_inv(), lambda cube: cube.U(), lambda cube: cube.U2(), lambda cube: cube.U_inv(), lambda cube: cube.D(), lambda cube: cube.D2(), lambda cube: cube.D_inv()]
	yet_moves = [lambda c: c.L(), lambda c: c.R(), lambda c: c.U(), lambda c: c.D(), lambda c: c.F(), lambda c: c.B()]
#	moved = []
#	moved.append(Unsolved_Rubiks(unsolved_state, []))
#	print(moved[0])
#	for l in yet_moves:
#		moved.append(l(moved[0]))
#	c = 1
#	while c < len(yet_moves) ** 6:
#		for l in yet_moves:
#			temp = l(moved[c])
#			moved.append(temp)
#		print(c)
#		c += 1
#	for n in range(1, len(moved)):
#		moved[n].is_solved()
#		print("State: {}, moves: {}".format(moved[n], moved[n].moves))
#	yet_moves = [lambda c: c.L(), lambda c: c.R(), lambda c: c.R2()]
	moved = []
	moved.append(Unsolved_Rubiks(unsolved_state, []))
	for l in yet_moves:
		t = l(moved[0])
		print("State: {}, Moves: {}".format(t, t.moves))
		
Charles_Rubiks()

"""

State: Left: ['R', 'R', 'Y', 'R'] Front: ['W', 'Y', 'W', 'G'] Right: ['G', 'B', 'O', 'O'] Back: ['R', 'Y', 'B', 'O'] Up: ['G', 'Y', 'G', 'O'] Down: ['B', 'W', 'B', 'W'], Moves: ['L']
State: Left: ['Y', 'R', 'R', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'B'] Back: ['O', 'B', 'Y', 'B'] Up: ['O', 'Y', 'Y', 'G'] Down: ['W', 'R', 'W', 'B'], Moves: ['R']
State: Left: ['R', 'B', 'R', 'R'] Front: ['Y', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'O'] Back: ['G', 'B', 'B', 'B'] Up: ['Y', 'O', 'O', 'Y'] Down: ['W', 'W', 'W', 'W'], Moves: ['U']
State: Left: ['Y', 'R', 'B', 'B'] Front: ['G', 'Y', 'R', 'R'] Right: ['G', 'B', 'G', 'G'] Back: ['R', 'B', 'O', 'O'] Up: ['O', 'Y', 'Y', 'O'] Down: ['W', 'W', 'W', 'W'], Moves: ['D']
State: Left: ['Y', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'Y'] Right: ['Y', 'B', 'O', 'O'] Back: ['R', 'B', 'B', 'B'] Up: ['O', 'Y', 'R', 'R'] Down: ['O', 'G', 'W', 'W'], Moves: ['F']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'Y', 'G', 'G'] Right: ['G', 'O', 'O', 'Y'] Back: ['B', 'R', 'B', 'B'] Up: ['R', 'Y', 'Y', 'O'] Down: ['W', 'W', 'O', 'B'], Moves: ['B']

[Program finished]

"""
# Thank you Byron Bay Woolworths and Australia Post, could not have a sanitized home or meals on wheels without you
# Thank you Services Australia and NDIS
# Disability Pension and National Disability Insurance Scheme
# I love my country Australia
# I love you Dad Mark William Watters, big bro Tai Truscott
# Almost finished my algorithm ... major error can wait until tommorrow. all tL, tR, tF, tB, tU, tD, and so on need to be copies, updating the state, and a way to keep track of moves