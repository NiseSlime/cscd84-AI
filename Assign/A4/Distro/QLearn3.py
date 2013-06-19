# CSC D84 - Winter 2013 - Assignment 4 - Q Learning
#
# This file is where you will implement the QLearning updates
# and the action selection process for the Mouse.
#
# Functions you have to write
#	Qlearn()
#	reward()
#	decideAction()
#
# Read the comments at the head of each function carefully and be
# sure to implement exactly what is requested.
#
# All work you do here is individual.
#
# Starter code: F.J.E. Jan. 30, 2013 
#
# Global data you will have access to (note each of these *MUST*
# be prefixed with 'QLearn_global_data.', e.g. 'QLearn_global_data.Ncats'
#
# 'Mouse'    -> A single entry list with mouse coordinates [x,y]
# 'Cats'     -> An single entry list with cat coordinates [x,y]
# 'Cheese'   -> An single entry list with cheese locations [x,y]
# 'msx','msy'-> Maximum size of the maze along x and y respectively,
#               this is set by QLearn_core_GL. DO NOT 
#               CHANGE. You only need this for indexing into A[][]
# 'A[][]'    -> An adjacency list encoding the maze connectivity.
#               The size of A[][] is (msx*msy) x 4, that is, it
#               contains one row for each location in the maze,
#               and for each row, it specifies 4 possible edges
#               to the top, right, bottom, and left neighbours
#               respectively.
#               Example: Say your mouse is at location [2,3], and
#                        you want to check where it can move to.
#                        The data for this location is stored at
#                        A[2+(3*QLearn_global_data.msx)][0] : Link to grid location [2,2]
#                        A[2+(3*QLearn_global_data.msx)][1] : Link to grid location [3,3]
#                        A[2+(3*QLearn_global_data.msx)][2] : Link to grid location [2,4]
#                        A[2+(3*QLearn_global_data.msx)][3] : Link to grid location [1,3]
#                        If the link is 1, the locations are connected,
#                        if the link is 0 there is a wall in between.
#
# 'Qtable'	An array of size [(msx*msy)^3][4] with one row per state, and
#		4 columns corresponding to the 4 possible mouse moves.
# 'alpha'	The Q-learning learning rate
# 'lamb' 	The Q-learning discount constant for future rewards
#
# YOU ARE NOT ALLOWED TO MODIFY ANY GLOBAL DATA EXCEPT FOR 'Qtable'.
# This is the only place where you need to update anything at all.
#

from math import *

# Import global data
import QLearn_global_data

# Function definitions

def QLearn(s,a,r,s_new):
	####################################################################
	# This function implements the Q-learning update rule. It updates an
	# entry in the Qtable given the experience tuple <s,a,r,s_new>
	# as discussed in lecture. 
	#
	# Return values: NONE
	####################################################################

	####################################################################
	## TO DO:
	##       Implement this functin to carry out the Qtable updates
	##	 This is a 1-line function! (it's a long line)
	####################################################################
	QLearn_global_data.Qtable[s][a] += QLearn_global_data.alpha * (r + (QLearn_global_data.lamb * max(QLearn_global_data.Qtable[s_new]) - QLearn_global_data.Qtable[s][a]))

def reward():
	####################################################################
	# This function computes and returns a reward value for the
	# CURRENT GAME CONFIGURATION (i.e. for the current Mouse, Cat,
	# and Cheese location). It is called by the code in QLearn_core_GL
	# during training to determine the reward associated with a given
	# state.
	#
	# The function can be as simple or as complicated as you like,
	# but it should give positive rewards for configurations that
	# are favorable to the mouse, and negative rewards for configurations
	# that favour the cat.
	#
	# Be careful! the reward function will have a STRONG impact on the
	# ability of your mouse to learn!
	####################################################################

	####################################################################
	## TO DO:
	##	Implement the reward function. It must return a real-valued
	##	scalar reward appropriate for the current game configuration.QLearn_global_data.
	##
	##	Document this function carefully in the REPORT.TXT
	####################################################################

	####################################################################
	# CRUNCHY:
	#	Implement a smart reward function that allows the mouse to
	#	learn with much fewer training samples. This should allow
	#	you to train on a 16x16 grid in a reasonable amount of time!
	#
	#	If you do this, explain in REPORT.TXT how it works and why
	#	it allows the mouse to learn faster. Be sure to note how
        #       long it takes to train. And beware: The QTable.pickle for
        #       a 16x16 grid is over 2Gb long, so don't run this anywhere
        #       where space is an issue!
	####################################################################
	mx, my = QLearn_global_data.Mouse[0]
	chx, chy = QLearn_global_data.Cheese[0]
	cx, cy = QLearn_global_data.Cats[0]
	if (QLearn_global_data.Mouse[0] == QLearn_global_data.Cats[0]):
		return -100

	if (QLearn_global_data.Mouse[0] == QLearn_global_data.Cheese[0]):
		return 100
	
	num_walls = 0
	for i in range(4):
		if (QLearn_global_data.A[mx+(my*QLearn_global_data.msx)][i] == 0):
			num_walls += 1
		
	if (num_walls == 3):
		return -80

	d_mch = abs(mx - chx) + abs(my - chy)  	 
	d_cm = d_mch =abs(cx - mx) + abs(cy - my)  
	reward = -(d_mch) + d_cm


	# Replace with your computed reward
	
	#reward = float(d_cm)/float(d_mch) 
	#reward = log(reward,10) * 10
	return reward


def decideAction(s):
	####################################################################
	# This function is called by QLearn_core_GL once the training is
	# complete. It is used to play the actual game against the
	# cat. The function should choose for the given input state 's'
	# the optimal action that is *ALLOWABLE*.
	#
	# This means, the optimal action that does not involve crossing a
	# wall. You must somehow use the Qtable and the A[][] adjacency
	# list to determine where the mouse should go.
	####################################################################

	####################################################################
	## TO DO:
	##  	Implement this function to enable the mouse to choose an
	##	optimal action for any given state 's'
	##
	##	The function MUST RETURN the *INDEX* of the optimal move
	##	as follows:
	##			idx=0 -> Mouse moves up
	##			idx=1 -> Mouse moves right
	##			idx=2 -> Mouse moves down
	##			idx=3 -> Mouse moves left
	####################################################################
	maxreward = -10000
	move = 0
	possible_loc = []
	mx, my = QLearn_global_data.Mouse[0]
	for i in range(4):
		if (QLearn_global_data.A[mx+(my*QLearn_global_data.msx)][i] == 1):
			possible_loc.append(i)

	for i in possible_loc:	
		if (QLearn_global_data.Qtable[s][i] > maxreward):
			move = i
			maxreward = QLearn_global_data.Qtable[s][i]
	return move
	

#def possibleNeighbours(s):
    #result_base = []
    #calc = s
    #base_mst = QLearn_global_data.msx * QLearn_global_data.msy
    #for i in range(2):
    #    if(calc < base_mst):
    #        result_base.append(calc)
    #        calc = 0
    #    else:
    #        calc = s / base_mst
    #        temp = s % base_mst
    #        result_base.append(temp)

    #result_base.reverse() 
    #mouse_loc = result_base[0] 
    #mx, my = QLearn_global_data.Mouse
    #possible_loc = []
    #for i in range(4):
    #	if ((QLearn_global_data.A[mouse_loc][i] == 1) and ([ != QLearn_global_data.Cats)):
    #		possible_loc.append(i)
    #return possible_loc
	
		
		 
		

		
	

