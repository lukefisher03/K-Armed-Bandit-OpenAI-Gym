'''
This is a simple K-Armed bandit environment, as mentioned in the book titled "Reinforcement Learning" by Sutton and Barto.
The idea is simple: your agent's environment consists of k-number of levers. In this specific repo it uses 10 levers.
Each lever has a reward value associated with actuating it. The agents job is to learn which levers to pull or not pull to
maximize its returned reward.

action space: Which lever, and whether or not to pull it(not pulling doesn't yield any points). -> MultiDiscrete([2 for _ in range(10)]) 
observation space: The 10 different levers and their respective states -> MultiDiscrete([10,2])

Rewards: Each lever has an associated reward value. Defined below.
'''
import gym
from gym import spaces
import numpy as np


#the position of each reward value indicates the respective lever. These can be modified as you'd like.
REWARDS = [-3,3,-2,1,5,-2,4,-1,1,5]

#TODO: Change class name from CustomEnv to something more descriptive.
class CustomEnv(gym.Env):
    metadata = {
        'render.modes' : ['human']
    }

    def __init__(self) -> None:
        super(CustomEnv, self).__init__()

        self.total_steps = 0
        self.total_reward = 0
        self.map = [0 for _ in range(10)] #Map defines the observation space for each episode/epoch.
        self.action_space = spaces.MultiDiscrete([10,2])
        #There are 10 levers and their respective on/off states will be returned to the agent as the observation.
        self.observation_space = spaces.MultiDiscrete([2 for _ in range(10)])
        self.reward_range = (-5,5)

    def step(self, action):
        reward = 0
        index, flip = action
        #print(action)
        done = False
        self.total_steps += 1

        if flip:
            if self.map[index] == 0:
                reward = REWARDS[index]
                self.map[index] = 1
            elif self.map[index] == 1:
                self.map[index] = 0
                reward = -REWARDS[index]
                
        if self.total_steps >= 10:
            done = True

        self.total_reward += reward
        #Should I base this on total reward or each step reward?
        return self.map, reward, done, {}

    def reset(self) -> spaces.MultiDiscrete:
        self.total_steps = 0
        self.total_reward = 0
        self.map = [0 for _ in range(10)]
        observation = self.map

        return observation


    def render(self, mode='human') -> None:
        print(f'{self.map}')
        print(f'Total Reward: {self.total_reward}')
        print(f'Total Steps: {self.total_steps}')
    
    def close(self) -> None:
        print("Closing the environment...")



        