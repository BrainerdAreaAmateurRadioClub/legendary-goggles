#  APRS Weather Station Installation Script
Use a Raspberry Pi 3 Model B to collect data from your personal weather station, display weather information in HTML format, continouously upload weather data to many popular weather sites, and transmit APRS weather information.

![400px-apruptx0004](https://cloud.githubusercontent.com/assets/25856695/23232743/058d03d0-f912-11e6-9278-4623a960dc05.jpg)

## Getting Started
```
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

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

Installing Required Packages
```
sudo apt-get -y update  
sudo apt-get -y upgrade
sudo apt-get -y install apache2
sudo apt-get -y install ax25-apps
sudo apt-get -y install ax25-tools
sudo apt-get -y install cmake
sudo apt-get -y install ftp
sudo apt-get -y install libusb-1.0-0-dev
sudo apt-get -y install numlockx
sudo apt-get -y install python-cheetah
sudo apt-get -y install python-configobj
sudo apt-get -y install python-imaging
sudo apt-get -y install python-serial
sudo apt-get -y install python-usb
sudo apt-get -y install sqlitebrowser

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
