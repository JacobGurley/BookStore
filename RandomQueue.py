import numpy as np
import random 
from ArrayQueue import ArrayQueue

class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)
            

    def remove(self) -> np.object :
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # todo
        if self.n == 0:
            raise IndexError("RandomQueue is empty")
        rand = random.randint(0, self.n - 1)
        #This will switch the first number (j) with a random number
        print(rand)
        self.a[(self.j + rand) % len(self.a)], self.a[self.j] = self.a[self.j], self.a[(self.j + rand) % len(self.a)]
        return super().remove()
     




