# -*- coding: utf-8 -*-
"""
Charles Truscott Watters
New paradigm Rubik's Cube Solving algorithm

Thank you Byron Central Hospital, edX, HarvardX and MITx

Copyright Charles Truscott, 2024 December

Byron Bay, NSW 2481


n = RubiksState(['W', 'O', 'G'], ['Y', 'O', 'G'], ['W', 'R', 'G'], ['Y', 'R', 'G'], ['W', 'O', 'B'], ['Y', 'O', 'B'], ['W', 'R', 'B'], ['Y','R', 'B'], [])
Front face: ['G', 'G', 'G', 'G']
Left Face: ['O', 'O', 'O', 'O']
Right Face: ['R', 'R', 'R', 'R']
Back Face: ['B', 'B', 'B', 'B']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'Y', 'Y', 'Y']

n = n.D()
Front face: ['G', 'G', 'O', 'O']
Left Face: ['O', 'O', 'B', 'B']
Right Face: ['R', 'R', 'G', 'G']
Back Face: ['B', 'B', 'R', 'R']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'Y', 'Y', 'Y']

n.is_solved()
Out[15]: False

n = n.Dinv()
Front face: ['G', 'G', 'G', 'G']
Left Face: ['O', 'O', 'O', 'O']
Right Face: ['R', 'R', 'R', 'R']
Back Face: ['B', 'B', 'B', 'B']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'Y', 'Y', 'Y']

n.is_solved()
Solved: ['D', 'D inverse']
Out[17]: True




n = RubiksState(['W', 'O', 'G'], ['Y', 'O', 'G'], ['W', 'R', 'G'], ['Y', 'R', 'G'], ['W', 'O', 'B'], ['Y', 'O', 'B'], ['W', 'R', 'B'], ['Y','R', 'B'], [])
Front face: ['G', 'G', 'G', 'G']
Left Face: ['O', 'O', 'O', 'O']
Right Face: ['R', 'R', 'R', 'R']
Back Face: ['B', 'B', 'B', 'B']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'Y', 'Y', 'Y']

n = n.L()
Front face: ['Y', 'G', 'Y', 'G']
Left Face: ['O', 'O', 'O', 'O']
Right Face: ['R', 'R', 'R', 'R']
Back Face: ['B', 'W', 'B', 'W']
Up face: ['G', 'W', 'G', 'W']
Down face:['B', 'Y', 'B', 'Y']

n = n.R()
Front face: ['Y', 'Y', 'Y', 'Y']
Left Face: ['O', 'O', 'O', 'O']
Right Face: ['R', 'R', 'R', 'R']
Back Face: ['W', 'W', 'W', 'W']
Up face: ['G', 'G', 'G', 'G']
Down face:['B', 'B', 'B', 'B']

n = n.Rinv()
Front face: ['Y', 'G', 'Y', 'G']
Left Face: ['O', 'O', 'O', 'O']
Right Face: ['R', 'R', 'R', 'R']
Back Face: ['B', 'W', 'B', 'W']
Up face: ['G', 'W', 'G', 'W']
Down face:['B', 'Y', 'B', 'Y']

n = n.Linv()
Front face: ['G', 'G', 'G', 'G']
Left Face: ['O', 'O', 'O', 'O']
Right Face: ['R', 'R', 'R', 'R']
Back Face: ['B', 'B', 'B', 'B']
Up face: ['W', 'W', 'W', 'W']
Down face:['Y', 'Y', 'Y', 'Y']

n.is_solved()
Solved: ['L', 'R', 'R inverse', 'L inverse']
Out[11]: True


"""
import itertools
# n = RubiksState([], [], [], [], [], [], [], [])
# n = RubiksState(['W', 'O', 'G'], ['B', 'O', 'Y'], ['W', 'R', 'G'], ['O', 'Y', 'G'], ['W', 'O', 'B'], ['B', 'R', 'Y'], ['W', 'R', 'B'], ['R', 'Y', 'G'], [])
class RubiksState(object):
    def __init__(self, tlf, blf, trf, brf, tlb, blb, trb, brb, moves):
        self.tlf = tlf
        self.blf = blf
        self.trf = trf
        self.brf = brf
        self.tlb = tlb
        self.blb = blb
        self.trb = trb
        self.brb = brb
        
        self.left_face = [self.tlb[1], self.tlf[1], self.blb[1], self.blf[1]]
        self.right_face = [self.trf[1], self.trb[1], self.brf[1], self.brb[1]]
        self.front_face = [self.tlf[2], self.trf[2], self.blf[2], self.brf[2]]
        self.back_face = [self.trb[2], self.tlb[2], self.brb[2], self.blb[2]]
        self.up_face  = [self.tlb[0], self.trb[0], self.tlf[0], self.trf[0]]
        self.down_face = [self.blf[0], self.brf[0], self.blb[0], self.brb[0]]
        self.orientation = [self.front_face, self.left_face, self.right_face, self.back_face, self.up_face, self.down_face]
        print("Front face: {}".format(self.front_face))
        print("Left Face: {}".format(self.left_face))
        print("Right Face: {}".format(self.right_face))
        print("Back Face: {}".format(self.back_face))
        print("Up face: {}".format(self.up_face))
        print("Down face:{}".format(self.down_face))
        self.moves = moves
    def L(self):
        """ TLF to TLB, TLB to BLB, BLB to BLF, BLF to TLF """
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        ntlf[0], ntlf[1], ntlf[2] = tblf[2], tblf[1], tblf[0]
        nblf[0], nblf[1], nblf[2] = tblb[2], tblb[1], tblb[0]
        ntlb[0], ntlb[1], ntlb[2] = ttlf[2], ttlf[1], ttlf[0]
        nblb[0], nblb[1], nblb[2] = ttlb[2], ttlb[1], ttlb[0]
        moves = self.moves.copy()
        moves.append('L')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def L2(self):
        """ TLF to BLB, BLB to TLF, TLB to BLF, BLF to TLB """
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        pass
    def Linv(self):
        """ TLF to BLF, BLF to BLB, BLB to TLB, TLB to TLF """
        
        ntlf, nblf, ntlb, nblb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, tblf, ttlb, tblb = self.tlf, self.blf, self.tlb, self.blb
        nblf[0], nblf[1], nblf[2] = ttlf[2], ttlf[1], ttlf[0]
        nblb[0], nblb[1], nblb[2] = tblf[2], tblf[1], tblf[0]
        ntlb[0], ntlb[1], ntlb[2] = tblb[2], tblb[1], tblb[0]
        ntlf[0], ntlf[1], ntlf[2] = ttlb[2], ttlb[1], ttlb[0]
        moves = self.moves.copy()
        moves.append('L inverse')
        n = RubiksState(ntlf, nblf, self.trf.copy(), self.brf.copy(), ntlb, nblb, self.trb.copy(), self.brb.copy(), moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
        
        pass
    def R(self):
        """ TRF to TRB, TRB to BRB, BRB to BRF, BRF to TRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ntrb[2], ntrb[1], ntrb[0] = ttrf[0], ttrf[1], ttrf[2]
        nbrb[2], nbrb[1], nbrb[0] = ttrb[0], ttrb[1], ttrb[2]
        nbrf[2], nbrf[1], nbrf[0] = tbrb[0], tbrb[1], tbrb[2]
        ntrf[2], ntrf[1], ntrf[0] = tbrf[0], tbrf[1], tbrf[2]
        moves = self.moves.copy()
        moves.append('R')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def R2(self):
        """ TRF to BRB, BRB to TRF, BRF to TRB, TRB to BRF """
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        pass
    def Rinv(self):
        """ TRF to BRF, BRF to BRB, BRB to TRB, TRB to TRF """
        ttrf, tbrf, ttrb, tbrb = self.trf, self.brf, self.trb, self.brb
        ntrf, nbrf, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        nbrf[0], nbrf[1], nbrf[2] = ttrf[2], ttrf[1], ttrf[0]
        nbrb[0], nbrb[1], nbrb[2] = tbrf[2], tbrf[1], tbrf[0]
        ntrb[0], ntrb[1], ntrb[2] = tbrb[2], tbrb[1], tbrb[0]
        ntrf[0], ntrf[1], ntrf[2] = ttrb[2], ttrb[1], ttrb[0]
        moves = self.moves.copy()
        moves.append('R inverse')
        n = RubiksState(self.tlf.copy(), self.blf.copy(), ntrf, nbrf, self.tlb.copy(), self.blb.copy(), ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
        pass
    def U(self):
        """ TLF to TRF, TRF to TRB, TRB to TLB, TLB to TLF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntrf[0], ntrf[1], ntrf[2] = ttlf[0], ttlf[2], ttlf[1]
        ntrb[0], ntrb[1], ntrb[2] = ttrf[0], ttrf[2], ttrf[1]
        ntlb[0], ntlb[1], ntlb[2] = ttrb[0], ttrb[2], ttrb[1]
        ntlf[0], ntlf[1], ntlf[2] = ttlb[0], ttlb[2], ttlb[1]
        moves = self.moves.copy()
        moves.append('U')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    def U2(self):
        """ TLF to TRB, TRB to TLF, TRF to TLB, TLB to TRF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        pass
    def Uinv(self):
        """ TLF to TLB, TLB to TRB, TRB to TRF, TRF to TLF """
        ntlf, ntlb, ntrf, ntrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, ttlb, ttrb = self.tlf, self.trf, self.tlb, self.trb
        ntlb[0], ntlb[1], ntlb[2] = ttlf[0], ttlf[2], ttlf[1]
        ntrb[0], ntrb[1], ntrb[2] = ttlb[0], ttlb[2], ttlb[1]
        ntrf[0], ntrf[1], ntrf[2] = ttrb[0], ttrb[2], ttrb[1]
        ntlf[0], ntlf[1], ntlf[2] = ttrf[0], ttrf[2], ttrf[1]
        moves = self.moves.copy()
        moves.append('U inverse')
        n = RubiksState(ntlf, self.blf, ntrf, self.brf, ntlb, self.blb, ntrb, self.brb, moves)
        return n
    
    def D(self):
        """ BLF to BRF, BRF to BRB, BRB to BLB, BLB to BLF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nbrf[0], nbrf[1], nbrf[2] = tblf[0], tblf[2], tblf[1]
        nbrb[0], nbrb[1], nbrb[2] = tbrf[0], tbrf[2], tbrf[1]
        nblb[0], nblb[1], nblb[2] = tbrb[0], tbrb[2], tbrb[1]
        nblf[0], nblf[1], nblf[2] = tblb[0], tblb[2], tblb[1]
        moves = self.moves.copy()
        moves.append('D')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def D2(self):
        """ BLF to BRB, BRB to BLF, BRF to BLB, BLB to BRF """
        pass
    def Dinv(self):
        """ BLF to BLB, BLB to BRB, BRB to BRF, BRF to BLF """
        nblf, nblb, nbrf, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        tblf, tbrf, tbrb, tblb = self.blf, self.brf, self.brb, self.blb
        nblb[0], nblb[1], nblb[2] = tblf[0], tblf[2], tblf[1]
        nbrb[0], nbrb[1], nbrb[2] = tblb[0], tblb[2], tblb[1]
        nbrf[0], nbrf[1], nbrf[2] = tbrb[0], tbrb[2], tbrb[1]
        nblf[0], nblf[1], nblf[2] = tbrf[0], tbrf[2], tbrf[1]
        moves = self.moves.copy()
        moves.append('D inverse')
        n = RubiksState(self.tlf, nblf, self.trf, nbrf, self.tlb, nblb, self.trb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
        pass
    def F(self):
        """ TLF to BLF, BLF to BRF, BRF to TRF, TRF to TLF """
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlf, ttrf, tblf, tbrf = self.tlf, self.trf, self.blf, self.brf
        nblf[0], nblf[1], nblf[2] = ttlf[1], ttlf[0], ttlf[2]
        nbrf[0], nbrf[1], nbrf[2] = tblf[1], tblf[0], tblf[2]
        ntrf[0], ntrf[1], ntrf[2] = tbrf[1], tbrf[0], tbrf[2]
        ntlf[0], ntlf[1], ntlf[2] = ttrf[1], ttrf[0], ttrf[2]
        moves = self.moves.copy()
        moves.append('F')
        n = RubiksState(ntlf, nblf, ntrf, nbrf, self.tlb, self.blb, self.trb, self.brb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def F2(self):
        """ TLF to BRF, BRF to TLF, TRF to BLF, BLF to TRF """
        ntlf, nblf, ntrf, nbrf = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        pass
    def Finv(self):
        """ TLF to TRF, TRF to BRF, BRF to BLF, BLF to TLF """
        pass
    def B(self):
        """ TLB to BLB, BLB to BRB, BRB to TRB, TRB to TLB """
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        ttlb, tblb, ttrb, tbrb = self.tlb, self.blb, self.trb, self.brb
        nblb[0], nblb[1], nblb[2] = ttlb[1], ttlb[0], ttlb[2]
        nbrb[0], nbrb[1], nbrb[2] = tblb[1], tblb[0], tblb[2]
        ntrb[0], ntrb[1], ntrb[2] = tbrb[1], tbrb[0], tbrb[2]
        ntlb[0], ntlb[1], ntlb[2] = ttrb[1], ttrb[0], ttrb[2]
        moves = self.moves.copy()
        moves.append('B')
        n = RubiksState(self.tlf, self.blf, self.trf, self.brf, ntlb, nblb, ntrb, nbrb, moves)
        #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
        return n
    def B2(self):
        """ TLB to BLB, BLB to TLB, TRB to BLB, BLB to TRB """
        ntlb, nblb, ntrb, nbrb = [0] * 3, [0] * 3, [0] * 3, [0] * 3
        pass
    def Binv(self):
        """ BLB to TLB, TLB to TRB, TRB to BRB, BRB to BLB """
        pass
    def is_solved(self):
        if self.blb == ['Y', 'O', 'B'] and self.tlb == ['W', 'O', 'B'] and self.brb == ['Y', 'R', 'B'] and self.trb == ['W', 'R', 'B'] and self.blf == ['Y', 'O', 'G'] and self.tlf == ['W', 'O', 'G'] and self.brf == ['Y', 'R', 'G'] and self.trf == ['W', 'R', 'G']:
            print('Solved: {}'.format(self.moves))
#            exit(1)
        if self.front_face == ['G', 'G', 'G', 'G'] and self.back_face == ['B', 'B', 'B', 'B'] and self.left_face == ['O', 'O', 'O', 'O'] and self.right_face == ['R', 'R', 'R', 'R'] and self.up_face == ['W', 'W', 'W', 'W'] and self.down_face == ['Y', 'Y', 'Y', 'Y']:
            return True
        else:
            return False
from queue import deque
import sys
def Charles():
    States = deque([])
    n = RubiksState(['W', 'O', 'G'], ['Y', 'O', 'G'], ['W', 'R', 'G'], ['Y', 'R', 'G'], ['W', 'O', 'B'], ['Y', 'B', 'R'], ['W', 'R', 'B'], ['Y','B', 'O'], [])
    n = RubiksState(['W', 'O', 'G'], ['Y', 'O', 'G'], ['W', 'R', 'G'], ['Y', 'R', 'G'], ['W', 'O', 'B'], ['Y', 'O', 'B'], ['W', 'R', 'B'], ['Y','R', 'B'], [])
    n = RubiksState(['O', 'B', 'Y'], ['R', 'B', 'Y', ], ['O', 'G', 'Y'], ['R', 'G', 'Y'], ['O', 'B', 'W'], ['R', 'B', 'W'], ['O', 'G', 'W'], ['R', 'G', 'W'], [])
    all_states = [n for n in itertools.permutations([['G', 'G', 'G', 'G'], ['B', 'B', 'B', 'B'], ['O', 'O', 'O', 'O'], ['R', 'R', 'R', 'R'], ['W', 'W', 'W', 'W'], ['Y', 'Y', 'Y', 'Y']])]
#    print(all_states)
#    sys.exit(1)
    #tlf, blf, trf, brf, tlb, blb, trb, brb, moves
    moves = [lambda s: s.L(), lambda s: s.R(), lambda s: s.U(), lambda s: s.D(), lambda s: s.F(), lambda s: s.B()]
    States.append(n)
    c = 0
    solved = False
    print(States)
    for move in moves:
        print(move(States[0]))
    for move in moves:
        States.append(move(States[0]))
    c = 0
    while solved != True:
        cm = States[c]
        for move in moves:
            print(move(cm).moves)
            States.append(move(cm))
        if cm.is_solved() == True:
            break
        c += 1
#    while n < 8 ** 6:
#        state = States.popleft()
#        for move in moves:
#            new_move = move(state)
#            print(new_move.moves)
#            States.append(new_move)
#            if new_move.front_face == ['G', 'G', 'G', 'G'] and new_move.back_face == ['B', 'B', 'B', 'B'] and new_move.left_face == ['O', 'O', 'O', 'O'] and new_move.right_face == ['R', 'R', 'R', 'R'] and new_move.up_face == ['W', 'W', 'W', 'W'] and new_move.down_face == ['Y', 'Y', 'Y', 'Y']:
#                print('Solved, {}'.format(new_move.moves))
#                break
#        n += 1
#    while solved != True:
#        state = States.popleft()
#        for move in moves:
#            t = move(state)
#            print(t.moves)
#            States.append(t)
#            if t.front_face == ['G', 'G', 'G', 'G'] and t.back_face == ['B', 'B', 'B', 'B'] and t.left_face == ['O', 'O', 'O', 'O'] and t.right_face == ['R', 'R', 'R', 'R'] and t.up_face == ['W', 'W', 'W', 'W'] and t.down_face == ['Y', 'Y', 'Y', 'Y']:
#                print('Solved, {}'.format(t.moves))
#                break
# #               sys.exit(1)
#            if t.is_solved() == True:
#                print('Solved, {}'.format(t.moves))
#                break
##                sys.exit(1)
#            if t.orientation in all_states:
#                print('Solved: {}'.format(t.moves))
#                break
#        if state.is_solved() == True:
#            solved = True
#            break
#        c += 1

#Charles()