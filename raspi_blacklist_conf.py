#!/usr/bin/env python3

import os, sys

def main():


    if(change_linux_directory ("/etc/modprobe.d/")                                                           == True):  sysexit()
    if(change_file_permissions("/etc/modprobe.d/raspi-blacklist.conf", 666)                                  == True):  sysexit()



    #check if file is present : try statement maybe?
    file = open('raspi-blacklist.conf','r')				                                     #== True):  sysexit(1)

    data = file.read()
    
    if(data.count("blacklist dvb_usb_rtl28xxu\n") == False):
        add_blacklist_dvb_usb_rtl28xxu = True
    else:
        add_blacklist_dvb_usb_rtl28xxu = False
        
    if(data.count("blacklist rtl_2830\n") == False):
        add_blacklist_rtl_2830 = True
    else:
        add_blacklist_rtl_2830 = False

    if(data.count("blacklist rtl_2832\n") == False):
        add_blacklist_rtl_2832 = True
    else:
        add_blacklist_rtl_2832 = False
  
    if((add_blacklist_dvb_usb_rtl28xxu) or (add_blacklist_rtl_2830) or (add_blacklist_rtl_2832)):
        file = open('raspi-blacklist.conf','a')
        if(add_blacklist_dvb_usb_rtl28xxu):
            file.write('blacklist dvb_usb_rtl28xxu\n')			      #== True):  sysexit()
        if(add_blacklist_rtl_2830):
            file.write('blacklist rtl_2830\n')	 	     	              #== True):  sysexit()
        if(add_blacklist_rtl_2832):
            file.write('blacklist rtl_2832\n')			              #== True):  sysexit()
        file.close()							      #== True):  sysexit()

    if(change_file_permissions("/etc/modprobe.d/raspi-blacklist.conf", 644)                                  == True):  sysexit()
    if(change_linux_directory ("/home/pi/Desktop/")                                                          == True):  sysexit()

    sys.exit(0)

def execute_shell_command(shell_command):

    # create shell command
    shell_command = shell_command

    # determine spaces to write
    spaces_to_write = (' ')
    for num in range(len(shell_command),99):
        spaces_to_write += (' ')

    # issue shell command
    if(os.system(shell_command) == False):
        sys.stdout.write(shell_command)
        sys.stdout.write(spaces_to_write)
        sys.stdout.write(':ok\n')
    else:
        sys.stdout.write(shell_command)
        sys.stdout.write(spaces_to_write)
        sys.stdout.write(':error\n')

def change_file_permissions(linux_file, permissions):

    # create shell command
    shell_command = ("sudo chmod " + str(permissions) + " " + linux_file) 

    # determine spaces to write
    spaces_to_write = (' ')
    for num in range(len(shell_command),99):
        spaces_to_write += (' ')

    # change file permissions
    if((os.path.isfile(linux_file)) == True):
        if(os.system(shell_command) == False):
            sys.stdout.write(shell_command)
            sys.stdout.write(spaces_to_write)
            sys.stdout.write(':ok\n')
        else:
            sys.stdout.write(shell_command)
            sys.stdout.write(spaces_to_write)
            sys.stdout.write(':error\n')
		
def change_linux_directory(linux_directory):

    # create shell command
    shell_command = ("cd " + linux_directory) 

    # determine spaces to write
    spaces_to_write = (' ')
    for num in range(len(shell_command),99):
        spaces_to_write += (' ')

    # change_linux_directory
    if((os.path.isdir(linux_directory)) == True):
        os.chdir(linux_directory)
        sys.stdout.write(shell_command)
        sys.stdout.write(spaces_to_write)
        sys.stdout.write(':ok\n')
    else:		
        sys.stdout.write(shell_command)
        sys.stdout.write(spaces_to_write)
        sys.stdout.write(':error\n')
		
def create_linux_directory(linux_directory):

    # create shell command
    shell_command = ("sudo mkdir " + linux_directory) 

    # determine spaces to write
    spaces_to_write = (' ')
    for num in range(len(shell_command),99):
        spaces_to_write += (' ')

    # create directory if not existing
    if((os.path.isdir(linux_directory)) == False):
        if(os.system(shell_command) == False):
            sys.stdout.write(shell_command)
            sys.stdout.write(spaces_to_write)
            sys.stdout.write(':ok\n')
        else:
            sys.stdout.write(shell_command)
            sys.stdout.write(spaces_to_write)
            sys.stdout.write(':error\n')
            
def remove_linux_directory(directory):

    # create shell command
    shell_command = ("sudo rm -r " + directory) 

    # determine spaces to write
    spaces_to_write = (' ')
    for num in range(len(shell_command),99):
        spaces_to_write += (' ')

    # remove directory if it exists
    if((os.path.isdir(directory)) == True):
        if(os.system(shell_command) == False):
            sys.stdout.write(shell_command)
            sys.stdout.write(spaces_to_write)
            sys.stdout.write(':ok\n')
        else:
            sys.stdout.write(shell_command)
            sys.stdout.write(spaces_to_write)
            sys.stdout.write(':error\n')

if __name__ == '__main__':
    main()
		
