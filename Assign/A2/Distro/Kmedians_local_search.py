###########################################################
#
# CSC D84 - A2 - Local search for K-medians problem
#
# In this script you will implement two methods for
# solving the K-medians problem:
#
# 1) Simple local search
#
# 2) Local search with deterministic annealing
#
# Your code will be called by Kmedians_core_GL to
# solve particular instances of the problem, so you
# should not add any tester functions here.
#
# You have access to the following global data (all
# prefixed by 'Kmedians_global_data.' )
#
# all_points      - List of [x,y] point coordinates
# current_medians - List of [x,y] with current medians
# N               - Number of points
# K               - Number of medians
# Temperature	  - Temperature for deterministic annealing
# Decay           - Decay factor for deterministic annealing
#
# Use the global 'current_cost' function to return the cost 
# of a potential solution, e.g.
#
#	Kmedians_global_data.current_cost(guess)
#	will return the cost of 'guess' where guess is
#       a lst of tuples containing a potential solution
#
# Sorry, that's bad style, but I claim poetic license!
# 
# Do not add any additional global data.
#
# Starter code: F.J.E. Dec. 2012
##########################################################

import Kmedians_global_data
import random
import math

def local_search():
	# This function carries out a local search to improve
	# the current guess. You can only examine *ONE* possible
	# update to the current solution per call. That is, at
	# most one of the current medians should change from
	# call to call. Note that this procedure is greedy
	# and will only update the current solution if its
	# new guess yields a better cost

	####################################################
        ## 
        ## TO DO: Complete this function to perform simple
        ##        local search for better solutions to the
        ##        K-medians problem.
        ##
        ##        Make sure your code updates the global
        ##        'current_medians' list!
        ####################################################

        point =random.randint(0, Kmedians_global_data.N-1)
        median = random.randint(0, Kmedians_global_data.K-1)
        temp_medians = list(Kmedians_global_data.current_medians)

        temp_medians.pop(median)
        temp_medians.append(Kmedians_global_data.all_points[point])
        
        if Kmedians_global_data.current_cost(temp_medians) < Kmedians_global_data.current_cost(Kmedians_global_data.current_medians):
                Kmedians_global_data.current_medians = temp_medians  
                print Kmedians_global_data.current_cost(temp_medians)
	return 

def deterministic_annealing():
	# This function carries out a local search using the
	# deterministic annealing method as discussed in lecture.
	# The 'temperature' is set by the initKmedians function.
        # Each call to this function will try a new solution
        # and accept it under the conditions specified by the
        # deterministic annealing method.
        # Also, each call to this function will update the
	# temperature as T=T*D, where D<1.0 is a decay factor that
	# controls how quickly the temperature decreases.
        # Both the temperature and decay factor are global
        # variables.
 
	# Each call to this function can examine only *ONE* 
	# guess at the solution.

	####################################################
        ## 
        ## TO DO: Complete this function to perform 
        ##        local search with deterministic annealing.
        ##
        ##        Make sure your code updates the global
        ##        'current_medians' list!
        ####################################################

        point =random.randint(0, Kmedians_global_data.N-1)
        median = random.randint(0, Kmedians_global_data.K-1)
        temp_medians = list(Kmedians_global_data.current_medians)

        temp_medians.pop(median)
        temp_medians.append(Kmedians_global_data.all_points[point])
        
        if Kmedians_global_data.current_cost(temp_medians) < Kmedians_global_data.current_cost(Kmedians_global_data.current_medians):
                Kmedians_global_data.current_medians = temp_medians  
                print Kmedians_global_data.current_cost(temp_medians)
        else:
                # get the probability
                cost_diff = abs(Kmedians_global_data.current_cost(temp_medians) - Kmedians_global_data.current_cost(Kmedians_global_data.current_medians))
                probability =  math.exp(-cost_diff/Kmedians_global_data.Temperature)        
                # generate a random float between 0 and 1 
                rand_float = random.random()

                if probability > rand_float:
                        Kmedians_global_data.current_medians = temp_medians  
                        print Kmedians_global_data.current_cost(temp_medians)
        Kmedians_global_data.Temperature = Kmedians_global_data.Temperature*Kmedians_global_data.Decay
	return
