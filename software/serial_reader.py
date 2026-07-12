import serial

PORT = "COM6"
BAUD_RATE = 9600

def read_serial_data():

    try:
        arduino = serial.Serial(PORT, BAUD_RATE, timeout=1)

        while True:

            if arduino.in_waiting:

                data = arduino.readline().decode().strip()

                print(data)

    except Exception as e:

        print("Connection Error:", e)


if __name__ == "__main__":
    read_serial_data()
