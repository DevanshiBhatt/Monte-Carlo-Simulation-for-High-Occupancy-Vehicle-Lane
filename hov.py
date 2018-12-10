"""
Simulating the probability of the estimated fines on the I-880 freeway
that a single occupancy vehicles will have to pay.
sov ~ single occupancy vehicle
hov ~ high occupancy vehicle
"""

from random import choice, randint, choices
from collections import Counter, defaultdict
import typing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Lanes:

    def init(self):
        self.num_sov = 0
        self.num_hov = 0
        self.weather=''
        self.weather_int=0
        self.accident=''
        self.accident_intensity=int
        #self.k=100

    def rand_gen_pert(self, low, likely, high, confidence=4, samples=10):
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

        beta = np.random.beta(a, b, samples)
        beta = beta * (high - low) + low
        return beta

    def fn_weather_int(self, no_of_samples):
        """
        Using 'Modified PERT' distribution to calculate the weather intensity
        :param no_of_samples: User input
        :return: List of Weather intensity
        """
        p = no_of_samples
        df['weather'] = choices(['Summer', 'Winter', 'Rains'], [0.5, 0.3, 0.2], k=p)
        weather_int_list=[]

        for season in df['weather']:
            if season == 'Summer':
                weather_int=0

            elif season == 'Winter':
                weather_int= np.median(self.rand_gen_pert(1, 4, 10, samples=10))

            else:
                weather_int= np.median(self.rand_gen_pert(1, 5, 10, samples=10))

            weather_int_list.append(round(weather_int, 2))
            df['weather_int'] = pd.DataFrame(weather_int_list)

        return weather_int_list


    def fn_accident_int(self, no_of_samples):
        """
        Using 'Modified PERT' distribution to calculate the accident intensity
        :param no_of_samples: User input
        :return: List of Accident intensity
        """
        p = no_of_samples
        # Randomly choosing accident
        df['accident'] = choices(['Yes', 'No'], [0.4, 0.6], k=p)
        accident_int_list = []

        for value in df['accident']:
            if value == 'No':
                accident_int=0
            else:
                accident_int= np.median(self.rand_gen_pert(1, 3, 10, samples=10))
            accident_int_list.append(round(accident_int, 2))
            df['accident_int'] = pd.DataFrame(accident_int_list)

        return accident_int_list


    def compute_AvgSpeed(self, df):
        """
        Calculating speed of vehicles on the road using accident intensity and weather intensity
        :param df: Dataframe containing fields Weather, Weather_Intensity , Accident , Accident Intensity
        :return: Modified dataframe with the new speed column
        """

        df['speed'] = np.where(((df['weather'] == 'Winter') & (df['weather_int'] > 3) & (df['accident_int'] > 3)) |
                               ((df['weather'] == 'Rains') & (df['weather_int'] > 3) & (df['accident_int'] > 3)),
                               (df['accident_int'] * df['weather_int']) / 2, randint(25, 30))

        return df


    def fn_vehicles(self, df, no_of_samples):
        """
        Calculating number of SOV , HOV, hybrid(fuel efficient) SOV vehicles, registered hybrid vehicles
        using 'Modified PERT' distribution method
        :param df: Dataframe containing field peak hour
        :param no_of_samples: User input
        :return: Modified dataframe with new columns HOV, SOV, Fuel efficient Vehicles
        and Registered Fuel efficient vehicles
        """
        p = no_of_samples
        # Choosing random values for Peak Hour
        df['peak_hour'] = choices(['Yes', 'No'], [0.5, 0.5], k=p)
        hov_list, sov_list, fuel_eff_list, fuel_eff_reg_list, fuel_eff_non_reg_list = ([] for i in range(5))
        # Generating random values for number of SOV , HOV based on online statistical data
        for i in df['peak_hour']:
            if i == 'Yes':
                hov_vehicles = round(np.median(self.rand_gen_pert(1500, 1740, 2000, samples=100)), 0)
                sov_vehicles = round(np.median(self.rand_gen_pert(150, 200, 300, samples=100)), 0)
            else:
                hov_vehicles = round(np.median(self.rand_gen_pert(1400, 1540, 1800, samples=100)), 0)
                sov_vehicles = round(np.median(self.rand_gen_pert(50, 100, 200, samples=100)), 0)
            # Calculating number of  fuel efficient hybrid vehicles and registered hybrid vehicles
            fuel_eff_vehicles = 0.2 * sov_vehicles
            reg_fuel_eff = 0.7 * fuel_eff_vehicles

            hov_list.append(hov_vehicles)
            sov_list.append(sov_vehicles)
            fuel_eff_list.append(round(fuel_eff_vehicles,0))
            fuel_eff_reg_list.append(round(reg_fuel_eff,0))
        # Appending the calculated values to the Dataframe
        df['hov'] = pd.DataFrame(hov_list)
        df['sov'] = pd.DataFrame(sov_list)
        df['fuel_efficient_sov'] = pd.DataFrame(fuel_eff_list)
        df['reg_fuel_eff'] = pd.DataFrame(fuel_eff_reg_list)

        return df


    def fn_fine(self, df):
        """
        Calculation of the estimated fine SOV have to pay
        :param df: Dataframe containing fields SOV and Registered hybrid vehicles
        :return: Modified Dataframe with new column Estimate Fine
        """
        # Calculation of the estimated fine SOV have to pay
        df['estimate_fine'] = (df['sov'] - df['reg_fuel_eff']) * 450 * 4
        return df

    def fn_camera_functional(self, df, no_of_samples):
        """
        Calculating actual fine earned by the state depending on the camera functionality
        :param df: Dataframe containing fields camera_functional , SOV , Registered hybrid vehicles
        :param no_of_samples: User input
        :return: Modified dataframe with the new column Actual_fine
        """
        p = no_of_samples
        # Choosing Camera functionality randomly
        df['camera_functional'] = choices(['Yes', 'No'], [0.8, 0.2], k=p)
        # Plotting distribution of Functionality of Camera
        plt.hist(df['camera_functional'], density=False)
        plt.title('Distribution of Camera Functionality')
        df['actual_fine'] = np.where(df['camera_functional'] == 'Yes', (0.8 * (df['sov'] - df['reg_fuel_eff']) * 450 * 4),
                                     0)
        return df


if __name__ == '__main__':
    no_of_samples = int(input('Enter the number of samples: '))
    # Creating dataset using all the calculated columns
    df = pd.DataFrame(columns=['peak_hour', 'hov', 'sov', 'fuel_efficient_sov', 'reg_fuel_eff',
                               'weather', 'weather_int', 'accident', 'accident_int', 'speed', 'estimate_fine',
                               'actual_fine', 'accident_fine', 'revenue_lost_per_day'])
    my_lane = Lanes()
    weather_int_list = my_lane.fn_weather_int(no_of_samples)
    accident_int_list = my_lane.fn_accident_int(no_of_samples)

    df = my_lane.compute_AvgSpeed(df)
    df = my_lane.fn_vehicles(df, no_of_samples)
    df = my_lane.fn_fine(df)
    df = my_lane.fn_camera_functional(df, no_of_samples)
    # Calculating revenue lost by the state due to unavailability of physical patrol/ functionality issues with Camera
    df['revenue_lost_per_day'] = df['estimate_fine'] - df['actual_fine']
    df.to_csv('HOV.csv')
    # Plotting Estimated Fine , Actual Fine and Revenue lost per day in histograms
    hist1 = df.hist(column='estimate_fine', bins=10)
    plt.show()
    hist1 = df.hist(column='actual_fine', bins=10)
    plt.show()
    hist1 = df.hist(column='revenue_lost_per_day', bins=10)
    plt.show()