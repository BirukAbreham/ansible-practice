sys_fs.apache
=============

This role installs and configures Apache 2.x from the sury.org repo on Debian
and Ubuntu. The sury.org repo is not used on Debian 8 hosts, as it is
unsupported.

Requirements
------------

This role requires at least Ansible 2.6. Earlier releases may work, but are not supported.

Role Variables
--------------

	apache_http_port: 80
	apache_https_port: 443

Ports to listen on.

	apache_disable_modules: []

List of modules to disable, as passed to a2dismod.

	apache_enable_modules: []

List of modules to enable, as passed to a2enmod.

	apache_http_vhosts:
	  - server_name: example.com
	apache_https_vhosts: []

Vhosts to create. TODO document once template is finished.

Example Playbook
----------------

    - hosts: web
	  vars:
	    - apache_disable_modules:
		    - mpm_prefork
	    - apache_enable_modules:
		    - mpm_event
      roles:
        - sys_fs.apache

License
-------

MIT
