#!/usr/bin/env python
# coding=utf-8
"""
@author: Jiawei Wu
@create time: 2019-12-06 23:15
@edit time: 2021-01-25 14:30
@desc: envs的init文件
"""


from gym.envs.registration import register
register(
    id='FindTreasure-v0',
    entry_point='rl4net.envs.findtreasure_env:FindTreasureEnv',
)
register(
    id='Maze-v0',
    entry_point='rl4net.envs.maze_env:MazeEnv',
)
register(
    id='PC-v0',
    entry_point='rl4net.envs.PC_env:radio_environment',
)
register(
    id='PA-v0',
    entry_point='rl4net.envs.power_allocation.pa_env:PAEnv',
)
register(
    id='PA-v1',
    entry_point='rl4net.envs.power_allocation.pa_rb_env:PAEnv',
)