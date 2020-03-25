import gym
from itertools import count
from collections import deque

from utils import SimpleMemory, preprocess, StatRecorder


env = gym.make('Breakout-v0')
obs = env.reset()

total_steps = 1e3
n_frames = 3

memory = SimpleMemory()
stats = StatRecorder

def get_start_frames(n):
    frames = deque(maxlen=n)
    for i in range(n):
        obs, reward, done, info = env.step(1)
        frames.append(preprocess(obs))
    return frames


frames = get_start_frames()
current_rewards = 0.0
current_timesteps = 0

for step in count(1):
    if step < total_steps:
        break
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)

    current_state = list(frames)
    frames.append(preprocess(obs))
    if not done:
        next_state = list(frames)
    else:
        next_state = None
    
    memory.append(current_state, action, next_state, reward)

    current_rewards += reward
    current_timesteps += 1

    if done:
        stats.rewards.append(current_rewards)
        stats.timesteps.append(current_timesteps)
        env.reset()
        frames = get_start_frames()
    
print(step)
print('Done')







