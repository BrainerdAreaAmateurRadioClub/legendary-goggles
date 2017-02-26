#  Working on instructions for building APRS WX Station with Raspberry Pi - Mitch Ahrenstorff AD0HJ - 02/26/17
Use a Raspberry Pi 3 Model B to collect data from your personal weather station, display weather information in HTML format, continouously upload weather data to many popular weather sites, and transmit APRS weather information.

![400px-apruptx0004](https://cloud.githubusercontent.com/assets/25856695/23232743/058d03d0-f912-11e6-9278-4623a960dc05.jpg)

## Getting Started
```
433 MHz PWS  -->  RTL-SDR --> RTL_433 --> weewx-sdr                            --> aprx   --> tnc-pi
Serial PWS   -->             usb to serial converter  --> weewx --> weewx-aprs --> xastir --> tnc-pi
USB Display  -->                   direct usb to rpi                           --> straight to serial tnc

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
```
### Prerequisites
```
Longitude: 46.584077 hi
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
##### Configure WeeWx



##### Build / Install APRX Software
```
git clone https://github.com/PhirePhly/aprx.git /home/pi/aprswx/aprx/
cd /home/pi/aprswx/aprx
wget 'http://thelifeofkenneth.com/aprx/debs/aprx_2.9.0_raspi.deb'
sudo dpkg -i /home/pi/aprswx/aprx/aprx_2.9.0_raspi.deb
```
##### create new aprx.conf
```
mycall AD0HJ

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
    serial-device /dev/ttyS0 19200 8n1 KISS
    callsign      $mycall
    tx-ok         true
    telem-to-is   false
</interface>

<beacon>
    beaconmode radio
    cycle-size  30m
    beacon srccall AD0HJ via WIDE1-1 file "/dev/shm/aprs.pkt"
</beacon>
```
##### do i need this?
```
sudo apt-get -y install ax25-apps
sudo apt-get -y install ax25-tools
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
