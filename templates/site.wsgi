import os, site, sys

prev_sys_path = list(sys.path)
site.addsitedir('{{ remote_project_root }}/{{ project_name_root }}/{% if folder_sub %}{{ folder_sub }}/{% endif %}lib/python2.6/site-packages')

sys.path.append('{{ remote_project_root }}/{{ project_name_root }}/{% if folder_sub %}{{ folder_sub }}/{% endif %}{{ folder_project }}')
sys.path.append('{{ remote_project_root }}/{{ project_name_root }}/{% if folder_sub %}{{ folder_sub }}/{% endif %}')

new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ['DJANGO_SETTINGS_MODULE'] = '{{ folder_project }}.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

