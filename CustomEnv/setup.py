from setuptools import setup
import stable_baselines3

setup(
    name='CustomEnv',
    version='0.0.1',
    #Note: at this moment in time sb3 requires this version of gym. Other versions seem to also work, but you may get an error
    install_requires=['gym==0.21']
)