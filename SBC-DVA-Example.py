# Import all required libraries
import machine, sys
import SBC_DVA_lib
from time import sleep

if __name__ == '__main__':
    try:
        # Initialization of the INA236
        SBC_DVA_lib.reset_ina236(0x40)
        SBC_DVA_lib.init_ina236(0, 7, 4, 4, 0, 0)
        SBC_DVA_lib.calibrate_ina236()
        SBC_DVA_lib.mask_enable(1)
        SBC_DVA_lib.write_alert_limit()
        SBC_DVA_lib.read_alert_limit()
        sleep(5)
        SBC_DVA_lib.manufacturer_ID()
        SBC_DVA_lib.device_ID()
        print("start")
        while True:
            # Main loop
            print("Current [A]: " + str(SBC_DVA_lib.read_current()) + ", Power [W]: " + str(SBC_DVA_lib.read_power()) + ", Shunt [V]: " + str(SBC_DVA_lib.read_shunt_voltage()), ", Bus [V]: " + str(SBC_DVA_lib.read_bus_voltage()))
            sleep(1)

    except KeyboardInterrupt:
        sys.exit()