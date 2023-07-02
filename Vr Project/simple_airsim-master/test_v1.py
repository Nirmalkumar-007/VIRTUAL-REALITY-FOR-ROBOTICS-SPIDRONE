import time
import keyboard  # Import the keyboard module

from simple_airsim.api import coordinate_system
from simple_airsim.api.drone import Drone
from simple_airsim.api.gui_manager import GUIManager
from simple_airsim.api.manager import Manager

# Global variable to track the drone's state
landed = False

def square(drone: Drone):
    drone.takeoff(True)
    while True:
        drone.move_by(7, 0, 0, True)
        drone.turn_by(0, 0, -90, True)
        for i in range(6):
            drone.move_by(5, 0, 0, True)
            drone.turn_by(0, 0, 90, True)
            drone.land()
        
        # Check if the drone should land or hover
        if landed:
            drone.land(True)
        else:
            drone.hover(True)
        
        time.sleep(0.1)

def key_press_callback(e):
    global landed

    # Check if the specific key is pressed
    if e.name == 'space':
        # Toggle the landed variable
        landed = not landed

if __name__ == '__main__':
    with Manager(coordinate_system.AIRSIM, method=square) as man:
        with GUIManager(man, 10, 10, 10, 3) as gui:
            # Register the key press callback function
            keyboard.on_press(key_press_callback)
            
            # Start the GUI manager
            gui.start()
