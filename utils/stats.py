import numpy as np


class StatRecorder:
    def __init__(self):
        self.rewards = []
        self.timesteps = []
        self.losses = []
    
    def reset(self):
        del self.rewards[:]
        del self.timesteps[:]
        del self.losses[:]

    def printStats(self):
        mean_reward = np.mean(self.rewards)
        mean_timestamp = np.mean(self.timesteps)
        mean_losses = np.mean(self.losses)
        print('Mean Rewards: {:.03f}'.format(mean_reward))
        print('Mean Timesteps: {:.03f}'.format(mean_timestamp))
        print('Mean Losses: {:.03f}'.format(mean_losses))
