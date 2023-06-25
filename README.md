## FOLLOW THESE STEPS TO SIMULATE THE DRONE IN THE ENVIRONMENT

1. Download unreal engine [version 4.27](https://www.unrealengine.com/en-US/download) from the marketplace.

2. Download  [Python version 3.7.](https://www.python.org/downloads/)

3. Download  [AIRSIM](https://github.com/microsoft/AirSim.git) from Microsoft.
4. Follow these steps to install the plugins and connect Unreal with the airsim.
```
https://github.com/microsoft/AirSim.git
```
5. Clone the repository
```
git@github.com:Nirmalkumar-007/VIRTUAL-REALITY-FOR-ROBOTICS-SPIDRONE.git
```
6. Launch the unreal engine and choose EL_grounds from the content browser.

7. Open maps from the EL_grounds and double click on the FINAL_MAPS. Here we can find the environment for the simulation. 

8. Now run the simulation in the unreal engine window.

9. Open the command prompt from the start menu and navigate to this directory

```
Vr Project\simple_airsim-master>
```
10. Once after reaching this directory in the command prompt type the following command in the CMD prompt and press ENTER.
```
Vr Project\simple_airsim-master> Python agricultural_drone_simulation.py
```
11. After entering the command in the prompt. A Python window will open. select the ALGORITHM MODE and press the start button.

![Screenshot 2023-06-25 215208](https://github.com/Nirmalkumar-007/VIRTUAL-REALITY-FOR-ROBOTICS-SPIDRONE/assets/93769409/78b34639-25fd-4516-a10e-822da37ee319)

12. The drone with the autonomous mode will be activated and the drone start to move freely in the environment & perform the spraying operation in the untreated areas. And incase if we need to spray the seeds manually, we can use the keyboard button "O". By pressing this the drone can be able to spray manually.
13. By pressing the F1 button from the keyboard, we can find the list of options the airsim can adopt. Few features are shown in the image below


![Screenshot 2023-06-25 215609](https://github.com/Nirmalkumar-007/VIRTUAL-REALITY-FOR-ROBOTICS-SPIDRONE/assets/93769409/38ebddde-14c7-467b-9661-fc4cb8672be8)

14. To stop the simulation, Just press the escape button in the unreal engine. And then go to the Python window and press stop. To simulate the drone again, Then follow the same instructions mentioned above.
15. These simulations can work fast or slow based on the graphics and other requirements.  
