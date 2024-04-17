#pylint:disable=W0612
# I love you, My father Mark William Watters
# Thank you Harvard University and Massachusetts Institute of Technology
# Charles Truscott Watters, Byron Bay Australia
# Certified in Computational Thinking using Python from MITx
# Certified in Data Science in Using Python for Research PH556 (Harvard Centre for Continuing Education, Harvard Extension School)
# Love you high rollin Dad, Mark William Watters
import sys
class Unsolved_Rubiks:
	def __init__(self, state, moves):
		self.state = state
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
		return
	def L(self):
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
		tL[0], tL[1], tL[2], tL[3] = prev_L[1], prev_L[3], prev_L[0], prev_L[2]
		tF[0], tF[2] = prev_D[0], prev_D[2]
		tB[1], tB[3] = prev_U[2], prev_U[0]
		tU[0], tU[2] = prev_F[0], prev_F[2]
		tD[0], tD[2] = prev_B[3], prev_B[1]
		new_matrix = [tL, tF, tR, tB, tU, tD]
		n = self.moves.copy()
		n.append("L")
#		self.moves.append("L")
		new_state = Unsolved_Rubiks(new_matrix, [])
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
	solved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]
	unsolved_state = solved_state
	state = Unsolved_Rubiks(unsolved_state, [])
	yet_moves =[lambda c: c.L(), lambda c: c.R(), lambda c: c.U(), lambda c: c.D(), lambda c: c.F(), lambda c: c.B()]
	States = []
	States.append(state)
	print(state.state, state.moves)
	for l in yet_moves:
		n = l(state)
		print(n, n.moves)
		States.append(n)
	c = 1
	while c < 18:
		for l in yet_moves:
			States.append(l(States[c]))
		c += 1
	print(States)
	for e in States:
		print(e, e.moves)
#	
Charles_Rubiks()

"""
[['R', 'R', 'R', 'R'], ['G', 'G', 'G', 'G'], ['O', 'O', 'O', 'O'], ['B', 'B', 'B', 'B'], ['Y', 'Y', 'Y', 'Y'], ['W', 'W', 'W', 'W']] []
Left: ['R', 'R', 'R', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'W', 'B', 'W'] []
Left: ['R', 'R', 'R', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'B', 'W', 'B'] ['R']
Left: ['B', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['U']
Left: ['R', 'R', 'B', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['D']
Left: ['R', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'R', 'R'] Down: ['O', 'O', 'W', 'W'] ['F']
Left: ['W', 'R', 'W', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'Y', 'Y'] Down: ['W', 'W', 'O', 'O'] ['B']

[Program finished]
[['R', 'R', 'R', 'R'], ['G', 'G', 'G', 'G'], ['O', 'O', 'O', 'O'], ['B', 'B', 'B', 'B'], ['Y', 'Y', 'Y', 'Y'], ['W', 'W', 'W', 'W']] []
Left: ['R', 'R', 'R', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'W', 'B', 'W'] []
Left: ['R', 'R', 'R', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'B', 'W', 'B'] ['R']
Left: ['B', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['U']
Left: ['R', 'R', 'B', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['D']
Left: ['R', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'R', 'R'] Down: ['O', 'O', 'W', 'W'] ['F']
Left: ['W', 'R', 'W', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'Y', 'Y'] Down: ['W', 'W', 'O', 'O'] ['B']
[<__main__.Unsolved_Rubiks object at 0x75ecef5810>, <__main__.Unsolved_Rubiks object at 0x75ecef5890>, <__main__.Unsolved_Rubiks object at 0x75ecef58d0>, <__main__.Unsolved_Rubiks object at 0x75ecef5910>, <__main__.Unsolved_Rubiks object at 0x75ecef5950>, <__main__.Unsolved_Rubiks object at 0x75ecef5850>, <__main__.Unsolved_Rubiks object at 0x75ecef59d0>, <__main__.Unsolved_Rubiks object at 0x75ecef5f10>, <__main__.Unsolved_Rubiks object at 0x75ecef6110>, <__main__.Unsolved_Rubiks object at 0x75ecef6310>, <__main__.Unsolved_Rubiks object at 0x75ecef6550>, <__main__.Unsolved_Rubiks object at 0x75ecef6790>, <__main__.Unsolved_Rubiks object at 0x75ecef69d0>, <__main__.Unsolved_Rubiks object at 0x75ecef6c90>, <__main__.Unsolved_Rubiks object at 0x75ecef6e90>, <__main__.Unsolved_Rubiks object at 0x75ecef7110>, <__main__.Unsolved_Rubiks object at 0x75ecef7390>, <__main__.Unsolved_Rubiks object at 0x75ecef7610>, <__main__.Unsolved_Rubiks object at 0x75ecef7890>, <__main__.Unsolved_Rubiks object at 0x75ecef7b50>, <__main__.Unsolved_Rubiks object at 0x75ecef7d50>, <__main__.Unsolved_Rubiks object at 0x75ecef7fd0>, <__main__.Unsolved_Rubiks object at 0x75eceec290>, <__main__.Unsolved_Rubiks object at 0x75eceec510>, <__main__.Unsolved_Rubiks object at 0x75eceec7d0>, <__main__.Unsolved_Rubiks object at 0x75eceeca90>, <__main__.Unsolved_Rubiks object at 0x75eceecc90>, <__main__.Unsolved_Rubiks object at 0x75eceecf10>, <__main__.Unsolved_Rubiks object at 0x75eceed190>, <__main__.Unsolved_Rubiks object at 0x75eceed410>, <__main__.Unsolved_Rubiks object at 0x75eceed690>, <__main__.Unsolved_Rubiks object at 0x75eceed950>, <__main__.Unsolved_Rubiks object at 0x75eceedb50>, <__main__.Unsolved_Rubiks object at 0x75eceeddd0>, <__main__.Unsolved_Rubiks object at 0x75eceee050>, <__main__.Unsolved_Rubiks object at 0x75eceee2d0>, <__main__.Unsolved_Rubiks object at 0x75eceee550>, <__main__.Unsolved_Rubiks object at 0x75eceee810>, <__main__.Unsolved_Rubiks object at 0x75eceeea10>, <__main__.Unsolved_Rubiks object at 0x75eceeec90>, <__main__.Unsolved_Rubiks object at 0x75eceeef10>, <__main__.Unsolved_Rubiks object at 0x75eceef190>, <__main__.Unsolved_Rubiks object at 0x75eceef410>, <__main__.Unsolved_Rubiks object at 0x75eceef690>, <__main__.Unsolved_Rubiks object at 0x75eceef890>, <__main__.Unsolved_Rubiks object at 0x75eceefad0>, <__main__.Unsolved_Rubiks object at 0x75eceefd10>, <__main__.Unsolved_Rubiks object at 0x75eceeff50>, <__main__.Unsolved_Rubiks object at 0x75ecee01d0>, <__main__.Unsolved_Rubiks object at 0x75ecee0490>, <__main__.Unsolved_Rubiks object at 0x75ecee0690>, <__main__.Unsolved_Rubiks object at 0x75ecee0910>, <__main__.Unsolved_Rubiks object at 0x75ecee0b90>, <__main__.Unsolved_Rubiks object at 0x75ecee0e10>, <__main__.Unsolved_Rubiks object at 0x75ecee1090>, <__main__.Unsolved_Rubiks object at 0x75ecee1350>, <__main__.Unsolved_Rubiks object at 0x75ecee1550>, <__main__.Unsolved_Rubiks object at 0x75ecee17d0>, <__main__.Unsolved_Rubiks object at 0x75ecee1a50>, <__main__.Unsolved_Rubiks object at 0x75ecee1cd0>, <__main__.Unsolved_Rubiks object at 0x75ecee1f50>, <__main__.Unsolved_Rubiks object at 0x75ecee2210>, <__main__.Unsolved_Rubiks object at 0x75ecee2410>, <__main__.Unsolved_Rubiks object at 0x75ecee2690>, <__main__.Unsolved_Rubiks object at 0x75ecee2910>, <__main__.Unsolved_Rubiks object at 0x75ecee2b90>, <__main__.Unsolved_Rubiks object at 0x75ecee2e10>, <__main__.Unsolved_Rubiks object at 0x75ecee30d0>, <__main__.Unsolved_Rubiks object at 0x75ecee32d0>, <__main__.Unsolved_Rubiks object at 0x75ecee3550>, <__main__.Unsolved_Rubiks object at 0x75ecee37d0>, <__main__.Unsolved_Rubiks object at 0x75ecee3a50>, <__main__.Unsolved_Rubiks object at 0x75ecee3cd0>, <__main__.Unsolved_Rubiks object at 0x75ecee3f90>, <__main__.Unsolved_Rubiks object at 0x75ecedc1d0>, <__main__.Unsolved_Rubiks object at 0x75ecedc450>, <__main__.Unsolved_Rubiks object at 0x75ecedc6d0>, <__main__.Unsolved_Rubiks object at 0x75ecedc950>, <__main__.Unsolved_Rubiks object at 0x75ecedcbd0>, <__main__.Unsolved_Rubiks object at 0x75ecedce50>, <__main__.Unsolved_Rubiks object at 0x75ecedd050>, <__main__.Unsolved_Rubiks object at 0x75ecedd290>, <__main__.Unsolved_Rubiks object at 0x75ecedd4d0>, <__main__.Unsolved_Rubiks object at 0x75ecedd710>, <__main__.Unsolved_Rubiks object at 0x75ecedd950>, <__main__.Unsolved_Rubiks object at 0x75eceddc10>, <__main__.Unsolved_Rubiks object at 0x75ecedde10>, <__main__.Unsolved_Rubiks object at 0x75ecede090>, <__main__.Unsolved_Rubiks object at 0x75ecede310>, <__main__.Unsolved_Rubiks object at 0x75ecede590>, <__main__.Unsolved_Rubiks object at 0x75ecede810>, <__main__.Unsolved_Rubiks object at 0x75ecedead0>, <__main__.Unsolved_Rubiks object at 0x75ecedecd0>, <__main__.Unsolved_Rubiks object at 0x75ecedef50>, <__main__.Unsolved_Rubiks object at 0x75ecedf1d0>, <__main__.Unsolved_Rubiks object at 0x75ecedf450>, <__main__.Unsolved_Rubiks object at 0x75ecedf6d0>, <__main__.Unsolved_Rubiks object at 0x75ecedf990>, <__main__.Unsolved_Rubiks object at 0x75ecedfb90>, <__main__.Unsolved_Rubiks object at 0x75ecedfe10>, <__main__.Unsolved_Rubiks object at 0x75ecf080d0>, <__main__.Unsolved_Rubiks object at 0x75ecf08350>, <__main__.Unsolved_Rubiks object at 0x75ecf085d0>, <__main__.Unsolved_Rubiks object at 0x75ecf08890>, <__main__.Unsolved_Rubiks object at 0x75ecf08a90>, <__main__.Unsolved_Rubiks object at 0x75ecf08d10>, <__main__.Unsolved_Rubiks object at 0x75ecf08f90>, <__main__.Unsolved_Rubiks object at 0x75ecf09210>, <__main__.Unsolved_Rubiks object at 0x75ecf09490>]
Left: ['R', 'R', 'R', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] []
Left: ['R', 'R', 'R', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'W', 'B', 'W'] []
Left: ['R', 'R', 'R', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'B', 'W', 'B'] ['R']
Left: ['B', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['U']
Left: ['R', 'R', 'B', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['D']
Left: ['R', 'W', 'R', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'R', 'R'] Down: ['O', 'O', 'W', 'W'] ['F']
Left: ['W', 'R', 'W', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'Y', 'Y'] Down: ['W', 'W', 'O', 'O'] ['B']
Left: ['R', 'R', 'R', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'W', 'Y', 'W'] []
Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'] ['R']
Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'W', 'B', 'W'] ['U']
Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'G', 'Y'] Down: ['B', 'B', 'W', 'W'] ['D']
Left: ['R', 'B', 'R', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'R', 'R'] Down: ['O', 'O', 'B', 'W'] ['F']
Left: ['B', 'R', 'W', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['B', 'W', 'O', 'O'] ['B']
Left: ['R', 'R', 'R', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'] []
Left: ['R', 'R', 'R', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'Y', 'W', 'B'] ['R', 'R']
Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'B', 'W', 'B'] ['R', 'U']
Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'Y', 'G'] Down: ['W', 'W', 'B', 'B'] ['R', 'D']
Left: ['R', 'W', 'R', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'R'] Down: ['O', 'O', 'W', 'B'] ['R', 'F']
Left: ['W', 'R', 'B', 'R'] Front: ['G', 'W', 'G', 'W'] Right: ['O', 'Y', 'O', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'Y', 'G'] Down: ['W', 'B', 'O', 'O'] ['R', 'B']
Left: ['B', 'R', 'B', 'R'] Front: ['W', 'R', 'W', 'G'] Right: ['G', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'Y'] Up: ['R', 'Y', 'G', 'Y'] Down: ['B', 'W', 'O', 'W'] []
Left: ['B', 'B', 'R', 'R'] Front: ['R', 'W', 'G', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'O', 'Y', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'O', 'W', 'O'] ['U', 'R']
Left: ['O', 'O', 'R', 'R'] Front: ['B', 'B', 'G', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'G', 'B', 'B'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['U', 'U']
Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['U', 'D']
Left: ['B', 'W', 'R', 'W'] Front: ['G', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'W'] ['U', 'F']
Left: ['W', 'B', 'W', 'R'] Front: ['R', 'R', 'G', 'G'] Right: ['G', 'Y', 'O', 'Y'] Back: ['B', 'O', 'B', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['W', 'W', 'O', 'G'] ['U', 'B']
Left: ['R', 'B', 'R', 'B'] Front: ['W', 'G', 'W', 'R'] Right: ['O', 'O', 'G', 'G'] Back: ['B', 'Y', 'O', 'Y'] Up: ['G', 'Y', 'R', 'Y'] Down: ['O', 'W', 'B', 'W'] []
Left: ['R', 'R', 'B', 'B'] Front: ['G', 'W', 'R', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'B', 'Y', 'O'] Up: ['Y', 'G', 'Y', 'R'] Down: ['W', 'B', 'W', 'B'] ['D', 'R']
Left: ['B', 'B', 'B', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'G', 'G', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['D', 'U']
Left: ['R', 'R', 'O', 'O'] Front: ['G', 'G', 'B', 'B'] Right: ['O', 'O', 'R', 'R'] Back: ['B', 'B', 'G', 'G'] Up: ['Y', 'Y', 'Y', 'Y'] Down: ['W', 'W', 'W', 'W'] ['D', 'D']
Left: ['R', 'W', 'B', 'W'] Front: ['R', 'G', 'R', 'G'] Right: ['Y', 'O', 'Y', 'G'] Back: ['B', 'B', 'O', 'O'] Up: ['Y', 'Y', 'B', 'R'] Down: ['G', 'O', 'W', 'W'] ['D', 'F']
Left: ['W', 'R', 'W', 'B'] Front: ['G', 'G', 'R', 'R'] Right: ['O', 'Y', 'G', 'Y'] Back: ['O', 'B', 'O', 'B'] Up: ['B', 'R', 'Y', 'Y'] Down: ['W', 'W', 'G', 'O'] ['D', 'B']
Left: ['W', 'W', 'R', 'R'] Front: ['O', 'G', 'W', 'G'] Right: ['Y', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'Y'] Up: ['G', 'Y', 'G', 'R'] Down: ['B', 'O', 'B', 'W'] []
Left: ['R', 'W', 'R', 'W'] Front: ['G', 'O', 'G', 'W'] Right: ['Y', 'Y', 'O', 'O'] Back: ['R', 'B', 'Y', 'B'] Up: ['Y', 'G', 'R', 'G'] Down: ['O', 'B', 'W', 'B'] ['F', 'R']
Left: ['B', 'B', 'R', 'W'] Front: ['R', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'O'] Back: ['Y', 'O', 'B', 'B'] Up: ['R', 'Y', 'R', 'Y'] Down: ['O', 'O', 'W', 'W'] ['F', 'U']
Left: ['R', 'W', 'B', 'B'] Front: ['G', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'G'] Back: ['B', 'B', 'Y', 'O'] Up: ['Y', 'Y', 'R', 'R'] Down: ['W', 'O', 'W', 'O'] ['F', 'D']
Left: ['R', 'O', 'R', 'O'] Front: ['G', 'G', 'G', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'B', 'B', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['Y', 'Y', 'W', 'W'] ['F', 'F']
Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'] ['F', 'B']
Left: ['R', 'R', 'W', 'W'] Front: ['W', 'G', 'O', 'G'] Right: ['O', 'Y', 'O', 'Y'] Back: ['B', 'Y', 'B', 'R'] Up: ['G', 'R', 'G', 'Y'] Down: ['B', 'W', 'B', 'O'] []
Left: ['W', 'R', 'W', 'R'] Front: ['G', 'W', 'G', 'O'] Right: ['O', 'O', 'Y', 'Y'] Back: ['Y', 'B', 'R', 'B'] Up: ['R', 'G', 'Y', 'G'] Down: ['W', 'B', 'O', 'B'] ['B', 'R']
Left: ['B', 'B', 'W', 'R'] Front: ['W', 'R', 'G', 'G'] Right: ['G', 'G', 'O', 'Y'] Back: ['O', 'Y', 'B', 'B'] Up: ['Y', 'R', 'Y', 'R'] Down: ['W', 'W', 'O', 'O'] ['B', 'U']
Left: ['W', 'R', 'B', 'B'] Front: ['G', 'G', 'W', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'Y', 'Y'] Down: ['O', 'W', 'O', 'W'] ['B', 'D']
Left: ['W', 'W', 'W', 'W'] Front: ['G', 'G', 'G', 'G'] Right: ['Y', 'Y', 'Y', 'Y'] Back: ['B', 'B', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'] ['B', 'F']
Left: ['O', 'R', 'O', 'R'] Front: ['G', 'G', 'G', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['B', 'B', 'B', 'B'] Up: ['W', 'W', 'Y', 'Y'] Down: ['W', 'W', 'Y', 'Y'] ['B', 'B']
Left: ['R', 'R', 'R', 'R'] Front: ['Y', 'G', 'Y', 'G'] Right: ['O', 'O', 'O', 'O'] Back: ['B', 'W', 'B', 'W'] Up: ['B', 'Y', 'B', 'Y'] Down: ['G', 'W', 'G', 'W'] []
Left: ['R', 'R', 'R', 'R'] Front: ['B', 'W', 'B', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'G', 'Y', 'G'] Up: ['W', 'G', 'W', 'G'] Down: ['Y', 'B', 'Y', 'G'] ['R']
Left: ['B', 'G', 'R', 'R'] Front: ['R', 'R', 'B', 'G'] Right: ['B', 'G', 'O', 'O'] Back: ['O', 'O', 'B', 'G'] Up: ['W', 'W', 'Y', 'Y'] Down: ['Y', 'W', 'Y', 'W'] ['U']
Left: ['R', 'R', 'B', 'G'] Front: ['B', 'G', 'R', 'R'] Right: ['O', 'O', 'B', 'G'] Back: ['B', 'G', 'O', 'O'] Up: ['W', 'Y', 'W', 'Y'] Down: ['Y', 'Y', 'W', 'W'] ['D']
Left: ['R', 'Y', 'R', 'W'] Front: ['B', 'B', 'G', 'G'] Right: ['W', 'O', 'Y', 'O'] Back: ['B', 'G', 'B', 'G'] Up: ['W', 'Y', 'R', 'R'] Down: ['O', 'O', 'Y', 'W'] ['F']
Left: ['Y', 'R', 'W', 'R'] Front: ['B', 'G', 'B', 'G'] Right: ['O', 'W', 'O', 'Y'] Back: ['B', 'B', 'G', 'G'] Up: ['R', 'R', 'W', 'Y'] Down: ['Y', 'W', 'O', 'O'] ['B']
Left: ['R', 'R', 'R', 'R'] Front: ['B', 'W', 'B', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'G', 'Y', 'G'] Up: ['W', 'G', 'W', 'G'] Down: ['Y', 'B', 'Y', 'Y'] []
Left: ['R', 'R', 'R', 'R'] Front: ['W', 'B', 'W', 'Y'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'Y', 'G', 'Y'] Up: ['G', 'W', 'G', 'W'] Down: ['B', 'Y', 'B', 'Y'] ['R', 'R']
Left: ['Y', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'W'] Right: ['W', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'Y'] ['R', 'U']
Left: ['R', 'R', 'Y', 'Y'] Front: ['W', 'W', 'R', 'R'] Right: ['O', 'O', 'W', 'W'] Back: ['Y', 'Y', 'O', 'O'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'Y', 'B'] ['R', 'D']
Left: ['R', 'B', 'R', 'B'] Front: ['W', 'W', 'W', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'R', 'R'] Down: ['O', 'O', 'B', 'Y'] ['R', 'F']
Left: ['B', 'R', 'Y', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['R', 'R', 'G', 'G'] Down: ['B', 'B', 'O', 'O'] ['R', 'B']
Left: ['Y', 'R', 'B', 'R'] Front: ['B', 'R', 'B', 'G'] Right: ['W', 'G', 'O', 'O'] Back: ['O', 'Y', 'B', 'G'] Up: ['R', 'G', 'W', 'Y'] Down: ['Y', 'W', 'O', 'W'] []
Left: ['B', 'Y', 'R', 'R'] Front: ['R', 'W', 'W', 'W'] Right: ['O', 'W', 'O', 'G'] Back: ['Y', 'O', 'G', 'Y'] Up: ['G', 'R', 'Y', 'G'] Down: ['B', 'O', 'B', 'O'] ['U', 'R']
Left: ['O', 'O', 'R', 'R'] Front: ['B', 'Y', 'W', 'G'] Right: ['R', 'R', 'O', 'O'] Back: ['W', 'G', 'B', 'Y'] Up: ['Y', 'G', 'Y', 'G'] Down: ['B', 'W', 'B', 'W'] ['U', 'U']
Left: ['B', 'Y', 'B', 'Y'] Front: ['R', 'R', 'R', 'R'] Right: ['W', 'G', 'W', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'B', 'W', 'W'] ['U', 'D']
Left: ['B', 'B', 'R', 'W'] Front: ['W', 'R', 'G', 'R'] Right: ['Y', 'G', 'Y', 'O'] Back: ['O', 'O', 'B', 'Y'] Up: ['G', 'G', 'R', 'Y'] Down: ['O', 'W', 'B', 'W'] ['U', 'F']
Left: ['B', 'Y', 'W', 'R'] Front: ['R', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'G'] Back: ['B', 'O', 'Y', 'O'] Up: ['R', 'B', 'Y', 'Y'] Down: ['B', 'W', 'O', 'G'] ['U', 'B']
Left: ['R', 'Y', 'R', 'B'] Front: ['B', 'G', 'W', 'R'] Right: ['O', 'O', 'W', 'G'] Back: ['B', 'G', 'O', 'G'] Up: ['W', 'Y', 'R', 'Y'] Down: ['O', 'B', 'Y', 'W'] []
Left: ['R', 'R', 'B', 'Y'] Front: ['W', 'B', 'R', 'W'] Right: ['W', 'O', 'G', 'O'] Back: ['Y', 'Y', 'Y', 'O'] Up: ['G', 'G', 'G', 'R'] Down: ['B', 'B', 'W', 'Y'] ['D', 'R']
Left: ['B', 'Y', 'B', 'Y'] Front: ['R', 'R', 'R', 'R'] Right: ['W', 'G', 'W', 'G'] Back: ['O', 'O', 'O', 'O'] Up: ['G', 'G', 'Y', 'Y'] Down: ['B', 'B', 'W', 'W'] ['D', 'U']
Left: ['R', 'R', 'O', 'O'] Front: ['W', 'G', 'B', 'Y'] Right: ['O', 'O', 'R', 'R'] Back: ['B', 'Y', 'W', 'G'] Up: ['G', 'Y', 'G', 'Y'] Down: ['W', 'B', 'W', 'B'] ['D', 'D']
Left: ['R', 'B', 'B', 'B'] Front: ['R', 'W', 'R', 'G'] Right: ['G', 'O', 'Y', 'G'] Back: ['B', 'Y', 'O', 'O'] Up: ['G', 'Y', 'Y', 'R'] Down: ['W', 'O', 'W', 'W'] ['D', 'F']
Left: ['W', 'R', 'W', 'Y'] Front: ['W', 'G', 'R', 'R'] Right: ['O', 'G', 'W', 'Y'] Back: ['O', 'B', 'O', 'Y'] Up: ['B', 'R', 'G', 'Y'] Down: ['B', 'B', 'G', 'O'] ['D', 'B']
Left: ['B', 'W', 'R', 'R'] Front: ['O', 'W', 'B', 'G'] Right: ['G', 'O', 'Y', 'O'] Back: ['B', 'R', 'B', 'G'] Up: ['W', 'Y', 'G', 'R'] Down: ['Y', 'O', 'Y', 'W'] []
Left: ['R', 'B', 'R', 'W'] Front: ['W', 'O', 'G', 'W'] Right: ['Y', 'G', 'O', 'O'] Back: ['R', 'Y', 'Y', 'Y'] Up: ['G', 'W', 'R', 'G'] Down: ['O', 'B', 'B', 'Y'] ['F', 'R']
Left: ['B', 'Y', 'R', 'W'] Front: ['R', 'B', 'G', 'G'] Right: ['W', 'W', 'Y', 'O'] Back: ['G', 'O', 'B', 'Y'] Up: ['R', 'G', 'R', 'Y'] Down: ['O', 'O', 'B', 'W'] ['F', 'U']
Left: ['R', 'B', 'B', 'Y'] Front: ['W', 'W', 'R', 'W'] Right: ['G', 'O', 'G', 'G'] Back: ['B', 'Y', 'Y', 'O'] Up: ['G', 'Y', 'R', 'R'] Down: ['B', 'O', 'W', 'O'] ['F', 'D']
Left: ['R', 'O', 'R', 'O'] Front: ['G', 'W', 'G', 'W'] Right: ['R', 'O', 'R', 'O'] Back: ['B', 'Y', 'B', 'Y'] Up: ['G', 'Y', 'W', 'B'] Down: ['Y', 'G', 'B', 'W'] ['F', 'F']
Left: ['B', 'B', 'W', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'] ['F', 'B']
Left: ['R', 'R', 'B', 'W'] Front: ['B', 'G', 'O', 'G'] Right: ['O', 'G', 'O', 'Y'] Back: ['B', 'G', 'Y', 'R'] Up: ['W', 'R', 'W', 'Y'] Down: ['Y', 'W', 'B', 'O'] []
Left: ['B', 'R', 'W', 'R'] Front: ['W', 'W', 'W', 'O'] Right: ['O', 'O', 'Y', 'G'] Back: ['Y', 'B', 'R', 'Y'] Up: ['R', 'G', 'G', 'G'] Down: ['B', 'B', 'O', 'B'] ['B', 'R']
Left: ['B', 'B', 'W', 'R'] Front: ['B', 'R', 'W', 'G'] Right: ['W', 'G', 'O', 'Y'] Back: ['O', 'G', 'Y', 'Y'] Up: ['G', 'R', 'Y', 'R'] Down: ['B', 'W', 'O', 'O'] ['B', 'U']
Left: ['B', 'R', 'Y', 'Y'] Front: ['W', 'G', 'W', 'R'] Right: ['O', 'G', 'W', 'G'] Back: ['B', 'B', 'O', 'Y'] Up: ['R', 'R', 'G', 'Y'] Down: ['O', 'B', 'O', 'W'] ['B', 'D']
Left: ['B', 'B', 'W', 'W'] Front: ['W', 'W', 'G', 'G'] Right: ['G', 'G', 'Y', 'Y'] Back: ['B', 'B', 'Y', 'Y'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'] ['B', 'F']
Left: ['O', 'R', 'O', 'R'] Front: ['W', 'G', 'W', 'G'] Right: ['O', 'R', 'O', 'R'] Back: ['Y', 'B', 'Y', 'B'] Up: ['W', 'B', 'G', 'Y'] Down: ['B', 'W', 'Y', 'G'] ['B', 'B']
Left: ['R', 'R', 'R', 'R'] Front: ['B', 'W', 'B', 'W'] Right: ['O', 'O', 'O', 'O'] Back: ['Y', 'G', 'Y', 'G'] Up: ['W', 'G', 'W', 'G'] Down: ['Y', 'B', 'Y', 'B'] []
Left: ['R', 'R', 'R', 'R'] Front: ['W', 'B', 'W', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'Y', 'G', 'Y'] Up: ['G', 'W', 'G', 'W'] Down: ['B', 'Y', 'B', 'Y'] ['R']
Left: ['Y', 'Y', 'R', 'R'] Front: ['R', 'R', 'W', 'W'] Right: ['W', 'W', 'O', 'O'] Back: ['O', 'O', 'Y', 'Y'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'] ['U']
Left: ['R', 'R', 'Y', 'Y'] Front: ['W', 'W', 'R', 'R'] Right: ['O', 'O', 'W', 'W'] Back: ['Y', 'Y', 'O', 'O'] Up: ['G', 'G', 'G', 'G'] Down: ['B', 'B', 'B', 'B'] ['D']
Left: ['R', 'B', 'R', 'B'] Front: ['W', 'W', 'W', 'W'] Right: ['G', 'O', 'G', 'O'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['G', 'G', 'R', 'R'] Down: ['O', 'O', 'B', 'B'] ['F']
Left: ['B', 'R', 'B', 'R'] Front: ['W', 'W', 'W', 'W'] Right: ['O', 'G', 'O', 'G'] Back: ['Y', 'Y', 'Y', 'Y'] Up: ['R', 'R', 'G', 'G'] Down: ['B', 'B', 'O', 'O'] ['B']
Left: ['R', 'R', 'R', 'R'] Front: ['W', 'B', 'W', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['G', 'Y', 'G', 'Y'] Up: ['G', 'W', 'G', 'W'] Down: ['B', 'Y', 'B', 'B'] []
Left: ['R', 'R', 'R', 'R'] Front: ['G', 'Y', 'G', 'B'] Right: ['O', 'O', 'O', 'O'] Back: ['W', 'B', 'W', 'B'] Up: ['Y', 'B', 'Y', 'B'] Down: ['W', 'G', 'W', 'B'] ['R', 'R', 'R']
Left: ['G', 'B', 'R', 'R'] Front: ['R', 'R', 'G', 'B'] Right: ['G', 'B', 'O', 'O'] Back: ['O', 'O', 'G', 'B'] Up: ['Y', 'Y', 'W', 'W'] Down: ['W', 'Y', 'W', 'B'] ['R', 'R', 'U']
Left: ['R', 'R', 'G', 'B'] Front: ['G', 'B', 'R', 'R'] Right: ['O', 'O', 'G', 'B'] Back: ['G', 'B', 'O', 'O'] Up: ['Y', 'W', 'Y', 'W'] Down: ['W', 'W', 'B', 'Y'] ['R', 'R', 'D']
Left: ['R', 'W', 'R', 'Y'] Front: ['G', 'G', 'B', 'B'] Right: ['Y', 'O', 'W', 'O'] Back: ['G', 'B', 'G', 'B'] Up: ['Y', 'W', 'R', 'R'] Down: ['O', 'O', 'W', 'B'] ['R', 'R', 'F']
Left: ['W', 'R', 'B', 'R'] Front: ['G', 'B', 'G', 'B'] Right: ['O', 'Y', 'O', 'W'] Back: ['G', 'G', 'B', 'B'] Up: ['R', 'R', 'Y', 'W'] Down: ['W', 'Y', 'O', 'O'] ['R', 'R', 'B']
Left: ['B', 'R', 'Y', 'R'] Front: ['W', 'R', 'W', 'W'] Right: ['G', 'W', 'O', 'O'] Back: ['O', 'G', 'Y', 'Y'] Up: ['R', 'Y', 'G', 'G'] Down: ['B', 'B', 'O', 'B'] []
Left: ['Y', 'B', 'R', 'R'] Front: ['R', 'B', 'G', 'B'] Right: ['O', 'G', 'O', 'W'] Back: ['G', 'O', 'Y', 'B'] Up: ['Y', 'R', 'G', 'W'] Down: ['W', 'O', 'W', 'O'] ['R', 'U', 'R']
Left: ['O', 'O', 'R', 'R'] Front: ['Y', 'B', 'G', 'W'] Right: ['R', 'R', 'O', 'O'] Back: ['G', 'W', 'Y', 'B'] Up: ['G', 'Y', 'G', 'Y'] Down: ['W', 'B', 'W', 'B'] ['R', 'U', 'U']
Left: ['Y', 'B', 'Y', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'W', 'G', 'W'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'W', 'B', 'B'] ['R', 'U', 'D']
Left: ['Y', 'W', 'R', 'B'] Front: ['G', 'R', 'W', 'R'] Right: ['G', 'W', 'G', 'O'] Back: ['O', 'O', 'Y', 'B'] Up: ['Y', 'Y', 'R', 'B'] Down: ['O', 'G', 'W', 'B'] ['R', 'U', 'F']
Left: ['W', 'B', 'B', 'R'] Front: ['R', 'R', 'G', 'W'] Right: ['G', 'Y', 'O', 'Y'] Back: ['Y', 'O', 'B', 'O'] Up: ['R', 'Y', 'G', 'G'] Down: ['W', 'B', 'O', 'W'] ['R', 'U', 'B']
Left: ['R', 'B', 'R', 'Y'] Front: ['W', 'W', 'B', 'R'] Right: ['O', 'O', 'G', 'W'] Back: ['Y', 'Y', 'O', 'Y'] Up: ['G', 'G', 'R', 'G'] Down: ['O', 'W', 'B', 'B'] []
Left: ['R', 'R', 'Y', 'B'] Front: ['G', 'W', 'R', 'B'] Right: ['G', 'O', 'W', 'O'] Back: ['G', 'B', 'G', 'O'] Up: ['Y', 'W', 'Y', 'R'] Down: ['W', 'Y', 'B', 'B'] ['R', 'D', 'R']
Left: ['Y', 'B', 'Y', 'B'] Front: ['R', 'R', 'R', 'R'] Right: ['G', 'W', 'G', 'W'] Back: ['O', 'O', 'O', 'O'] Up: ['Y', 'Y', 'G', 'G'] Down: ['W', 'W', 'B', 'B'] ['R', 'D', 'U']
Left: ['R', 'R', 'O', 'O'] Front: ['G', 'W', 'Y', 'B'] Right: ['O', 'O', 'R', 'R'] Back: ['Y', 'B', 'G', 'W'] Up: ['Y', 'G', 'Y', 'G'] Down: ['B', 'W', 'B', 'W'] ['R', 'D', 'D']
Left: ['R', 'W', 'Y', 'W'] Front: ['R', 'G', 'R', 'W'] Right: ['Y', 'O', 'G', 'W'] Back: ['Y', 'B', 'O', 'O'] Up: ['Y', 'G', 'B', 'R'] Down: ['G', 'O', 'B', 'B'] ['R', 'D', 'F']
Left: ['B', 'R', 'B', 'B'] Front: ['G', 'W', 'R', 'R'] Right: ['O', 'Y', 'G', 'G'] Back: ['O', 'Y', 'O', 'B'] Up: ['Y', 'R', 'Y', 'G'] Down: ['W', 'W', 'W', 'O'] ['R', 'D', 'B']
Left: ['W', 'B', 'R', 'R'] Front: ['O', 'G', 'W', 'W'] Right: ['Y', 'O', 'G', 'O'] Back: ['Y', 'R', 'Y', 'Y'] Up: ['G', 'G', 'W', 'R'] Down: ['B', 'O', 'B', 'B'] []
Left: ['R', 'W', 'R', 'B'] Front: ['G', 'O', 'W', 'B'] Right: ['G', 'Y', 'O', 'O'] Back: ['R', 'B', 'G', 'B'] Up: ['Y', 'G', 'R', 'W'] Down: ['O', 'Y', 'W', 'B'] ['R', 'F', 'R']
Left: ['Y', 'B', 'R', 'B'] Front: ['R', 'W', 'W', 'W'] Right: ['G', 'G', 'G', 'O'] Back: ['Y', 'O', 'Y', 'B'] Up: ['R', 'Y', 'R', 'G'] Down: ['O', 'O', 'W', 'B'] ['R', 'F', 'U']
Left: ['R', 'W', 'Y', 'B'] Front: ['G', 'G', 'R', 'B'] Right: ['Y', 'O', 'W', 'W'] Back: ['Y', 'B', 'G', 'O'] Up: ['Y', 'G', 'R', 'R'] Down: ['W', 'O', 'B', 'O'] ['R', 'F', 'D']
Left: ['R', 'O', 'R', 'O'] Front: ['W', 'G', 'W', 'G'] Right: ['R', 'O', 'R', 'O'] Back: ['Y', 'B', 'Y', 'B'] Up: ['Y', 'G', 'B', 'W'] Down: ['G', 'Y', 'W', 'B'] ['R', 'F', 'F']
Left: ['W', 'W', 'B', 'B'] Front: ['G', 'G', 'W', 'W'] Right: ['Y', 'Y', 'G', 'G'] Back: ['Y', 'Y', 'B', 'B'] Up: ['R', 'R', 'R', 'R'] Down: ['O', 'O', 'O', 'O'] ['R', 'F', 'B']

[Program finished]
"""