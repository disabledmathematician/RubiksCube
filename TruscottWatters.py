# I love you, My father Mark William Watters
# Thank you Harvard University and Massachusetts Institute of Technology
# Charles Truscott Watters, Byron Bay Australia
# Certified in Computational Thinking using Python from MITx
# Certified in Data Science in Using Python for Research PH556 (Harvard Centre for Continuing Education, Harvard Extension School)
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
		self.moves.append("F")
		new_state = Unsolved_Rubiks(self.state.copy(), self.moves.copy())
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
		tB[0], tB[1], tB[2], tB[3] = prev_B[2], prev_B[0], prev_B[3], prev_B[1]
		tU[0], tU[1] = prev_L[2], prev_L[0]
		tL[0], tL[2] = prev_D[2], prev_D[3]
		tD[2], tD[3] = prev_R[3], prev_R[1]
		tR[1], tR[3] = prev_U[0], prev_U[1]
		self.moves.append("B")
		new_state = Unsolved_Rubiks(self.state.copy(), self.moves.copy())
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
		tU[0], tU[1], tU[2], tU[3] = prev_U[2], prev_U[0], prev_U[3], prev_U[1]
		tL[0], tL[1] = prev_B[0], prev_B[1]
		tB[0], tB[1] = prev_R[0], prev_R[1]
		tR[0], tR[1] = prev_F[0], prev_F[1]
		tF[0], tF[1] = prev_L[0], prev_L[1]
		self.moves.append("U")
		new_state = Unsolved_Rubiks(self.state.copy(), self.moves.copy())
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
		tD[0], tD[1], tD[2], tD[3] = prev_D[2], prev_D[0], prev_D[3], prev_D[1]
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
		return str("Left: {} Front: {} Right: {} Back: {} Up: {} Down: {}".format(self.state[0], self.state[1], self.state[2], self.state[3], self.state[4], self.state[5]))

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
#	yet_moves = [lambda cube: cube.F(), lambda cube: cube.F2(), lambda cube: cube.F(), lambda cube: cube.R(), lambda cube: cube.L()]
#	yet_moves = [lambda cube: cube.B(), lambda cube: cube.F()]
	yet_moves = [lambda cube: cube.U(), lambda cube: cube.U2(), lambda cube: cube.U()]
	moved = []
	moved.append(cube)
	for l in yet_moves:
		n = l(moved[0])
		
		print("State: {} Moves: {}".format(n, n.moves))
"""
State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'R', 'R'] Down: ['O', 'O', 'W', 'W'] Moves: ['F']
State: Left: ['R', 'Y', 'R', 'Y'] Front: ['G', 'G', 'G', 'G'] Right: ['W', 'O', 'W', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'O', 'O'] Down: ['R', 'R', 'W', 'W'] Moves: ['F', 'F', 'F']
State: Left: ['R', 'Y', 'R', 'Y'] Front: ['G', 'R', 'G', 'W'] Right: ['W', 'W', 'O', 'O'] Back: ['O', 'B', 'Y', 'B'] Up: ['Y', 'G', 'O', 'G'] Down: ['R', 'B', 'W', 'B'] Moves: ['F', 'F', 'F', 'R']
State: Left: ['Y', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'W'] Right: ['W', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'] Moves: ['F', 'F', 'F', 'R', 'L']

[Program finished]

State: Left: ['R', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'R', 'R'] Down: ['O', 'O', 'W', 'W'] Moves: ['F']
State: Left: ['R', 'Y', 'R', 'Y'] Front: ['G', 'G', 'G', 'G'] Right: ['W', 'O', 'W', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'O', 'O'] Down: ['R', 'R', 'W', 'W'] Moves: ['F', 'F', 'F']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] Moves: ['F', 'F', 'F', 'F']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'B', 'W', 'B'] Moves: ['F', 'F', 'F', 'F', 'R']
State: Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'] Moves: ['F', 'F', 'F', 'F', 'R', 'L']

[Program finished]
State: Left: ['W', 'R', 'W', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'Y', 'Y'] Down: ['W', 'W', 'O', 'O'] Moves: ['B']
State: Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'] Moves: ['B', 'F']

[Program finished]

State: Left: ['B', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] Moves: ['U']
State: Left: ['G', 'G', 'R', 'R'] Front: ['O', 'O', 'G', 'G'] Right: ['B', 'B', 'O', 'O'] Back: ['R', 'R', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] Moves: ['U', 'U', 'U']
State: Left: ['R', 'R', 'R', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] Moves: ['U', 'U', 'U', 'U']

[Program finished]
"""
Charles_Rubiks()

# Thank you Byron Bay Woolworths and Australia Post, could not have a sanitized home or meals on wheels without you
# Thank you Services Australia and NDIS
# Thank you Byron Central Hospital Tuckeroo.
# I have paranoid Schizophrenia, am blind, have a brain tumour injury, varicose veins and a memory disorder
# Clozapine working a miracle