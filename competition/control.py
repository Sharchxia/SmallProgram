import serial
from serial.tools import list_ports

def list_p(length=12):  # 设置切割串口名称的长度，返回所有串口的列表，如果为0则不对名称进行切割
    portL = list_ports.comports()
    if len(portL) == 0:
        print('\033[0;32mNo ports available\033[0m')  # 没串口的情况
        return []
    else:
        for i in range(len(portL)):
            print(str(portL[i]))
            if length:
                portL[i] = str(portL[i])[:length]
            else:
                portL[i] = str(portL[i])
        print()
        return portL

def connect(port:str):
    s = serial.Serial(port, 9600, timeout=0.05)
    return s	

def control(flag: str, target):
    flag = flag.encode()
    while True:
        print('<<<', end='')
        s = input()
        if s=='quit':
            break
        else:
            target.write(flag)
		
	
if __name__ == '__main__':
    p = list_p()[0]
    ser = connect(p)
    control('1', ser)
