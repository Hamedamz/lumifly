# LumiFly
A prototype for flying light specks

![image](images/assembled_drone.jpeg)

## Steps to reproduce
1. Flash the firmware to the flight controller
2. Connect the motors and other connections
3. Test the direction of rotation for each motor
4. Assemble the parts on the frame
5. Configure the flight controller and Raspberry Pi


## List of parts
1. [iFlight BLITZ Whoop F7 AIO flight controller](https://shop.iflight.com/BLITZ-Whoop-F7-AIO-Pro1927) (1X)
2. [1404 Plus 6000kv motors](https://www.myfpvstore.com/motors/rcinpower-smoox-1404-plus-whoop-motor-gunmetal-blue-6000kv/?srsltid=AfmBOoqFCYuKe_lZ4RztSoZIATdFEbraSl6UrF0mSqzx-S929OD5cDPk4uk) (4X)
3. [HQ Prop T3X2X3 Tri-Blade 3" Prop 4 Pack 1.5mm Shaft](https://www.racedayquads.com/products/hq-prop-t3x2x3-1-5mm-shaft-tri-blade-3-prop-4-pack-choose-color?currency=USD&variant=40070619332721&stkn=ed68f1cb6bdd&tw_source=google&tw_adid=717685084952&tw_campaign=21821665874&gad_source=1&gclid=Cj0KCQiA0fu5BhDQARIsAMXUBOJjdMI9eP1X8UswLH8dP3WppF2tAKTShEN8dZYi1DE7O35mmgM2xEEaAqgSEALw_wcB) (1X)
4. [Raspberry Pi Zero 2 W + SD card with Raspberry OS](https://www.pishop.us/product/raspberry-pi-zero-2-w/?src=raspberrypi) (1X)
5. [Raspberry Pi Camera Module 3 Wide NoIR](https://www.pishop.us/product/raspberry-pi-camera-module-3-wide-noir/) (1X)
6. [Lipo Battery 850mAh 80C 11.1V 3S](https://a.co/d/hYqlLo6) (1X)
7. [4pcs XT30 XT-30 to XT60 XT-60 Male Female RC Connector Adapter](https://a.co/d/1hygTM4) (1X)
8. [M2 screws](https://a.co/d/6PfypLR) (1X)
9. [Enameled copper wire](https://a.co/d/gU8BKby) (1X)
10. [Charger](https://a.co/d/1dvDkIm) (1X)
11. [Molex connectors](https://a.co/d/1OW0Edu)

## Flash iNav to the flight controller.
This prototype uses iFlight BLITZ Whoop F7 AIO which is a all-in-one flight controller with built-in ESC.
The default firmware on the BLITZ Whoop F7 AIO is BetaFlight. Here is how to replace it with iNav. This guide is partially based on [this video](https://www.youtube.com/watch?v=xdf3yhlgJyc).

```
default firmware (December 2024):
# version
# Betaflight / STM32F745 (S745) 4.5.1 Jul 27 2024 / 07:57:01 (77d01ba3b) MSP API: 1.46
# config rev: 11c7dec
# board: manufacturer_id: IFRC, board_name: IFLIGHT_BLITZ_F7_AIO
```

1. Download and install the latest and stable version of [iNav Configurator](https://github.com/iNavFlight/inav-configurator/releases).
2. Download and install the latest and stable version of [BetaFlight Configurator](https://github.com/betaflight/betaflight-configurator/releases).
3. Since at the time of writing this, there is no official target for the BLITZ Whoop F7 AIO, we need to use [an unofficially built target](https://github.com/iNavFlight/inav/pull/8988#issuecomment-2208333643). The file is also available in the `flight_controller/inav_target/inav_7.1.2_IFLIGHT_BLITZ_F7_AIO.hex` folder.
See these for more details:
   - [source coed of the target](https://github.com/iNavFlight/inav/tree/master/src/main/target/IFLIGHT_BLITZ_F7_AIO)
   - [target pull request](https://github.com/iNavFlight/inav/pull/8977)
   - [A reddit thread about the target](https://www.reddit.com/r/fpv/comments/1bs79lq/hi_for_the_blitz_f745_do_you_guys_know_which/)
4. Open iNav Configurator. If you have issues running the application on Mac, run the following command.
    ```
    xattr -cr path/to/INAV\ Configurator.app
    ```
5. Connect the flight controller to the computer via USB.
6. Hit the `Connect` button. It should automatically navigate to the CLI tab in the iNav Configurator.
7. Write `verson` command and hit enter.
8. Save the output to a file for your reference. This is for when we want to revert to the original firmware if needed.
9. Hit the `Disconnect` button. Keep the USB cable connected to the computer.
10. Close iNav Configurator.
11. Open BetaFlight Configurator.
12. Hit the `Connect` button.
13. Go to the `Presets` tab.
14. Hit the `Save Backup` button and save the file.
15. Also, if you have configured the ports already take a note of the configurations in the `Ports` tab as well.
16. Close BetaFlight Configurator.
17. Open iNav Configurator.
18. Hit the `Connect` button.
19. Go to the `Firmware Flasher` tab.
20. First hit the `Auto-selct Target` to see if it can find any official targets.
21. If it showed "Connot prefetch firmware: Non-iNav firmware", search manually by typing `iflight` in the search targets... field.
22. Open the `Choose a Board` dropdown to see if it has "BLITZ Whoop F7 AIO".
23. If not, hit the `Load Firmware [Local]` button in the bottom right corner and select `inav_7.1.2_IFLIGHT_BLITZ_F7_AIO.hex` file.
24. Hit the `Flash Firmware` button.
25. After it's flashed successfully, hit the `Connect` button again.
26. It will ask you about what kind of UAV you are building, I chose Mini Qual with 3" Propellers.

## Connections
1. Measure and cut the motor's wires (I kept around 32 mm).
2. Solder the wires to the motor pins on the flight controller board. For now the order of the wires doesn't matter we'll test the rotation direction in the next step and reorder them if necessary. You can use the pins on either side of the board. I used the upper part (where the USB port is present)
3. Solder the XT30 wire to the power pins (red to the + and black to -). I used the upper side pins.
4. Solder the capacitor the power pins, pay attention to the - and + pins. I connected the capacitor to the bottom side.
5. Connect the male Molex connector to the 5V and GND pins of the flight controller (red to 5V and black to the GND).
6. See [this guide](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio) for Raspberry Pi pins and [this](https://ardupilot.org/plane/docs/common-iflight-blitzf7AIO.html#pinout) for the flight controller pins.
I used [Molex connectors](https://a.co/d/1OW0Edu).
7. Cut two pieces of 10-cm enameled copper wire and solder them to the T4 and R4 pins on the flight controller board.
   TIP: make sure the coating of the enameled wire melts as you solder them for proper connection.
8. Connect the TX pin of the Raspberry Pi to the RX pin of the flight controller.
9. Connect the RX pin of the Raspberry Pi to the TX pin of the flight controller.
![image](images/fc_raspberry_connection.jpeg)
![image](images/raspberry_fc_connection.jpeg)

## Test motor
Note: remove the propellers before testing the motors.

1. Connect to the flight controller using the iNAV Configurator.
2. Go to the Outputs tab.
3. In the Configuration section `enable motor and servo output`. Then, click `Save and Reboot`.
4. Connect again and go to the Outputs tab.
5. In the Motor section enable `I understand the risks, propellers are removed - Enable motor control.`Reboot might be required to enable motor control.
6. Place the motors in the correct direction in front of you. M2 and M4 are the front motors. The white arrow printed on the flight controller board shows the front direction, in our setup it should be facing the table. Note that the motors are facing down in this setup.
   ![image](images/parts_top_view.jpeg) 
7. Connect a battery to the flight controller.
8. Spin each motor slowly and feel the direction of rotation with your fingers.
9. If the motor is rotating in the wrong direction note its number.
10. Grab your solder and swap any two wires of the motor with wrong direction to reverse its rotation direction.
11. Finally, test one more time to make sure each motor rotates in the direction shown in the picture (M1 and M4 cw, M2 and M3 ccw).

## Connect Raspberry Pi to the flight controller

### Power
Connect the GND and 5V pins of the flight controller to the corresponding pins of Raspberry Pi. See [this guide](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio) for Raspberry Pi pins and [this](https://ardupilot.org/plane/docs/common-iflight-blitzf7AIO.html#pinout) for the flight controller pins.
I used [Molex connectors](https://a.co/d/1OW0Edu).

### UART Connection
SERIAL4 and SERIAL7 pins are free for custom applications. See [here](https://ardupilot.org/plane/docs/common-iflight-blitzf7AIO.html#pinout).
I used SERIAL4 (T4 and R4 ports) for the communication of Raspberry Pi with the flight controller.

1. Connect to the flight controller using the iNAV Configurator.
2. Go to the Ports tab.
3. Find the UART connected to the Raspberry Pi.
4. Enable the MSP protocol for that UART.
5. Configure the raspberry pi to enable UART:
   - add the following lines to the `/boot/firmware/config.txt`:
     ```
     enable_uart=1
     dtoverlay=disable-bt
     ```
   - Ensure there is no line like `console=serial0,115200` in `/boot/firmware/cmdline.txt`. If present, remove it to prevent the Raspberry Pi from using UART for console output.
   - reboot Raspberry Pi: `sudo reboot`
6. Power up the drone via a battery.
7. Run `uart/test.py` on the Raspberry Pi to test the communication.

### Troubleshoot
- Ensure TX and RX pins are properly connected (use GPIO 14 for TX and GPIO 15 for RX).
- Use a multimeter or a simple circuit like an LED and a battery to test the connections of UART pins.
- Ensure `ls -l /dev/serial*` shows an entry.
- Ensure the baud rate is set correctly (115200 is typical for iNAV).