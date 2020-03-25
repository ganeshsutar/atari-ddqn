from collections import deque
from collections import namedtuple
import random

Transition = namedtuple('Transition', ['state', 'action', 'next_state', 'reward'])

class SimpleMemory:
    def __init__(self, maxlen=1e6):
        self.capacity = maxlen
        self.memory = deque(maxlen=maxlen)
    
    def store(self, *args):
        self.memory.append(Transition(*args))
    
    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)




