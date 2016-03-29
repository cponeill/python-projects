#!/usr/bin/env python

#Copyright Brown Tech Services, 2016
#This is a python command-line tool for adding, suspending, and re-enabling client sites

from subprocess import call
from sys import argv

#print argv[1]
#exit()

def add(cliname):
    cliemail = raw_input("Client email: ")

    #Set some variables to know where to put things
    location = "/{0}.img".format(cliname)
    ddof = "of=" + location
    docroot = "/var/www/html/{0}".format(cliname)

    #Create and mount a loop device for holding the site
    print("Making the .img file...")
    call(['fallocate','-l','300M',location])
    print("Done!")
    print("Filling it with zeroes...")
    call(['dd','if=/dev/zero',ddof,'count=512k'])
    print("Done!")
    call(['mkdir',docroot])
    print("Creating loop device filesystem...")
    call(['mkfs',location])
    print("Done!")
    print("Modifying fs table and mounting the device...")
    with open('/etc/fstab','a') as f:
        f.write("\n{0} {1} auto loop 0 0".format(location,docroot))
    call(['mount',docroot])
    print("Done!")

    #Set permissions on the new site document root
    print("Setting permissions...")
    call(['chown','-R','www-data:www-data',docroot])
    call(['chmod','755',docroot])
    print("Done!")

    #Modify an Apache2 v-host file to add to the sites
    configfile = '''<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.

        ServerName www.{0}.tk
        ServerAlias {0}.tk
        ServerAdmin {1}
        DocumentRoot /var/www/html/{0}
        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${{APACHE_LOG_DIR}}/error.log
        CustomLog ${{APACHE_LOG_DIR}}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>\n\n'''.format(cliname,cliemail) #Needed to add newlines so that Let's Encrypt could work correctly

    confloc = "/etc/apache2/sites-available/{0}.conf".format(cliname)

    with open(confloc,'w') as g:
        g.write(configfile)

    #Enable the site, and done!
    call(['a2ensite',cliname])
    call(['service','apache2','reload'])
    print("All done with everything!")

def suspend(cliname):
    original = "/etc/apache2/sites-available/{0}.conf".format(cliname)
    ssloriginal = "/etc/apache2/sites-available/{0}-le-ssl.conf".format(cliname)

    redir = "/etc/apache2/sites-available/{0}-rd.conf".format(cliname)
    sslredir = "/etc/apache2/sites-available/{0}-rd-le-ssl.conf".format(cliname)

    insertion = "Redirect / https://www.browntech.tk\n"

    lines = open(original,'r').readlines()
    working = open(redir,'w')
    for line in lines:
        working.write(line)
        if "DocumentRoot" in line: working.write(insertion)
    working.close()

    lines = open(ssloriginal,'r').readlines()
    working = open(sslredir,'w')
    for line in lines:
        working.write(line)
        if "DocumentRoot" in line: working.write(insertion)
    working.close()

    rdsite = "{0}-rd".format(cliname)
    origssl = "{0}-le-ssl".format(cliname)
    rdssl = "{0}-rd-le-ssl".format(cliname)

    call(['a2dissite',cliname,origssl])
    call(['a2ensite',rdsite,rdssl])
    call(['service','apache2','reload'])

def enable(cliname):
    rdsite = "{0}-rd".format(cliname)
    origssl = "{0}-le-ssl".format(cliname)
    rdssl = "{0}-rd-le-ssl".format(cliname)

    call(['a2ensite',cliname,origssl])
    call(['a2dissite',rdsite,rdssl])
    call(['service','apache2','reload'])

    rdfile = "/etc/apache2/sites-available/{0}.conf".format(rdsite)
    sslrdfile = "/etc/apache2/sites-available/{0}.conf".format(rdssl)

    call(['rm',rdfile,sslrdfile])

if len(argv) != 3:
    print("Usage: clientools add|suspend|enable clientname")
    exit()

if argv[1] == "add": add(argv[2])
elif argv[1] == "suspend": suspend(argv[2])
elif argv[1] == "enable": enable(argv[2])
else:
    print("Usage: clientools add|suspend|enable clientname")
    exit()
