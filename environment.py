

from typing import List
import numpy
from collections.abc import Callable
from collections.abc import Sequence
import copy 
from numpy.core.records import array
import hashlib
import agent
from matplotlib import pyplot as plt


class Environment():
    matrix = numpy.array
    def __init__(self,width, height, obstacles: List[List[int]]):#, obstacles: Sequence[Sequence[int]]):
        self.matrix = numpy.zeros((width,height))
        self.hash_matrix = copy.deepcopy(self.matrix)
        self.width = width
        self.height = height
        self.obstacles = obstacles

        #create obstacles
        for obstacle_pos in obstacles:
           self.matrix[obstacle_pos[0], obstacle_pos[1]] = int(1)


        #create a hash matrix of matrix coordinate
        for row in range(0,self.matrix.shape[0]):
            for col in range(0, self.matrix.shape[1]):
                self.hash_matrix[row, col] = abs(hash(str([row, col]))) % (10 ** 8)
        
    def get_matrix_dimension(self):
        return [self.width, self.height]

    def get_environment_matrix(self):
        return self.matrix

    def get_environment_hash_matrix(self):
        return self.hash_matrix

    def print_environment_hash_matrix(self): 
        print("\n",self.hash_matrix,"hash_matrix\n")

    def get_obstacles(self):
        l = self.obstacles
        xs = [x[0] for x in l]
        ys = [y[1] for y in l] 
        return xs, ys
    
    def get_free(self):
        x_coord, y_coord = numpy.where(self.get_environment_matrix()[:,:] == 0)
        return x_coord, y_coord

    def print_environment(self):
        print("\n",self.get_environment_matrix(),"env matrix\n")
    ####
    #
    #   draw obstacle map
    #   input: 
    #       env: enviroment matrix (NOT HASH MATRIX)
    #       agent: agent
    #   output:
    #       plt: plot
    ####
    def draw_map(self, agent: agent.Agent):
        ox = self.get_obstacles()[0]
        oy = self.get_obstacles()[1]
        fx = self.get_free()[0]
        fy = self.get_free()[1]

        data = self.get_environment_hash_matrix()[::-1]
        fig = plt.figure()
        plt.figure(figsize=(self.get_matrix_dimension()[0], self.get_matrix_dimension()[1]))
        plt.xlabel('Y Axis', fontsize=18)
        plt.ylabel('X Axis', fontsize=18)


        plt.xlim(-1, data.shape[1])
        plt.ylim(-1, data.shape[0])
        plt.xticks(numpy.arange(0,data.shape[1],1))
        plt.yticks(numpy.arange(0,data.shape[0],1))
        plt.grid(True)
        plt.scatter(fy, fx, s=300, c='cyan', marker='s')  
        plt.scatter(oy, ox, s=300, c='gray', marker='s')
        plt.scatter(agent.get_initial_state()[1], agent.get_initial_state()[0], s=300, c='red', marker='s')
        plt.scatter(agent.get_goal_state()[1], agent.get_goal_state()[0], s=300, c='yellow', marker='s')
        return plt



