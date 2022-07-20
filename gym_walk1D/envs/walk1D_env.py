import gym
from gym import error, spaces, utils
import numpy as np
from gym.utils import seeding

class walk1DEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.action_space = spaces.Discrete(3) # Right=1; Left=-1; Do Nothing=0
    self.observation_space = np.array([-1,-1,0,1,1])  # Environment: (-1,-1,0,1,1)
  
  def step(self, action):
    # remember that the state is the index of the vector
    if action == 2: #moving right
      self.state += 1
      reward = observation_space[state]
    elif action == 1: # moving left
      self.state += -1
      reward = observation_space[state]
    elif action == 0: # not moving
      self.state += 0
      reward = observation_space[state]
    
    if reward == 2:
      done = True
      info = {}
    elif reward == -1:
      done = True
      info = {}
    return state, reward, done, info
  def reset(self):
    self.state = 2 # the state represent also the index of the vector that in turn is the environment
    return state
  def render(self, mode='human', close=False):
    environment = np.zeros(5,)
    environment[state] = reward
    return environment
