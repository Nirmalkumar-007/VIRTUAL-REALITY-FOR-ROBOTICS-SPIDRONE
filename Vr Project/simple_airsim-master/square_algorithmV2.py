import time

from simple_airsim.api import coordinate_system
from simple_airsim.api.drone import Drone
from simple_airsim.api.gui_manager import GUIManager
from simple_airsim.api.manager import Manager


def square(drone: Drone):
    drone.takeoff(True)
    while True:
    	for _ in range(4):
        	drone.command(0, 0.5, 0, 0)  # Move forward by pitching 0.5
        	time.sleep(1)  # Wait for 1 second
        	drone.command(0, 0, 0.5, 0)  # Turn right by increasing the yaw rate to 0.5
        	time.sleep(1)  # Wait for 1 second
        	drone.command(0, -0.5, 0, 0)  # Move backward by pitching -0.5
        	time.sleep(1)  # Wait for 1 second
        	drone.command(0, 0, -0.5, 0)  # Turn left by decreasing the yaw rate to -0.5
        	time.sleep(1)  # Wait for 1 second



if __name__ == '__main__':
    with Manager(coordinate_system.AIRSIM, method=square) as man:
        with GUIManager(man, 10, 10, 10, 3) as gui:
            gui.start()



