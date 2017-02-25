#!/usr/bin/env python3

import os, sys

def main():

#    collect_user_information()
    install_required_packages()
    setup_for_new_installation()
    create_rtl_sdr_blacklist()
    build_install_rtl_sdr()
    build_install_rtl_433()
    build_install_weewx()
#    build_install_weewx_sdr()
#    build_install_weewx_aprs()
#    build_install_aprx()

def collect_user_information():

    #ans=True
    #while ans:
    #    print ("""
    #    1.Add a Student
    #    2.Delete a Student
    #    3.Look Up Student Record
    #    4.Exit/Quit
    #    """)
    #    ans=raw_input("What would you like to do? ") 
    #    if ans=="1": 
    #        print("\n Student Added") 
    #    elif ans=="2":
    #        print("\n Student Deleted") 
    #    elif ans=="3":
    #        print("\n Student Record Found") 
    #    elif ans=="4":
    #        print("\n Goodbye") 
    #    elif ans !="":
    #        print("\n Not Valid Choice Try again") 


    mitch = "#--------------------------------------------------------------------------------------------------#\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "#                                                                                                  #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "# Raspberry Pi 3 APRS WX Station Installation Script                                               #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "#                                                                                                  #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "#--------------------------------------------------------------------------------------------------#\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "#                                                                                                  #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "# Menu Options                                                                                     #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "#                                                                                                  #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "#--------------------------------------------------------------------------------------------------#\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "# 1) Full Installation                                                                             #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "# 2) Install 433 MHz                                                                               #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "# 3) Install WeeWx                                                                                 #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "# 4) Install Weewx SDR                                                                             #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "# 5) Install APRX                                                                                  #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "# 6) Exit Installation Script                                                                      #\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()
    mitch = "#--------------------------------------------------------------------------------------------------#\n"
    if(update_status_message(mitch)                                                                           == True):  sysexit()

    user_callsign_ssid = input("Enter you Callsign/SSID: ")
    print ("you entered " + user_callsign_ssid) 



    #if(change_linux_directory ("/home/pi/Desktop/")                                                          == True):  sysexit()
    #if(execute_command_in_shell("sudo apt-get -y install numlockx")                                          == True):  sysexit()
    #if(execute_command_in_shell("/usr/bin/numlockx on")                                                      == True):  sysexit()

    # different install levels
    # test one step at a time

#    user_callsign_ssid = input("Enter you Callsign/SSID: ")
#    print ("you entered " + user_callsign_ssid) 

#    user_elevation = input("Enter you elevation: ")
#    print ("you entered " + user_elevation) 

#    user_latitude = input("Enter you latitude: ")
#    print ("you entered " + user_latitude) 

#    user_longitude = input("Enter you longitude: ")
#    print ("you entered " + user_longitude) 

#    user_measurement_system = input("Enter you measurement system: ")
#    print ("you entered " + user_measurement_system) 
    
    # Breezy Point, MN, USA                                                                             #
    # 377, meter                                                                                        #
    # 46.584                                                                                            #
    # -94.216                                                                                           #
    # us                                                                                                #
    # 0                                                                                                 #    

def install_required_packages():

    # install package dependencies needed for software
    if(update_status_message  ("updating available packages list")                                          == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y update")                                                    == True):  sysexit()
    if(update_status_message  ("upgrading all installed packages")                                          == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y upgrade")                                                   == True):  sysexit()
    if(update_status_message  ("installing package apache2")                                                == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install apache2")                                           == True):  sysexit()
    if(update_status_message  ("installing package ax25-apps")                                              == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install ax25-apps")                                         == True):  sysexit()
    if(update_status_message  ("installing package ax25-tools")                                             == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install ax25-tools")                                        == True):  sysexit()
    if(update_status_message  ("installing package cmake")                                                  == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install cmake")                                             == True):  sysexit()
    if(update_status_message  ("installing package ftp")                                                    == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install ftp")                                               == True):  sysexit()
    if(update_status_message  ("installing package libusb-1.0-0-dev")                                       == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install libusb-1.0-0-dev")                                  == True):  sysexit()
    if(update_status_message  ("installing package numlockx")                                               == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install numlockx")                                          == True):  sysexit()
    if(update_status_message  ("installing package python-cheetah")                                         == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install python-cheetah")                                    == True):  sysexit()
    if(update_status_message  ("installing package python-configobj")                                       == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install python-configobj")                                  == True):  sysexit()
    if(update_status_message  ("installing package python-imaging")                                         == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install python-imaging")                                    == True):  sysexit()
    if(update_status_message  ("installing package python-serial")                                          == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install python-serial")                                     == True):  sysexit()
    if(update_status_message  ("installing package python-usb")                                             == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install python-usb")                                        == True):  sysexit()
    if(update_status_message  ("installing package sqlitebrowser")                                          == True):  sysexit()
    if(execute_shell_command  ("sudo apt-get -y install sqlitebrowser")                                     == True):  sysexit()

def setup_for_new_installation():

    # tasks to do before software build and install  
    if(update_status_message  ("creating directory /home/pi/aprswx/")                                       == True):  sysexit()
    if(create_linux_directory ("/home/pi/aprswx/")                                                          == True):  sysexit()
    if(update_status_message  ("removing directory /home/pi/aprswx/rtl-sdr/")                               == True):  sysexit()
    if(remove_linux_directory ("/home/pi/aprswx/rtl-sdr/")                                                  == True):  sysexit()
    if(update_status_message  ("removing directory /home/pi/aprswx/rtl_433/")                               == True):  sysexit()
    if(remove_linux_directory ("/home/pi/aprswx/rtl_433/")                                                  == True):  sysexit()
    if(update_status_message  ("removing directory /home/pi/aprswx/weewx/")                                 == True):  sysexit()
    if(remove_linux_directory ("/home/pi/aprswx/weewx/")                                                    == True):  sysexit()
    if(update_status_message  ("removing directory /home/pi/aprswx/weewx-sdr/")                             == True):  sysexit()
    if(remove_linux_directory ("/home/pi/aprswx/weewx-sdr/")                                                == True):  sysexit()
    if(update_status_message  ("removing directory /home/pi/aprswx/weewx-aprs/")                            == True):  sysexit()
    if(remove_linux_directory ("/home/pi/aprswx/weewx-aprs/")                                               == True):  sysexit()
    if(update_status_message  ("removing directory /home/pi/aprswx/aprx/")                                  == True):  sysexit()
    if(remove_linux_directory ("/home/pi/aprswx/aprx/")                                                     == True):  sysexit()
    if(update_status_message  ("removing directory /home/weewx/bin/")                                       == True):  sysexit()
    if(remove_linux_directory ("/home/weewx/bin/")                                                          == True):  sysexit()
    if(update_status_message  ("enabling num lock")                                                         == True):  sysexit()
    if(execute_shell_command  ("/usr/bin/numlockx on")                                                      == True):  sysexit()

def create_rtl_sdr_blacklist():

    # remove rtl-sdr module from kernel / # add rtl-sdr devices to raspi-blacklist.conf
    if(update_status_message  ("unload dvb_usb_rtl28xxu kernel module")                                     == True):  sysexit()
    if(execute_shell_command  ("sudo rmmod dvb_usb_rtl28xxu")                                               == True):  sysexit()
    if(update_status_message  ("changing working directory to /etc/modprobe.d/")                            == True):  sysexit()
    if(change_linux_directory ("/etc/modprobe.d/")                                                          == True):  sysexit()
    if(update_status_message  ("changing /etc/modprobe.d/raspi-blacklist.conf file permissions")            == True):  sysexit()      
    if(change_file_permissions("/etc/modprobe.d/raspi-blacklist.conf", 666)                                 == True):  sysexit()
    if(update_status_message  ("adding rtl-sdr entries to /etc/modprobe.d/raspi-blacklist.conf")            == True):  sysexit()
    if(update_raspi_blacklist ("dvb_usb_rtl28xxu", "rtl_2830", "rtl_2832")                                  == True):  sysexit()
    if(update_status_message  ("changing /etc/modprobe.d/raspi-blacklist.conf file permissions")            == True):  sysexit()      
    if(change_file_permissions("/etc/modprobe.d/raspi-blacklist.conf", 644)                                 == True):  sysexit()
    if(update_status_message  ("enabling num lock")                                                         == True):  sysexit()
    if(execute_shell_command  ("sudo udevadm control --reload-rules")                                       == True):  sysexit()
    # unplug dongle and reinstall?
		
def build_install_rtl_sdr():

    # build and install rtl-sdr software
    if(update_status_message  ("changing working directory to /home/pi/aprswx/")                            == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/")                                                          == True):  sysexit()
    if(update_status_message  ("cloning rtl-sdr repository from git.osmocom.org")                           == True):  sysexit()
    if(execute_shell_command  ("sudo git clone git://git.osmocom.org/rtl-sdr.git")                          == True):  sysexit()
    if(update_status_message  ("making directory /home/pi/aprswx/rtl-sdr/build/")                           == True):  sysexit()
    if(execute_shell_command  ("sudo mkdir /home/pi/aprswx/rtl-sdr/build/")                                 == True):  sysexit()
    if(update_status_message  ("changing working directory to /home/pi/aprswx/rtl-sdr/build/")              == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/rtl-sdr/build/")                                            == True):  sysexit()
    if(update_status_message  ("generating makefile for rtl-sdr")                                           == True):  sysexit()
    if(execute_shell_command  ("sudo cmake /home/pi/aprswx/rtl-sdr/ -DINSTALL_UDEV_RULES=ON")               == True):  sysexit()
    if(update_status_message  ("compiling rtl-sdr application")                                             == True):  sysexit()
    if(execute_shell_command  ("sudo make")                                                                 == True):  sysexit()
    if(update_status_message  ("installing rtl-sdr application")                                            == True):  sysexit()
    if(execute_shell_command  ("sudo make install")                                                         == True):  sysexit()
    if(update_status_message  ("???")                                                                       == True):  sysexit()
    if(execute_shell_command  ("sudo ldconfig")                                                             == True):  sysexit()

def build_install_rtl_433():

    # build and install rtl_433 software
    if(update_status_message  ("changing working directory to /home/pi/aprswx/")                            == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/")                                                          == True):  sysexit()
    if(update_status_message  ("cloning rtl_433 repository from github.com/merbanan/")                      == True):  sysexit()
    if(execute_shell_command  ("sudo git clone https://github.com/merbanan/rtl_433.git")                    == True):  sysexit()
    if(update_status_message  ("making directory /home/pi/aprswx/rtl_433/build/")                           == True):  sysexit()
    if(execute_shell_command  ("sudo mkdir /home/pi/aprswx/rtl_433/build/")                                 == True):  sysexit()
    if(update_status_message  ("changing working directory to /home/pi/aprswx/rtl_433/build/")              == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/rtl_433/build/")                                            == True):  sysexit()
    if(update_status_message  ("generating makefile for rtl_433 install using CMake")                       == True):  sysexit()
    if(execute_shell_command  ("sudo cmake /home/pi/aprswx/rtl_433/")                                       == True):  sysexit()
    if(update_status_message  ("compiling rtl_433 application")                                             == True):  sysexit()
    if(execute_shell_command  ("sudo make")                                                                 == True):  sysexit()
    if(update_status_message  ("installing rtl_433 application")                                            == True):  sysexit()
    if(execute_shell_command  ("sudo make install")                                                         == True):  sysexit()

def build_install_weewx():

    # build and install weewx software
    if(update_status_message  ("changing working directory to /home/pi/aprswx/")                            == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/")                                                          == True):  sysexit()
    if(update_status_message  ("cloning weewx repository from github.com/weewx/")                           == True):  sysexit()
    if(execute_shell_command  ("sudo git clone https://github.com/weewx/weewx.git")                         == True):  sysexit()
    if(update_status_message  ("changing working directory to /home/pi/aprswx/weewx")                       == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/weewx/")                                                    == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo ./setup.py build")                                                     == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo ./setup.py install --no-prompt")                                       == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo cp /home/weewx/util/init.d/weewx.debian /etc/init.d/weewx")            == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo chmod +x /etc/init.d/weewx")                                           == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo update-rc.d weewx defaults 98")                                        == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo /etc/init.d/weewx start")                                              == True):  sysexit()

def build_install_weewx_sdr():

    # build and install weewx-sdr software
    if(update_status_message  ("changing working directory to /home/pi/aprswx/")                            == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/")                                                          == True):  sysexit()
    if(update_status_message  ("cloning weewx-sdr repository from github.com/matthewwall/")                 == True):  sysexit()
    if(execute_shell_command  ("sudo git clone https://github.com/matthewwall/weewx-sdr.git")               == True):  sysexit()
    if(update_status_message  ("changing working directory to /home/pi/aprswx/weewx-sdr")                   == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/weewx-sdr")                                                 == True):  sysexit()
    if(execute_shell_command  ("sudo wget \'https://github.com/matthewwall/weewx-sdr/archive/master.zip\'") == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo /home/weewx/bin/wee_extension --install master.zip")                   == True):  sysexit()
    if(update_status_message  ("changing working directory to /home/weewx/")                                == True):  sysexit()
    if(change_linux_directory ("/home/weewx/")                                                              == True):  sysexit()
    if(update_status_message  ("changing /home/weewx/weewx.conf file permissions")                          == True):  sysexit()
    if(change_file_permissions("/home/weewx/weewx.conf", 666)                                               == True):  sysexit()
    if(update_status_message  ("adding weewx-sdr entries to  /home/weewx/weewx.conf")                       == True):  sysexit()
    #if(update_weewx_conf      ()                                                                            == True):  sysexit()

    
    file = open('/home/weewx/weewx.conf','a')
    file.write('\n')
    file.write('\n')
    file.write('##############################################################################\n')
    file.write('\n')
    file.write('#  This section defines sensors for weewx-sdr driver.\n')
    file.write('\n')
    file.write('[SDR]\n')
    file.write('    driver = user.sdr\n')
    file.write('    cmd = rtl_433 -q -U -F json -G\n')
    file.write('    path = /usr/local/bin/\n')
    file.write('    [[sensor_map]]\n')
    file.write('        windDir = wind_dir.08FA.Acurite5n1Packet\n')
    file.write('        windSpeed = wind_speed.08FA.Acurite5n1Packet\n')
    file.write('        outTemp = temperature.08FA.Acurite5n1Packet\n')
    file.write('        outHumidity = humidity.08FA.Acurite5n1Packet\n')
    file.write('        rain_total = rain_total.0BFA.Acurite5n1Packet\n')
    file.write('        inTemp = temperature.24A4.AcuriteTowerPacket\n')
    file.write('        inHumidity= humidity.24A4.AcuriteTowerPacket\n')            
    file.write('\n')
    file.write('##############################################################################\n')
    file.close()


    if(update_status_message  ("changing /home/weewx/weewx.conf file permissions")                           == True):  sysexit()
    if(change_file_permissions("/home/weewx/weewx.conf", 666)                                                == True):  sysexit()

def build_install_weewx_aprs():

    # build and install weewx-aprs software
    if(update_status_message  ("changing working directory to /home/pi/aprswx/")                            == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/")                                                          == True):  sysexit()
    if(update_status_message  ("cloning weewx repository from github.com/cavedon/")                         == True):  sysexit()
    if(execute_shell_command  ("sudo git clone https://github.com/cavedon/weewx-aprs.git")                  == True):  sysexit()
    if(update_status_message  ("changing working directory to /home/pi/aprswx/weewx-aprs")                  == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/weewx-aprs")                                                == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo wget \'https://github.com/cavedon/weewx-aprs/archive/v0.1.tar.gz\'")   == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo /home/weewx/bin/wee_extension --install v0.1.tar.gz")                  == True):  sysexit()

    ## Options for extension 'aprs'
    #[APRS]
    #    comment = ""
    #    include_position = 1
    #    symbol_code = _
    #    symbol_table = /
    #    output_filename = /dev/shm/aprs.pkt


    #    sudo nano /home/weewx/bin/user/aprs.py                                                         #
    #    *** comment out these lines ***                                                                #
    #    if record.get('windGust') is not None:                                                         #
    #        # Gust (peak wind speed in mph in the last 5 minutes)                                      #
    #        data.append('g%03.f' % record['wind_average'])                                             #
    #   else:                                                                                          #
    #        data.append('g...')                                                                        #

    #[ -d /home/weewx/ ] && sudo rm /home/weewx/weewx.conf.*
    # delete /home/weewx/weewx.conf.* by date?
    # weewx.conf.20170213192805
    # weewx.conf.20170213195839

def build_install_aprx():
    
    # build and install weewx software
    if(update_status_message  ("changing working directory to /home/pi/aprswx/")                            == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/")                                                          == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo git clone https://github.com/PhirePhly/aprx.git /home/pi/aprswx/aprx/")== True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(update_status_message  ("changing working directory to /home/pi/aprswx/weewx-sdr")                   == True):  sysexit()
    if(change_linux_directory ("/home/pi/aprswx/aprx")                                                      == True):  sysexit()
    if(execute_shell_command  ("sudo wget \'http://thelifeofkenneth.com/aprx/debs/aprx_2.9.0_raspi.deb\'")  == True):  sysexit()
    if(update_status_message  ("")                                                                          == True):  sysexit()
    if(execute_shell_command  ("sudo dpkg -i /home/pi/aprswx/aprx/aprx_2.9.0_raspi.deb")                    == True):  sysexit()

    sys.stdout.write('sudo chmod 666 /etc/aprx.conf ')
    if (os.system("sudo chmod 666 /etc/aprx.conf ") == False):
        sys.stdout.write('                                                                       :ok\n')
    else:
        sys.stdout.write('                                                                       :error\n')

    if(update_status_message  ("changing working directory to /home/etc")                                   == True):  sysexit()
    if(change_linux_directory ("/home/etc/")                                                                == True):  sysexit()
 


    file = open('aprx.conf','w')
    file.write('mycall AD0HJ\n')
    file.write('\n')
    file.write('<aprsis>\n')
    file.write('    passcode -1\n')
    file.write('    server    rotate.aprs2.net\n')
    file.write('</aprsis>\n')
    file.write('\n')
    file.write('<logging>\n')
    file.write('    pidfile /var/run/aprx.pid\n')
    file.write('    rflog /var/log/aprx/aprx-rf.log\n')
    file.write('    aprxlog /var/log/aprx/aprx.log\n')
    file.write('</logging>\n')
    file.write('\n')
    file.write('<interface>\n')
    file.write('    serial-device /dev/ttyS0 19200 8n1 KISS\n')
    file.write('    callsign     $mycall\n')
    file.write('    tx-ok        true\n')
    file.write('    telem-to-is  false\n')
    file.write('</interface>\n')
    file.write('\n')
    file.write('<beacon>\n')
    file.write('    beaconmode radio\n')
    file.write('    cycle-size  30m\n')
    file.write('    beacon srccall AD0HJ via WIDE1-1 file "/dev/shm/aprs.pkt"\n')
    file.write('</beacon>\n')
    file.close()

    sys.stdout.write('sudo chmod 644 /etc/aprx.conf ')
    if (os.system("sudo chmod 644 /etc/aprx.conf ") == False):
        sys.stdout.write('                                                                       :ok\n')
    else:
        sys.stdout.write('                                                                       :error\n')


    #sudo sed -ie 's/console=serial0,115200 //g'              /boot/cmdline.txt                          #
    #sudo chmod 666                                           /boot/config.txt                           #
    #if ! grep -Fxq "enable_uart=1"                           /boot/config.txt; then                     #
    #    echo -e 'enable_uart=1'                | sudo tee -a /boot/config.txt; fi                       #
    #sudo chmod 755                                           /boot/config.txt                           #


    # aprx autostart


    # sudo /home/weewx/bin/wee_config --reconfigure                                                     #
    # Breezy Point, MN, USA                                                                             #
    # 377, meter                                                                                        #
    # 46.584                                                                                            #
    # -94.216                                                                                           #
    # us                                                                                                #
    # 0                                                                                                 #

def execute_shell_command(shell_command):

    # issue shell command
    if(os.system(shell_command) == False):
        sys.stdout.write(':ok\n')
    else:
        sys.stdout.write(':error\n')

def change_file_permissions(linux_file, permissions):

    # create shell command
    shell_command = ("sudo chmod " + str(permissions) + " " + linux_file) 

    # change file permissions
    if((os.path.isfile(linux_file)) == True):
        if(os.system(shell_command) == False):
           sys.stdout.write(':ok\n')
        else:
            sys.stdout.write(':error\n')
		
def change_linux_directory(linux_directory):

    # create shell command
    shell_command = ("cd " + linux_directory) 

    # change_linux_directory
    if((os.path.isdir(linux_directory)) == True):
        os.chdir(linux_directory)
        sys.stdout.write(':ok\n')
    else:		
        sys.stdout.write(':ok\n')
		
def close_file_for_updating (file_name, file_handle):

    # close file for read/write
    file_handle[0].close    
    sys.stdout.write(':ok\n')        

    # return error code
    return 0

def create_linux_directory(linux_directory):

    # create shell command
    shell_command = ("sudo mkdir " + linux_directory) 

    # create directory if not existing
    if((os.path.isdir(linux_directory)) == False):
        if(os.system(shell_command) == False):
            sys.stdout.write(':ok\n')
        else:
            sys.stdout.write(':error\n')
    else:
        sys.stdout.write(':ok\n')
            
def open_file_for_updating (file_name, file_handle):

    # open file for read/write
    file_handle[0] = open("/etc/modprobe.d/raspi-blacklist.conf", "r+")    

    # see if file open was successful
    if(file_handle[0] != None):
        sys.stdout.write(':ok\n')        
    else:
        sys.stdout.write(':error\n')             

def remove_linux_directory(directory):

    # create shell command
    shell_command = ("sudo rm -r " + directory) 

    # remove directory if it exists
    if((os.path.isdir(directory)) == True):
        if(os.system(shell_command) == False):
            sys.stdout.write(':ok\n')
        else:
            sys.stdout.write(':error\n')
    else:
        sys.stdout.write(':ok\n')        

def update_raspi_blacklist(item_1, item_2, item_3):

    # open / read raspi-blacklist.conf
    file_handle  = open("/etc/modprobe.d/raspi-blacklist.conf", "r+")
    file_content = file_handle.read()

    # add dvb_usb_rtl28xxu
    if(file_content.count(item_1) == 0):
        file_handle.write(item_1 + "\n")

    # add rtl_2830
    if(file_content.count(item_2) == 0):
        file_handle.write(item_2 + "\n")

    # add rtl_2832
    if(file_content.count(item_3) == 0):
        file_handle.write(item_3 + "\n")

    # close file
    file_handle.close()

    sys.stdout.write(':ok\n')
    
def update_status_message(status_message):

    # determine spaces to write
    spaces_to_write = ('')
    if((len(status_message)-1) < 100):
        for num in range((len(status_message)-1), 100):
            spaces_to_write += (' ')

    # print status message
    sys.stdout.write(status_message)
    sys.stdout.write(spaces_to_write)

    # return error code
    return 0

#    # print shell command
#    shell_command = ("sudo rm -r " + directory) 
#
#    # determine spaces to write
#    spaces_to_write = (' ')
#    for num in range(len(shell_command),100):
#        spaces_to_write += (' ')
#
#    # remove directory if it exists
#    if((os.path.isdir(directory)) == True):
#        if(os.system(shell_command) == False):
#            sys.stdout.write(shell_command)
#            sys.stdout.write(spaces_to_write)
#            sys.stdout.write(':ok\n')
#        else:
#            sys.stdout.write(shell_command)
#            sys.stdout.write(spaces_to_write)
#            sys.stdout.write(':error\n')



if __name__ == '__main__':
    main()


#!/bin/bash
#---------------------------------------------------------------------------------------------------#
# tested on linux raspberrypi 4.4.38-v7+ #938 mitchell.ahrenstorff@gmail.com AD0HJ 02/15/17         #
#---------------------------------------------------------------------------------------------------#
#sudo apt-get -y update                                                                              #
#sudo apt-get -y upgrade                                                                             #
#sudo apt-get -y install apache2                                                                     #
#sudo apt-get -y install ax25-apps                                                                   #
#sudo apt-get -y install ax25-tools                                                                  #
#sudo apt-get -y install cmake                                                                       #
#sudo apt-get -y install ftp                                                                         #
#sudo apt-get -y install libusb-1.0-0-dev                                                            #
#sudo apt-get -y install numlockx                                                                    #
#sudo apt-get -y install python-cheetah                                                              #
#sudo apt-get -y install python-configobj                                                            #
#sudo apt-get -y install python-imaging                                                              #
#sudo apt-get -y install python-serial                                                               #
#sudo apt-get -y install python-usb                                                                  #
#---------------------------------------------------------------------------------------------------#
#[ ! -d /home/pi/aprswx/                      ] && mkdir      /home/pi/aprswx/                       #
#[   -d /home/pi/aprswx/rtl-sdr/              ] && sudo rm -r /home/pi/aprswx/rtl-sdr/               #
#[   -d /home/pi/aprswx/rtl_433/              ] && sudo rm -r /home/pi/aprswx/rtl_433/               #
#[   -d /home/pi/aprswx/weewx/                ] && sudo rm -r /home/pi/aprswx/weewx/                 #
#[   -d /home/pi/aprswx/weewx-sdr/            ] && sudo rm -r /home/pi/aprswx/weewx-sdr/             #
#[   -d /home/pi/aprswx/weewx-aprs/           ] && sudo rm -r /home/pi/aprswx/weewx-aprs/            #
#[   -d /home/pi/aprswx/aprx/                 ] && sudo rm -r /home/pi/aprswx/aprx/                  #
#[   -d /home/weewx/bin/                      ] && sudo rm -r /home/weewx/bin/                       #
#[   -d /home/weewx/                          ] && sudo rm    /home/weewx/weewx.conf.*               #
#[   -f /lib/systemd/system/hciattach.service ] && sudo rm    /lib/systemd/system/hciattach.service  #
#---------------------------------------------------------------------------------------------------#
#git clone git://git.osmocom.org/rtl-sdr.git /home/pi/aprswx/rtl-sdr/                                #
#mkdir /home/pi/aprswx/rtl-sdr/build/                                                                #
#cd /home/pi/aprswx/rtl-sdr/build/                                                                   #
#cmake ../ -DINSTALL_UDEV_RULES=ON                                                                   #
#make                                                                                                #
#sudo make install                                                                                   #
#sudo ldconfig                                                                                       #
#---------------------------------------------------------------------------------------------------#
#git clone https://github.com/merbanan/rtl_433.git /home/pi/aprswx/rtl_433/                          #
#mkdir /home/pi/aprswx/rtl_433/build/                                                                #
#cd /home/pi/aprswx/rtl_433/build/                                                                   #
#cmake ../                                                                                           #
#make                                                                                                #
#sudo make install                                                                                   #
#rtl_433                                                                                             #
#---------------------------------------------------------------------------------------------------#
#sudo chmod 666                                           /etc/modprobe.d/raspi-blacklist.conf       #
#if ! grep -Fxq "blacklist dvb_usb_rtl28xxu"              /etc/modprobe.d/raspi-blacklist.conf; then #
#    echo -e 'blacklist dvb_usb_rtl28xxu'   | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf; fi   #
#if ! grep -Fxq "blacklist rtl_2830"                      /etc/modprobe.d/raspi-blacklist.conf; then #
#    echo -e 'blacklist rtl_2830'           | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf; fi   #
#if ! grep -Fxq "blacklist rtl_2832"                      /etc/modprobe.d/raspi-blacklist.conf; then #
#    echo -e 'blacklist rtl_2832'           | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf; fi   #
#sudo chmod 644                                           /etc/modprobe.d/raspi-blacklist.conf       #
#---------------------------------------------------------------------------------------------------#
#git clone https://github.com/weewx/weewx.git /home/pi/aprswx/weewx/                                 #
#cd /home/pi/aprswx/weewx/                                                                           #
#./setup.py build                                                                                    #
#sudo ./setup.py install --no-prompt                                                                 #
#[ -f /home/weewx/weewx.conf.* ] && sudo rm /home/weewx/weewx.conf.*                                 #
#---------------------------------------------------------------------------------------------------#
#sudo cp /home/weewx/util/init.d/weewx.debian /etc/init.d/weewx                                      #
#sudo chmod +x /etc/init.d/weewx                                                                     #
#sudo update-rc.d weewx defaults 98                                                                  #
#sudo /etc/init.d/weewx start                                                                        #
#---------------------------------------------------------------------------------------------------#
#git clone https://github.com/matthewwall/weewx-sdr.git /home/pi/aprswx/weewx-sdr/                   #
#wget 'https://github.com/matthewwall/weewx-sdr/archive/master.zip' -P /home/pi/aprswx/weewx-sdr/    #
#sudo /home/weewx/bin/wee_extension --install /home/pi/aprswx/weewx-sdr/master.zip                   #
#---------------------------------------------------------------------------------------------------#
#sudo chmod 666                                           /home/weewx/weewx.conf                     #
#if ! grep -Fxq "[SDR]"                                   /home/weewx/weewx.conf; then               #
#    printf '\n###########################' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf '#############################' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf '######################\n\n[SD' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'R]\n    driver = user.sdr\n  ' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf '  cmd = rtl_433 -q -U -F json' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf ' -G\n    path = /usr/local/bi' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'n/\n    [[sensor_map]]\n     ' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf '   windDir = wind_dir.08FA.Ac' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'urite5n1Packet\n        windS' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'peed = wind_speed.08FA.Acurit' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'e5n1Packet\n        outTemp =' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'temperature.08FA.Acurite5n1Pa' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'cket\n        outHumidity = h' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'umidity.08FA.Acurite5n1Packet' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf '\n        rain_total = rain_t' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'otal.0BFA.Acurite5n1Packet\n ' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf '       inTemp = temperature.2' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf '4A4.AcuriteTowerPacket\n     ' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf '   inHumidity= humidity.24A4.' | sudo tee -a /home/weewx/weewx.conf                     #
#    printf 'AcuriteTowerPacket\n'          | sudo tee -a /home/weewx/weewx.conf; fi                 #
#sudo chmod 644                                           /home/weewx/weewx.conf                     #
#---------------------------------------------------------------------------------------------------#
#git clone https://github.com/cavedon/weewx-aprs.git /home/pi/aprswx/weewx-aprs/                     #
#wget 'https://github.com/cavedon/weewx-aprs/archive/v0.1.tar.gz' -P /home/pi/aprswx/weewx-aprs/     #
#sudo /home/weewx/bin/wee_extension --install /home/pi/aprswx/weewx-aprs/v0.1.tar.gz                 #
#---------------------------------------------------------------------------------------------------#
#    sudo nano /home/weewx/bin/user/aprs.py                                                         #
#    *** comment out these lines ***                                                                #
#    if record.get('windGust') is not None:                                                         #
#        # Gust (peak wind speed in mph in the last 5 minutes)                                      #
#        data.append('g%03.f' % record['wind_average'])                                             #
#    else:                                                                                          #
#        data.append('g...')                                                                        #
#---------------------------------------------------------------------------------------------------#
#git clone https://github.com/PhirePhly/aprx.git /home/pi/aprswx/aprx/                               #
#wget 'http://thelifeofkenneth.com/aprx/debs/aprx_2.9.0_raspi.deb' -P /home/pi/aprswx/aprx/          #
#sudo dpkg -i /home/pi/aprswx/aprx/aprx_2.9.0_raspi.deb                                              #
#---------------------------------------------------------------------------------------------------#
#sudo sed -ie 's/console=serial0,115200 //g'              /boot/cmdline.txt                          #
#sudo chmod 666                                           /boot/config.txt                           #
#if ! grep -Fxq "enable_uart=1"                           /boot/config.txt; then                     #
#    echo -e 'enable_uart=1'                | sudo tee -a /boot/config.txt; fi                       #
#sudo chmod 755                                           /boot/config.txt                           #
#---------------------------------------------------------------------------------------------------#
#sudo touch                                               /lib/systemd/system/hciattach.service      #
#echo -e '[Unit]'                           | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -n 'ConditionPathIsDirectory=/proc/'  | sudo tee -a /lib/systemd/system/hciattach.service      # 
#echo -n 'device-tree/soc/gpio@7e200000/'   | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e 'bt_pins'                          | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e 'Before=bluetooth.service'         | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e 'After=dev-ttyS0.device'           | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e ''                                 | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e '[Service]'                        | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e 'Type=forking'                     | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -n 'ExecStart=/usr/bin/hciattach /d'  | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -n 'ev/ttyS0 bcm43xx 921600 noflow '  | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e '-'                                | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e ''                                 | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e '[Install]'                        | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e 'WantedBy=multi-user.target'       | sudo tee -a /lib/systemd/system/hciattach.service      #
#echo -e ''                                 | sudo tee -a /lib/systemd/system/hciattach.service      #
#---------------------------------------------------------------------------------------------------#
# http://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3/
# http://65.41.143.157:800/docs/tncpi.html
#---------------------------------------------------------------------------------------------------#
# sudo /home/weewx/bin/wee_config --reconfigure                                                     #
# Breezy Point, MN, USA                                                                             #
# 377, meter                                                                                        #
# 46.584                                                                                            #
# -94.216                                                                                           #
# us                                                                                                #
# 0                                                                                                 #
#---------------------------------------------------------------------------------------------------#
#  /etc/aprx.conf                                                                                   #
#  mycall AD0HJ
#
#  <aprsis>
#      passcode -1
#      server    rotate.aprs2.net
#  </aprsis>
#
#  <logging>
#      pidfile /var/run/aprx.pid
#      rflog /var/log/aprx/aprx-rf.log
#      aprxlog /var/log/aprx/aprx.log
#  </logging>
#
#  <interface>
#      serial-device /dev/ttyS0  19200 8n1    KISS
#      callsign     $mycall  # callsign defaults to $mycall
#      tx-ok        true     # transmitter enable defaults to false
#      telem-to-is  false    # set to 'false' to disable
#  </interface>
#
#  <beacon>
#      beaconmode radio  # Send packet via APRS-IS and radio.
#      cycle-size  5m
#      beacon srccall AD0HJ via WIDE1-1 file "/dev/shm/aprs.pkt"
#  </beacon>
#---------------------------------------------------------------------------------------------------#
# /etc/ax25/axports 
#
# The format of this file is:
#
# name callsign speed paclen window description
#
#0      AD0HJ           19200   256     5       TNC-PI
#1      OH2BNS-1        1200    255     2       144.675 MHz (1200  bps)
#2      OH2BNS-9        38400   255     7       TNOS/Linux  (38400 bps)
#---------------------------------------------------------------------------------------------------#
# sudo kissattach /dev/ttyS0 1 10.0.1.1
#---------------------------------------------------------------------------------------------------#
# sudo aprx -vvvv
#---------------------------------------------------------------------------------------------------#
#mycall AD0HJ
#
#<aprsis>
#    passcode -1
#    server    rotate.aprs2.net
#</aprsis>
#
#<logging>
#    pidfile /var/run/aprx.pid
#    rflog /var/log/aprx/aprx-rf.log
#    aprxlog /var/log/aprx/aprx.log
#</logging>
#
#<interface>
#    ax25-device  AD0HJ
#    callsign     $mycall  # callsign defaults to $mycall
#    tx-ok        true     # transmitter enable defaults to false
#    telem-to-is  false    # set to 'false' to disable
#</interface>
#
#<beacon>
#    beaconmode radio  # Send packet via APRS-IS and radio.
#    cycle-size  5m
#    beacon srccall AD0HJ via WIDE1-1 file "/dev/shm/aprs.pkt"
#</beacon>
