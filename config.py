config = {
    'domain_sub' : False, # If deploying to a subdomain enter value as 'domain_sub' : 'SUBDOMAIN',
    'domain_base' : 'PRIMARYDOMAIN',
    'project_name_root' : 'PROJECT_ROOT_DIR',
    'folder_sub' : 'virtualenv',
    'folder_project' : 'PROJECT_DIR',

    'remote_apache' : '/usr/local/apache2/conf',
    'remote_project_root' : '/home/python',

    'local_project_root' : 'LOCAL_PROJECT_ROOT_DIR',

    'owner' : 'USER_NAME',
    'group' : 'USER_GROUP',
    'server_admin_email' : 'ADMIN@DOMAIN.COM',

    'hosts' : ('SSH_HOST', ),

    'slice_api' : 'SLICEHOST_API_KEY',
    'slice_id' : 'SLICEHOST_SLICE_ID',
    }

if config['domain_sub']:
    config['domain'] = '%s.%s' % (config['domain_sub'], config['domain_base'])
