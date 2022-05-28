import gym
from CustomEnv.custom_env.custom_env import CustomEnv
from stable_baselines3 import PPO

env = gym.make('CustomEnv-v0')

model = PPO('MlpPolicy', env, verbose=True)
model.learn(total_timesteps=50000)

obs = env.reset()

epis = 1
for epi in range(epis):
    done = False
    while not done:
        action, _state = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        env.render()

        if done:
            print('DONE')
            break
    obs = env.reset()

env.close()