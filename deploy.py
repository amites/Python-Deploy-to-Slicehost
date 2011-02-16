import sys

from jinja2 import Template
from fabric.api import *
from fabric.contrib.files import *
from fabric.operations import *

from config import *

@hosts(*config['hosts'])
def new_site(config=config):
    # set folder vars
    apache_cfg_file = '%s/sites-available/%s' % (config['remote_apache'], config['domain'])
    apache_cfg_active = '%s/sites-enabled/%s' % (config['remote_apache'], config['domain'])

    upload_template('apache.conf', apache_cfg_file, config, True, 'templates', True)
    sudo( 'ln -s %s %s' % (apache_cfg_file, apache_cfg_active) )

    folder = {
        'project_base' : '%s/%s' % (config['remote_project_root'], config['project_name_root']),
        }
    if not exists(folder['project_base']):
        sudo( 'mkdir %s' % folder['project_base'] )

    try:
        folder['project_root'] = '%s/%s' % (folder['project_base'], config['folder_sub'])
        if not exists(folder['project_root']):
            sudo ( 'virtualenv %s' % folder['project_root'] )
    except:
        folder['project_root'] = folder['project_base']


    folder['project_apache'] = '%s/apache' % folder['project_root']
    if not exists(folder['project_apache']):
        sudo('mkdir %s' % folder['project_apache'])

    upload_template('site.wsgi', folder['project_apache'], config, True, 'templates', True)

    folder['project_logs'] = '%s/logs' % folder['project_root']
    if not exists(folder['project_logs']):
        sudo('mkdir %s' % folder['project_logs'])

    folder['project_repo'] = '%s/repo' % folder['project_root']
    if not exists(folder['project_repo']):
        sudo('mkdir %s' % folder['project_repo'])
        sudo('cd %s' % folder['project_repo'])
        sudo('git init --bare')
        sudo('chmod 0777 -R %s' % folder['project_repo'])

    try:
        local('cd %s' % config['local_project_root'], False)
        local('git remote add origin ssh://%s/%s' % (config['hosts'][0], folder['project_repo']), False)
        local('git push', False)
    except:
        print 'git not setup!!'

    try:
        sudo('chown -R %s:%s %s' % (config['owner'], config['group'], folder['project_base']))
    except:
        pass

    return folder

