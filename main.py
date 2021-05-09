import socket
from umodbus import conf
from umodbus.client import tcp
from time import sleep



######################################################################################################################
# Initialize Values (This block will test the excepted error to occur)...
try:
    print("Code Initializing...")

    # Enable values to be signed (default is False).
    conf.SIGNED_VALUES = True

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.88', 7777))



######################################################################################################################
# The try section has failed (handle the error)...
except:
    print('Something went wrong with Try block...')
    print('Check the remote IP address is available...')
    print('Check the Modbus Slave is actually turned on...')
    exit()



######################################################################################################################
# The try section has been successful (If there is no exception then this block will be executed)...
else:
    print('Code Running...')

    # Main Program Loop...
    while True:

        # Returns a message or Application Data Unit (ADU) specific for doing
        # Modbus TCP/IP.
        # write_message = tcp.write_multiple_coils(slave_id=1, starting_address=1, values=[1, 0, 1, 1])
        read_message_01 = tcp.read_holding_registers(slave_id=1, starting_address=3, quantity=1)

        # Response depends on Modbus function code. This particular returns the
        # amount of coils written, in this case it is.
        response = tcp.send_message(read_message_01, sock)

        print(response)

        sleep(0.1)



######################################################################################################################
# Finally block always gets executed either exception is generated or not...
finally:

    print('sock.close...')
    sock.close()
    sleep(0.5)

    print('Code Stopped...')
    exit()

