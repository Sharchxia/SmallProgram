import time
import serial
import struct
from serial.tools import list_ports
from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil

# 定义arm_and_takeoff函数，使无人机解锁并起飞到目标高度
# 参数aTargetAltitude即为目标高度，单位为米
def arm_and_takeoff(aTargetAltitude):
    # 进行起飞前检查
    print("Basic pre-arm checks")
    # vehicle.is_armable会检查飞控是否启动完成、有无GPS fix、卡曼滤波器
    # 是否初始化完毕。若以上检查通过，则会返回True
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    # 解锁无人机（电机将开始旋转）
    print("Arming motors")
    # 将无人机的飞行模式切换成"GUIDED"（一般建议在GUIDED模式下控制无人机）
    vehicle.mode = VehicleMode("GUIDED")
    # 通过设置vehicle.armed状态变量为True，解锁无人机
    vehicle.armed = True
 # 在无人机起飞之前，确认电机已经解锁
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    # 发送起飞指令
    print("Taking off!")
    # simple_takeoff将发送指令，使无人机起飞并上升到目标高度
    vehicle.simple_takeoff(aTargetAltitude)

    # 在无人机上升到目标高度之前，阻塞程序
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # 当高度上升到目标高度的0.95倍时，即认为达到了目标高度，退出循环
        # vehicle.location.global_relative_frame.alt为相对于home点的高度
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        # 等待1s
        time.sleep(1)

#定义方向控制
def send_body_ned_velocity(velocity_x, velocity_y, velocity_z, duration=0):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_NED, # frame Needs to be MAV_FRAME_BODY_NED for forward/back left/right control.
        0b0000111111000111, # type_mask
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # m/s
        0, 0, 0, # x, y, z acceleration
        0, 0)
    vehicle.send_mavlink(msg)
        # time.sleep(1)

def check():
    global s
    _check = [0, 0, 0, 0, 0]
    s.reset_input_buffer()
    time.sleep(1)
    try:
        _check[0] = __convert_to_int(s.read(4).hex())
        s.write('0'.encode())
        _check[1] = __convert_to_int(s.read(4).hex())
        s.write('0'.encode())
        _check[2] = __convert_to_int(s.read(4).hex())
        s.write('0'.encode())
        _check[3] = __convert_to_int(s.read(4).hex())
        s.write('0'.encode())
        _check[4] = __convert_to_int(s.read(4).hex())
        s.write('0'.encode())
    except:
        pass
    print(_check)
    if sum(_check) >= 3:
        return True
    return False

def throw():
    global BACK_FLAG
    global s
    for i in range(3):
        s.write('1'.encode())
        time.sleep(0.1)
    time.sleep(4)
    BACK_FLAG = 1

def fly_and_check(dis, direction):
    global X_HAVE_FLIED, Y_HAVE_FLIED
    direction = direction % 4 if direction>=0 else 0
    t = int(dis / CRUISE_SPEED)
    print(t)
    x, y, z = 0, 0, 0
    for i in range(t):
       # while vehicle.location.global_relative_frame.alt <= HEIGHT * 0.95:
        #     send_body_ned_velocity(0, 0, RISE_SPEED)
        #     print('height is:', vehicle.location.global_relative_frame.alt)
        #     time.sleep(0.3)
        send_body_ned_velocity(0,0,RISE_SPEED)
        print('height is ', vehicle.location.global_relative_frame.alt)
        try:
            vehicle.wait_for_alt(alt=HEIGHT*0.95, timeout=5, epsilon=0.5)
        except:
            vehicle.VehicleMode('LAND')
            return
        if direction == 0:
            x, y, z = CRUISE_SPEED, 0, 0
        elif direction == 1:
            x, y, z = -CRUISE_SPEED, 0, 0
        elif direction == 2:
            x, y, z = 0, CRUISE_SPEED, 0
        elif direction == 3:
            x, y, z = 0, -CRUISE_SPEED, 0
        X_HAVE_FLIED += x
        Y_HAVE_FLIED += y
        send_body_ned_velocity(x, y, z)
        print('speed_x is %f, speed_y is %f, speed_z is %f, hight is %f' % (x,y,z,vehicle.location.global_relative_frame.alt))
        # if check():
        #     send_body_ned_velocity(0, 0, 0)
        #     throw()
        #     break

        time.sleep(1)

def back():
    throw()
    global X_HAVE_FLIED, Y_HAVE_FLIED
    total = (X_HAVE_FLIED**2+Y_HAVE_FLIED**2)**.5
    x = -X_HAVE_FLIED/total*BACK_SPEED
    y = -Y_HAVE_FLIED/total*BACK_SPEED
    t = int(total/BACK_SPEED)
    send_body_ned_velocity(x, y, 0)
    i = 0
    while i < t+1:
        if vehicle.location.global_relative_frame.alt <= HEIGHT * 0.95:
            send_body_ned_velocity(0, 0, RISE_SPEED)
            print('height is ', vehicle.location.global_relative_frame.alt)
            try:
                vehicle.wait_for_alt(alt=HEIGHT*0.95, timeout=5, epsilon=0.5)
                i -= 1
            except:
                break
        else:
            send_body_ned_velocity(x, y, 0)
        i += 1
        time.sleep(1)
    vehicle.VehicleMode("LAND")

def cruise(x_r=4, y_r=2):
    y_r = y_r/VIEW_REGION
    fly_times = 0
    while fly_times<=y_r*2 and not BACK_FLAG:
        fly_times += 1
        if fly_times % 4 == 1:
            fly_and_check(x_r, 0)
        elif fly_times % 4 == 3:
            fly_and_check(x_r, 1)

        if BACK_FLAG:
            break

        fly_times += 1
        fly_and_check(1.5, 2)

    if vehicle.location.global_relative_frame.alt <= HEIGHT * 0.95:
        send_body_ned_velocity(0, 0, RISE_SPEED)
        try:
            vehicle.wait_for_alt(alt=HEIGHT*.95, timeout=5, epsilon=0.5)
        except:
            vehicle.VehicleMode('LAND')
            return
    send_body_ned_velocity(0, 0, 0)
    
    back()


def list_p(length=12):  # 设置切割串口名称的长度，返回所有串口的列表，如果为0则不对名称进行切割
    portL = list_ports.comports()
    if len(portL) == 0:
        print('\033[0;32mNo ports available\033[0m')  # 没串口的情况
        return []
    else:
        for i in range(len(portL)):
            if length:
                portL[i] = str(portL[i])[:length]
            else:
                portL[i] = str(portL[i])
        return portL


def __convert_to_int(origin: str, small=True) -> int:  # 输入要求是长度为8的代表16进制的字符串
    num = 0
    try:
        if small:
            num = struct.unpack('<i', bytes.fromhex(origin))[0]  # 小端转换
        else:
            num = struct.unpack('>i', bytes.fromhex(origin))[0]  # 大端转换
    except Exception as e:
        pass
    print(origin)
    return num


if __name__ == '__main__':
    BACK_FLAG = 0
    BACK_SPEED = 4
    CRUISE_SPEED = 0.5
    RISE_SPEED = 1
    REGION_X = 6
    REGION_Y = 6
    VIEW_REGION = 2
    X_HAVE_FLIED, Y_HAVE_FLIED = 0, 0
    HEIGHT = 4
    SIGN = b'\xf2\x03\x00\x00\xf2\x03\x00\x00'
    s = None



    if len(list_p()):
        print('serial port is:',list_p()[0])
        s = serial.Serial(list_p()[0], 9600, timeout=0.05)
    #for i in range(100):
        #throw()
        #print(1)
        #time.sleep(0.5)

    # 改为当前连接的pixhawk飞控的端口
    #connection_string = '/dev/ttyUSB0'
    print('vehicle port is:', list_p()[1])
    connection_string = list_p()[1]
    print('Connecting to vehicle on: %s' % connection_string)
    # connect函数将会返回一个Vehicle类型的对象，即此处的vehicle
    # 即可认为是无人机的主体，通过vehicle对象，我们可以直接控制无人机
    vehicle = connect(connection_string, wait_ready=True, baud=921600)
    arm_and_takeoff(HEIGHT)
    cruise(REGION_X, REGION_Y)
    

