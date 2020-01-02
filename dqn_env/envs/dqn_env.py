import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class DQNEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  
  def __init__(self, reward_f):
    self.reward_f = reward_f
    self.color_size = 2
    self.reset()
    
  def step(self, action):
    self.image[self.position] = action
    
  def reset(self):
    self.image = np.random.randn(28, 28, 1)
    self.position = np.array([0, 0])
    
  def render(self, mode='human', close=False):
    pass
