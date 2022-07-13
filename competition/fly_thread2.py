import time
import serial
import struct
from serial.tools import list_ports
from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
from threading import Thread
import RPi.GPIO as GPIO

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

def check():
    global THROW_FLAG, THROW_TIME
    time.sleep(2)
    _check = [0, 0, 0, 0, 0]
    _check_index = 0
    while THROW_TIME < 2:
        try:
            _check[_check_index] = __convert_to_int(com_port.read(4).hex())
            _check_index = 0 if _check_index >= 4 else _check_index + 1

            print('\033[0;32mElements in check array are \033[0m:',_check)
            if sum(_check) >= credible_threshold and not THROW_FLAG:  # if condition is fitted
                THROW_TIME += 1
                THROW_FLAG = 1
                print('\033[0;36m=====================================================')
                print('=====================================================\033[0m')
                print('\033[0;33mA credible object has been detected, the target number is %d\033[0m' % (THROW_TIME))
                print('\033[0;32mElements in target array are \033[0m:',_check)
                print('\033[0;36m=====================================================')
                print('=====================================================\033[0m')
            
                _check = [0, 0, 0, 0, 0]
                time.sleep(5)
                com_port.reset_input_buffer()
            if BACK_FLAG or LAND_FLAG:
                break
        except:
            print('\033[0;31mSome Errors occured in com_port\033[0m')
            break
    print('\033[0;35m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!!!\033[0mCom-port thread has stopped\033[0;35m!!!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\033[0m')

def throw(flag):
    print('\033[0;32mGoods will be throwed\033[0m')
    if flag == 1:
        print('first')
        pwm.ChangeDutyCycle(4.5)
    elif flag == 2:
        pwm.ChangeDutyCycle(6.8)
        print('second')

def fly_and_check(flag=0):
    global X_HAVE_FLIED, Y_HAVE_FLIED, LAND_FLAG, THROW_FLAG, BACK_FLAG
    one_distance = (REGION_X**2+REGION_Y**2)**0.5
    fly_time = one_distance/CRUISE_SPEED  # get the time of vehicle flying in x direction
    print('\033[0;32mTime for flying in this direction is:\033[0m', fly_time)

    x_speed = REGION_X/one_distance*CRUISE_SPEED
    y_speed = REGION_Y/one_distance*CRUISE_SPEED
    x, y, z = 0, 0, 0
    have_fly = 0
    while have_fly < fly_time:
        have_fly += TIME_RANGE
        x, y, z = 0, 0, RISE_SPEED
        send_body_ned_velocity(x, y, z)
        print('\033[0;32mHeight is:\033[0m ', vehicle.location.global_relative_frame.alt)
        try:
            vehicle.wait_for_alt(alt=HEIGHT, timeout=5, epsilon=0.5)
            send_body_ned_velocity(0, 0, 0)
        except:
            print('\033[0;31mTimeout while rising in fly process, vehicle will land\033[0m')
            LAND_FLAG = 1
            return
        
        if THROW_FLAG:
            send_body_ned_velocity(0, 0, 0)
            time.sleep(0.5)
            throw(THROW_TIME)
            # time.sleep(2.5)
            THROW_FLAG = 0
            BACK_FLAG = 1
            break
            if THROW_TIME == 2:
                throw(THROW_TIME)
                time.sleep(0.2)
                BACK_FLAG = 1
                break
        
        if flag%2:
            x, y, z = x_speed, y_speed, 0
        else:
            x, y, z = x_speed, -y_speed, 0
        send_body_ned_velocity(x, y, z)
        time.sleep(TIME_RANGE)

        X_HAVE_FLIED += x * TIME_RANGE
        Y_HAVE_FLIED += y * TIME_RANGE

        print('Speed_\033[0;32mx\033[0m is %f, speed_\033[0;32my\033[0m is %f, speed_\033[0;32mz\033[0m is %f, \033[0;32mhight\033[0m is %f' % (x,y,z,vehicle.location.global_relative_frame.alt))

def back():
    global X_HAVE_FLIED, Y_HAVE_FLIED, LAND_FLAG
    print('\033[0;33mBegin to go back\033[0m')
    total = (X_HAVE_FLIED**2+Y_HAVE_FLIED**2)**.5  # calculate the total straight distance vehicle would fly
    x_speed = -X_HAVE_FLIED/total*BACK_SPEED
    y_speed = -Y_HAVE_FLIED/total*BACK_SPEED

    have_fly = 0
    fly_time = total/BACK_SPEED

    print('\033[0;32mBacing distance is:\033[0m', total)
    print('\033[0;32mTime needed is \033[0m%d, \033[0;32mVelocity in x-direction is \033[0m%f, \033[0;32mVelocity in y-direction is \033[0m%f' % ( fly_time, x_speed, y_speed))
    

    while have_fly < fly_time:
        have_fly += TIME_RANGE
        x, y, z = 0, 0, RISE_SPEED
        if vehicle.location.global_relative_frame.alt <= HEIGHT:
            send_body_ned_velocity(x, y, z)
            print('\033[0;32mHeight is:\033[0m ', vehicle.location.global_relative_frame.alt)
        try:
            print('\033[0;34mRising to keep safe\033[0m')
            vehicle.wait_for_alt(alt=HEIGHT, timeout=5, epsilon=0.5)
            send_body_ned_velocity(0, 0, 0)
        except:
            print('\033[0;31mTimeout while rising in backing process, vehicle will land\033[0m')
            print('\033[0;33mLanding command has been operated\033[0m')
            vehicle.mode = VehicleMode('LAND')
            LAND_FLAG = 1
            return
        x, y, z = x_speed, y_speed, 0
        send_body_ned_velocity(x, y, 0)
        time.sleep(TIME_RANGE)
    time.sleep(1)
    vehicle.mode = VehicleMode("LAND")
    LAND_FLAG = 1
    print('\033[0;32mLanding command has been operated\033[0m')

def cruise(turn_time=0):
    global BACK_FLAG
  
    fly_times = 0
    while fly_times < turn_time:
        fly_and_check(fly_times)
        fly_times += 1

        if LAND_FLAG:
            print('\033[0;33mLanding command has been operated\033[0m')
            vehicle.mode = VehicleMode('LAND')
            return

        send_body_ned_velocity(0, 0, 0)
        if BACK_FLAG:
            break

    
    BACK_FLAG = 1
    send_body_ned_velocity(0, 0, 0)
    back()


def list_p(length=12):  # 设置切割串口名称的长度，返回所有串口的列表，如果为0则不对名称进行切割
    portL = list_ports.comports()
    if len(portL) == 0:
        print('\033[0;32mNo ports available\033[0m')  # 没串口的情况
        return []
    else:
        for i in range(len(portL)):
            print(i, str(portL[i]))
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
    except:
        pass
    return num


if __name__ == '__main__':
    THROW_FLAG = 0
    LAND_FLAG = 0
    THROW_TIME = 0
    BACK_FLAG = 0

    # Speeds that vehicle would take in the proess
    BACK_SPEED = 2  # m/s
    CRUISE_SPEED = 0.3# m/s
    RISE_SPEED = 0.15  # m/s
    TIME_RANGE = 0.1  # seconds

    # Distance that vehicle would fly through.
    # And some other parameter for space
    REGION_X = 6  # meters
    REGION_Y = 3  # meters
    TURN_T = 3 
    HEIGHT = 3.6  # meters

    # Variables recording distances that have been passed through
    X_HAVE_FLIED, Y_HAVE_FLIED = 0, 0 

    # A value between 0 and 5. if the number of times of detecting a target is not smaller than this value, the hanging object would be tossed
    credible_threshold = 1  # an integer is smaller than 6 and bigger than 0
    
    # All ports that are connected to this Raspberry-pi
    ports = list_p()

    pwm_pin = 18

    if len(ports):
       # print('\033[0;32mPlease enter the index of port used as com-seria:\033[0m', end=' ')
       # com_serial = int(input())
        #print('\033[0;32mPlease enter the index of port used as vehicle-serial:\033[0m', end=' ')
       # vehicle_serial = int(input())
       # print('\033[0;32mcom-serial port is:\033[0m',ports[com_serial])
        com_port = serial.Serial("/dev/artpi", 9600, timeout=0.2)
        # 改为当前连接的pixhawk飞控的端口
        #connection_string = '/dev/ttyUSB0'
        #print('\033[0;32mvehicle port is:\033[0m', ports[vehicle_serial])
        connection_string = '/dev/feikong'
        print('Connecting to vehicle on: %s' % connection_string)
        #connect函数将会返回一个Vehicle类型的对象，即此处的vehicle
        #即可认为是无人机的主体，通过vehicle对象，我们可以直接控制无人机
        vehicle = connect(connection_string, wait_ready=True, baud=921600)

        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pwm_pin, GPIO.OUT)
        pwm = GPIO.PWM(pwm_pin, 50)
        pwm.start(0)
        try:
            pwm.ChangeDutyCycle(2)
            time.sleep(0.5)
            arm_and_takeoff(HEIGHT)
            detect_thread = Thread(target=check)
            detect_thread.start()
            cruise(TURN_T)
            pwm.ChangeDutyCycle(2)
            time.sleep(0.2)
            pwm.stop()
            GPIO.cleanup()
            print('++++++++++++++++++++++++++++++++++++')
            print('++ Main thread has finished tasks ++')
            print('++++++++++++++++++++++++++++++++++++')
        except:
            vehicle.mode = VehicleMode('LAND')
            BACK_FLAG = 1
            LAND_FLAG = 1
            pwm.ChangeDutyCycle(2)
            time.sleep(1)
            pwm.stop()
            GPIO.cleanup()
        finally:
            vehicle.mode = VehicleMode('LAND')
    else:
        print('\033[0;33mNo available port\033[0m')
    

