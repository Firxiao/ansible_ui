import os.path

# LDAP settings exapmle
#NT4_DOMAIN = ""
#LDAP_URL = "ldap://ldapserver:port"
#BIND_USER = "CN=adreader,OU=xxx,OU=xxx,DC=xxx,DC=xxxx"
#BIND_PASSWORD = "*****"
#SEARCH_DN = "ou=xxxx,dc=xxxx,dc=xxxx"

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # use mysql backend.
        'NAME': 'ansible',                      # Database name.
        'USER': 'ansibleuser',                      # mysql user.
        'PASSWORD': 'password',                  # mysql password.
        'HOST': 'localhost',                     # mysql hostname or ip
        'PORT': '3306',                      # mysql port
    },
}

# Mail settings
MAIL_SENDER = "sender@domain.com"
MAIL_SMTP = "mail.domain.com"

# Ansible-playbook path
ANSIBLE_PLAYBOOK = '/Users/Firxiao/virtualenv/ansibleweb/bin/ansible-playbook'
