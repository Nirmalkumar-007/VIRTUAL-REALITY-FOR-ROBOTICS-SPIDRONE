FINAL ASSIGNMENT - GROUP15 - SPIDRONE. 
---
---
# VIRTUAL REALITY FOR ROBOTICS
GROUP MEMBERS:
-  [Nirmal Kumar Ravikumar](https://github.com/Nirmalkumar-007)
-  [Jerin Joy](https://github.com/Nirmalkumar-007)
-  [Abdul Rauf](https://github.com/Nirmalkumar-007)
-  [Krishant tharun](https://github.com/Nirmalkumar-007)

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
large agricultural land. The drone is able to detect the type of areas to spray, monitor the current condition and spray where the areas are not well treated,
and acquire the data coming from the environment on its own. Within the agricultural drone market, there are
many claims that drones can be used to measure crop health and take spraying action according to the required
parameters.
- As the initial step, we started up by creating an environment by using the unreal engine which represents
an agricultural land where the spraying action will be carried out. In addition to that we parallelly build a map
and imported the drone from the Plugin called AIRSIM.
- As mentioned before, this drone is built in a way that the robot can switch between the automatic and man-
dual modes in spraying. With this, the user can have the option to opt for their preferred mode. The drone automatically detects poorly treated areas and perfectly treated areas.
- This helps the drone decides where the spraying action needs to be carried out. Usually, the low-treated areas
need to be sprayed, so the drone gets the feedback and takes the decision on its own about where and when
the action needs to take place. 
- There are some possibilities for the user to interrupt the drone when missions
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
are UNREAL ENGINE (4.27), MICROSOFT AIRSIM, the details
of the mentioned tools are described below.
- #### UNREAL ENGINE: 
   - Unreal Engine is a complete suite of creation tools for game development, archi-
textural, and automotive visualization, linear film and television content creation, broadcast, and live event
production, training and simulation, and other real-time applications.
   - The Unreal engine has a lot of versions with advanced features. For this task, we used unreal engine version 4.27 for simulating the drone in the environment. 
   - MARKET PLACE: This is a place where we can get the landscapes, foliages, effects, and many features required to fulfill a project. We used most of the features in our project.


- #### MICROSOFT AIRSIM: 
   - AirSim (Aerial Informatics and Robotics Simulation) is an open-source, cross-
platform simulator for drones, ground vehicles such as cars and various other objects, built on Epic Games
proprietary Unreal Engine 4 as a platform for AI research. 
   - It is developed by Microsoft and can be used to
experiment with deep learning, computer vision, and reinforcement learning algorithms for autonomous vehicles.

   - This allows the testing of autonomous solutions without worrying about real-world damage.
AirSim, a simulator developed by Microsoft, offers various functions specifically designed for drone applications. 

Here are some key features of AirSim for drone functions:

- Realistic Drone Simulation: AirSim provides a highly realistic simulation environment for drones, including accurate physics-based dynamics, flight controls, and environmental conditions. This allows developers to test and refine their drone algorithms in a safe and controlled virtual environment.

- Sensor Simulation: AirSim supports the simulation of various sensors commonly used in drones, including cameras, lidar, and depth sensors. These sensors generate realistic data, enabling developers to train and evaluate perception algorithms for tasks like object detection, tracking, and mapping.

- Autonomous Navigation: AirSim allows developers to design and test autonomous navigation algorithms for drones. It provides APIs for controlling the drone's movements and accessing its state, enabling the implementation and evaluation of path planning, obstacle avoidance, and waypoint following algorithms.

- Customizable Environments: AirSim allows users to create custom environments and scenarios for drone simulations. This flexibility enables developers to simulate a wide range of real-world scenarios, including different terrains, weather conditions, and lighting variations.

- Machine Learning Integration: AirSim seamlessly integrates with popular machine learning frameworks like TensorFlow and PyTorch. This enables developers to train and evaluate AI models using simulated drone data, facilitating the development of advanced drone control and perception algorithms.

- Multi-Drone Simulations: AirSim supports the simulation of multiple drones simultaneously. This functionality is particularly useful for testing swarm coordination algorithms and evaluating the performance of distributed drone systems.

By providing a realistic and customizable simulation environment, AirSim empowers developers to accelerate the development and testing of drone algorithms, ultimately leading to safer and more capable autonomous drone systems.

----
#### TOOLS:

![Screenshot 2023-06-21 155250](https://github.com/Nirmalkumar-007/VIRTUAL-REALITY-FOR-ROBOTICS-SPIDRONE/assets/93769409/3d901f90-1fd1-4147-bcdb-5032d831ac02)


- There are more tools required for completing the assigned work. The main three tools used in this project
are UNREAL ENGINE (4.27), MICROSOFT AIRSIM, the details
of the mentioned tools are described below.
----
#### TOOLS:

![Screenshot 2023-06-21 155444](https://github.com/Nirmalkumar-007/VIRTUAL-REALITY-FOR-ROBOTICS-SPIDRONE/assets/93769409/7849b234-db2b-49bf-93e0-5103fed61632)

- There are more tools required for completing the assigned work. The main three tools used in this project
are UNREAL ENGINE (4.27), MICROSOFT AIRSIM, the details
of the mentioned tools are described below.
----
#### TOOLS:

![Screenshot 2023-06-21 154446](https://github.com/Nirmalkumar-007/VIRTUAL-REALITY-FOR-ROBOTICS-SPIDRONE/assets/93769409/be0bc581-6b76-4a22-9708-337be6a92e07)

- There are more tools required for completing the assigned work. The main three tools used in this project
are UNREAL ENGINE (4.27), MICROSOFT AIRSIM, the details
of the mentioned tools are described below.
