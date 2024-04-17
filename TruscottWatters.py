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
			return True
		return False
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
#		self.moves.append("R")
		n.append("R")
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def R_inv(self):
		raise NotImplementedError
#		new_state = self.R()
#		new_state = new_state.R()
#		new_state = new_state.R()
#		new_state.moves.pop()
#		new_state.moves.pop()
#		new_state.moves.pop()
#		new_state.moves.append("R inverse")
#		return new_state
	def R2(self):
		raise NotImplementedError
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
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def L_inv(self):
		raise NotImplementedError
	def L2(self):
		raise NotImplementedError
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
		raise NotImplementedError
	def F2(self):
		raise NotImplementedError
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
		raise NotImplementedError
	def B2(self):
		raise NotImplementedError
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
		tL[0], tL[1] = prev_F[0], prev_F[1]
		tB[0], tB[1] = prev_L[0], prev_L[1]
		tR[0], tR[1] = prev_B[0], prev_B[1]
		tF[0], tF[1] = prev_R[0], prev_R[1]
		new_matrix = [tL, tF, tR, tB, tU, tD]
		n = self.moves.copy()
		n.append("U")
#		self.moves.append("U")
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def U2(self):
		raise NotImplementedError
	def U_inv(self):
		raise NotImplementedError
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
#		self.moves.append("D")
		new_state = Unsolved_Rubiks(new_matrix, n)
		return new_state
	def D_inv(self):
		raise NotImplementedError
	def D2(self):
		raise NotImplementedError
	def __str__(self):
		return str("Left: {} Front: {} Right: {} Back: {} Up: {} Down: {}".format(self.state[0], self.state[1], self.state[2], self.state[3], self.state[4], self.state[5]))

def Charles_Rubiks():
	solved_state = [["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]]
	ns = Unsolved_Rubiks(solved_state, [])
	ns1 = ns.R()
	ns2 = ns.L()
	ns = ns.R()
	ns = ns.L()
	print("ns")
	print(ns)
	print(ns.R(), ns.L())
	my_cube = [["B", "R", "B", "Y"], ["W", "B", "G", "G"], ["O", "O", "Y", "R"], ["G", "O", "W", "R"], ["Y", "W", "G", "W"], ["R", "O", "Y", "B"]]
	state = Unsolved_Rubiks(my_cube, [])
#	noviy = ns.state.copy()
	yet_moves =[lambda c: c.L(), lambda c: c.R(), lambda c: c.U(), lambda c: c.D(), lambda c: c.F(), lambda c: c.B()]
#	Can't solve my cube just as of yet
	States = []
	States.append(state)
	print(state.state, state.moves)
	for l in yet_moves:
		n = l(state)
		print(n, n.moves)
		States.append(n)
	print(States)
	t = False
	x = 1
	while t == False:
		while x <= len(States):
			f = States[x]
			for l in yet_moves:
				mov = l(f)
				States.append(mov)
				if mov.is_solved() == True:
					print("{} Solved by {}".format(ns.state, mov.moves))
					t = True
			x += 1
	try:
		Unsolved_Rubiks([["R", "R", "R", "R"], ["G", "G", "G", "G"], ["O", "O", "O", "O"], ["B", "B", "B", "B"], ["Y", "Y", "Y", "Y"], ["W", "W", "W", "W"]], [])
	except NotImplementedError as e:
		print(e)
#	for e in States:
#		print(e, e.moves)
""" I love you, my precious Father Mark William Watters. I love you unconditionally
All the credit for Tai as our carer
""" 
Charles_Rubiks()
