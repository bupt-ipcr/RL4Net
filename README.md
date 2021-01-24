# RL4Net

RL4Net is a reinforcement learning platform based on Pytorch and OpenAI Gym.The supported interface algorithms currently include:

- Sarsa

- Qlearning

- Deep Q-Network (DQN)

- Deep Deterministic Policy Gardient (DDPG)

## Installation

**Notice:** The platform uses pytorch and numpy. It is recommended to use conda to create a new environment and install it.

RL4Net is currently hosted on PyPI. It requires Python >= 3.6.

You can simply install RL4Net from PyPI with the following command:

```python
pip install rl4net
```

You can also install with the newest version through GitHub:

```python
pip install git+https://github.com/bupt-ipcr/RL4Net.git@master
```

Or install it after downloading it locally:

```python
git clone https://github.com/bupt-ipcr/RL4Net
```

Enter folder and install it with pip:

```python
cd RL4Net
pip install .
```

After installation, run examples :

```python
python examples/ddpg.py
```

If no error occurs, you have successfully installed RL4Net.

## Documentation

Todo

## Quick Start

You can create your own reinforcement learning agent through the base class provided in `rl4net.agents`.The general method is as follows:

```python
# import base class
from rl4net.agents import xxxBase
# inherit and complete necessary methods
class myxxx(xxxBase):  
    def _build_net(self):
        pass
```

learn more about the usage, by codes examples and  annotated documentations under `examples/` .



Simple neural networks built on pytorch are also provided in `rl4net.models`. You can take it as a simple implement of DRL neural network.

```python
from rl4net.models import SimpleDQNNet
```



Third, if you want to call the attached envs, you should run  `__init__.py` to register to `gym`. After that you can use standard `gym` methods to create it.

```python
import rl4net.env  
env = gym.make('Maze-v0')
```

## Contributing

VVALB is still under development. More algorithms and features are going to be added and we always welcome contributions to help make VVLAB better. If you would like to contribute, please check out this link.

