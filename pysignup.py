#Script used to add new users to the www.brownvpn.tk system
#Copyright 2016
#Though this script is already in pretty good shape, any improvement suggestions are welcome

from subprocess import call

print "Welcome!"
try:
    while True:
        name = raw_input("Please choose a username: ")
        characters = len(name)
        if not name.isalnum():
            print "Please choose an alphanumeric username."
            continue
        if characters < 2:
            print "Please choose a username of at least 2 characters."
            continue
        if characters > 8:
            print "Please choose a username of at most 8 characters."
            continue
        if "sudo" in name:
            print "Sorry, but you're not clever enough for that."
            continue
        print "Trying to add user..."
        if call(["sudo", "adduser", name]) == 0:
            print "Done!"
            break
        else:
            continue
    print "Creating .bash_history file for {0}...".format(name)
    file = "/home/{0}/.bash_history".format(name)
    bashrc = "/home/{0}/.bashrc".format(name)
    call(['sudo','touch',file])
    print "Done!"
    print "Creating Python Projects folder for {0}...".format(name)
    directory = "/home/{0}/PyProjects".format(name)
    call(['sudo','mkdir',directory])
    print "Done!"
    print "Updating projects..."
    call(['sudo','updateprojs'])
    print "Done!"
    print "Some last minute fixes..."
    call(['sudo','chattr', '+i', file])
    call(['sudo','chattr','+i',bashrc])
    homedir = "/home/" + name
    call(['sudo','chmod','700',homedir])
    call(['sudo','usermod','-a','-G','students',name])
    print "Done!"
    print "{0} has been added to the system!".format(name)
    print "Goodbye!"
    exit()
except KeyboardInterrupt:
    print "\nSign-up Aborted. Goobye!"
    exit()
