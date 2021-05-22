import socket
from tkinter import *
from umodbus import conf
from umodbus.client import tcp
from time import sleep



######################################################################################################################
# Initialize variables...
ControlCommandWord1 = int()
ControlCommandWord2 = int()
ControlCommandWord3 = int()
ControlCommandWord4 = int()
ControlDataWord1 = int()
ControlDataWord2 = int()
ControlDataWord3 = int()
ControlDataWord4 = int()
ControlDataWord5 = int()
ControlDataWord6 = int()
ControlDataWord7 = int()
ControlDataWord8 = int()
ExecuteControlModbusWrite = bool()



######################################################################################################################
# Function to check if a bit in an integer is ON or OFF...
# Integer range is 0 to 65535, bit range is 0 to 15...
def BitCheck(Integer_to_BitCheck, BitToCheck):
    if (Integer_to_BitCheck & (1 << BitToCheck)):
        return True # Bit is Logic 1 (one)
    else:
        return False # Bit is Logic 0 (zero)



######################################################################################################################
# Function to set a bit in an integer ON...
# CtrlWord range is 1 to 4, bit range is 0 to 15...
def BitSet(CtrlWord, bit):

    global ControlCommandWord1
    global ControlCommandWord2
    global ControlCommandWord3
    global ControlCommandWord4
    global ExecuteControlModbusWrite

    temp_output = int()

    if bit == 0:
        temp_output = int(0) | int(1)
    if bit == 1:
        temp_output = int(0) | int(2)
    if bit == 2:
        temp_output = int(0) | int(4)
    if bit == 3:
        temp_output = int(0) | int(8)
    if bit == 4:
        temp_output = int(0) | int(16)
    if bit == 5:
        temp_output = int(0) | int(32)
    if bit == 6:
        temp_output = int(0) | int(64)
    if bit == 7:
        temp_output = int(0) | int(128)
    if bit == 8:
        temp_output = int(0) | int(256)
    if bit == 9:
        temp_output = int(0) | int(512)
    if bit == 10:
        temp_output = int(0) | int(1024)
    if bit == 11:
        temp_output = int(0) | int(2048)
    if bit == 12:
        temp_output = int(0) | int(4096)
    if bit == 13:
        temp_output = int(0) | int(8192)
    if bit == 14:
        temp_output = int(0) | int(16384)
    if bit == 15:
        temp_output = int(0) | int(-32768)

    if CtrlWord == 1:
        ControlCommandWord1 = temp_output
    if CtrlWord == 2:
        ControlCommandWord2 = temp_output
    if CtrlWord == 3:
        ControlCommandWord3 = temp_output
    if CtrlWord == 4:
        ControlCommandWord4 = temp_output

    temp_output = 0
    ExecuteControlModbusWrite = True



######################################################################################################################
# Initialize values (This block will test the excepted error to occur)...
try:
    print("Code Initializing...")

    # Modbus Client...
    # Enable values to be signed (default is False).
    conf.SIGNED_VALUES = True

    # Create TCP/IP connection.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.1.88', 7777))

    # Make some register arrays to store received Modbus Data.
    Received_Data_HR = list()
    Received_Data_IR = list()



    # tkinter GUI...
    root = Tk()
    root.geometry("900x600")
    root.configure(bg='grey')

    # Code for widgets...
    Label_Rasp_Pi_Hour      = StringVar()
    Label_Rasp_Pi_Minute    = StringVar()
    Label_Rasp_Pi_Second    = StringVar()
    Label_Rasp_Pi_uSecond   = StringVar()
    Label_Rasp_Pi_Year      = StringVar()
    Label_Rasp_Pi_Month     = StringVar()
    Label_Rasp_Pi_Day       = StringVar()

    Label_Rasp_Pi_ProgramStatus     = StringVar()
    Label_Rasp_Pi_Temp              = StringVar()
    Label_Rasp_Pi_StatusDataWord1   = StringVar()
    Label_Rasp_Pi_StatusDataWord2   = StringVar()
    Label_Rasp_Pi_StatusDataWord3   = StringVar()
    Label_Rasp_Pi_StatusDataWord4   = StringVar()
    Label_Rasp_Pi_StatusDataWord5   = StringVar()
    Label_Rasp_Pi_StatusDataWord6   = StringVar()
    Label_Rasp_Pi_StatusDataWord7   = StringVar()
    Label_Rasp_Pi_StatusDataWord8   = StringVar()
    Label_Rasp_Pi_StatusDataWord9   = StringVar()
    Label_Rasp_Pi_StatusDataWord10  = StringVar()
    Label_Rasp_Pi_StatusDataWord11  = StringVar()
    Label_Rasp_Pi_StatusDataWord12  = StringVar()
    Label_Rasp_Pi_StatusDataWord13  = StringVar()
    Label_Rasp_Pi_StatusDataWord14  = StringVar()
    Label_Rasp_Pi_StatusDataWord15  = StringVar()
    Label_Rasp_Pi_StatusDataWord16  = StringVar()

    Header_01 = Label(root, text="---------------------------- Modbus TCP Client (Master) - Live Raspberry Pi Modbus Data ----------------------------", bg='grey', fg='black')
    Header_01.grid(row=0, columnspan=99, sticky=EW)

    Header_01_Spacer = Label(root, text="", bg='grey', fg='black')
    Header_01_Spacer.grid(row=1, columnspan=99, sticky=EW)

    Label_Time_Hour_Text            = Label(root, bg='grey', text="Hour = ").grid(row=2, column=0, sticky=E)
    Label_Time_Minute_Text          = Label(root, bg='grey', text="Minute = ").grid(row=3, column=0, sticky=E)
    Label_Time_Second_Text          = Label(root, bg='grey', text="Second = ").grid(row=4, column=0, sticky=E)
    Label_Time_uSecond_Text         = Label(root, bg='grey', text="uSecond = ").grid(row=5, column=0, sticky=E)
    Label_Time_Year_Text            = Label(root, bg='grey', text="Year = ").grid(row=6, column=0, sticky=E)
    Label_Time_Month_Text           = Label(root, bg='grey', text="Month = ").grid(row=7, column=0, sticky=E)
    Label_Time_Day_Text             = Label(root, bg='grey', text="Day = ").grid(row=8, column=0, sticky=E)
    Label_ProgramStatus_Text        = Label(root, bg='grey', text="Prg. Sts = ").grid(row=9, column=0, sticky=E)
    Label_Temperature_Text          = Label(root, bg='grey', text="DegC. = ").grid(row=10, column=0, sticky=E)
    Label_Time_Hour_Variable        = Label(root, bg='grey', textvariable=Label_Rasp_Pi_Hour).grid(row=2, column=1, sticky=W)
    Label_Time_Minute_Variable      = Label(root, bg='grey', textvariable=Label_Rasp_Pi_Minute).grid(row=3, column=1, sticky=W)
    Label_Time_Second_Variable      = Label(root, bg='grey', textvariable=Label_Rasp_Pi_Second).grid(row=4, column=1, sticky=W)
    Label_Time_uSecond_Variable     = Label(root, bg='grey', textvariable=Label_Rasp_Pi_uSecond).grid(row=5, column=1, sticky=W)
    Label_Time_Year_Variable        = Label(root, bg='grey', textvariable=Label_Rasp_Pi_Year).grid(row=6, column=1, sticky=W)
    Label_Time_Month_Variable       = Label(root, bg='grey', textvariable=Label_Rasp_Pi_Month).grid(row=7, column=1, sticky=W)
    Label_Time_Day_Variable         = Label(root, bg='grey', textvariable=Label_Rasp_Pi_Day).grid(row=8, column=1, sticky=W)
    Label_ProgramStatus_Variable    = Label(root, bg='grey', textvariable=Label_Rasp_Pi_ProgramStatus).grid(row=9, column=1, sticky=W)
    Label_Temperature_Variable      = Label(root, bg='grey', textvariable=Label_Rasp_Pi_Temp).grid(row=10, column=1, sticky=W)

    Label_StatusDataWord1_Text  = Label(root, bg='grey', text="Data 1 = ").grid(row=2, column=4, sticky=E)
    Label_StatusDataWord2_Text  = Label(root, bg='grey', text="Data 2 = ").grid(row=3, column=4, sticky=E)
    Label_StatusDataWord3_Text  = Label(root, bg='grey', text="Data 3 = ").grid(row=4, column=4, sticky=E)
    Label_StatusDataWord4_Text  = Label(root, bg='grey', text="Data 4 = ").grid(row=5, column=4, sticky=E)
    Label_StatusDataWord5_Text  = Label(root, bg='grey', text="Data 5 = ").grid(row=6, column=4, sticky=E)
    Label_StatusDataWord6_Text  = Label(root, bg='grey', text="Data 6 = ").grid(row=7, column=4, sticky=E)
    Label_StatusDataWord7_Text  = Label(root, bg='grey', text="Data 7 = ").grid(row=8, column=4, sticky=E)
    Label_StatusDataWord8_Text  = Label(root, bg='grey', text="Data 8 = ").grid(row=9, column=4, sticky=E)
    Label_StatusDataWord9_Text  = Label(root, bg='grey', text="Data 9 = ").grid(row=2, column=6, sticky=E)
    Label_StatusDataWord10_Text = Label(root, bg='grey', text="Data 10 = ").grid(row=3, column=6, sticky=E)
    Label_StatusDataWord11_Text = Label(root, bg='grey', text="Data 11 = ").grid(row=4, column=6, sticky=E)
    Label_StatusDataWord12_Text = Label(root, bg='grey', text="Data 12 = ").grid(row=5, column=6, sticky=E)
    Label_StatusDataWord13_Text = Label(root, bg='grey', text="Data 13 = ").grid(row=6, column=6, sticky=E)
    Label_StatusDataWord14_Text = Label(root, bg='grey', text="Data 14 = ").grid(row=7, column=6, sticky=E)
    Label_StatusDataWord15_Text = Label(root, bg='grey', text="Data 15 = ").grid(row=8, column=6, sticky=E)
    Label_StatusDataWord16_Text = Label(root, bg='grey', text="Data 16 = ").grid(row=9, column=6, sticky=E)
    Label_StatusDataWord1_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord1).grid(row=2, column=5, sticky=W)
    Label_StatusDataWord2_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord2).grid(row=3, column=5, sticky=W)
    Label_StatusDataWord3_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord3).grid(row=4, column=5, sticky=W)
    Label_StatusDataWord4_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord4).grid(row=5, column=5, sticky=W)
    Label_StatusDataWord5_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord5).grid(row=6, column=5, sticky=W)
    Label_StatusDataWord6_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord6).grid(row=7, column=5, sticky=W)
    Label_StatusDataWord7_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord7).grid(row=8, column=5, sticky=W)
    Label_StatusDataWord8_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord8).grid(row=9, column=5, sticky=W)
    Label_StatusDataWord9_Variable  = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord9).grid(row=2, column=7, sticky=W)
    Label_StatusDataWord10_Variable = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord10).grid(row=3, column=7, sticky=W)
    Label_StatusDataWord11_Variable = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord11).grid(row=4, column=7, sticky=W)
    Label_StatusDataWord12_Variable = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord12).grid(row=5, column=7, sticky=W)
    Label_StatusDataWord13_Variable = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord13).grid(row=6, column=7, sticky=W)
    Label_StatusDataWord14_Variable = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord14).grid(row=7, column=7, sticky=W)
    Label_StatusDataWord15_Variable = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord15).grid(row=8, column=7, sticky=W)
    Label_StatusDataWord16_Variable = Label(root, bg='grey', textvariable=Label_Rasp_Pi_StatusDataWord16).grid(row=9, column=7, sticky=W)

    Button_01_Spacer = Label(root, text="", bg='grey', fg='black')
    Button_01_Spacer.grid(row=11, columnspan=99, sticky=EW)

    Button_02_Spacer = Label(root, text="", bg='grey', fg='black')
    Button_02_Spacer.grid(row=12, columnspan=99, sticky=EW)

    Button_CtrlWord_Text_01  = Label(root, bg='grey', text="Ctrl Word #1").grid(row=13, column=0, sticky=E)

    Button_CtrlWord_Bit_00 = Button(root, text="Bit 0", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 0)).grid(row=13, column=2)
    Button_CtrlWord_Bit_01 = Button(root, text="Bit 1", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 1)).grid(row=13, column=3)
    Button_CtrlWord_Bit_02 = Button(root, text="Bit 2", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 2)).grid(row=13, column=4)
    Button_CtrlWord_Bit_03 = Button(root, text="Bit 3", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 3)).grid(row=13, column=5)
    Button_CtrlWord_Bit_04 = Button(root, text="Bit 4", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 4)).grid(row=13, column=6)
    Button_CtrlWord_Bit_05 = Button(root, text="Bit 5", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 5)).grid(row=13, column=7)
    Button_CtrlWord_Bit_06 = Button(root, text="Bit 6", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 6)).grid(row=13, column=8)
    Button_CtrlWord_Bit_07 = Button(root, text="Bit 7", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 7)).grid(row=13, column=9)

    Button_CtrlWord_Bit_08 = Button(root, text="Bit 8", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 8)).grid(row=14, column=2)
    Button_CtrlWord_Bit_09 = Button(root, text="Bit 9", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 9)).grid(row=14, column=3)
    Button_CtrlWord_Bit_10 = Button(root, text="Bit 10", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 10)).grid(row=14, column=4)
    Button_CtrlWord_Bit_11 = Button(root, text="Bit 11", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 11)).grid(row=14, column=5)
    Button_CtrlWord_Bit_12 = Button(root, text="Bit 12", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 12)).grid(row=14, column=6)
    Button_CtrlWord_Bit_13 = Button(root, text="Bit 13", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 13)).grid(row=14, column=7)
    Button_CtrlWord_Bit_14 = Button(root, text="Bit 14", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 14)).grid(row=14, column=8)
    Button_CtrlWord_Bit_15 = Button(root, text="Bit 15", fg="black", bg='grey', height=1, width=7, command=lambda: BitSet(1, 15)).grid(row=14, column=9)

    Entry_01_Spacer = Label(root, text="", bg='grey', fg='black')
    Entry_01_Spacer.grid(row=15, columnspan=99, sticky=EW)

    Entry_Text  = Label(root, bg='grey', text="Control Data").grid(row=16, column=0, sticky=E)

    Entry_01 = Entry(root, width=7).grid(row=16, column=2)
    Entry_02 = Entry(root, width=7).grid(row=16, column=3)
    Entry_03 = Entry(root, width=7).grid(row=16, column=4)
    Entry_04 = Entry(root, width=7).grid(row=16, column=5)
    Entry_05 = Entry(root, width=7).grid(row=16, column=6)
    Entry_06 = Entry(root, width=7).grid(row=16, column=7)
    Entry_07 = Entry(root, width=7).grid(row=16, column=8)
    Entry_08 = Entry(root, width=7).grid(row=16, column=9)

    Footer_01_Spacer = Label(root, text="", bg='grey', fg='black')
    Footer_01_Spacer.grid(row=98, columnspan=99, sticky=EW)

    Footer_01 = Label(root, text="---------------------------- Long Live Modbus ----------------------------", bg='grey', fg='black')
    Footer_01.grid(row=99, columnspan=99, sticky=EW)



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

        Write_Data_HR = list()
        Write_Data_HR.append(ControlCommandWord1)
        Write_Data_HR.append(ControlCommandWord2)
        Write_Data_HR.append(ControlCommandWord3)
        Write_Data_HR.append(ControlCommandWord4)
        Write_Data_HR.append(ControlDataWord1)
        Write_Data_HR.append(ControlDataWord2)
        Write_Data_HR.append(ControlDataWord3)
        Write_Data_HR.append(ControlDataWord4)
        Write_Data_HR.append(ControlDataWord5)
        Write_Data_HR.append(ControlDataWord6)
        Write_Data_HR.append(ControlDataWord7)
        Write_Data_HR.append(ControlDataWord8)

        write_HR_message_01 = tcp.write_multiple_registers(slave_id=1, starting_address=0, values=[1])
        write_HR_message_02 = tcp.write_multiple_registers(slave_id=1, starting_address=1, values=Write_Data_HR)
        read_HR_message_01 = tcp.read_holding_registers(slave_id=1, starting_address=100, quantity=7)
        read_IR_message_01 = tcp.read_input_registers(slave_id=1, starting_address=0, quantity=18)

        # Response depends on Modbus function code. This particular returns the
        # amount of coils written, in this case it is.
        write_HR_message_01_response = tcp.send_message(write_HR_message_01, sock)
        if ExecuteControlModbusWrite:
            write_HR_message_02_response = tcp.send_message(write_HR_message_02, sock)
            ExecuteControlModbusWrite = False
        read_HR_message_01_response = tcp.send_message(read_HR_message_01, sock)
        read_IR_message_01_response = tcp.send_message(read_IR_message_01, sock)

        for x in read_HR_message_01_response:
            Received_Data_HR.append(x)

        Label_Rasp_Pi_Hour.set(str(Received_Data_HR[0]))
        Label_Rasp_Pi_Minute.set(str(Received_Data_HR[1]))
        Label_Rasp_Pi_Second.set(str(Received_Data_HR[2]))
        Label_Rasp_Pi_uSecond.set(str(Received_Data_HR[3]))
        Label_Rasp_Pi_Year.set(str(Received_Data_HR[4]))
        Label_Rasp_Pi_Month.set(str(Received_Data_HR[5]))
        Label_Rasp_Pi_Day.set(str(Received_Data_HR[6]))

        for x in read_IR_message_01_response:
            Received_Data_IR.append(x)

        Label_Rasp_Pi_ProgramStatus.set(str(Received_Data_IR[0]))
        Label_Rasp_Pi_Temp.set(str(Received_Data_IR[1]))
        Label_Rasp_Pi_StatusDataWord1.set(str(Received_Data_IR[2]))
        Label_Rasp_Pi_StatusDataWord2.set(str(Received_Data_IR[3]))
        Label_Rasp_Pi_StatusDataWord3.set(str(Received_Data_IR[4]))
        Label_Rasp_Pi_StatusDataWord4.set(str(Received_Data_IR[5]))
        Label_Rasp_Pi_StatusDataWord5.set(str(Received_Data_IR[6]))
        Label_Rasp_Pi_StatusDataWord6.set(str(Received_Data_IR[7]))
        Label_Rasp_Pi_StatusDataWord7.set(str(Received_Data_IR[8]))
        Label_Rasp_Pi_StatusDataWord8.set(str(Received_Data_IR[9]))
        Label_Rasp_Pi_StatusDataWord9.set(str(Received_Data_IR[10]))
        Label_Rasp_Pi_StatusDataWord10.set(str(Received_Data_IR[11]))
        Label_Rasp_Pi_StatusDataWord11.set(str(Received_Data_IR[12]))
        Label_Rasp_Pi_StatusDataWord12.set(str(Received_Data_IR[13]))
        Label_Rasp_Pi_StatusDataWord13.set(str(Received_Data_IR[14]))
        Label_Rasp_Pi_StatusDataWord14.set(str(Received_Data_IR[15]))
        Label_Rasp_Pi_StatusDataWord15.set(str(Received_Data_IR[16]))
        Label_Rasp_Pi_StatusDataWord16.set(str(Received_Data_IR[17]))

        # Check if a bit in an integer is ON or OFF... (testing only)
        #x = BitCheck(65535, 15)
        #print(x)

        #print(Received_Data_HR)

        Received_Data_HR.clear()
        Received_Data_IR.clear()
        Write_Data_HR.clear()

        root.update_idletasks()
        root.update()

        sleep(0.1)



######################################################################################################################
# Finally block always gets executed either exception is generated or not...
finally:

    print('sock.close...')
    sock.close()
    sleep(0.5)

    print('Code Stopped...')
    exit()



######################################################################################################################
#def CheckBoxCmd(event):
#    root.update()
