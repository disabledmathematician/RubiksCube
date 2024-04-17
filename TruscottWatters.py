#pylint:disable=W0612
# I love you, My father Mark William Watters
# Thank you Harvard University and Massachusetts Institute of Technology
# Charles Truscott Watters, Byron Bay Australia
# Certified in Computational Thinking using Python from MITx
# Certified in Data Science in Using Python for Research PH556 (Harvard Centre for Continuing Education, Harvard Extension School)
# Love you high rollin Dad, Mark William Watters
# Not finished yet. Need to get off my phone, pesky stalkerware malware, Android c&C
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
	unsolved_state = [['R', "O", "R", "R"], ["Y", "B", "G", "G"], ["Y", "G", "O", "O"], ["Y", "B", "B", "B"], ["Y", "R", "G", "O"], ["W", "W", "W", "W"]]
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
	while c < 6 ** 3:
		for l in yet_moves:
			tS= l(States[c])
			States.append(tS)
			tS.is_solved()
			if tS.state == solved_state:
				print("{}".format(tS.state))
				print("The moves to solve sequentially are {}".format(S.moves))
				sys.exit()
		c += 1
	print(States)
	for e in States:
		print(e, e.moves)
#	
Charles_Rubiks()
