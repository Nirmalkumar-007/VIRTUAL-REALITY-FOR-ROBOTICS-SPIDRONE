FINAL ASSIGNMENT - GROUP15 - SPIDRONE. 
---
---
# VIRTUAL REALITY FOR ROBOTICS
GROUP MEMBERS:
-  [Nirmal Kumar Ravikumar](https://github.com/Nirmalkumar-007)
-  [Jerin Joy](https://github.com/Nirmalkumar-007)
-  [Abdul Rauf](https://github.com/Nirmalkumar-007)

SUPERVISOR:
-  Prof.  [Gianni Vercelli](https://rubrica.unige.it/personale/VUZCWVtr)


---
### PROJECT TOPIC: 
### PRECISION SPRAYING AND SEEDING FROM THE AIR VIA AGRICULTURAL DRONES.

#### SYNOPSIS:
- Create an autonomous UAV that works using a predefined plan that can be used to spray pesticides over large agricultural land. 
- The drone is able to detect the type of areas to spray in the environment on its own. 
- Then monitor the current condition and acquire the data coming from the environment.

---- 

#### INTRODUCTION:
- In the modern world, maintaining a huge agricultural field is a major issue for humans. However, drones
can break that barrier by overtaking the responsibilities of maintaining the fields in the given context. The two
acronyms for drones are unmanned aerial vehicles (UAV) and unmanned aerial systems (UAS).  
- The term UAV
means a drone, while UAS includes drones and their associated tools (e.g., flight software or cameras). Both
the UAV and UAS terms are typically used in technical and regulatory fields.
- Most drones fall under the categories of rotary or fixed-wing. A rotary-style drone would be similar to a
helicopter which is cheaper and versatile, while a fixed-wing drone looks exactly like an airplane. 
- A third type of
drone is a hybrid, which has both rotary and fixed wings. Considering the agricultural application, the Multi
copter drones are very useful to accomplish a task with a lot of advantages.
- Thermal radiation, or temperature, can be measured using longer infrared wavelengths. Plants that are
either dead or stressed should be warmer due to decreased evapotranspiration, which thermal cameras can
detect. 
- This could be useful in irrigated fields in Delaware. There are numerous claims in the agricultural drone
market that drones can be used to measure crop health. In many cases, these businesses use multispectral
data to observe how plants reflect various wavelengths of light. 
- Precision spraying and seeding from the air via
agricultural drones are our fields of development for the course of this Virtual reality for robotics. To Create
a semi-autonomous UAV that works using a predefined plan in an agricultural field for spraying applications.
Further details about the state of the art are described in detail below.



---
#### DESCRIPTION:
- Creating semiautonomous UAVs that work using a predefined plan that can be used to spray pesticides over
large agricultural land. The drone is able to detect the type of areas to spray, monitor the current condition,
and acquire the data coming from the environment on its own. Within the agricultural drone market, there are
many claims that drones can be used to measure crop health and take spraying action according to the required
parameters.
- As the initial step, we started up by creating an environment by using the unreal engine which represents
an agricultural land where the spraying action will be carried out. Then we are now focusing on the drone part
of importing a previously existing 3d model available on the internet which satisfies the needs. Hence the drone
can be able to acquire knowledge from the environment. In addition to that we are parallelly building a map
and implementing our flight plan by creating a 3D trajectory using Ardu copter software to control the drones
and plan the mission using the mission planning feature of the software.
- As mentioned before, this drone is built in a way that the robot can switch between the automatic and man-
dual modes. With this, the user can have the option to opt for their preferred mode. When the drone functions
it should automatically obtain feedback from the drone and display or monitor the status of the payload and
the current GPS location in the ground control station. A heat map is very important in our simulation as it
shows the poorly treated areas and perfectly treated areas on the map.
- his helps the drone decides where the spraying action needs to be carried out. Usually, the low-treated areas
need to be sprayed, so the drone gets the feedback and takes the decision on its own about where and when
the action needs to take place. There are some possibilities for the user to interrupt the drone when missions
in the emergency situations like a low battery, empty payload, bad weather conditions, and so on. In case of
an emergency based on these factors, the drone can immediately return back to the ground control station to
avoid unnecessary accidents.
- This drone is represented in the environment from a Third person’s perspective for the precision spraying
process. Along with this a base ground control station for the drone is also built to make the drone return
home when out of the spraying liquid or when the battery is low. This ground control station is located near
agricultural land which makes the work easier for the drones.

---
#### TOOLS:
- There are more tools required for completing the assigned work. The main three tools used in this project
are UNREAL ENGINE (4.27), MICROSOFT AIRSIM, and the ARDUpilot for reference mapping. the details
of the mentioned tools are described below.
- UNREAL ENGINE: 
   - Unreal Engine is a complete suite of creation tools for game development, archi-
tectural, and automotive visualization, linear film and television content creation, broadcast and live event
production, training and simulation, and others real-time applications.
- MICROSOFT AIRSIM: 
   - AirSim (Aerial Informatics and Robotics Simulation) is an open-source, cross-
platform simulator for drones, ground vehicles such as cars and various other objects, built on Epic Games’
proprietary Unreal Engine 4 as a platform for AI research. It is developed by Microsoft and can be used to
experiment with deep learning, computer vision and reinforcement learning algorithms for autonomous vehicles.
This allows testing of autonomous solutions without worrying about real-world damage
---
