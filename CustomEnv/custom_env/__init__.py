from gym.envs.registration import register

register(
    id='CustomEnv-v0',
    entry_point='CustomEnv.custom_env:CustomEnv',
    max_episode_steps=11
)