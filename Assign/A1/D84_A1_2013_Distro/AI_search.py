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

  # get total cost for all the cheeses and return the minimum cost
  min_distance = 100000000
  for cheese in AI_global_data.Cheese:
    dist = (abs(cheese[0] - x) + abs(cheese[1] - y))
    if dist < min_distance:
      min_distance = dist
  return min_distance		# Of course, you should change this to
			# return your computed cost

def Astar_cost_nokitty(x,y):
  # Use this function to compute the heuristic cost estimate for
  # location [x,y] given the locations of cheese. This function
  # *CAN* use cat locations in computing the cost. 

  ###############################################################
  ## TO DO: Implement the heuristic cost computation. 
  ##        Your function must implement an admissible heuristic!
  ###############################################################
  # get total cost for all the cheeses and return the minimum cost
  min_cheese = Astar_cost(x,y)
  goal = [0, 10000, 500, 200, 100, 50, 10]
  danger = [0, 1000000, 500, 200, 50, 35, 20, 5]
  # get total cost of cats 2 and add it
  for cat in AI_global_data.Cats:
    dist =  (abs(cat[0] - x) + abs(cat[1] - y))
    if min_cheese < 7 and min_cheese>0:
      index = min_cheese
      min_cheese = min_cheese / goal[index]
    if dist < 7 and dist > 0:
      min_cheese = danger[dist] * min_cheese

    # else: 
    #   dist = min_cheese
    # if dist < min_distance:
    #   min_distance = dist
  return min_cheese		# Of course, you should change this to
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
  ##      - Mouse can't go through cats. If your search 
  ##          reaches a location with a cat, it must backtrack.
  ##        - If multiple cheeses exist, return the path to the
  ##          first cheese found
  ###################################################################

  BFS_queue = []
  BFS_queue.append([AI_global_data.Mouse[0][0],AI_global_data.Mouse[0][1]])
  k=0
  AI_global_data.Maze[AI_global_data.Mouse[0][0]][AI_global_data.Mouse[0][1]] = k
  AI_global_data.P[AI_global_data.Mouse[0][0]][AI_global_data.Mouse[0][1]] = 1
  dct = {}
  
  # print "******************************************************"
  # print BFS_queue
  # print "******************************************************"
  while BFS_queue:
    x = BFS_queue[0][0]
    y = BFS_queue[0][1]
    #print "*************************************************************"
    #print BFS_queue 
    #print "*************************************************************"
    BFS_queue.pop(0)
    if checkForCheese(x,y):
      # print "Cheese is at (%d, %d)" % (x,y)
      AI_global_data.MousePath.append([x,y])
      while AI_global_data.Maze[x][y] != 0:
        lst = dct[(x,y)]
        # print "*************************************************************"
        # print lst
        # print "*************************************************************"
        AI_global_data.MousePath.append(lst)
        x = lst[0]
        y = lst[1]
      return 1
    index = (x + (y * AI_global_data.msx))
    #Top
    if AI_global_data.A[index][0] == 1 and AI_global_data.P[x][y-1] == 0:
      # print "Maze[x][y-1]"
      BFS_queue.append((x,y-1))
      k+=1
      AI_global_data.Maze[x][y-1] = k
      AI_global_data.P[x][y-1] = 1
      dct[(x,y-1)] = (x,y)
      #Right
    if AI_global_data.A[index][1] == 1 and AI_global_data.P[x+1][y] == 0:
      # print "Maze[x+1][y]"
      BFS_queue.append((x+1,y))
      k+=1
      AI_global_data.Maze[x+1][y] = k
      AI_global_data.P[x+1][y] = 1
      dct[(x+1,y)] = (x,y)
      #Bottom
    if AI_global_data.A[index][2] == 1 and AI_global_data.P[x][y+1] == 0:
      # print "Maze[x][y+1]"
      BFS_queue.append((x,y+1))
      k+=1
      AI_global_data.Maze[x][y+1] = k
      AI_global_data.P[x][y+1] = 1
      dct[(x,y+1)] = (x,y)
      #Left
    if AI_global_data.A[index][3] == 1 and AI_global_data.P[x-1][y] == 0:
      # print "Maze[x-1][y]"
      BFS_queue.append((x-1,y))
      k+=1
      AI_global_data.Maze[x-1][y] = k
      AI_global_data.P[x-1][y] = 1
      dct[(x-1,y)] = (x,y)
    # print "*************************************************************"
    # print dct.items() 
    # print "*************************************************************"
  return 0  # No path found

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

  if (cnt == 0):
    DFS_stack.append([AI_global_data.Mouse[0][0], AI_global_data.Mouse[0][1]])
    AI_global_data.Maze[AI_global_data.Mouse[0][0]][AI_global_data.Mouse[0][1]] = 0
    AI_global_data.P[AI_global_data.Mouse[0][0]][AI_global_data.Mouse[0][1]] = 1

  node = DFS_stack.pop()
  x = node[0]
  y = node[1]
  if checkForCheese(x,y):
    AI_global_data.MousePath.append(node)
    return 1

  index = (x + (y * AI_global_data.msx))
  # Top
  if AI_global_data.A[index][0] == 1 and AI_global_data.P[x][y-1] == 0:
    AI_global_data.P[x][y-1] = 1
    AI_global_data.Maze[x][y-1] = cnt
    if DFS([(x, y-1)],cnt+1):
      AI_global_data.MousePath.append((x, y-1))
      return 1

  # Right
  if AI_global_data.A[index][1] == 1 and AI_global_data.P[x+1][y] == 0:
    AI_global_data.P[x+1][y] = 1
    AI_global_data.Maze[x+1][y] = cnt
    if DFS([(x+1, y)],cnt+1):
      AI_global_data.MousePath.append((x+1, y))
      return 1
  
  # Bottom
  if AI_global_data.A[index][2] == 1 and AI_global_data.P[x][y+1] == 0:
    DFS_stack.append((x, y+1))
    AI_global_data.P[x][y+1] = 1
    AI_global_data.Maze[x][y+1] = cnt
    if DFS([(x, y+1)],cnt+1):
      AI_global_data.MousePath.append((x, y+1))
      return 1
  
  # Left
  if AI_global_data.A[index][3] == 1 and AI_global_data.P[x-1][y] == 0:
    AI_global_data.P[x-1][y] = 1
    AI_global_data.Maze[x-1][y] = cnt
    if DFS([(x-1, y)],cnt+1):
      AI_global_data.MousePath.append((x-1, y))
      return 1
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

  Astar_queue = []
  Astar_queue.append([AI_global_data.Mouse[0][0],AI_global_data.Mouse[0][1]])
  k=0
  AI_global_data.Maze[AI_global_data.Mouse[0][0]][AI_global_data.Mouse[0][1]] = k
  AI_global_data.P[AI_global_data.Mouse[0][0]][AI_global_data.Mouse[0][1]] = 1
  dct = {}
  past_dist = 0
  while Astar_queue:
    # print "Astar_queue is "
    # print Astar_queue
    dist2cheese = 10000000
    index = 0
    min_index = 0
    while index < len(Astar_queue):
      node = Astar_queue[index]
      x = node[0]
      y = node[1]
      node_dist = AI_global_data.P[x][y] + Astar_cost(x, y)
      if node_dist < dist2cheese:
        dist2cheese = node_dist
        min_index = index
      index+=1
    # print "the min_index is " + str(min_index) 
    # print "dist2cheese is " + str(dist2cheese)

    x = Astar_queue[min_index][0]
    y = Astar_queue[min_index][1]
    Astar_queue.pop(min_index)
    
    if checkForCheese(x,y):
      # print "Cheese is at (%d, %d)" % (x,y)
      AI_global_data.MousePath.append([x,y])
      while AI_global_data.Maze[x][y] != 0:
        lst = dct[(x,y)]
        # print "*************************************************************"
        # print lst
        # print "*************************************************************"
        AI_global_data.MousePath.append(lst)
        x = lst[0]
        y = lst[1]
      return 1
    index = (x + (y * AI_global_data.msx)) 
    past_dist = AI_global_data.P[x][y] + 1
    if AI_global_data.A[index][0] == 1 and AI_global_data.P[x][y-1] == 0:
      # print "Maze[x][y-1]"
      Astar_queue.append((x,y-1))
      k+=1
      AI_global_data.Maze[x][y-1] = k
      AI_global_data.P[x][y-1] = past_dist 
      dct[(x,y-1)] = (x,y)
      #Right
    if AI_global_data.A[index][1] == 1 and AI_global_data.P[x+1][y] == 0:
      # print "Maze[x+1][y]"
      Astar_queue.append((x+1,y))
      k+=1
      AI_global_data.Maze[x+1][y] = k
      AI_global_data.P[x+1][y] = past_dist 
      dct[(x+1,y)] = (x,y)
      #Bottom
    if AI_global_data.A[index][2] == 1 and AI_global_data.P[x][y+1] == 0:
      #print "Maze[x][y+1]"
      Astar_queue.append((x,y+1))
      k+=1
      AI_global_data.Maze[x][y+1] = k
      AI_global_data.P[x][y+1] = past_dist 
      dct[(x,y+1)] = (x,y)
      #Left
    if AI_global_data.A[index][3] == 1 and AI_global_data.P[x-1][y] == 0:
      #print "Maze[x-1][y]"
      Astar_queue.append((x-1,y))
      k+=1
      AI_global_data.Maze[x-1][y] = k
      AI_global_data.P[x-1][y] = past_dist 
      dct[(x-1,y)] = (x,y)  

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
  Astar_queue = []
  Astar_queue.append([AI_global_data.Mouse[0][0],AI_global_data.Mouse[0][1]])
  k=0
  AI_global_data.Maze[AI_global_data.Mouse[0][0]][AI_global_data.Mouse[0][1]] = k
  AI_global_data.P[AI_global_data.Mouse[0][0]][AI_global_data.Mouse[0][1]] = 1
  dct = {}
  past_dist = 0
  while Astar_queue:
    #print "Astar_queue is "
    #print Astar_queue
    dist2cheese = 10000000
    index = 0
    min_index = 0
    while index < len(Astar_queue):
      node = Astar_queue[index]
      x = node[0]
      y = node[1]
      node_dist = AI_global_data.P[x][y] + Astar_cost_nokitty(x, y)
      if node_dist < dist2cheese:
        dist2cheese = node_dist
        min_index = index
      index+=1
    #print "the min_index is " + str(min_index) 
    #print "dist2cheese is " + str(dist2cheese)

    x = Astar_queue[min_index][0]
    y = Astar_queue[min_index][1]
    Astar_queue.pop(min_index)
    
    if checkForCheese(x,y):
      # print "Cheese is at (%d, %d)" % (x,y)
      AI_global_data.MousePath.append([x,y])
      while AI_global_data.Maze[x][y] != 0:
        lst = dct[(x,y)]
        # print "*************************************************************"
        # print lst
        # print "*************************************************************"
        AI_global_data.MousePath.append(lst)
        x = lst[0]
        y = lst[1]
      return 1
    index = (x + (y * AI_global_data.msx)) 
    past_dist = AI_global_data.P[x][y] + 1
    if AI_global_data.A[index][0] == 1 and AI_global_data.P[x][y-1] == 0:
      # print "Maze[x][y-1]"
      Astar_queue.append((x,y-1))
      k+=1
      AI_global_data.Maze[x][y-1] = k
      AI_global_data.P[x][y-1] = past_dist 
      dct[(x,y-1)] = (x,y)
      #Right
    if AI_global_data.A[index][1] == 1 and AI_global_data.P[x+1][y] == 0:
      # print "Maze[x+1][y]"
      Astar_queue.append((x+1,y))
      k+=1
      AI_global_data.Maze[x+1][y] = k
      AI_global_data.P[x+1][y] = past_dist 
      dct[(x+1,y)] = (x,y)
      #Bottom
    if AI_global_data.A[index][2] == 1 and AI_global_data.P[x][y+1] == 0:
      #print "Maze[x][y+1]"
      Astar_queue.append((x,y+1))
      k+=1
      AI_global_data.Maze[x][y+1] = k
      AI_global_data.P[x][y+1] = past_dist 
      dct[(x,y+1)] = (x,y)
      #Left
    if AI_global_data.A[index][3] == 1 and AI_global_data.P[x-1][y] == 0:
      #print "Maze[x-1][y]"
      Astar_queue.append((x-1,y))
      k+=1
      AI_global_data.Maze[x-1][y] = k
      AI_global_data.P[x-1][y] = past_dist 
      dct[(x-1,y)] = (x,y)
  # Nothing to return! MousePath is global
  return 0



