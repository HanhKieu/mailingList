#!/usr/bin/python3
#######################################
#-------------WRITTEN BY---------------
#-/-/-/-/-/-/-\-\-\-\-\-\-\-\-\-\-\-\-\
# H   H        A       N    N     H   H
# H   H       A A      N N  N     H   H
# H H H      A A A     N   NN     H H H
# H   H     A     A    N   NN     H   H
# H   H    A       A   N    N     H   H
#-/-/-/-/-/-/-\-\-\-\-\-\-\-\-\-\-\-\-\
#######################################
#######################################
# o/////+++++//////////////////////////o
# o....------........---:::--------....+
# o....-----.-//////::-------::/++--...o
# s....--/o+/-```````````````````o/--..o
# s...--s/```````````````````````+/---.o
# y..---y````````````````````````o----.s
# y..---s:```````````````````````s----.s
# y..---:s``````````````````````-s----.s
# s..----y````s:``````````/h````o:----.s
# s..----s-```.`````````````````s-----.s
# s..----:+````````````````````.s--.--.s
# s..-----y````````````````````+/-..--.s
# s......-d````:+++////:/::/-``s--..--.s
# s......-y:```````````````````h------.s
# s....---sy:````````````````/hm/---...s
# s..---/ymmNmy+.```````.:/smNNmmh+...-s
# s..:ohmmmmmNmmNho/oshmNmNNmmmmmmmh:--s
# s-ymmmmmmmmmNNNmNmNNNNNNmmmmmmmmmmms-s
# smmmmmmmmmmmmmNNmmmNNmmmmmmmmmmmmmmmho
########PURPOSE OF THIS SCRIPT#########
#The purpose of this script is to
#compile a list of emails of people
#we can send surveys to
#######################################
__author__ = 'hhkieu'

import re

writeFile = open('mailingList.txt','w')
i = 0  # the checker for every 10 UNDERGRADUATE ACCOUNT
with open('userdb', 'r') as myFile:
    for line in myFile:
        if re.search('UND$', line):
            if(i % 10 == 0):  # for every 10 UNDERGRAD STUDENTS
                student = line.split(':')
                if re.search('@', student[-2]):
                    writeFile.write(student[-2] + '\n')
            i += 1
