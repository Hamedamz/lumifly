This prototype uses [iFlight BLITZ Whoop F7 AIO](https://shop.iflight.com/BLITZ-Whoop-F7-AIO-Pro1927) which is a all-in-one flight controller with built-in ESC.

## Default firmware on flight controller (December 2024)
```
# version
# Betaflight / STM32F745 (S745) 4.5.1 Jul 27 2024 / 07:57:01 (77d01ba3b) MSP API: 1.46
# config rev: 11c7dec
# board: manufacturer_id: IFRC, board_name: IFLIGHT_BLITZ_F7_AIO
```

## Flash iNav to the flight controller.
The default firmware on the BLITZ Whoop F7 AIO is BetaFlight. Here is how to flash iNav to it. This guide is partially based on [this video](https://www.youtube.com/watch?v=xdf3yhlgJyc).

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


## Power the Raspberry Pi
Connect the GND and 5V pins of the flight controller to the raspberry pi. See [this guide](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio) for Raspberry Pi pins and [this](https://ardupilot.org/plane/docs/common-iflight-blitzf7AIO.html#pinout) for the flight controller pins.
I used [Molex connectors](https://a.co/d/1OW0Edu).


## UART Connection
SERIAL4 and SERIAL7 pins are free for custom applications. See [here](https://ardupilot.org/plane/docs/common-iflight-blitzf7AIO.html#pinout).
I used SERIAL4 (T4 and R4 ports) and [enameled wires](https://a.co/d/74X3URF) for the communication of Raspberry Pi with the flight controller.

1. Connect the TX pin of the Raspberry Pi to the RX pin of the flight controller.
2. Connect the RX pin of the Raspberry Pi to the TX pin of the flight controller.
3. Connect to the flight controller using the iNAV Configurator.
4. Go to the Ports tab.
5. Find the UART connected to the Raspberry Pi.
6. Enable the MSP protocol for that UART.
7. Configure the raspberry pi to enable UART:
   - add the following lines to the `/boot/firmware/config.txt`:
     ```
     enable_uart=1
     dtoverlay=disable-bt
     ```
   - Ensure there is no line like `console=serial0,115200` in `/boot/firmware/cmdline.txt`. If present, remove it to prevent the Raspberry Pi from using UART for console output.
   - reboot Raspberry Pi: `sudo reboot`
8. Power up the drone.
9. Run `test.py` to test the communication.

### Troubleshoot
- Ensure TX and RX pins are properly connected (use GPIO 14 for TX and GPIO 15 for RX).
- Use a multimeter or a simple circuit like an LED and a battery to test the connections of UART pins.
- Ensure `ls -l /dev/serial*` shows an entry.
- Ensure the baud rate is set correctly (115200 is typical for iNAV).