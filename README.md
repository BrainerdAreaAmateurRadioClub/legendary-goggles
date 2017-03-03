##  Working on instructions for building APRS WX Station with Raspberry Pi - Mitch Ahrenstorff AD0HJ - 03/02/17
Use a Raspberry Pi 3 Model B to collect data from your personal weather station, display weather information in HTML format, continouously upload weather data to many popular weather sites, and transmit APRS weather information.

![400px-apruptx0004](https://cloud.githubusercontent.com/assets/25856695/23232743/058d03d0-f912-11e6-9278-4623a960dc05.jpg)

## Getting Started
WeeWX is the software that we will use in this project to collect, display, and upload information from our Personal Weather Station.  The ability of WeeWX to allow add-on drivers and services is what makes it flexible enough to not only gather data from a large selection of weather instruments but also generate the output that we will need to source to our APRS software.  In addition, WeeWX will generate HTML formatted reports for display on a monitor or website and push data to weather collection services like WeatherUnderground, PWSweather.com, and the Civilian Weather Observation Program.

Any Personal Weather Station that you intend to use or purchase will need to have either WeeWX serial/USB, WeeWX extension driver, or rtl_433 driver support for interfacing with the WeeWX software.  Take a look at the WeeWX Hardware Guide, the WeeWX GitHub Wiki, and the rtl_433 GitHub site to see what support is offered for your Personal Weather Station.  




There are a few items that you will need to consider before setting up your own Raspberry Pi 3 APRS WX Station.
- What weather information will I want to gather and display?
- How will I get data from my Personal Weather Station in the WeeWX software?
- Will my Raspberry Pi 3 have a dedicated setup or will it be accessed remotely?
- Will I have access to the internet through either ethernet or wireless?
- How will I power the Raspberry Pi 3?
- Send to weather services like WUnderground, CWOP?
- APRS software (Xastir vs. APRX vs. other?)
- TNC (TNC-Pi, Dire Wolf, KPC TNC, Kenwood D710) 
- How will I send APRS information to the transceiver?

The simplest weather information that you can gather with a Personal Weather Station (PWS) are readings like temperature and relative humidity.  More advanced units add items such as barometric pressure, wind speed, and rainfall amounts.  The most expensive weather stations that you can buy support sensors for exotic measurements such as solar radiation, leaf wetness, and soil moisture/temperature.  If you already own a Personal Weather Station that you want to use, your decision is much simpler as you will simply use the information that it provides.  Sometimes you can add information from multiple weather stations, as is the case with 433.92 MHz ISM band wireless devices that are supported by rtl_433 (https://github.com/merbanan/rtl_433).

One way to decide what measurements are desired is to investigate the different options for displaying weather data for yourself or other users.  For example, the Kenwood D710 will display these measurements on its weather display screen: rainfall, temperature, wind direction, wind speed, barometric pressure, and relative humidity.  The default WeeWX and Wunderground show even more items...

Most Personal Weather Stations (PWS) will be interfaced to the Raspberry Pi 3 with either a serial interface, a USB interface, or by a RTL-SDR dongle.  More interfacing options are available using the WeeWx Drivers.  The WeeWx Hardware Guide shows weather stations that can be connected via serial or USB interface.  Wireless 433.92 MHz Personal Weather Stations that can be decoded by using the RTL-SDR dongle are shown on the rtl_433 GitHub page.

(http://www.weewx.com/docs/hardware.htm)
(https://github.com/merbanan/rtl_433)
(https://github.com/weewx/weewx/wiki)

### Prerequisites
```
Longitude: 46.584077
Latitude: -94.216453
Elevation: 1237 feet
APRSIS: 
WUnderground PWS:
```
### Hardware
```
CanaKit Raspberry Pi 3 with 2.5A Micro USB Power Supply     https://tinyurl.com/hmko6eg  $ 41.99
Coastal ChipWorks TNC-Pi 2 TNC-X for Raspberry Pi Kit       https://tinyurl.com/hykfmzq  $ 40.00
NooElec NESDR SMArt Premium RTL-SDR 0.5PPM TCXO             https://tinyurl.com/zns9elq  $ 21.95
GeauxRobot Raspberry Pi 3 2-layer Dog Bone Stack Clear      https://tinyurl.com/zgow34m  $ 17.99
SanDisk Ultra 32GB microSDHC UHS-I Card with Adapter        https://tinyurl.com/zgjctvq  $ 12.94
Digikey AE40M-5-ND CBL RIBBON 40COND 0.050 MULTI 5'         https://tinyurl.com/h7wg2pk  $ 12.50
Digikey 931-1069-ND 433MHz Right Angle Whip Antenna         https://tinyurl.com/jgoxawz  $  8.34
Digikey WM50012-40-ND CONN HDR DUAL 40POS .100 SRT AU       https://tinyurl.com/zjztc4j  $  6.70
Digikey AKC40B-ND CONN IDC SKT 40POS W/POL GOLD             https://tinyurl.com/zvobuhk  $  2.78
Digikey AKC40B-ND CONN IDC SKT 40POS W/POL GOLD             https://tinyurl.com/zvobuhk  $  2.78
Digikey 972-09SBE-ND BACKSHELL DB9 CLAM SLIM BLACK          https://tinyurl.com/jbbc8ec  $  2.70
Digikey 209ME-ND CONN DSUB PLUG 9POS STR SLDR CUP           https://tinyurl.com/gwkt9v4  $  0.81 
```
### Software
```
raspbian jessie -> http://www.raspbian.org
rtl-sdr         -> http://osmocom.org/projects/sdr/wiki/rtl-sdr
rtl_433         -> https://github.com/merbanan/rtl_433
weewx-sdr       -> https://github.com/matthewwall/weewx-sdr
weewx           -> http://weewx.com
weewx-aprs      -> https://github.com/cavedon/weewx-aprs
aprx            -> http://thelifeofkenneth.com/aprx
sqlitebrowser   -> http://sqlitebrowser.org/
```
### Installing
Here are the steps that I used to get my APRS Weather Station working.

##### Installing Raspbian Jessie OS to SDHC Card
```
https://www.raspberrypi.org/downloads/raspbian/
https://members.sdcard.org/downloads/formatter_4/
https://sourceforge.net/projects/win32diskimager/
```
##### Installing Packages from Raspbian Repository
```
sudo apt-get -y update                                              &&
sudo apt-get -y upgrade                                             &&
sudo apt-get -y install apache2                                     &&
sudo apt-get -y install cmake                                       &&
sudo apt-get -y install ftp                                         &&
sudo apt-get -y install libusb-1.0-0-dev                            &&
sudo apt-get -y install numlockx                                    &&
sudo apt-get -y install python-cheetah                              &&
sudo apt-get -y install python-configobj                            &&
sudo apt-get -y install python-imaging                              &&
sudo apt-get -y install python-serial                               &&
sudo apt-get -y install python-usb                                  &&
sudo apt-get -y install sqlitebrowser
```
##### Build / Install RTL-SDR Software
```
mkdir /home/pi/aprswx/                                              &&
cd /home/pi/aprswx/                                                 &&
git clone git://git.osmocom.org/rtl-sdr.git                         &&
mkdir /home/pi/aprswx/rtl-sdr/build/                                &&
cd /home/pi/aprswx/rtl-sdr/build/                                   &&
cmake ../ -DINSTALL_UDEV_RULES=ON                                   &&
make                                                                &&
sudo make install                                                   &&
sudo ldconfig                                                       &&
cd /home/pi/
```
##### Build / Install RTL_433 Software
```
cd /home/pi/aprswx/                                                 &&
git clone https://github.com/merbanan/rtl_433.git                   &&
mkdir /home/pi/aprswx/rtl_433/build/                                &&
cd /home/pi/aprswx/rtl_433/build                                    &&
cmake ../                                                           &&
make                                                                &&
sudo make install                                                   &&
cd /home/pi/
```
##### Add RTL-SDR Devices to Blacklist File
```
sudo chmod 666 /etc/modprobe.d/raspi-blacklist.conf &&
if ! grep -Fxq "blacklist dvb_usb_rtl28xxu"          /etc/modprobe.d/raspi-blacklist.conf; then
  echo -e 'blacklist dvb_usb_rtl28xxu' | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf; fi
if ! grep -Fxq "blacklist rtl_2830"                  /etc/modprobe.d/raspi-blacklist.conf; then
    echo -e 'blacklist rtl_2830'       | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf; fi
if ! grep -Fxq "blacklist rtl_2832"                  /etc/modprobe.d/raspi-blacklist.conf; then
    echo -e 'blacklist rtl_2832'       | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf; fi
sudo chmod 644                                       /etc/modprobe.d/raspi-blacklist.conf

sudo rmmod dvb_usb_rtl28xxu
sudo nano /etc/modprobe.d/raspi-blacklist.conf
dvb_usb_rtl28xxu
rtl_2830
rtl_2832
CTRL+X
unplug RTL-SDR and reinsert
```
##### Testing RTL_433 Software
```
rtl_433 -q -U -G
CTRL+C to quit

Sample Output:
2017-02-26 22:00:00 :	Acurite 5n1 sensor
	sensor_id:	 0x8FA
	channel:	 A
	sequence_num:	 0
	battery:	 OK
	message_type:	 56
	wind_speed:	 0.0 mph
	temperature:	 65.3 F
	humidity:	 31
2017-02-26 22:00:20 :	Acurite 5n1 sensor
	sensor_id:	 0x8FA
	channel:	 A
	sequence_num:	 2
	battery:	 OK
	message_type:	 49
	wind_speed:	 0.0 mph
	wind_dir_deg:	 0.0
	wind_dir:	 N
	rainfall_accumulation:	 0.00 in
	raincounter_raw:	 410
```
##### Build / Install WeeWx Software
```
cd /home/pi/aprswx/                                                 &&
git clone https://github.com/weewx/weewx.git                        &&
cd /home/pi/aprswx/weewx                                            &&
sudo ./setup.py build                                               &&
sudo ./setup.py install --no-prompt                                 &&
cd /home/weewx/util/init.d/                                         &&
sudo cp weewx.debian /etc/init.d/weewx                              &&
sudo chmod +x /etc/init.d/weewx                                     &&
sudo update-rc.d weewx defaults 98                                  &&
sudo /etc/init.d/weewx start                                        &&
cd /home/pi/
```
##### Testing WeeWx Software


##### Build / Install WeeWx-SDR Software
```
cd /home/pi/aprswx/                                                 &&
git clone https://github.com/matthewwall/weewx-sdr.git              &&
cd /home/pi/aprswx/weewx-sdr                                        &&
wget 'https://github.com/matthewwall/weewx-sdr/archive/master.zip'  &&
sudo /home/weewx/bin/wee_extension --install master.zip             &&
cd /home/pi/
```   
##### Add WeeWx-SDR Stanza to WeeWx.conf 
```
sudo nano /home/weewx/weewx.conf

##############################################################################

#  This section defines sensors for weewx-sdr driver.

[SDR]
    driver = user.sdr
    cmd = rtl_433 -q -U -F json -G
    path = /usr/local/bin/
    [[sensor_map]]
        windDir     = wind_dir.08FA.Acurite5n1Packet
        windSpeed   = wind_speed.08FA.Acurite5n1Packet
        outTemp     = temperature.08FA.Acurite5n1Packet
        outHumidity = humidity.08FA.Acurite5n1Packet
        rain_total  = rain_total.0BFA.Acurite5n1Packet
        inTemp      = temperature.24A4.AcuriteTowerPacket
        inHumidity  = humidity.24A4.AcuriteTowerPacket            

##############################################################################
```
##### Build / Install WeeWx-APRS Software
```
cd /home/pi/aprswx/                                                 &&
git clone https://github.com/cavedon/weewx-aprs.git                 &&
cd /home/pi/aprswx/weewx-aprs                                       &&
wget 'https://github.com/cavedon/weewx-aprs/archive/v0.1.tar.gz'    &&
sudo /home/weewx/bin/wee_extension --install v0.1.tar.gz            &&
cd /home/pi
```
##### Modify WeeWx-APRS Script
```
sudo nano /home/weewx/bin/user/aprs.py

*** comment out these lines ***
#    if record.get('windGust') is not None:
#        # Gust (peak wind speed in mph in the last 5 minutes)
#        data.append('g%03.f' % record['wind_average'])
#   else:
#        data.append('g...')
```
##### Configure WeeWx
```
sudo /home/weewx/bin/wee_config --reconfigure

Breezy Point, MN, USA
1238, foot
+46.584
-94.216
us
0

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx restart
open /home/weewx/public_html/index.html
check /var/log/user.log
```
##### Build / Install APRX Software
```
cd /home/pi/aprswx/                                                 &&
git clone https://github.com/PhirePhly/aprx.git                     &&
cd /home/pi/aprswx/aprx                                             &&
wget 'http://thelifeofkenneth.com/aprx/debs/aprx_2.9.0_raspi.deb'   &&
sudo dpkg -i /home/pi/aprswx/aprx/aprx_2.9.0_raspi.deb
```
##### Disable Serial Terminal / Enable UART
```
sudo sed -ie 's/console=serial0,115200 //g'              /boot/cmdline.txt       &&
sudo chmod 666                                           /boot/config.txt        &&
if ! grep -Fxq "enable_uart=1"                           /boot/config.txt; then  
    echo -e 'enable_uart=1'                | sudo tee -a /boot/config.txt; fi    && 
sudo chmod 755                                           /boot/config.txt        &&
```
##### create new aprx.conf
```
sudo rm /etc/aprx.conf
sudo nano /etc/aprx.conf

mycall AD0HJ-13

<aprsis>
    passcode -1
    server   rotate.aprs2.net
</aprsis>

<logging>
    pidfile /var/run/aprx.pid
    rflog   /var/log/aprx/aprx-rf.log
    aprxlog /var/log/aprx/aprx.log
</logging>

<interface>
    serial-device /dev/serial0 19200 8n1 KISS
    callsign      $mycall
    tx-ok         true
    telem-to-is   false
</interface>

<beacon>
    beaconmode radio
    cycle-size  5m
    beacon srccall AD0HJ via WIDE1-1 file "/dev/shm/aprs.pkt"
</beacon>
```
##### start aprx 
```
sudo aprx -vvv
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
