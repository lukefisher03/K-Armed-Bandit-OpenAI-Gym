# K-Armed-Bandit-OpenAI-Gym
A simple OpenAI gym environment for testing rapid development of reinforcement learning algs/envs. A set of levers is presented to the agent and they must decide which levers to pull and which ones to avoid. If you wish to change the number of levers then you'll need to modify reward, action, and observation spaces.

Rewards for each respective lever (*can be modified*): -3, 3, -2, 1 , 5, -2, 4, -1, 1, 5
Action Space: Which lever to pull and whether or not to pull it. ```spaces.MultiDiscrete([10,2])```

Observation Space: The list of lever states: ```spaces.MultiDiscrete([2 for _ in range(10)])```

The terminal state is only caused by taking 10 steps/actions.

## Installing the environment
While inside the local repo run:
```
pip install -e CustomEnv
```

### Using Stable-Baselines3
Being an OpenAI gym environment, you can use sb3 for rapid testing of multiple different RL algorithms. The default example uses PPO with 50,000 timesteps.

#### To-Do/Ideas
1. Entirely different reward values for turning off switches. 
2. Allow the alg to prematurely end before 10 steps.
3. GUI?
