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
			print("Solved by: {}".format(self.moves))
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
		for n in range(0, 2, 1):
			new_state = self.R()
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
	unsolved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]

	yet_moves = [lambda cube: cube.R(), lambda cube: cube.R2(), lambda cube: cube.R_inv(), lambda cube: cube.L(), lambda cube: cube.L2(), lambda cube: cube.L_inv(), lambda cube: cube.F(), lambda cube: cube.F2(), lambda cube: cube.F_inv(), lambda cube: cube.B(), lambda cube: cube.B2(), lambda cube: cube.B_inv(), lambda cube: cube.U(), lambda cube: cube.U2(), lambda cube: cube.U_inv(), lambda cube: cube.D(), lambda cube: cube.D2(), lambda cube: cube.D_inv()]
	moved = []
	moved.append(Unsolved_Rubiks(unsolved_state, []))
	print(moved[0])
	for l in yet_moves:
		moved.append(l(moved[0]))
	c = 1
	while c < 18 ** 1:
		for l in yet_moves:
			temp = l(moved[c])
			moved.append(temp)
		print(c)
		c += 1
	for e in moved:
#		if e.is_solved() == True:
#			break
		print("State: {}, moves: {}".format(e, e.moves))
		
""" Left: ['R', 'R', 'R', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W']
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: []
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'R', 'R'] Down: ['O', 'O', 'W', 'W'], moves: ['F']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'R', 'R'] Down: ['O', 'O', 'W', 'W'], moves: ['F']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'R', 'R'] Down: ['O', 'O', 'W', 'W'], moves: ['F']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'Y', 'Y'] Down: ['W', 'W', 'O', 'O'], moves: ['B']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'Y', 'Y'] Down: ['W', 'W', 'O', 'O'], moves: ['B']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'Y', 'Y'] Down: ['W', 'W', 'O', 'O'], moves: ['B']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'], moves: ['R', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'], moves: ['R', 'L']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'], moves: ['R', 'F']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'], moves: ['R', 'B']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'], moves: ['R', 'U']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'], moves: ['R', 'D']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'], moves: ['L', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'], moves: ['L', 'L']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'], moves: ['L', 'F']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'], moves: ['L', 'B']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'], moves: ['L', 'U']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'], moves: ['L', 'D']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'], moves: ['F', 'R']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'], moves: ['F', 'L']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'], moves: ['F', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['F', 'B']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'], moves: ['F', 'U']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'], moves: ['F', 'D']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'], moves: ['B', 'R']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'], moves: ['B', 'L']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'], moves: ['B', 'F']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'], moves: ['B', 'B']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'], moves: ['B', 'U']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'], moves: ['B', 'D']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'], moves: ['U', 'R']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'], moves: ['U', 'L']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'], moves: ['U', 'F']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'], moves: ['U', 'B']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'U']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['U', 'D']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'W', 'R', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'O'] Up: ['Y', 'G', 'Y', 'R'] Down: ['W', 'B', 'W', 'B'], moves: ['D', 'R']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'W', 'R', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'O'] Up: ['Y', 'G', 'Y', 'R'] Down: ['W', 'B', 'W', 'B'], moves: ['D', 'R']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'W', 'R', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'O'] Up: ['Y', 'G', 'Y', 'R'] Down: ['W', 'B', 'W', 'B'], moves: ['D', 'R']
State: Left: ['R', 'B', 'R', 'B'] Front: ['W', 'G', 'W', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'Y', 'O', 'Y'] Up: ['G', 'Y', 'R', 'Y'] Down: ['O', 'W', 'B', 'W'], moves: ['D', 'L']
State: Left: ['R', 'B', 'R', 'B'] Front: ['W', 'G', 'W', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'Y', 'O', 'Y'] Up: ['G', 'Y', 'R', 'Y'] Down: ['O', 'W', 'B', 'W'], moves: ['D', 'L']
State: Left: ['R', 'B', 'R', 'B'] Front: ['W', 'G', 'W', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'Y', 'O', 'Y'] Up: ['G', 'Y', 'R', 'Y'] Down: ['O', 'W', 'B', 'W'], moves: ['D', 'L']
State: Left: ['R', 'W', 'B', 'W'] Front: ['R', 'G', 'R', 'G'] Right: ['Y', 'O', 'Y', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'B', 'R'] Down: ['G', 'O', 'W', 'W'], moves: ['D', 'F']
State: Left: ['R', 'W', 'B', 'W'] Front: ['R', 'G', 'R', 'G'] Right: ['Y', 'O', 'Y', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'B', 'R'] Down: ['G', 'O', 'W', 'W'], moves: ['D', 'F']
State: Left: ['R', 'W', 'B', 'W'] Front: ['R', 'G', 'R', 'G'] Right: ['Y', 'O', 'Y', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'B', 'R'] Down: ['G', 'O', 'W', 'W'], moves: ['D', 'F']
State: Left: ['W', 'R', 'W', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'Y', 'G', 'Y'] Back: ['O', 'B', 'O', 'B'] Up: ['B', 'R', 'Y', 'Y'] Down: ['W', 'W', 'G', 'O'], moves: ['D', 'B']
State: Left: ['W', 'R', 'W', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'Y', 'G', 'Y'] Back: ['O', 'B', 'O', 'B'] Up: ['B', 'R', 'Y', 'Y'] Down: ['W', 'W', 'G', 'O'], moves: ['D', 'B']
State: Left: ['W', 'R', 'W', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'Y', 'G', 'Y'] Back: ['O', 'B', 'O', 'B'] Up: ['B', 'R', 'Y', 'Y'] Down: ['W', 'W', 'G', 'O'], moves: ['D', 'B']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'U']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'U']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'U']
State: Left: ['R', 'R', 'O', 'O'] Front: ['G', 'G', 'B', 'B'] Right: ['O', 'O', 'R', 'R'] Back: ['B', 'B', 'G', 'G'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'D']
State: Left: ['R', 'R', 'O', 'O'] Front: ['G', 'G', 'B', 'B'] Right: ['O', 'O', 'R', 'R'] Back: ['B', 'B', 'G', 'G'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'D']
State: Left: ['R', 'R', 'O', 'O'] Front: ['G', 'G', 'B', 'B'] Right: ['O', 'O', 'R', 'R'] Back: ['B', 'B', 'G', 'G'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'D']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'W', 'R', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'O'] Up: ['Y', 'G', 'Y', 'R'] Down: ['W', 'B', 'W', 'B'], moves: ['D', 'R']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'W', 'R', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'O'] Up: ['Y', 'G', 'Y', 'R'] Down: ['W', 'B', 'W', 'B'], moves: ['D', 'R']
State: Left: ['R', 'R', 'B', 'B'] Front: ['G', 'W', 'R', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'O'] Up: ['Y', 'G', 'Y', 'R'] Down: ['W', 'B', 'W', 'B'], moves: ['D', 'R']
State: Left: ['R', 'B', 'R', 'B'] Front: ['W', 'G', 'W', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'Y', 'O', 'Y'] Up: ['G', 'Y', 'R', 'Y'] Down: ['O', 'W', 'B', 'W'], moves: ['D', 'L']
State: Left: ['R', 'B', 'R', 'B'] Front: ['W', 'G', 'W', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'Y', 'O', 'Y'] Up: ['G', 'Y', 'R', 'Y'] Down: ['O', 'W', 'B', 'W'], moves: ['D', 'L']
State: Left: ['R', 'B', 'R', 'B'] Front: ['W', 'G', 'W', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'Y', 'O', 'Y'] Up: ['G', 'Y', 'R', 'Y'] Down: ['O', 'W', 'B', 'W'], moves: ['D', 'L']
State: Left: ['R', 'W', 'B', 'W'] Front: ['R', 'G', 'R', 'G'] Right: ['Y', 'O', 'Y', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'B', 'R'] Down: ['G', 'O', 'W', 'W'], moves: ['D', 'F']
State: Left: ['R', 'W', 'B', 'W'] Front: ['R', 'G', 'R', 'G'] Right: ['Y', 'O', 'Y', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'B', 'R'] Down: ['G', 'O', 'W', 'W'], moves: ['D', 'F']
State: Left: ['R', 'W', 'B', 'W'] Front: ['R', 'G', 'R', 'G'] Right: ['Y', 'O', 'Y', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'B', 'R'] Down: ['G', 'O', 'W', 'W'], moves: ['D', 'F']
State: Left: ['W', 'R', 'W', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'Y', 'G', 'Y'] Back: ['O', 'B', 'O', 'B'] Up: ['B', 'R', 'Y', 'Y'] Down: ['W', 'W', 'G', 'O'], moves: ['D', 'B']
State: Left: ['W', 'R', 'W', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'Y', 'G', 'Y'] Back: ['O', 'B', 'O', 'B'] Up: ['B', 'R', 'Y', 'Y'] Down: ['W', 'W', 'G', 'O'], moves: ['D', 'B']
State: Left: ['W', 'R', 'W', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'Y', 'G', 'Y'] Back: ['O', 'B', 'O', 'B'] Up: ['B', 'R', 'Y', 'Y'] Down: ['W', 'W', 'G', 'O'], moves: ['D', 'B']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'U']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'U']
State: Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'U']
State: Left: ['R', 'R', 'O', 'O'] Front: ['G', 'G', 'B', 'B'] Right: ['O', 'O', 'R', 'R'] Back: ['B', 'B', 'G', 'G'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'D']
State: Left: ['R', 'R', 'O', 'O'] Front: ['G', 'G', 'B', 'B'] Right: ['O', 'O', 'R', 'R'] Back: ['B', 'B', 'G', 'G'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'D']
State: Left: ['R', 'R', 'O', 'O'] Front: ['G', 'G', 'B', 'B'] Right: ['O', 'O', 'R', 'R'] Back: ['B', 'B', 'G', 'G'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'], moves: ['D', 'D']

[Program finished]

""" 
Charles_Rubiks()

# Thank you Byron Bay Woolworths and Australia Post, could not have a sanitized home or meals on wheels without you
# Thank you Services Australia and NDIS
# Disability Pension and National Disability Insurance Scheme
# I love my country Australia
# I love you Dad Mark William Watters, big bro Tai Truscott
# Almost finished my algorithm ... major error can wait until tommorrow. all tL, tR, tF, tB, tU, tD, and so on need to be copies, updating the state, and a way to keep track of moves