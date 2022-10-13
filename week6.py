# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:57:33 2022

@author: lukeg
"""

import math
import time

def test_timing(state):
    start = time.time()
    output = minimax_value(state)
    end = time.time()
    
    print("Example play: " + str(output[1]) + "\nTime taken: " +  str(end-start) + "\nWinner: " + str((output[0])[0]))

def minimax_value(state):
    game_state = state[0]
    player_turn = state[1]
    if player_turn == 1:
        final = maxValue(game_state, -math.inf, math.inf)
    if player_turn == 2:
        final = minValue(game_state, -math.inf, math.inf)
        
    temp = final[0]
    bestpath = list([])
    for i in range(len(final[1])):     
        if temp == 1:
            temp2 = (final[1])[i]
            temp2 = (temp2,1)
            bestpath.append(temp2)
            temp = 0
        else:
            temp2 = (final[1])[i]
            temp2 = (temp2,2)
            bestpath.append(temp2)
            temp = 1
            
    bestpath.append(state)
    bestpath.reverse()
    return final, bestpath 
        
def maxValue(state, alpha, beta):
    if state == []:
        path = []
        return 1, path
    else:
        maxeval = -math.inf
        piles = nextState(state)
        for pile in piles:
            v, path = minValue(pile, alpha, beta)
            if v > maxeval:
                maxeval = v
                bestpath = path
                bestsuccessor = pile
                if v >= beta:
                    return maxeval, bestpath
            if v > alpha:
                alpha = maxeval
        bestpath.append(bestsuccessor)
        return maxeval, bestpath
            
def minValue(state, alpha, beta):
    if state == []:
        path = []
        return -1, path
    else:
        mineval = math.inf
        piles = nextState(state)
        for pile in piles:
            v, path = maxValue(pile, alpha, beta)
            if v < mineval:
                mineval = v
                bestpath = path
                bestsuccessor = pile
                if v <= alpha:
                    return mineval, bestpath
            if v < beta:
                beta = v
        bestpath.append(bestsuccessor)
        return mineval, bestpath
            
        
def nextState(game_state):
    templist = list([])
    for i in range(len(game_state)):
        for j in range(3):
            temp = list(game_state)
            temp[i] -=j+1
            if temp[i] == 0:
                temp.pop(i)
                templist.append(list(temp))
                break
            else:
                templist.append(list(temp))           
    return templist

test_timing(([5,5,5],1))