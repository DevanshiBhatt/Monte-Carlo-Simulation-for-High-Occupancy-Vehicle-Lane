"""
Simulating the probability of the estimated fines on the I-880 freeway
that the single occupancy vehicles will have to pay.
"""

from random import choice, randint
from collections import Counter, defaultdict
import typing

distance=400

class Lane:
    def _init_(self):
        self.num_sov=0
        self.num_hov=0
        self.weather=''
        self.weather_int=0
        self.accident=''
        self.accident_intensity=int

    def random_gen(self):
        random_dict = {}
        for i in range(10):
            self.num_sov = randint(0, 300)
            #print('Number of single occupant vehicles per hour: ', num_sov)

            self.num_hov = randint(1500, 1800)
            #print('Number of high occupant vehicles per hour: ', num_hov)

            self.accident = choice([True, False])        #unpredictable variable
            if self.accident == True:
                self.accident_intensity = randint(1, 10)
            else:
                self.accident_intensity = 0
            #print('intensity of an accident occurred: ',accident_intensity)

            self.weather = choice(['Summer', 'Winter', 'Rains'])
            if self.weather == 'Winter' or self.weather== 'Rains':
                self.weather_int = randint(1,10)
            else:
                self.weather_int = 0
            #print('Season:' , weather, ', Weather intensity: ', weather_int)


            random_dict[i]=[]
            # random_dict[key].append(num_sov)
            # random_dict[key].append(num_hov)
            # random_dict[key].append(accident_intensity)
            # random_dict[key].append(weather)
            # random_dict[key].append(weather_int)
            random_dict[i] = [self.num_sov, self.num_hov, self.accident_intensity, self.weather, self.weather_int]
            print(self.compute_AvgSpeed())
            #print(speed)
        return random_dict

    def compute_AvgSpeed(self) -> int:
        speed_list = []
        time_list = []
        #for i in random_dict.keys():

        if self.weather == 'Winter':
            if self.accident_intensity in range(7, 11) and self.weather_int in range(7, 11):
                speed = (self.accident_intensity + self.weather_int) / 2
                time = distance/speed
            else:
                speed = randint(25, 30)
                time = distance/speed

        elif self.weather == 'Rains':
            if self.accident_intensity in range(7, 11) and self.weather_int in range(7, 11):
                speed = (self.accident_intensity * self.weather_int) / 7
                time = distance/speed
            else:
                speed = randint(25, 30)
                time = distance/speed
        else:
            if self.accident_intensity in range(7, 11) and self.weather_int in range(7, 11):
                speed = (self.accident_intensity * self.weather_int) / 5
                time = distance/speed
            else:
                speed = randint(25, 30)
                time = distance/speed

        speed_list.append(speed)
        time_list.append(round(time,2))
        return speed,time


if __name__ == '__main__':
    my_lane = Lane()
    my_lane.random_gen()

#print(random_dict)
#compute_AvgSpeed(random_dict)
#print()
#compute_time()
