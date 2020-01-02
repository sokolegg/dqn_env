import gym
from gym import error, spaces, utils
from gym.utils import seeding

class DQNEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  
  def __init__(self, reward_f):
    self.reward_f = reward_f
    
  def step(self, action):
    pass
    
  def reset(self):
    pass
    
  def render(self, mode='human', close=False):
    pass
