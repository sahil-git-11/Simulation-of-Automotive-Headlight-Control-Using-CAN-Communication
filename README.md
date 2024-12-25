This Python-based simulation models a vehicle's Lighting Control ECU and its interaction with the CAN network for headlight management. The system includes the following components:

Headlight Controller (Application Layer):

Manages the headlight's state (ON, OFF, AUTO).
Responds to commands for high-beam and daytime running lights (DRL).
Simulates ambient light detection using random values.
Logs the current state of headlights for debugging and testing purposes.
CAN Communication Layer:

Simulates sending and receiving CAN messages using a queue (Queue).
Enables inter-ECU communication for sending commands like "ON," "OFF," "AUTO," "HIGH_BEAM," and "DRL."
Lighting Control ECU (Main Logic):

Integrates the Headlight Controller and CAN Communication.
Continuously listens for incoming CAN messages and processes them using the Headlight Controller.
Command Sender Simulation:

Mimics another ECU that periodically sends commands to the Lighting Control ECU.
Execution Flow:

A secondary thread generates CAN messages representing headlight commands.
The main ECU processes these commands and updates the headlight state accordingly.
The system continuously logs the headlight state and errors, if any.
