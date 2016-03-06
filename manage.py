#Version : Phython/Django 2.7.6, PostgreSQL 9.3.4
#Author : Vaibhavi Desai
#Github username : desaivaibhavi
#email : ranihaileydesai@gmail.com

#!/usr/bin/env python
import os
import sys
import uuid

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infohub.settings")

    from django.core.management import execute_from_command_line

    # hack to prevent admin prompt
    if len(sys.argv) == 2 and sys.argv[1] == 'syncdb':
        sys.argv.append('--noinput')


    execute_from_command_line(sys.argv)
    
    #additional code to create superuser 

    if 'syncdb' in sys.argv:
        from django.contrib.auth.models import User
        admin_id = 'admin'
        admin_email = "admin@superuser.com"
        admin_password = "admin_pass"


         # admin exists?
        user_list = User.objects.filter(username=admin_id)
        if len(user_list) == 0: 
            print 'create superuser: ' + admin_id
            new_admin = User.objects.create_superuser(admin_id, admin_email,admin_password)
            
            from webhub.models import Pcuser
            user = Pcuser(user=new_admin, phone="", gender="", location="", verified = uuid.uuid4().hex)
            user.save()
        else: 
            print 'admin exists'
    
    
