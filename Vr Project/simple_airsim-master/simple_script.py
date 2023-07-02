from simple_airsim.api import coordinate_system
from simple_airsim.api.drone import Drone
from simple_airsim.api.gui_manager import GUIManager
from simple_airsim.api.manager import Manager

def my_algorithm(drone: Drone):
    # Add your code here
    pass

if __name__ == '__main__':
    with Manager(coordinate_system.AIRSIM, method=my_algorithm) as man:
        with GUIManager(man, 10, 10, 10, 3) as gui:
            gui.start()