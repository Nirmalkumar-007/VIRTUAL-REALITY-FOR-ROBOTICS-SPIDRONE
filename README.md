# VIRTUAL REALITY FOR ROBOTICS 
## FINAL ASSIGNMENT - GROUP15 - SPIDRONE. 
### PROJECT TOPIC: 
### PRECISION SPRAYING AND SEEDING FROM THE AIR VIA AGRICULTURAL DRONES.
----

GROUP MEMBERS:
-  [Nirmal Kumar Ravikumar](https://github.com/Nirmalkumar-007)
-  [Jerin Joy](https://github.com/Nirmalkumar-007)
-  [Abdul Rauf](https://github.com/Nirmalkumar-007)
-  [Krishant Tharun](https://github.com/Nirmalkumar-007)

UNDER THE GUIDANCE OF,
-  Prof.  [Gianni Vercelli](https://rubrica.unige.it/personale/VUZCWVtr)


---


#### SYNOPSIS:
- Create an autonomous UAV that works using a predefined plan that can be used to spray pesticides over large agricultural land. 
- The drone is able to detect the type of areas to spray in the environment on its own. 
- Then monitor the current condition and acquire the data coming from the environment.

---- 

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
#### TOOLS USED:
- There are more tools required for completing the assigned work. The main three tools used in this project
are UNREAL ENGINE (4.27), MICROSOFT AIRSIM, the details
of the mentioned tools are described below.
- #### UNREAL ENGINE: 
   - Unreal Engine is a complete suite of creation tools for game development, archi-
textural, and automotive visualization, linear film and television content creation, broadcast, and live event
production, training and simulation, and other real-time applications.
   - The Unreal engine has a lot of versions with advanced features. For this task, we used unreal engine version 4.27 for simulating the drone in the environment. 
   - MARKET PLACE: This is a place where we can get the landscapes, foliages, effects, and many features required to fulfill a project. We used most of the features in our project.

- #### PYTHON 3.7:
   - Python 3.7 is a versatile and beginner-friendly programming language. With clean syntax and a rich ecosystem, it's ideal for web development, data analysis, and automation. New features like data classes and improved type hinting enhance coding efficiency. Python's extensive standard library and active community support make it a powerful choice for developers of all levels. 

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
#### ENVIRONMENT:

- In Unreal Engine, the environment refers to the virtual world or scene created within the engine. It includes terrain, vegetation, lighting, weather, and objects to build immersive worlds.
- Developers can sculpt terrain, place vegetation, and use advanced lighting techniques. Weather effects like rain and fog can be added, and various props and objects populate the environment.
- Unreal Engine offers tools for creating realistic or stylized environments for games, VR, and architectural visualizations. It allows for customization and flexibility to achieve desired aesthetics and gameplay requirements.
- To build an environment in Unreal Engine:
  
     - Gather or create assets (textures, models, etc.).
     - Sculpt and shape the terrain using Unreal Engine's tools.
     - Set up lighting for desired effects.
     - Create and apply materials to surfaces. 
     - Place assets strategically within the environment.
     - Enhance visuals with post-processing effects.
     - Optimize performance for smooth running.
     - Iterate and test for refinement.
       
----
#### 1. LANDSCAPE AND HEIGHT MAP:

- There are more tools required for completing the assigned work. The main three tools used in this project
are UNREAL ENGINE (4.27), MICROSOFT AIRSIM, the details
of the mentioned tools are described below.

----

#### 2. FOLIAGES:

- This environment is designed for carrying out spraying actions on agricultural land using UAVs. As a initial stage the agricultural areas with crops are being construted. After the basic construction the 

----
#### 2. :

- This environment is designed for carrying out spraying actions on agricultural land using UAVs. As a initial stage the agricultural areas with crops are being construted. After the basic construction the 

----
#### 2. FOLIAGES:

- This environment is designed for carrying out spraying actions on agricultural land using UAVs. As a initial stage the agricultural areas with crops are being construted. After the basic construction the 

----
#### 5. CODE, LIBRARIES AND DEPENDENCIES:
   //CODE
   import time
   from simple_airsim.api import coordinate_system
   from simple_airsim.api.drone import Drone
   from simple_airsim.api.gui_manager import GUIManager
   from simple_airsim.api.manager import Manager
   def square(drone: Drone):
       drone.takeoff(True)
       while True:
           drone.move_by(7, 0, 0, True)
           drone.turn_by(0, 0, -90, True)
           for i in range(6):
               drone.move_by(5, 0, 0, True)
               drone.turn_by(0, 0, 90, True)
           time.sleep(0.1)
   if __name__ == '__main__':
       with Manager(coordinate_system.AIRSIM, method=square) as man:
           with GUIManager(man, 10, 10, 10, 3) as gui:
               gui.start()

   
- The code starts with the necessary imports. The simple_airsim.api module is imported, which includes classes for interacting with AirSim. The time module is imported for introducing a small delay between drone movements.

- The square function is defined, which takes a Drone object as an argument. Inside the function, the drone is instructed to take off by calling the drone. takeoff(True). The True argument indicates that the function should wait for the drone to reach the desired altitude before continuing.

- The code enters an infinite loop using while True. This loop is responsible for executing the square flight pattern repeatedly.

- Within the loop, the drone moves forward by 7 units using drone.move_by(7, 0, 0, True). The function takes the parameters for movement in the X, Y, and Z directions, with the last argument True indicating that the function should wait for the movement to complete before proceeding.

- After moving forward, the drone turns left by 90 degrees using drone.turn_by(0, 0, -90, True). The function specifies the rotation angles in the roll, pitch, and yaw axes, with the yaw component set to -90 degrees to indicate a left turn.

- Next, a for loop is used to repeat the following steps six times. This loop is responsible for executing the sides of the square.

- Within the loop, the drone moves forward by 5 units using drone.move_by(5, 0, 0, True). It then turns right by 90 degrees using drone.turn_by(0, 0, 90, True). This sequence of movements creates a side of the square.

- A small delay of 0.1 seconds is introduced between each movement using time.sleep(0.1). This helps to create a smoother flight pattern.

- The main execution block starts with a with statement. It creates a Manager object with the coordinate system set to AIRSIM and the flight pattern method set to the square function defined earlier. The with statement ensures proper initialization and cleanup of the manager.

- Inside the with block, a GUIManager object is created. It takes the Manager object and specifies the dimensions of the GUI window (10 units in length, 10 units in width, and 3 units in height).

- Finally, the gui.start() function is called, which launches the GUI window and starts the execution of the flight pattern. This allows us to visualize the drone's movement in the GUI window.

----



https://github.com/Nirmalkumar-007/VIRTUAL-REALITY-FOR-ROBOTICS-SPIDRONE/assets/93769409/9d4a93e6-2a86-4514-8aef-772beb2953ef




