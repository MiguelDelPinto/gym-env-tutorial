# OpenAIGym Tutorial: Creating new environments

This tutorial contains the steps that can be performed to start a new OpenAIGym project, and to create a new environment.

## Steps

1. Create a new repository (in this example, the name is `gym_game`).

2. Setup the project's folder structure like so:
  ```sh
  gym_game/
    setup.py
    gym_game/
      __init__.py
      envs/
        __init__.py
        env.py
  ```

3. `gym_game/setup.py` should have:

  ```python
  from setuptools import setup

  setup(name='gym_game',
        version='0.0.1',
        install_requires=['gym'] # And any other dependencies needed
  )
  ```
The `setuptools` package helps to build and install Python packages, which will be useful further ahead. The `name` and `version` arguments denote the name and version of your package, and the `install_requires` parameter is an array that should contain all Python libraries that your program depends on.

4. `gym_game/gym_game/__init__.py` should have:
  ```python
  from gym.envs.registration import register

  register(
      id='game-env-v0',
      entry_point='gym_game.envs:ExampleEnv',
  )
  ```

By calling the `register()` function, you can load your environment, and thus make it available to be called by `gym.make()`. The `entry_point` argument should have the path to your environment class, following that notation.

5. `gym_game/gym_game/envs/__init__.py` should have:
  ```python
  from gym_game.envs.env import ExampleEnv
  ```

This imports `ExampleEnv`, the class that implements your custom environment.

6. `gym_game/gym_game/envs/env.py` should look something like:
  ```python
  import gym
  from gym import error, spaces, utils
  from gym.utils import seeding

  class ExampleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
      ...
    def step(self, action):
      ...
    def reset(self):
      ...
    def render(self, mode='human'):
      ...
    def close(self):
  ```

The `ExampleEnv` class extends `gym.Env`, the generic OpenAIGym environment class. The metadata attribute describes some additional information about a gym environment/class that is not needed during training but is useful when performing things like Python tests, for example.

The class should override the 4 following methods:

#### `step()`
Function that performs a certain action (given by the parameter `action`). The method should return 4 values, in this order:

* `observation` **(object)**: an environment-specific object representing your observation of the environment. For example, the board state in a board game.
* `reward` **(float)**: amount of reward achieved by the previous action. The scale varies between environments, but the goal is always to increase your total reward.
* `done` **(boolean)**: whether it’s time to reset the environment again. Most (but not all) tasks are divided up into well-defined episodes, and done being True indicates the episode has terminated. (For example, perhaps the pole tipped too far, or you lost your last life.)
* `info` **(dict)**: diagnostic information useful for debugging. It can sometimes be useful for learning (for example, it might contain the raw probabilities behind the environment’s last state change). However, official evaluations of your agent are not allowed to use this for learning.

#### `reset()`
Function that resets the environment and should be called when an episode ends (i.e. when the `done` return value from the `step()` function is `True`).

#### `render()`
Function that renders onto the screen or console the current state of the environment. The `mode` parameter's use is to know if the render should be human-friendly or not.

#### `close()`
Method that is called to cleanup and shut down the environment.

Inside the [`env.py`](https://github.com/MiguelDelPinto/gym-env-tutorial/blob/main/gym_game/gym_game/envs/env.py) file you can find more information about these methods.

7. After you have installed your package with `pip install -e gym_game`, you can create an instance of the environment with `gym.make('gym_game:game-env-v0')`.

## Helpful Links and Resources

Here are some concrete examples of environment implementations:
* [gym-soccer](https://github.com/openai/gym-soccer) - Official OpenAI repository, that implements soccer-based reinforcement learning tasks, in which the agent needs to score goals. Uses various environments (one with a goalkeeper, one without, etc).
* [gym-tictactoe](https://github.com/haje01/gym-tictactoe) - Simple concrete example, that has a TicTacToe environment.

You should also check out the [official OpenAIGym docs](https://gym.openai.com/docs/), that go over this whole process, in some parts with a bit more detail.
