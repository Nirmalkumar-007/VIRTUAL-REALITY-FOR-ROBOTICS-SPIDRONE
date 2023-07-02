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