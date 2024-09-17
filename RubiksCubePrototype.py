#pylint:disable=W0613
from queue import deque

# August 30, International Day of the Disappeared


""" Charles Truscott Watters, developing my own algorithm to solve the Rubik's cube 2 x 2 Byron Bay NSW 2481. Thank you John Flynn Hospital and Byron Bay Hospital. Thank you MITx, MIT OCW and Harvard CCE """

""" Thank you Byron Central Hospital Tuckeroo. Thank you Eric Grimson, John Guttag and Ana Bell and all at MITx """



#  theta c to the n (18 ^ n) complexity, exponential computational complexity

""" Top Left Front, Top Right Front, Bottom Left Front, Bottom Right Front, Top Left Back, Top Right Back, Bottom Right Back, Bottom Left Back """
class RubiksState(object):
	def __init__(self, tlf, trf, blf, brf, tlb, blb, trb, brb, moves):
#	def __init__(self, left_face, front_face, right_face, back_face, top_face, down_face, moves):
#		self.tlf = [0] * 3
#		self.trf= [0] * 3
#		self.blf = [0] * 3
#		self.brf= [0] * 3
#		self.tlb = [0] * 3
#		self.trb= [0] * 3
#		self.brb = [0] * 3
#		self.blb= [0] * 3
#		

		self.left_face = [self.tlf[1], self.blf[1], self.tlb[1], self.blb[1]]
		self.front_face = [self.tlf[2], self.blf[2], self.trf[2], self.brf[2]]
		self.right_face = [self.trf[1], self.brf[1], self.trb[1], self.blb[1]]
		self.back_face = [self.tlb[2], self.trb[2], self.blb[2], self.brb[2]]
		self.top_face = [self.tlb[0], self.tlf[0], self.trf[0], self.trb[0]]
		self.down_face = [self.blb[0], self.blf[0], self.brb[0], self.brf[0]]
		self.moves = moves

	def L(self):
		""" Top Left Front to Bottom Left Front.
Bottom Left Front to Bottom Left Back
Bottom Left Back to Top Left Back
Top Left Back to Top Left Front """
# Aaaah, Erroneous decision 
	# Indices 0, 1, 2 to 2, 1, 0 (mapping)
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		new_blf = [0] * 3
		new_blb = [0] * 3
		new_tlb = [0] * 3
		new_tlf = [0] * 3
		new_blf[0], new_blf[1], new_blf[2] = ttlf[2], ttlf[1], ttlf[0] # Bottom Left Front becomes Top Left Front
		new_blb[0], new_blb[1], new_blb[2] = tblf[2], tblf[1], tblf[0] # Bottom Left Back becomes Bottom Left Front
		new_tlb[0], new_tlb[1], new_tlb[2] = tblb[2], tblb[1], tblb[0] #  Top Left Back becomes Bottom Left Back
		new_tlf[0], new_tlf[1], new_tlf[2] = ttlb[2], ttlb[1], ttlb[0] # Top Left Front becomes Top Left Back
		elcopy = self.moves.copy()
		elcopy.append("L")
		return RubiksState(elcopy)
#		return RubiksState(left_face, front_face, right_face, back_face, top_face, down_face, elcopy)
	def L2(self):
		elcopy = self.moves.copy()
		elcopy.append("L2")
		pass
	def Linv(self):
		elcopy = self.moves.copy()
		elcopy.append("L inverse")
		pass
	def R(self):
		# Indices 0, 1, 2 to 2, 1, 0 (mapping)
		""" Top Right Front to Bottom Right Front.
	Bottom Right Front to Bottom Right Back
	Bottom Right Back to Top Right Back
	Top Right Back to Top Right Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nbrf, nbrb, ntrb, ntrf = [0] * 3, [0] * 3, [0] * 3,[0] * 3
		nbrf[0], nbrf[1], nbrf[2] = ttrf[2], ttrf[1], ttrf[0]
		nbrb[0], nbrb[1], nbrb[2] = tbrf[2], tbrf[1], tbrf[0]
		ntrb[0], ntrb[1], ntrb[2] = tbrb[2], tbrb[1], tbrb[0]
		ntrf[0], ntrf[1], ntrf[2] = ttrb[2], ttrb[1], ttrb[0]
		elcopy = self.moves.copy()
		elcopy.append("R")
		return RubiksState(elcopy)
		pass
	def R2(self):
		elcopy = self.moves.copy()
		elcopy.append("R2")
		return RubiksState(elcopy)
		pass
	def Rinv(self):
		elcopy = self.moves.copy()
		elcopy.append("R inverse")
		return RubiksState(elcopy)
		pass
	def U(self):
		# Indices 0, 1, 2 to 0, 2, 1 (mapping)
		""" Top Left Front to Top Left Back
	Top Left Back to Top Right Back. Top Right Back to Top Right Front. Top Right Front to Top Left Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		ntlb = [0] * 3
		ntrb = [0] * 3
		ntrf = [0] * 3
		ntlf = [0] * 3
		ntlb[0], ntlb[1], ntlb[2] = ttlf[0], ttlf[2], ttlf[1]
		ntrb[0], ntrb[1], ntrb[2] = ttlb[0], ttlb[2], ttlb[1]
		ntrf[0], ntrf[1], ntrf[2] = ttrb[0], ttrb[2], ttrb[1]
		ntlf[0], ntlf[1], ntlf[2] = ttrf[0], ttrf[2], ttrf[1]
		
		elcopy = self.moves.copy()
		elcopy.append("U")
		return RubiksState(elcopy)
		pass
	def U2(self):
		elcopy = self.moves.copy()
		elcopy.append("U2")
		return RubiksState(elcopy)
		pass
	def Uinv(self):
		elcopy = self.moves.copy()
		elcopy.append("Up inverse")
		return RubiksState(elcopy)
		pass
	def D(self):
		# Indices 0, 1, 2 to 0, 2, 1 (mapping)
		""" Bottom Left Front to Bottom Left Back
		Bottom Left Back to Bottom Right Back. Bottom Right Back to Bottom Right Front
		Bottom Right Front to Bottom Left Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		nblb, nbrb, nbrf, nblf= [0] * 3, [0] * 3, [0] * 3, [0] * 3
		nblb[0], nblb[1], nblb[2] = tblf[0], tblf[2], tblf[1]
		nbrb[0], nbrb[1], nbrb[2] = tblb[0], tblb[2], tblb[1]
		nbrf[0], nbrf[1], nbrf[2] = tbrb[0], tbrb[2], tbrb[1]
		nblf[0], nblf[1], nblf[2] = tbrf[0], tbrf[2], tbrf[1]
		elcopy = self.moves.copy()
		elcopy.append("D")
		return RubiksState(elcopy)
		pass
	def D2(self):
		elcopy = self.moves.copy()
		elcopy.append("D2")
		return RubiksState(elcopy)
		pass
	def Dinv(self):
		elcopy = self.moves.copy()
		elcopy.append("Down inverse")
		return RubiksState(elcopy)
		pass
	def F(self):
		# Indices 0, 1, 2 to 1, 0, 2 (mapping)
		""" Bottom Left Front to Top Left Front. Top Left Front to Top Right Front. Top Right Front to Bottom Right Front. Bottom Right Front to Bottom Left Front """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		ntlf, ntrf, nbrf, nblf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
		ntlf[0], ntlf[1], ntlf[2] = tblf[1], tblf[0], tblf[2]
		ntrf[0], ntrf[1], ntrf[2] = ttlf[1], ttlf[0], ttlf[2]
		nbrf[0], nbrf[1], nbrf[2] = ttrf[1], ttrf[0], ttrf[2]
		nblf[0], nblf[1], nblf[2] = tbrf[1], tbrf[0], tbrf[2]
		elcopy = self.moves.copy()
		elcopy.append("F")
		return RubiksState(elcopy)
		pass
	def F2(self):
		elcopy = self.moves.copy()
		elcopy.append("F2")
		return RubiksState(elcopy)
		pass
	def Finv(self):
		elcopy = self.moves.copy()
		elcopy.append("F inverse")
		return RubiksState(elcopy)
		pass
	def B(self):
		# Indices 0, 1, 2 to 1, 0, 2 (mapping)
		""" Bottom Left Back to Top Left Back. Top Left Back to Top Right Back. Top Right Back to Bottom Right Back. Bottom Right Back to Bottom Left Back """
		ttlf = self.tlf.copy()
		tblf = self.blf.copy()
		ttrf = self.trf.copy()
		tbrf = self.brf.copy()
		ttlb = self.tlb.copy()
		tblb = self.blb.copy()
		ttrb = self.trb.copy()
		tbrb = self.brb.copy()
		
		elcopy = self.moves.copy()
		elcopy.append("B")
		return RubiksState(elcopy)
		pass
	def B2(self):
		elcopy = self.moves.copy()
		elcopy.append("B2")
		return RubiksState(elcopy)
		pass
	def Binv(self):
		elcopy = self.moves.copy()
		elcopy.append("B inverse")
		return RubiksState(elcopy)
		pass
		
	def is_solved(self):
		if self.left_face == ["R", "R", "R", "R"] and self.front_face == ["G", "G", "G", "G"] and self.right_face == ["O", "O", "O", "O"] and self.back_face == ["B", "B", "B", "B"] and self.top_face == ["W", "W", "W", "W"] and self.down_face == ["Y", "Y" , "Y" , "Y"]:
				return True
		else:
				return False


def CharlesTruscottRubiks():
	item = RubiksState([])
	state = deque([])
	state.append(item)
	moves = [lambda s: s.L(), lambda s: s.R(), lambda s: s.U(), lambda s: s.D(), lambda s: s.F(),  lambda s: s.B() ]
#	moves = [lambda s: s.L(), lambda s: s.L2(), lambda s: s.Linv(), lambda s: s.R(), lambda s: s.R2(), lambda s: s.Rinv(), lambda s: s.U(), lambda s: s.U2(), lambda s: s.Uinv(), lambda s: s.D(), lambda s: s.D2(), lambda s: s.Dinv(), lambda s: s.F(), lambda s: s.F2(), lambda s: s.Finv(), lambda s: s.B(), lambda s: s.B2(), lambda s: s.Binv()]
	print(state[0].moves)
	for move in moves:
		e = move(RubiksState([]))
		state.append(e)
	state.popleft()
	c = 0
	print(state)
#	for move in moves:
#		for s in state:
#			print(s, s.moves, move(s).moves)
	# 18 = 3 x 6 moves, eighteen to the n combinatorially sound moves.
	# 18 ^ 3 = all possible 18 moves 3 times over
	print("Charles Truscott Watters. My Rubik's cube solution Python algorithm.")
	from time import sleep
	while c < 18 ** 3:
		elem = state.popleft()
		for move in moves:
			state.append(move(elem))
			print(move(elem), move(elem).moves)
			sleep(0.2)
		c += 1


def CharlesTruscottSim():
#	left_face, front_face, right_face, back_face, top_face, do)wn_face, moves
	left = ["G", "R", "B", "O"]
	front = ["B", "G", "G", "G"]
	right = ["R", "B", "R", "B"]
	back = ["O", "O", "O", "R"]
	top =["W", "W", "W", "W"]
	down = ["Y", "Y", "Y", "Y"]
	cube = RubiksState(left, front, right, back, top, down, [])
	print(cube.left_face, cube.front_face, cube.right_face, cube.back_face, cube.top_face, cube.down_face)
#	Needed = True
#	while Needed:
#		s = str(input("Enter a move"))
#		if s == "quit":
#			Needed = False
#			exit()
#		if s == "L":
#			cube = cube.L()
#			print(cube.left_face)
#			print(cube.front_face)
#			print(cube.right_face)
#			print(cube.back_face)
#			print(cube.top_face)
#			print(cube.down_face)
#CharlesTruscottSim()
CharlesTruscottRubiks()