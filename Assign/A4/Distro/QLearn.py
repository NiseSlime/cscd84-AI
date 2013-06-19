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
# http://artint.info/html/ArtInt_265.html
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

	QLearn_global_data.Qtable[s][a] = QLearn_global_data.Qtable[s][a] + QLearn_global_data.alpha * (r + QLearn_global_data.lamb * max(QLearn_global_data.Qtable[s_new]) - QLearn_global_data.Qtable[s][a]) 
	return

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
	##	scalar reward appropriate for the current game configuration.
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

	dist2cat = abs(QLearn_global_data.Mouse[0][0]-QLearn_global_data.Cats[0][0]) + abs(QLearn_global_data.Mouse[0][1]-QLearn_global_data.Cats[0][1])  	 
	dist2cheese = abs(QLearn_global_data.Mouse[0][0] - QLearn_global_data.Cheese[0][0]) + abs(QLearn_global_data.Mouse[0][1] - QLearn_global_data.Cheese[0][1])  
	cheeseNcat = abs(QLearn_global_data.Cheese[0][0]-QLearn_global_data.Cats[0][0]) + abs(QLearn_global_data.Cheese[0][1]-QLearn_global_data.Cats[0][1])
	maxDist = QLearn_global_data.msx 


	if(dist2cheese < 2):
		return 10000
	
	if(dist2cat < 2):
		return -10000


	reward = (maxDist - dist2cheese) + dist2cat + (dist2cheese - cheeseNcat)*2

	return reward  	# Replace with your computed reward

# Replace with your computed reward



	# mx = QLearn_global_data.Mouse[0][0]
	# my =  QLearn_global_data.Mouse[0][1]	
	# points = 0

	# dist2cat = abs(QLearn_global_data.Mouse[0][0]-QLearn_global_data.Cats[0][0]) + abs(QLearn_global_data.Mouse[0][1]-QLearn_global_data.Cats[0][1])  	 
	# dist2cheese = abs(QLearn_global_data.Mouse[0][0] - QLearn_global_data.Cheese[0][0]) + abs(QLearn_global_data.Mouse[0][1] - QLearn_global_data.Cheese[0][1])  
	# if dist2cheese < 5:
	# 	points = 1000
	# if dist2cat < 2:
	# 	points = -100000


	# return (10000 - dist2cheese) + points
	
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

	value = -1000000
	index = 0
	x = QLearn_global_data.Mouse[0][0]
	y = QLearn_global_data.Mouse[0][1]
	action = 0
	while action < 4:
		if QLearn_global_data.A[x+(y*QLearn_global_data.msx)][action] == 1:
			temp = QLearn_global_data.Qtable[s][action]
			if temp > value:
				value = temp
				index = action
		action+=1
	return index	# Replace this with your return value!

