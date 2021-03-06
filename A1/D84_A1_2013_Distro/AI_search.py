# This is the script that implements the different search algorithms
# that you will try with the mouse. 
#
# The algorithms you are responsible for are:
#
#	BFS
#	DFS
#	A* search
#	A* search with cat heuristic
#
# Read the comments at the head of each function carefully and be
# sure to return exactly what is requested. Also, be sure to 
# update the Maze[][] array. Read below for details.
#
# All work you do here is individual.
#
# Starter code: F.J.E. Aug. 8, 2012 (start early! see?)
#
# Global data you will have access to (note each of these *MUST*
# be prefixed with 'AI_global_data.', e.g. 'AI_global_data.Ncats'
#
# 'Ncats'    -> An integer holding the numebr of cats in the game
# 'Ncheese'  -> An integer holding the number of cheese chunks
# 'Mouse'    -> A single entry list with mouse coordinates [x,y]
# 'Cats'     -> An Ncats x 2 list with cat coordinates [x,y]
# 'Cheese'   -> An Ncheese x 2 list with cheese locations [x,y]
# 'msx','msy'-> Maximum size of the maze along x and y respectively,
#               this is fixed at 32 for both directions. DO NOT 
#               CHANGE. You only need this for indexing into A[][]
# 'Maze[][]' -> An array of size msx x msy (32 x 32) you will use
#               to record the order in which each location in the
#               maze is 'discovered' during search. i.e., if
#               Maze[i][j]=k then location [i][j] was the kth
#               location explored by your search function
# 'P[][]'    -> An array of size msx x msy (32 x 32) you can use for
#               storing any node-related temporary data you may need
#               during search.
# 'A[][]'    -> An adjacency list encoding the maze connectivity.
#               The size of A[][] is (AI_global_data.msx*msy) x 4, that is, it
#               contains one row for each location in the maze,
#               and for each row, it specifies 4 possible edges
#               to the top, right, bottom, and left neighbours
#               respectively.
#               Example: Say your mouse is at location [2,3], and
#                        you want to check where it can move to.
#                        The data for this location is stored at
#                        A[2+(3*AI_global_data.msx)][0] : Link to grid location [2,2]
#                        A[2+(3*AI_global_data.msx)][1] : Link to grid location [3,3]
#                        A[2+(3*AI_global_data.msx)][2] : Link to grid location [2,4]
#                        A[2+(3*AI_global_data.msx)][3] : Link to grid location [1,3]
#                        If the link is 1, the locations are connected,
#                        if the link is 0 there is a wall in between.
# 'MousePath' -> You will use this list to return a path from the
#                mouse to the cheese. It will be used by the search
#                core to update the mouse position at each turn.
#                Be sure to store information in the order requested,
#                and make sure each [x,y] location pair contains 
#                only valid locations.
#
# You *CAN NOT MODIFY* anything other than 'MousePath' and 'P' in the global data
# described above. Doing so will cause your program to give results that
# disagree with our automatic testing and you'll get zero.

from math import *

# Import global data
import AI_global_data

# Function definitions

def checkForCats(x,y):
  # A little helper function to tell you if there is a cat at [x,y].
  # Returns 1 if there is a cat, 0 otherwise.
  for i in range(AI_global_data.Ncats):
   if (AI_global_data.Cats[i][0]==x and AI_global_data.Cats[i][1]==y):
    return 1

  return 0

def checkForCheese(x,y):
  # A little helper function to tell you if there is cheese at [x,y].
  # Returns 1 if there is cheese, 0 otherwise.
  for i in range(AI_global_data.Ncheese):
   if (AI_global_data.Cheese[i][0]==x and AI_global_data.Cheese[i][1]==y):
    return 1
  
  return 0

def Astar_cost(x,y):
  # Use this function to compute the heuristic cost estimate for
  # location [x,y] given the locations of cheese. This function
  # *MUST NOT* use cat locations in computing the cost. 

  ###############################################################
  ## TO DO: Implement the heuristic cost computation. 
  ##        Your function must implement an admissible heuristic!
  ###############################################################

  return 0		# Of course, you should change this to
			# return your computed cost

def Astar_cost_nokitty(x,y):
  # Use this function to compute the heuristic cost estimate for
  # location [x,y] given the locations of cheese. This function
  # *CAN* use cat locations in computing the cost. 

  ###############################################################
  ## TO DO: Implement the heuristic cost computation. 
  ##        Your function must implement an admissible heuristic!
  ###############################################################

  return 0		# Of course, you should change this to
			# return your computed cost

def BFS():
  # Breadth-first search

  ###################################################################
  ## TO DO: Implement BFS here starting at the mouse's location
  ##        and ending at the cheese location. Be sure to update
  ##        the Maze[][] array to indicate in which order maze
  ##        locations were expanded while looking for a path to
  ##        the cheese. 
  ##
  ## Notes:
  ##        - This is *NOT A RECURSIVE* function. Do not attempt
  ##          to turn it into a recursion - you will blow the
  ##          stack easily.
  ##        - If a path is found, return 1, and update 
  ##          AI_global_data.MousePath to contain the path 
  ##          from *END TO START*, that is, the first entry
  ##          in the list will be the cheese location, and
  ##          the last entry will be the mouse location.
  ##          The function will return 1 in this case.
  ##        - If no path is found, set AI_global_data.MousePath
  ##          to be an empty list, and return 0. The mouse
  ##          will wait at its current location for cats to move
  ##          away from possible paths to the cheese.
  ##        - Add any local data you need.
  ##        - Be careful to expand each location only once!
  ##        - Given a current location [x,y], its neighbours
  ##          *MUST* be expanded in the following order:
  ##          top, right, bottom, left.
  ##	    - Mouse can't go through cats. If your search 
  ##          reaches a location with a cat, it must backtrack.
  ##        - If multiple cheeses exist, return the path to the
  ##          first cheese found
  ###################################################################

  return 0	# No path found

def DFS(DFS_stack,cnt):
  # Depth-first search

  ###################################################################
  ## TO DO: Implement DFS here starting at the mouse's location
  ##        and ending at the cheese location. Be sure to update
  ##        the Maze[][] array to indicate in which order maze
  ##        locations were expanded while looking for a path to
  ##        the cheese. 
  ##
  ## Notes:
  ##        - This is a *RECURSIVE* function, do not try to turn
  ##          it into an iterative one. DFS is an ideal candidate
  ##          for recursion. There are several ways to build the
  ##          mouse path once you find the cheese, but one way is 
  ##          to get the path directly from the recursion sequence.  
  ##        - Except for the recursive nature of DFS, the same
  ##          conditions apply as for BFS above.
  ##        - For a given node, its children will also be expanded
  ##          in order top,right,bottom,left.
  ###################################################################

  return 0	# No path found

def Astar():
  # A* search

  ###################################################################
  ## TO DO: Implement A* search as discussed in lecture. Note that
  ##        I am not giving you the heuristic cost function. You
  ##        are responsible for coming up with an *admissible*
  ##        heuristic (justify your choice and explain why it is
  ##        admissible in your report).
  ##
  ## Notes:
  ##        - Same conditions apply as for BFS and DFS.
  ##        - This is *NOT* a recursive function. 
  ##        - Expansion order given by cost estimate. Be sure to
  ##          compute the cost for each location correctly! and note
  ##          it is *NOT* only the heuristic cost.
  ##        - If multiple cheeses exist, you need to account for that
  ##          somehow in the heuristic cost function. Explain in
  ##          the report how you handle this.
  ###################################################################

  return 0 	# No path

def Astar_nokitty():
  # A* search with cat-dependent heuristic

  ###################################################################
  ## TO DO: This is an improved version of A* that not only  
  ##        uses cheese locations in the heuristic cost function, 
  ##        but also tries to account for cat locations. Your
  ##        heuristic should be such that the mouse avoids as
  ##        far as possible going too near any cats while at the
  ##        same time finding efficiently a path to the cheese.
  ##
  ##        Explain your heuristic cost function, how the cheese 
  ##        and cat locations influence the cost, and whether it
  ##        is admissible or not.
  ##
  ## Notes:
  ##        - Same conditions apply as for BFS and DFS and Astar.
  ###################################################################

  # Nothing to return! MousePath is global
  return 0



