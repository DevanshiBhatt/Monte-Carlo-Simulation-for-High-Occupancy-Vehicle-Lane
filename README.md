# 590PR Final_Project

# Title: Simulations for the fines paid by Single Occupancy Vehicles on a High Occupany Vehicle Lane 

## Team Member(s): Aditya Kadrekar | Ankita Pant | Devanshi Bhatt

# Monte Carlo Simulation Scenario & Purpose:
The purpose of this simulation is to predict the fine that a Single Occupant Vehicle (SOV) will have to pay, under different circumstances, when it enters the High Occupant Vehicle  (HOV) lane. There is an assumption that single occupied vehicles take the HOV lanes (we are randomizing the number of SOV on the HOV lanes based on historical data). For comparison basis, we are also calculating the speed and time taken by high occupancy vehicles & general purpose vehicles (GPV) to cover the same distance. We will also predict the probability of faster/slower highway trips for express transit services like Bus Rapid Transit (BRT) or any high occupancy vehicle. The amount of revenue that the state will earn or lose in a day from the collection of fines is also simulated.

## Simulation's variables of uncertainty
There are the variables which are getting randomly generated - accident, no_of_accidents, weather, weather_intensity, camera_functionality, no of HOV vehicles, no of SOV vehicles, no of general purpose vehicles (GPV), hov_speed and gpv_speed. 

## accident:
Since accidents are very frequent on highways, we are using a boolean value to determine the frequency where True would mean accident has occured and False would mean accident hasn't occured.

## no_of_accidents:
When the accident occurs (i.e when True) it generates a pert distribution from the range 1-10 indicating the number of accidents and when accident doesn't occer (i.e when False) it returns 0.

## weather & weather_intensity:
We are considering three seasons i.e Winter, Rain and Summer. We are assuming that even in extreme summers it doesn't affect the traffic. Therefore, the weather intensity during summers is 0. But for winters and rainy season, we understand that extreme winters and rains can affect the traffic. Thus, for winter and rains we generate a random value from the range 1-10 indicating the intensity of the snow/rain.

## peak_hour:
In most cities/states the HOV lanes do not function for the entire day. The HOV lanes only operate during rush hours when the traffic is heaviest and HOV lanes are most likely to save time for car-poolers. During off-peak hours, these states either open the lanes to all traffic or simply close them until the next scheduled opening. For simulation purpose, the time-frames from 5:30am to 9:30am and from 4:00pm to 7:00pm have been considered as the peak hours. The peak_hour is an uncertain variable which can have values 'Yes' or 'No' and these values will be generated randomly.

## camera_functionality:
This variable is for considering cases where even when a SOV enters a HOV lane it won't be charged because the assigned police officer is not at his/her assigned position or the camera which monitors is not functional due to some technicalities. We are going to assign weights to these probabilities since the camera not functioning is less as well. When the camera is functional, the range of probability of camera catching a violator is 0.8-1


## Other variables 

## no. of HOV vehicles & no. of SOV vehicles:
Based on historical data, we found out that no of vehciles on a HOV lane is approximiately 1740 vehicles/hour. On the basis of this value, we have assigned a range for both HOV' and SOV'. These 2 variables will help in simulating the time taken by the HOV to pass the HOV lane.

## hov_speed:
This variable is of prime importance as it will help us in simulating the time taken by the HOV to pass the 20 mile stretch. It is calculated using no of accidents occurred, no of HOV vehicles/GPV vehicles, weather and weather_intensity as these parameters affect the speed of the vehicle. For example, speed of the vehicle decreases in extreme weather conditions or when an accident occurs. 

## gpv_speed:
This variable is of prime importance as it will help us in simulating the time taken by the GPV to pass the 20 mile stretch. It is calculated using accident intensity, no of HOV vehicles/GPV vehicles, weather and weather_intensity as these parameters affect the speed of the vehicle. For example, speed of the vehicle decreases in extreme weather conditions or when an accident occurs. 

## hov_time & gpv_time:
We are calculating time for the hov and gpv lane which will give us a comparative study of both lanes.

## fuel_efficient_sov:
Out of the total number of SOV vehicles, there are some which are fuel-efficient or hybrid. These few vehicles are allowed to travel on the HOV lane inspite of being SOV. A variable is thus defined for the number of fuel efficient SOV vehicles on the HOV lane. However, whether or not these vehicles will pay some or no fine depends on another variable. 

## reg_fuel_eff:
This variable gives the number of vehicles that are fuel-efficient and also registered to use the HOV lane. These vehicles are not required to pay the fine.

## hov_emission & gpv_emission:
All the vehicles emit harmful pollutants which are toxic for the environment. We found a study which gave us values for how much carbon monoxide vehicles emit at certain speeds (https://www.accessmagazine.org/spring-1995/are-hov-lanes-really-better/). The values for these variables are calculated on the basis of hov_speed and gpv_speed.

## estimate_fine:
This variable gives us the estimated fine considering that all vehicle who violate the hov lane rules get caught.

## actual_fine:
This variable gives us the actual fine the state collects assuming that camera is not able to detect all the vehicle who violate the rules.

## revenue_lost_per_day:
This variable gives us the difference between estimate_fine and actual_fine.

## Hypothesis or hypotheses before running the simulation:
1. All SOV vehicles are required to pay the same fine when they enter into an HOV lane. 
2. HOV lanes help in reducing the travel time in comparison to general purpose lanes.

## Assumptions:
1. At any given time of day, the number of fuel-efficient/hybrid SOV vehicles is 20% of the actual number of SOV vehicles in the HOV lane.
2. Out of the total number of fuel-efficient/hybrid SOV vehicles, 70% are registered to drive in the HOV lane.
3. The fine amount that an SOV vehicle is required to pay when it enters the HOV lane is $450.
4. The basic assumption is there are always general purpose lanes besides a hov lane.
5. The distance of the general purpose vehicle lane and high occupancy vehicle is considered to be same i.e 20 miles to get a better estimate of the values for comparison.

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
This is a basic summary of what we plan to analyze through our findings (subject to change)
- Is there an increase/decrease in the single occupancy vehicle on the HOV lanes on the basis of fines they are paying? How much loss does the state incur in terms of the revenue earned from the fines collected from the hybrid SOV vehicles?
- Are HOV lanes really benefitting people in reducing their travel time? Is there a potential pressure to convert under performing HOV lanes to general-purpose use?
- Does the state earn a revenue which is greater than the amount it spends for installing the cameras throughout the HOV lane?  
## Instructions on how to use the program:
- Make sure you are using Python 3.6 and above.
- Download and run the python file.
- There will be a prompt to enter the number of samples you want to use for performing the simualation. 

## All Sources Used:
http://people.eecs.berkeley.edu/~varaiya/papers_ps.dir/accessF05v2.pdf
https://ops.fhwa.dot.gov/publications/fhwahop08034/hot1_0.htm
https://en.wikipedia.org/wiki/High-occupancy_vehicle_lane
https://www.seattletimes.com/seattle-news/transportation/how-many-hov-lane-cheaters-are-there-and-how-many-get-caught/
https://www.tn.gov/tdot/high-occupancy-vehicle--hov--lane.html
https://www.latimes.com/local/california/la-me-ln-clean-air-car-decals-20180917-story.html
https://www.wklaw.com/consequences-of-driving-alone-in-the-carpool-or-hov-lane/
https://www.accessmagazine.org/spring-1995/are-hov-lanes-really-better/
