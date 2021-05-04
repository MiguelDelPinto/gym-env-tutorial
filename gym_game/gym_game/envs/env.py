import gym
from gym import error, spaces, utils
from gym.utils import seeding

class ExampleEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    ...


  def step(self, action):
    """Run one timestep of the environment's dynamics. When end of episode is reached, you are responsible for calling 
    'reset()' to reset this environment's state.

    Accepts an action and returns a tuple (observation, reward, done, info).

    Arguments:
        action (object): an action provided by the agent

    Returns:
        observation (object): agent's observation of the current environment
        reward (float) : amount of reward returned after previous action
        done (bool): whether the episode has ended, in which case further step() calls will return undefined results
        info (dict): contains auxiliary diagnostic information (helpful for debugging, and sometimes learning)
    """
    ...

  def reset(self):
    """Resets the environment to an initial state and returns an initial observation.

    Note that this function should not reset the environment's random number generator(s); random variables in the 
    environment's state should be sampled independently between multiple calls to `reset()`. In other words, each 
    call of 'reset()' should yield an environment suitable for a new episode, independent of previous episodes.

    Returns:
        observation (object): the initial observation.
    """
    ...

  def render(self, mode='human'):
    """Renders the environment.

    The set of supported modes varies per environment. (And some environments do not support rendering at all.) 
    By convention, if mode is:

    - human: render to the current display or terminal and return nothing. Usually for human consumption.
    - rgb_array: Return an numpy.ndarray with shape (x, y, 3), representing RGB values for an x-by-y pixel image, 
      suitable for turning into a video.
    - ansi: Return a string (str) or StringIO.StringIO containing a terminal-style text representation. The text 
    can include newlines and ANSI escape sequences (e.g. for colors).

    Note:
        Make sure that your class's metadata 'render.modes' key includes the list of supported modes. It's recommended 
        to call super() in implementations to use the functionality of this method.

    Args:
        mode (str): the mode to render with

    Example:

    class MyEnv(Env):
        metadata = {'render.modes': ['human', 'rgb_array']}

        def render(self, mode='human'):
            if mode == 'rgb_array':
                return np.array(...) # return RGB frame suitable for video
            elif mode == 'human':
                ... # pop up a window and render
            else:
                super(MyEnv, self).render(mode=mode) # just raise an exception
    """
    ...

  def close(self):
    """Performs any necessary cleanup.

    Environments will automatically close() themselves when
    garbage collected or when the program exits.
    """
    ...