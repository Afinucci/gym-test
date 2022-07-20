import gym
from gym import error, spaces, utils
import numpy as np
from gym.utils import seeding

class walk1DEnv(gym.Env):
  """
  Custom Environment that follows gym interface.
  This is a simple env where the agent must learn to go always left. 
  """
  # Because of google colab, we cannot implement the GUI ('human' render mode)
  metadata = {'render.modes': ['console']}
  # Define constants for clearer code
  LEFT = 0
  RIGHT = 1

  def __init__(self, grid_size=5):
    # Size of the 1D-grid
    self.grid_size = grid_size
    # Initialize the agent at the middle of the grid. Please change the number 2 hereafter if the size of the grid changes!
    self.agent_pos = grid_size - 2

    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions, we have two: left and right
    n_actions = 2
    self.action_space = spaces.Discrete(n_actions)
    # The observation will be the coordinate of the agent
    # this can be described both by Discrete and Box space
    self.observation_space = spaces.Box(low=0, high=self.grid_size,
                                        shape=(1,), dtype=np.float32)
  def reset(self):
    """
    Important: the observation must be a numpy array
    :return: (np.array) 
    """
    # Initialize the agent at the right of the grid
    self.agent_pos = self.grid_size - 2
    # here we convert to float32 to make it more general (in case we want to use continuous actions)
    return np.array([self.agent_pos]).astype(np.float32)
  
  def step(self, action):
    if action == self.LEFT:
      self.agent_pos -= 1
    elif action == self.RIGHT:
      self.agent_pos += 1
    else:
      raise ValueError("Received invalid action={} which is not part of the action space".format(action))

    # Account for the boundaries of the grid
    self.agent_pos = np.clip(self.agent_pos, 0, self.grid_size)

    # Are we at the right of the grid?
    done = bool(self.agent_pos == self.grid_size)

    # Null reward everywhere except when reaching the goal (left of the grid)
    reward = 1 if self.agent_pos == self.grid_size else 0

    # Optionally we can pass additional info, we are not using that for now
    info = {}

    return np.array([self.agent_pos]).astype(np.float32), reward, done, info
  
  def step(self, action):
    
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
    state = 2 # the state represent also the index of the vector that in turn is the environment
    return state
  def render(self, mode='human', close=False):
    environment = np.zeros(5,)
    environment[state] = reward
    return environment
