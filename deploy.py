#!/usr/bin/python3
from pathlib import Path
import subprocess as sp
# prj
PRJ_NAME = "gcms"
PRJ_WEBPORT = 80
PRJ_ROOJ = Path(__file__).parent
PYTHON_CMD = "/usr/local/conda/envs/django/bin/python3"
        
# nginx
NGINX_SITECONF_DEFAULT = Path("/etc/nginx/sites-enabled/default")
NGINX_SITECONF_PATH = Path("/etc/nginx/sites-enabled/")
NGINX_SITECONF_PRJLINK = NGINX_SITECONF_PATH / f"nginx-{PRJ_NAME}.conf"
NGINX_SITECONF_PRJ = PRJ_ROOJ / f"config/nginx-{PRJ_NAME}.conf"
NGINX_SITECONF_TEMPLAT = \
f"""
server {{
    listen		{PRJ_WEBPORT};

    location / {{
        uwsgi_pass	unix:///run/uswgi-{PRJ_NAME}.sock;
        include		 /etc/nginx/uwsgi_params; 
    }}

    location /collected_static/ {{
        root {PRJ_ROOJ}/;
    }}

    location /protected_file/ {{
        internal;
        alias {PRJ_ROOJ}/media/;
    }}        
}}
"""        
if NGINX_SITECONF_DEFAULT.exists():
    NGINX_SITECONF_DEFAULT.unlink()
if NGINX_SITECONF_PRJLINK.exists():
    NGINX_SITECONF_PRJLINK.unlink()   

NGINX_SITECONF_PRJLINK.symlink_to(PRJ_ROOJ / f"config/nginx-{PRJ_NAME}.conf")

if NGINX_SITECONF_PRJ.exists():
    NGINX_SITECONF_PRJ.unlink()
with open(NGINX_SITECONF_PRJ,"a") as nginx_file:
    nginx_file.write(NGINX_SITECONF_TEMPLAT)

# uwsgi
UWSGI_CONF_PRJ = PRJ_ROOJ / f"config/uwsgi-{PRJ_NAME}.ini"
UWSGI_CONF_TEMPLAT = \
f"""
[uwsgi]
chdir={PRJ_ROOJ}
module={PRJ_NAME}.wsgi:application
socket=/run/uwsgi-{PRJ_NAME}.sock
workers=2
pidfile=/run/uwsgi-{PRJ_NAME}.pid
uid=www-data
gid=www-data
master=true
enable-threads=true
vacuum=true
daemonize=/var/uwsgi-{PRJ_NAME}.log
disable-logging=true
thunder-lock=true
""" 
if UWSGI_CONF_PRJ.exists():
    UWSGI_CONF_PRJ.unlink()
with open(UWSGI_CONF_PRJ,"a") as uwsgi_file:
    uwsgi_file.write(UWSGI_CONF_TEMPLAT)

# static files
sp.run([PYTHON_CMD,"manage.py","collectstatic"])

# database
# sp.run([PYTHON_CMD,"manage.py","makemigrations"])
# sp.run([PYTHON_CMD,"manage.py","migrate"])
