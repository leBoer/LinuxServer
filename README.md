# Introduction
This is a simple item catalog application, similar to the one submitted for a previous Udacity project. However, this time it is hosted on AWS. The challenge is in setting up a Linux (Ubuntu), Apache, Postgresql, Python stack.

## Necessary information
1. IP Address: 52.27.112.205
2. SSH Port: 2200
3. Complete URL: http://188.166.146.26/
4. Password for user "grader" is "22438608"

## Software installed
- apache2
- libapache2-mod-wsgi
- postgresql
- git
- python-dev
- python-pip
- sqlalcemy
- httplib2
- Flask

## Configurations
1. Created a user named grader and granted sudo permissions
2. Updated all packages
3. Configured local timezone to UTC
4. Changed the SSH port from 22 to 2200
5. Configured a UFW to only allow incoming connections for SSH(port 2200), HTTP (port 80), and NTP (port 123)
6. Added user catalog to postgresql with CREATEDB privileges
7. /etc/apache2/sites-available/000-default.conf looks like this:

		<VirtualHost *:80>
        	ServerName 52.27.112.205

	        ServerAdmin admin@52.27.112.205
	        DocumentRoot /var/www/app/app

	        ErrorLog ${APACHE_LOG_DIR}/error.log
	        CustomLog ${APACHE_LOG_DIR}/access.log combined

	        WSGIScriptAlias / /var/www/app/app/myapp.wsgi
	        <Directory /var/www/app/app/>
	        Order allow,deny
	        Allow from all
	        </Directory>
	        Alias /static /var/www/app/app/static
	        <Directory /var/www/app/app/static/>
	        Order allow,deny
	        Allow from all
	        </Directory>
		</VirtualHost>

## Resources used
- askubuntu.com
- Udacity Forums
- Stack Overflow
- Digital Ocean
- Google.com
