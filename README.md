# 590PR Final_Project

# Title: Fines Paid by Single Occupancy Vehicle on a High Occupany Vehicle Lane Simulation

## Team Member(s): Aditya Kadrekar | Ankita Pant | Devanshi Bhatt

# Monte Carlo Simulation Scenario & Purpose:
The purpose of this simulation is to predict the fine that a single occupant vehicle (SOV) will have to pay, under different circumstances, when it enters the high occupant vehicle lane. There is an assumption that single occupied vehicles take the HOV lanes (we are randomizing the number of SOV on the HOV lanes based on historical data). We will also predict the probability of faster/slower highway trips for express transit services like Bus Rapid Transit (BRT) or any high occupancy vehicle.

## Simulation's variables of uncertainty
There are 8 random variables which are getting randomly generated - accident, accident_intensity, weather, weather_intensity, camera_functionality/police_presence, no of HOV vehicles, no of SOV vehicles and speed. 

## accident:
Since accidents are very frequent on highways, we are using a boolean value to determine the frequency where True would mean accident has occured and False would mean accident hasn't occured.

## accident_intensity:
When the accident occurs (i.e when True) it generates a random value from the range 1-10 indicating the intensity of the accident and when accident doesn't occer (i.e when False) it returns 0.

## weather & weather_intensity:
We are considering three seasons i.e Winter, Rain and Summer. We are assuming that even in extreme summers it doesn't affect the traffic. Therefore, the weather intensity during summers is 0. But for winters and rainy season, we understand that extreme winters and rains can affect the traffic. Thus, for winter and rains we generate a random value from the range 1-10 indicating the intensity of the snow/rain.

## camera_functionality/police_presence:
This variable is for considering cases where even when a SOV enters a HOV lane it won't be charged because the assigned police officer is not at his/her assigned position or the camera which monitors is not functional due to some technicalities. We are going to assign weights to these probabilities since the likelihood of police officer not being at his/her position is less or the camera not functioning is less as well. We are yet to decide which one to choose out of these two.

# The above variables will help in simulating the fines charged to the SOV.

## no of HOV vehicles & no of SOV vehicles:
Based on historical data, we found out that no of vehciles on a HOV lane is approximiately 1740 vehicles/hour. On the basis of this value, we have assigned a range for both HOV' and SOV'. These 2 variables will help in simulating the time taken by the HOV to pass the HOV lane.

## speed:
This variable is of prime importance as it will help us in simulating the time taken by the HOV to pass the HOV lane. It is calculated using accident intensity, weather and weather_intensity as these parameters affect the speed of the vehicle. For example, speed of the vehicle decreases in extreme weather conditions or when an accident occurs. 

## Hypothesis or hypotheses before running the simulation:
- All SOV vehicle will have to pay the same fine when they enter a HOV lane
- HOV lanes help in reducing the travel time

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
This is a basic summary of what we plan to analyze through our findings (subject to change)
- Is there a increase/decrease in the single occupancy vehicle on the HOV lanes on the basis of fines they are paying?
- Are HOV lanes really benefitting people in reducing their travel time?
- Is there a potential pressure to convert under performing HOV lanes to general-purpose use?

## Instructions on how to use the program:
Make sure you are using Python 3.6 and above.
Download and run the python file.
There will be a prompt to enter the total distance (in miles) of the HOV lane. 

## All Sources Used:
http://people.eecs.berkeley.edu/~varaiya/papers_ps.dir/accessF05v2.pdf
https://ops.fhwa.dot.gov/publications/fhwahop08034/hot1_0.htm
