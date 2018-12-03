"""
Simulating the probability of the estimated fines on the I-880 freeway
that the single occupancy vehicles will have to pay.
"""

from random import choice, randint, choices
import random
from collections import Counter, defaultdict
import typing
import numpy as np
import pandas as pd
from numpy import random
#import matplotlib.pyplot as plt

class Lanes:

    def init(self):
        self.num_sov = 0
        self.num_hov = 0
        self.weather=''
        self.weather_int=0
        self.accident=''
        self.accident_intensity=int
        #self.k=k

    def rand_gen_WinterRains(self,low, likely, high, confidence=4, samples=10):
        """Produce random numbers according to the 'Modified PERT'
        distribution.

        :param low: The lowest value expected as possible.
        :param likely: The 'most likely' value, statistically, the mode.
        :param high: The highest value expected as possible.
        :param confidence: This is typically called 'lambda' in literature
                            about the Modified PERT distribution. The value
                            4 here matches the standard PERT curve. Higher
                            values indicate higher confidence in the mode.
                            Currently allows values 1-18

        Formulas from "Modified Pert Simulation" by Paulo Buchsbaum.
        """

        mean = (low + confidence * likely + high) / (confidence + 2.0)

        a = (mean - low) / (high - low) * (confidence + 2)
        b = ((confidence + 1) * high - low - confidence * likely) / (high - low)

        weather_int = np.random.beta(a, b, samples)
        weather_int = weather_int * (high - low) + low
        return weather_int

    def fn_weather_int(self):
        df['weather'] = choices(['Summer', 'Winter', 'Rains'], [0.5, 0.3, 0.2], k=100)
        weather_int_list=[]

        for season in df['weather']:
            if season == 'Summer':
                weather_int=0

            elif season == 'Winter':
                weather_int= np.median(self.rand_gen_WinterRains(10, 4, 2, samples=10))

            else:
                weather_int= np.median(self.rand_gen_WinterRains(10, 5, 2, samples=10))
            weather_int_list.append(round(weather_int, 2))
            df['weather_int'] = pd.DataFrame(weather_int_list)

        return weather_int_list

    def fn_accident_int(self):
        df['accident'] = choices(['Yes', 'No'], [0.4, 0.6], k=100)
        accident_int_list = []

        for value in df['accident']:
            if value == 'No':
                accident_int=0
            else:
                accident_int= np.median(self.rand_gen_WinterRains(10, 4, 2, samples=10))
            accident_int_list.append(round(accident_int, 2))
            df['accident_int'] = pd.DataFrame(accident_int_list)

        return accident_int_list

    def compute_AvgSpeed(self, df):
        speed_list = []
        time_list = []
        #for i in random_dict.keys():

        #df['speed'] = np.where(df['accident_int'] in range(7, 11),'yes','no')

        #indiv[(indiv['CITY'] == 'CHAMPAIGN') & (indiv['STATE'] == 'IL')]

        #print(df[(df['weather'] == 'Winter') & (df['weather_int'] >5)])

        #print(df[df.weather == 'Winter'])
        #print(type(df['accident_int']))

        df['speed'] = np.where(((df['weather'] == 'Winter') & (df['weather_int'] > 3) & (df['accident_int'] > 3)) |
                               ((df['weather'] == 'Rains') & (df['weather_int'] > 3) & (df['accident_int'] > 3)),
                               (df['accident_int'] * df['weather_int']) / 2, randint(25, 30))

        return df

    def fn_vehicles(self, df):
        df['peak_hour'] = choices(['Yes', 'No'], [0.5, 0.5], k=100)

        hov_list = []
        sov_list = []
        fuel_eff_list = []
        fuel_eff_reg_list = []
        fuel_eff_non_reg_list = []
        for i in df['peak_hour']:
            if i == 'Yes':
                hov_vehicles = round(np.median(self.rand_gen_WinterRains(2000, 1740, 1600, samples=10)), 0)
                sov_vehicles = round(np.median(self.rand_gen_WinterRains(300, 200, 150, samples=10)), 0)
            else:
                hov_vehicles = round(np.median(self.rand_gen_WinterRains(1800, 1540, 1400, samples=10)), 0)
                sov_vehicles = round(np.median(self.rand_gen_WinterRains(200, 100, 50, samples=10)), 0)
            fuel_eff_vehicles = 0.2 * sov_vehicles
            reg_fuel_eff = 0.7 * fuel_eff_vehicles
            non_reg_fuel_eff = 0.3 * fuel_eff_vehicles
            hov_list.append(hov_vehicles)
            sov_list.append(sov_vehicles)
            fuel_eff_list.append(round(fuel_eff_vehicles,0))
            fuel_eff_reg_list.append(round(reg_fuel_eff,0))
            fuel_eff_non_reg_list.append(round(non_reg_fuel_eff,0))
        df['hov'] = pd.DataFrame(hov_list)
        df['sov'] = pd.DataFrame(sov_list)
        df['fuel_efficient_cars'] = pd.DataFrame(fuel_eff_list)
        df['reg_fuel_eff'] = pd.DataFrame(fuel_eff_reg_list)
        df['non_reg_fuel_eff'] = pd.DataFrame(fuel_eff_non_reg_list)

        return df

    def fn_fine(self, df):
        df['fine'] = (df['sov'] - df['reg_fuel_eff']) * 450 * 4

        return df

    #
    # def random_gen(self):
    #     random_dict = {}
    #     for i in range(10):
    #         self.num_sov = randint(0, 300)
    #         #print('Number of single occupant vehicles per hour: ', num_sov)
    #
    #         self.num_hov = randint(1500, 1800)
    #         #print('Number of high occupant vehicles per hour: ', num_hov)
    #
    #         self.accident = choice([True, False])        #unpredictable variable
    #         if self.accident == True:
    #             self.accident_intensity = randint(1, 10)
    #         else:
    #             self.accident_intensity = 0
    #         #print('intensity of an accident occurred: ',accident_intensity)
    #
    #         self.weather = choice(['Summer', 'Winter', 'Rains'])
    #         if self.weather == 'Winter' or self.weather== 'Rains':
    #             self.weather_int = randint(1,10)
    #         else:
    #             self.weather_int = 0
    #         #print('Season:' , weather, ', Weather intensity: ', weather_int)
    #
    #
    #         random_dict[i]=[]
    #         # random_dict[key].append(num_sov)
    #         # random_dict[key].append(num_hov)
    #         # random_dict[key].append(accident_intensity)
    #         # random_dict[key].append(weather)
    #         # random_dict[key].append(weather_int)
    #         random_dict[i] = [self.num_sov, self.num_hov, self.accident_intensity, self.weather, self.weather_int]
    #         print(self.compute_AvgSpeed())
    #         p = plt.hist(self.mod_pert_random(self, 10, 4, 2, confidence=4, samples=10000),
    #                      bins=500,
    #                      density=False)
    #         #plt.show()
    #         #print(self.mod_pert_random(10, 4, 2, 4, samples=10000))
    #         #print(speed)
    #     return random_dict
    #
    #
    # def compute_AvgSpeed(self) -> int:
    #     speed_list = []
    #     time_list = []
    #     #for i in random_dict.keys():
    #
    #     if self.weather == 'Winter':
    #         if self.accident_intensity in range(7, 11) and self.weather_int in range(7, 11):
    #             speed = (self.accident_intensity + self.weather_int) / 2
    #             time = distance/speed
    #         else:
    #             speed = randint(25, 30)
    #             time = distance/speed
    #
    #     elif self.weather == 'Rains':
    #         if self.accident_intensity in range(7, 11) and self.weather_int in range(7, 11):
    #             speed = (self.accident_intensity * self.weather_int) / 7
    #             time = distance/speed
    #         else:
    #             speed = randint(25, 30)
    #             time = distance/speed
    #     else:
    #         if self.accident_intensity in range(7, 11) and self.weather_int in range(7, 11):
    #             speed = (self.accident_intensity * self.weather_int) / 5
    #             time = distance/speed
    #         else:
    #             speed = randint(25, 30)
    #             time = distance/speed
    #
    #     speed_list.append(speed)
    #     time_list.append(round(time,2))
    #     return speed, time
    #

if __name__ == '__main__':
    #k = input('Enter the number of simulations: ')
    df = pd.DataFrame(columns=['peak_hour', 'hov', 'sov', 'fuel_efficient_cars', 'reg_fuel_eff', 'non_reg_fuel_eff',
                               'weather', 'weather_int', 'accident', 'accident_int', 'speed', 'fine', 'accident_fine'])
    my_lane = Lanes()
    #df = my_lane.fn_vehicles(df)
    weather_int_list = my_lane.fn_weather_int()
    #print(weather_int_list)
    accident_int_list = my_lane.fn_accident_int()
    #print(accident_int_list)
    df = my_lane.compute_AvgSpeed(df)
    df = my_lane.fn_vehicles(df)
    df = my_lane.fn_fine(df)
    print(df)
    df.to_csv('HOV.csv')