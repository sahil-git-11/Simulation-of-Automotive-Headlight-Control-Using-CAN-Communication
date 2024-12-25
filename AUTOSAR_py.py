
import time
import random
from queue import Queue

# simulates CAN message queue
can_message_queue = Queue()

# application Layer: headlight control logic
class HeadlightController:
    def __init__(self):
        self.state = "OFF"  # initial state of headlights
        self.high_beam = False  # high-beam state
        self.drl = False  # daytime running lights state

    def control_headlights(self, command):
        
        #controls the headlights based on received command.
        
        if command == "ON":
            self.state = "ON"
            self.high_beam = False
            self.drl = False
        elif command == "OFF":
            self.state = "OFF"
            self.high_beam = False
            self.drl = False
        elif command == "AUTO":
            # automatic control based on external light conditions taken as random input 
            ambient_light = random.randint(0, 100)  # simulate ambient light sensor
            if ambient_light < 50:
                self.state = "ON"
            else:
                self.state = "OFF"
        elif command == "HIGH_BEAM":
            if self.state == "ON":
                self.high_beam = True
            else:
                print("Error: Cannot activate high beam when headlights are OFF.")
        elif command == "DRL":
            self.drl = True
            self.state = "OFF"
        else:
            print("Invalid Command")

        self._log_state()

    def _log_state(self):
        #
        #Logs the current state of the headlights.
        
        print(f"Headlights: {self.state}, High Beam: {'ON' if self.high_beam else 'OFF'}, DRL: {'ON' if self.drl else 'OFF'}")

# simulating CAN Protocol
class CANCommunication:
    def send_message(self, message):
        
        #Simulates sending a CAN message.
        
        print(f"Sending CAN message: {message}")
        can_message_queue.put(message)

    def receive_message(self):
        
        #simulates receiving a CAN message.
        
        if not can_message_queue.empty():
            message = can_message_queue.get()
            print(f"Received CAN message: {message}")
            return message
        return None

# Main code for ECU Simulation
class LightingControlECU:
    def __init__(self):
        self.headlight_controller = HeadlightController()
        self.can_communication = CANCommunication()

    def run(self):
        
        #simulates the ECU operation.
        
        print("Lighting Control ECU is running...")
        while True:
            # Simulate receiving CAN messages
            message = self.can_communication.receive_message()
            if message:
                self.headlight_controller.control_headlights(message)
            

# Simulate another ECU sending CAN messages
def simulate_command_sender(can_comm):
    commands = ["ON", "HIGH_BEAM", "AUTO", "DRL", "OFF"]
    for command in commands:
        time.sleep(3)  # Send command every 3 seconds
        can_comm.send_message(command)

# Main simulation
if __name__ == "__main__":
    # Instantiate ECU and CAN Communication
    ecu = LightingControlECU()
    can_comm = ecu.can_communication

    # Start a parallel thread to simulate another ECU
    import threading
    sender_thread = threading.Thread(target=simulate_command_sender, args=(can_comm,))
    sender_thread.start()

    # Run the ECU
    ecu.run()
