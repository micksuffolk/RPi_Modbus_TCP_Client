# Modbus_TCP_Client_Python

This project contains two 'main' Python files...
main.py = Mikes Raspberry Pi Project, contains code specific to this projects requirements.
main_ModbusTCPclientBase = A good starting point to make another Modbus TCP Client project.

Modbus TCP Client, requests data from the server, and writes data to the server using the following function codes...
04 Read Input Registers (3xxxxx)
03 Read Holding Registers (4xxxxx)
06 Write Single Holding Register (4xxxxx)
16 Write Multiple Holding Registers (4xxxxx)
