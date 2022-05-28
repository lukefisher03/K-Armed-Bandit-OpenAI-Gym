'''
Sample k-armed bandit problem environment. To be used with stable-baselines3

There are 10 actions represented as levers with different reward values. The
agent's job is to maximize it's reward by avoiding levers that subtract the total
reward. 
'''
import gym
from gym import spaces
import numpy as np


#the position of each reward value indicates the respective lever.

REWARDS = [-3,3,-2,1,5,-2,4,-1,1,5]


class CustomEnv(gym.Env):
    metadata = {
        'render.modes' : ['human']
    }

    def __init__(self) -> None:
        super(CustomEnv, self).__init__()

        self.total_steps = 0
        self.total_reward = 0
        self.map = [0 for _ in range(10)]
        #https://www.gymlibrary.ml/content/spaces/?highlight=discrete#discrete
        #Define 3 possible actions
        '''
        States of each individual lever are either on/off.

        Action-Space: MultiDiscrete[2,11]. There are 10 levers[0-9] and two options [0,1].

        Observation space: list of lever states -> [0,0,0,1,0,1,1,0,1,0]

        Rewards: Each lever has a reward number ranging from -5 to +5. These values
        remain static throughout all of the training.
        The agent must modify it's policy for maximum rewards.
        '''
        self.action_space = spaces.MultiDiscrete([10,2])
        #There are 10 levers and their respective on/off states will be returned to the agent as the observation.
        self.observation_space = spaces.MultiDiscrete([2 for _ in range(10)])
        self.reward_range = (-5,5)
    def _get_obs(self) -> spaces.MultiDiscrete:
        return self.map

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
        #reset the total steps variable

        info = {
            "total_reward":self.total_reward
        }

        self.total_steps = 0
        self.total_reward = 0
        self.map = [0 for _ in range(10)]
        observation = self._get_obs()

        return observation


    def render(self, mode='human') -> None:
        print(f'{self.map}')
        print(f'Total Reward: {self.total_reward}')
        print(f'Total Steps: {self.total_steps}')
    
    def close(self) -> None:
        print("Closing the environment...")



        