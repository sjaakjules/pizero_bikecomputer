![title](https://user-images.githubusercontent.com/12926652/89370669-47178000-d71c-11ea-896f-0d98f4cbd5da.jpg)

# Pi Zero Bikecomputer
a GPS and ANT+ bike computer based on Raspberry Pi Zero (W, WH)

# Table of Contents

- [Abstract](#abstract)
- [Features](#features)
- [Specs](#Specs)
- [Comparison with other bike computers](#comparison)
- [Parts List](#parts-list)
- [Assembly](#assembly)
- [Installation](#installation)
  - [macOS or Linux](#macOS-or-Linux)
  - [Raspberry Pi OS](#Raspberry-Pi-OS)
- [Quick Start](#quick-start)
  - [Run on X Window](#Run-on-X-Window)
  - [Run in a console](#Run-in-a-console)
- [Usage](#usage)
- [Q&A](#qa)


# Abstract

Pi Zero Bikecomputer is a GPS and ANT+ bike computer based on Raspberry Pi Zero(W, WH). This is the first DIY project in the world integrated with necesarry hardwares and softwares for modern bike computer. It measures and records position(GPS), ANT+ sensor(speed/cadence/power) and I2C sensor(pressure/temperature/accelerometer, etc). It also displays these values, even maps and courses in real-time. In addition, it write out log into .fit format file.

In this project, Pi Zero Bikecomputer got basic functions needed for bike computers. Next target is to add new functions which existing products do not have!

You will enjoy both cycling and the maker movement with Pi Zero Bikecomputer!

Here is detail articles in Japanese.

[I tried to make a bikecomputer, the result was pretty good](https://qiita.com/hishi/items/46619b271daaa9ad41b3)

[Let's make a bikecomputer with Raspberry Pi Zero (W, WH)](https://qiita.com/hishi/items/46619b271daaa9ad41b3)


<img width="841" alt="system-01" src="https://user-images.githubusercontent.com/12926652/90346486-3c39e500-e064-11ea-8613-712296515288.png">

<img width="841" alt="system-02" src="https://user-images.githubusercontent.com/12926652/90346717-7f955300-e066-11ea-94c5-69adcdd5bc7c.png">


# Features

- Easy to make
  - Use modules available at famous Maker stores.
  - Assemble in Raspberry Pi ecosystems.
  - Install with basic commands such as `apt-get install`, `pip` and `git` command.

- Customization
  - Only need modules you want to use. Pi Zero Bikecomputer detects your modules.

- Supports cross platform develop environments
  - Pi Zero Bikecomputer uses [Python](https://www.python.org) and [PyQt5](https://pypi.org/project/PyQt5/) GUI library. So, you can run on Raspberry Pi OS, some Linux, macOS and Windows.


# Specs

Some functions depend on your parts.

## General

| Specs | Detail | Note |
|:-|:-|:-|
| Logging | Yes | See as below |
| Sensors | Yes | See as below |
| Positioning | Yes | A GPS module is required. See as below. |
| GUI | Yes | See as below |
| Wifi | Yes | Built-in wifi |
| Battery life(Reference) | 18h | with 3000mAh mobile battery([Garmin Charge Power Pack](https://buy.garmin.com/en-US/US/p/571552)) and MIP Reflective color LCD. |

## Logging

| Specs | Detail | Note |
|:-|:-|:-|
| Stopwatch | Yes | Raw data is stored by sqlite3 |
| Lap | Yes | [Total, Lap, Pre lap] x [HR, Speed, Cadence, Power] |
| Cumulative value | Yes | [Total, Lap, Pre lap] x [Distance, Works, Ascent, Descent] |
| Auto stop | Yes |  |
| Recording insterval | 1s |  Smart recording is not supported. |
| Resume | Yes |  |
| Output .fit log file | Yes |  |
| Upload to STRAVA | Yes |  |
| Live sending | Yes | But I can't find a good dashboard service like as Garmin LiveTrack |

## Sensors

| Specs | Detail | Note |
|:-|:-|:-|
| ANT+ heartrate sensor |  Yes | ANT+ USB dongle is required. |
| ANT+ speed sensor |  Yes | ANT+ USB dongle is required. |
| ANT+ cadence sensor |  Yes | ANT+ USB dongle is required. |
| ANT+ speed&cadence sensor |  Yes | ANT+ USB dongle is required. |
| ANT+ powermeter |  Yes | ANT+ USB dongle is required. Calibration is not supported. |
| Bluetooth sensors |  No |  |
| Barometric altimeter | Yes | An I2c sensor(pressure, temperature) is required. |
| Accelerometer | Yes | An I2c sensor is required. |
| Magnetometer | Yes | An I2c sensor is required. |
| Light sensor | Yes | An I2c sensor is required. |

## Positioning

| Specs | Detail | Note |
|:-|:-|:-|
| Map | Yes | Support map tile format like OSM. So, offline map is available with local caches. |
| Course on the map| Yes | A course file(.tcx) is required. |
| Course profile | Yes | A course file(.tcx) is required. |
| Cuesheet | Yes | Use course points included in course files. |

- Map with [Toner Map](http://maps.stamen.com/)
  - Very useful with 2 colors displays (black and white).
  - <img src ="https://camo.qiitausercontent.com/0c2cf8d528b613a4665aa62170e2e9ee4a8ab90a/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3130303734312f38623335636566652d663836302d643662662d396366642d3963633336643561313863622e706e67" width=320 height=240 />
- Map with custimized [Mapbox](https://www.mapbox.com)
  - Use 8 colors suitable for MIP Reflective color LCD.
  - <img src ="https://camo.qiitausercontent.com/3dde7fcb864f8226c23332a30c33ab743b0b2b06/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3130303734312f66663366353439362d373266642d353831352d656533332d3437303862623364323565392e706e67" width=320 height=240 />
- Course profile
  -  <img src ="https://camo.qiitausercontent.com/e2d197a1cb6fea4341a8bc7dfd89be86dab3d784/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3130303734312f33393064333061652d653765632d623738652d346365322d3036303232313433663566612e706e67" width=320 height=240 />
- Display on PiTFT2.4
  - <img src ="https://pbs.twimg.com/media/EW5TJ96UMAAIXJq?format=png&name=900x900" width=500 height=375 />

## GUI

| Specs | Detail | Note |
|:-|:-|:-|
| Basic page(values only) | Yes |  |
| Graph | Yes | Altitude and performance(HR, PWR) |
| Customize data pages | Yes | With layout.yaml |
| ANT+ pairing | Yes |  |
| Adjust wheel size | Yes |  |
| Adjust altitude | Yes |  |
| Language localization | Yes | Font and translation file of items are required. |

- Performance graph
  - <img src ="https://camo.qiitausercontent.com/05c8c8facf076fbc3faf6abe848493ac0e82ffc1/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3130303734312f39316336643837382d666436632d383262652d663638642d6533303531323832356631662e706e67" width=320 height=240 />
- Language localization
  - <img src ="https://user-images.githubusercontent.com/12926652/90345269-3808ca00-e05a-11ea-91fe-42efbcd6040b.png" width=320 height=310 />


## Experimental functions

### ANT+ multiscan

it displays three of the people around you in the order in which you caught sensors using ANT+ continuous scanning mode.

- ![multiscan](https://camo.qiitausercontent.com/97904ae429c191677e9ece3cd113e07dfe8eefb2/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f3130303734312f33383765663432332d346631642d623332352d666235642d6638623434646332396564362e6a706567)


# Comparison with other bike computers

- 200km ride with Garmin Edge 830 and Pizero Bikecomputer ([strava activity](https://www.strava.com/activities/2834588492))

- ![title-03.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/100741/b355cb92-8e7f-6b3f-7cd0-98ba8803a56c.png)

| Items | Edge830 | Pi Zero Bikecomputer |
|:-:|:-:|:-:|
| Distance | 193.8 km  | 194.3 km  |
| Work |  3,896 kJ | 3,929 kJ  |
| Moving time | 9:12 | 9:04  |
| Total Ascent | 2,496 m | 2,569 m |


# Parts List

## [Raspberry Pi Zero W / WH](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)

<img src ="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F100741%2F41773d64-fc33-cc2a-190a-ce14b7b6b24c.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=393a8049c6f10a90dc8cc1f6e2030426" width=384 height=480 />

## Display

### [PiTFT 2.4](https://www.adafruit.com/product/2455) 

- (good) easy to assemble
- (bad) hard to see in direct sunshine
- <img src ="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F100741%2Fe16fc94e-7449-80df-c044-b8705789345e.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=ca5f5dcbdbe33f473187a50c2b585b81" width=480 height=360 />

### [MIP Reflective color LCD module 2.7" w/ backlight](https://international.switch-science.com/catalog/5395/) 

[Connection board for MIP Reflective color LCD to FRDM-K64F](https://international.switch-science.com/catalog/5393/) is also needed

- (good) very visible even in direct sunshine
- (good) ultra-low power consumption
- (bad) very expensive
- (bad) 8 colors only
- recomended if you don't think costs. Commercial products often uses a reflective LCD.
- ![MIP Reflective color LCD](https://qiita-user-contents.imgix.net/https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEV8NXnaVAAEjoFS%3Fformat%3Dpng%26name%3Dsmall?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=3b5218cc2e1d11c88eec77bbebadbaef)

### [PaPiRus ePaper / eInk Screen HAT for Raspberry Pi](https://uk.pi-supply.com/products/papirus-epaper-eink-screen-hat-for-raspberry-pi) or [DFRobot e-ink Display Module for Raspberry Pi 4B/3B+/Zero W](https://www.dfrobot.com/product-1866.html)

- (good) very visible
- (good) ultra-low power consumption
- (bad) slow drawing
- (bad) no backlight
- (bad) 2 colors only
- <img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEWcpqIRVcAECnhm%3Fformat%3Dpng%26name%3Dmedium?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=e63859ff88d76213591bfaab25111aca" width=480 height=360 />
PaPiRus ePaper / eInk Screen HAT for Raspberry Pi
- <img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEWvezNTXgAATZuN%3Fformat%3Dpng%26name%3Dmedium?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=5c0e572fce9492179d347bfb58e312fc" width=480 height=360 />
DFRobot e-ink Display Module for Raspberry Pi 4B/3B+/Zero W

## ANT+ USB dongle
- available in eBay or aliexpress
- also need micro USB OTG Adapter : like [adafruit adapter](https://www.adafruit.com/product/2910). 
- ![ANT+ USB dongle + USB OTG Adapter](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F100741%2F2a2639eb-7515-4dff-33d1-864a274a4919.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=348720e6c0bc82111195ac699fdc04b6)

## GPS module

UART with GPSd is recomended. I2C(Sparkfun qwiic or Adafruit STEMMA QT) is experimental.

### [SparkFun ZOE-M8Q](https://www.sparkfun.com/products/15193)

- UART, I2C(Sparkfun qwiic) and SPI
- an [antenna](https://www.sparkfun.com/products/15246) is also needed
- stable and low power consumption
- recommended as of 2020/6.

### [Akizuki Denshi GPS module](http://akizukidenshi.com/catalog/g/gK-09991/)

- UART
- easy to get in Tokyo (buy at Akihabara)
- cheap and low power consumption

### [Adafruit Mini GPS PA1010D](https://www.adafruit.com/product/4415)

- UART and I2C(Adafruit STEMMA QT)

### [Adafruit Ultimate GPS Breakout](https://www.adafruit.com/product/746)
- UART

## I2C sensors

Adafuit circuitpython library is required except some sensors(\*1). Refer to learing page of each sensors.

If you use Sparkfun Qwiic or Adafruit STEMMA QT sensors, [SparkFun Qwiic SHIM for Raspberry Pi](https://www.sparkfun.com/products/15794) is very useful for connecting sensors.

### pressure, temperature

for altitude, grade, and total ascent/descent

- [BMP280](https://shop.pimoroni.com/products/enviro-phat) (\*1)
- [BMP38X](https://www.dfrobot.com/product-1928.html)
- [LPS33HW](https://www.adafruit.com/product/4414) (\*1)

### IMU

Accelerometer is used for stop detection when using GPS.Magnetometer sensors are used in compasses. 

- [LSM303](https://shop.pimoroni.com/products/enviro-phat) (\*1); 
- [LSM6DS](https://www.adafruit.com/product/4485): Accel / Gyro
- [LSM9DS1](https://www.sparkfun.com/products/13944): Accel / Gyro / Mag 
- [LIS3MDL](https://www.adafruit.com/product/4485): Mag 
- [BMX160](https://www.dfrobot.com/product-1928.html): Accel / Gyro / Mag

### Light

for auto backlight when using MIP Reflective color LCD

- [TCS3472](https://shop.pimoroni.com/products/enviro-phat)
- [VCNL4040](https://www.adafruit.com/product/4161)

### Button

must required for displays which don't have buttons like MIP display

- [Button SHIM](https://shop.pimoroni.com/products/button-shim)

### Battery

get battery percent, etc.

- [PiJuice HAT](https://uk.pi-supply.com/products/pijuice-standard) / [PiJuice Zero](https://uk.pi-supply.com/products/pijuice-zero)

## SD card
- youw own (over 8GB)
- [SanDisk® High Endurance microSD™ Card](https://shop.westerndigital.com/products/memory-cards/sandisk-high-endurance-uhs-i-microsd#SDSQQNR-032G-AN6IA) is recommended if you use several years.

## Case

- make a nice case if you can use 3D printer.
- [Topeak SMARTPHONE DRYBAG 5"](https://www.topeak.com/global/en/products/weatherproof-ridecase-series/1092-smartphone-drybag-5%22) is easy to use. It is waterproof.


# Assembly

## Displays with headers (PiTFT or E-ink displays)

## Displays with non headers ()


# Installation

Assume Python version 3 environment. Version 2 is not supported.

## macOS or Linux

```
$ git clone https://github.com/hishizuka/pizero_bikecomputer.git
$ pip3 install PyQt5 numpy oyaml pillow
$ pip3 install git+https://github.com/hishizuka/pyqtgraph.git
$ cd pizero_bikecomputer
```

Note:
Pyqt version 5.15.0 in macOS has [a qpushbutton issue](https://bugreports.qt.io/browse/QTBUG-84852), so installing version 5.14.2 is recommended.


```
$ pip3 install PyQt5==5.14.2
```

## Raspberry Pi OS

Assume Raspberry Pi OS (32-bit) with desktop, not Raspberry Pi OS (32-bit) Lite. I haven't checked the procedure in Lite, but in the future I will try minimum OS such as Lite or buildroot.

Also, your Raspberry Pi is connected to internet and updated with `apt-get update & apt-get upgrade`.

Here is [my setup guide in Japanese](https://qiita.com/hishi/items/8bdfd9d72fa8fe2e7573).

### Common

Install in the home directory of default user "pi".

```
$ cd
$ git clone https://github.com/hishizuka/pizero_bikecomputer.git
$ sudo apt-get install python3-pip cython3 cmake gawk python3-numpy python3-pyqt5
$ sudo pip3 install oyaml
$ sudo apt-get install wiringpi python3-smbus python3-rpi.gpio python3-psutil python3-pil
$ sudo pip3 install git+https://github.com/hishizuka/pyqtgraph.git
$ cd pizero_bikecomputer
```

### GPS module

#### UART GPS

Assume Serial interface is on and login shell is off in raspi-config and GPS device is connected as /dev/ttyS0. If GPS device is /dev/ttyAMA0, modify gpsd config file(/etc/default/gpsd).

```
$ sudo apt-get install gpsd gpsd-clients python3-dateutil
$ sudo pip3 install gps3 timezonefinder 
$ sudo cp install/etc/default/gpsd /etc/default/gpsd
$ sudo systemctl enable gpsd
```

#### I2C GPS (experimental)

Assume I2C interface is on in raspi-config.

```
$ sudo apt-get install python3-dateutil
$ sudo pip3 install timezonefinder adafruit-circuitpython-gps
```


### USB ANT+ dongle

```
$ sudo apt-get install libusb-1.0-0 python3-usb
$ sudo pip3 install git+https://github.com/hishizuka/openant.git
$ sudo systemctl enable pigpiod
```


### Display

Assume SPI interface is on in raspi-config.

#### PiTFT 2.4

Follow [official setup guide](https://learn.adafruit.com/adafruit-2-4-pitft-hat-with-resistive-touchscreen-mini-kit/overview) of Adafruit, or [my setup guide (Japanese)](https://qiita.com/hishi/items/bdd630666277e4f8162a).

Additionally, install programs which to turn the PiTFT 2.4 backlight on and off.

```
$ sudo cp install/usr/local/bin/disable-pitft /usr/local/bin/
$ sudo cp install/usr/local/bin/enable-pitft /usr/local/bin/
```

Install the program which turns off the backlight at shutdown.

```
$ sudo cp install/etc/systemd/system/disable-pitft.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl enable disable-pitft.service
```

If you run the program in a console, you need to build Qt5 and PyQt5 because the package python3-pyqt5 provided with Raspbian OS does not include a touchscreen library(tslib).

Note:

The touchscreen does not work properly in Raspbian OS(Buster) + Qt　5.14(or higher) + PyQt 5.14(or higher) from some issues. So, if you use PiTFT, I recomand to run on X Window at present.
In Raspbian OS(Stretch) + Qt　5.12.3 + PyQt 5.12.3, the touchscreen works.

##### Build Qt

Follow ["Building Qt 5.12 LTS for Raspberry Pi on Raspbian"](https://www.tal.org/tutorials/building-qt-512-raspberry-pi) with Raspberry Pi 4 4GB or 8GB. Use the compile option "-platform linux-rpi-g++" for Raspberry Pi 1 or zero, not use options for Raspberry Pi 4 and so on.
Use the same SD card on Raspberry Pi 4.

You will need libts-dev package before configure of Qt. (from [RaspberryPi2EGLFS](https://wiki.qt.io/RaspberryPi2EGLFS))

```
sudo apt-get install libudev-dev libinput-dev libts-dev libxcb-xinerama0-dev libxcb-xinerama0
```

##### Build PyQt5

Follow [PyQt Reference Guide](https://www.riverbankcomputing.com/static/Docs/PyQt5/installation.html).
The source is avaiable [here](https://pypi.org/project/PyQt5/#files)

```
$ cd
$ mkdir work; cd work
$ wget NEWEST-PYQT5-PACKAGE-SOURCE-FILE
$ sudo pip3 install PyQt-builder
$ sip-build --no-make --qmake PATH-TO-YOUR-QMAKE
$ cd build
$ make -j4
$ sudo make install
$ sudo pip3 install PyQt5-sip
```

#### MIP Reflective color LCD module

You can use python3-pyqt5 package. Don't need building Qt.

```
$ sudo apt-get install python3-spidev python3-pigpio
$ sudo pip3 install spidev --upgrade
$ sudo systemctl enable pigpiod
$ sudo systemctl start pigpiod
```

#### E-ink Displays

You can use python3-pyqt5 package too.

##### PaPiRus ePaper / eInk Screen HAT for Raspberry Pi

Follow [official setup guide](https://github.com/PiSupply/PaPiRus)

##### DFRobot e-ink Display Module for Raspberry Pi 4B/3B+/Zero W

Follow [official setup guide](https://wiki.dfrobot.com/Raspberry_Pi_e-ink_Display_Module_SKU%3A_DFR0591) and install manually.


### I2C sensors

Assume I2C interface is on in raspi-config.

#### Main sensors (pressure, temperature, IMU and light)

Install pip packages of the sensors you own.

Here is an example.
```
$ sudo pip3 install adafruit-circuitpython-bmp280
```

| Maker | Sensor | additional pip package |
|:-|:-|:-|
| [Pimoroni](https://shop.pimoroni.com) | [Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat) | None |
| [Adafruit](https://www.adafruit.com) | [BMP280](https://www.adafruit.com/product/2651) | adafruit-circuitpython-bmp280 |
| [Adafruit](https://www.adafruit.com) | [LPS33HW](https://www.adafruit.com/product/4414) | adafruit-circuitpython-lps35hw |
| [Strawberry Linux](https://strawberry-linux.com) | [LPS33HW](https://strawberry-linux.com/catalog/items?code=12133) | None |
| [DFRobot](https://www.dfrobot.com) | [BMX160+BMP388](https://www.dfrobot.com/product-1928.html) | adafruit-circuitpython-bmp3xx, BMX160(*1) | 
| [Adafruit](https://www.adafruit.com) | [LSM6DS33 + LIS3MDL](https://www.adafruit.com/product/4485) | adafruit-circuitpython-lsm6ds adafruit-circuitpython-lis3mdl |
| [Adafruit](https://www.adafruit.com) | [LSM9DS1](https://www.adafruit.com/product/4634) | adafruit-circuitpython-lsm9ds1 | 
| [Adafruit](https://www.adafruit.com) | [VCNL4040](https://www.adafruit.com/product/4161) | adafruit-circuitpython-vcnl4040 |

*1 Install manually https://github.com/spacecraft-design-lab-2019/CircuitPython_BMX160


#### Button SHIM

```
$ sudo apt-get install buttonshim
```

#### PiJuice HAT

Follow [official setup guide](https://github.com/PiSupply/PiJuice/tree/master/Software) of PiSupply/PiJuice


# Quick Start

## Run on X Window

If you run the program from SSH login shell, add the following environment variable.

```
export DISPLAY=:0.0
```

Then, run the program.

```
$ python3 pizero_bikecomputer.py -f
```

### Run from the lancher menu.

Making launcher menu or desktop icon may be useful.

![lancher menu](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F100741%2Fc466c6f0-ede8-5de2-2061-fbbbcccb93fc.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=864176ddffe3895226a6fd8bf20fb4d0)

Make "New Item" in Main Menu Editor, and set "/home/pi/pizero_bikecomputer/exec.sh" in "Command:" field.

![short cut](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F100741%2Fe318acf1-3c89-0537-956c-9e64738b8f81.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&w=1400&fit=max&s=fedb51b245af88bffc2e090031cf10a3)

### Run with autostart

If you are using the autologin option, you can run the program automatically using the following procedure。

```
$ mkdir -p ~/.config/lxsession/LXDE-pi
$ cp /etc/xdg/lxsession/LXDE-pi/autostart ~/.config/lxsession/LXDE-pi/
$ echo "@/home/pi/pizero_bikecomputer/exec.sh" >> ~/.config/lxsession/LXDE-pi/autostart
```

## Run in a console

### manual execution

#### PiTFT

Before run the program, add the following environment variables.

```
$ export QT_QPA_PLATFORM=linuxfb:fb=/dev/fb1
$ export QT_QPA_EVDEV_TOUCHSCREEN_PARAMETERS=/dev/input/event0:rotate=270
$ export QT_QPA_FB_TSLIB=1
$ export TSLIB_FBDEVICE=/dev/fb1
$ export TSLIB_TSDEVICE=/dev/input/event0
$ python3 pizero_bikecomputer.py
```

#### MIP Reflective color LCD module or E-Ink displays

Before run the program, add the following environment variable.

```
$ export QT_QPA_PLATFORM=offscreen
$ python3 pizero_bikecomputer.py
```

### run as a service

If you use displays in console environment not X Window, install auto-run service and shutdown service.

#### auto-run service

If you use MIP Reflective color LCD module or E-Ink displays, modify install/etc/systemd/system/pizero_bikecomputer.service.

```
ExecStart=/home/pi/pizero_bikecomputer/exec-mip.sh
```

Install servece scripts.

```
$ sudo cp install/etc/systemd/system/pizero_bikecomputer.service /etc/systemd/system/
$ sudo cp install/usr/local/bin/pizero_bikecomputer_shutdown /usr/local/bin/
$ sudo cp install/etc/systemd/system/pizero_bikecomputer_shutdown.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl enable pizero_bikecomputer.service
$ sudo systemctl enable pizero_bikecomputer_shutdown.service
```

#### test

The output of the log file will be in "./log/debug.txt".

```
$ sudo systemctl start pizero_bikecomputer.service
```


# Usage


```
$ python3 pizero_bikecomputer.py --demo
```

Temporarily use with map downloading. A course file is required(see [Usage](Usage)). After launching the program, go to the map screen.


# Q&A


# License

This repository is available under the [GNU General Public License v3.0](https://github.com/hishizuka/pizero_bikecomputer/blob/master/LICENSE)

# Author

[hishizuka](https://github.com/hishizuka/) ([@pi0bikecomputer](https://twitter.com/pi0bikecomputer) at twitter)
