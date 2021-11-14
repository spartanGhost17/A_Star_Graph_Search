import queue
from typing import *

class Agent():
    moves_list = []
    initial_state = []
    goal_state = []

    def __init__(self, initial_state: List[int], goal_state: List[int], motion_cost: List[int]):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.motion_cost = motion_cost #[Up_cost, Down_cost, Left_cost, Right_cost]

    def get_motion_cost(self):
        return self.motion_cost  

    def get_initial_state_hash(self):
        return abs(hash(str(self.initial_state))) % (10 ** 8)

    def get_goal_state_hash(self):
        return abs(hash(str(self.goal_state))) % (10 ** 8)

    def get_initial_state(self):
        return self.initial_state

    def get_goal_state(self):
        return self.goal_state
        
    def update_moves_list(self, moves):      
        self.moves_list = moves

    def get_moves_list(self):
        return self.moves_list
#ag = Agent([0,0], [4,3], [1,1,1,1])
#print(" list szr ", ag.get_moves_list(), ag.goal_state)