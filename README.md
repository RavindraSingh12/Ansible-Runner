CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Configuration
 * Usage
 * Tasks and Solutions
 * Troubleshooting
 * Maintainers
 
INTRODUCTION
------------

This playbook is intended solely for self imrovement purposes. In this playbook we are 
exploring [ansible-runner](https://ansible-runner.readthedocs.io/en/stable/intro.html) package for python to run Ansible programmatically.

 * For a full description of the module, visit the project page:
 
   * [Introduction of Ansible Runner](https://ansible-runner.readthedocs.io/en/stable/intro.html)
   * [Python integration of the module](https://ansible-runner.readthedocs.io/en/stable/python_interface.html)
   * [Git repo Ansible Runner](https://github.com/ansible/ansible-runner/blob/devel/ansible_runner/)
   
REQUIREMENTS
------------

This playbook requires the following modules:

 * Python = 3+
 * Ansible = 2.9+
 * Centos7
 * pip3
 * Enable [password less ssh](https://www.redhat.com/sysadmin/passwordless-ssh) on all minion nodes from Ansible master.
 
INSTALLATION
------------
 
 * Create a [virtual env](https://docs.python.org/3/library/venv.html) in your desired location.

 * Activate the virtual env.
    * source venvname/bin/activate
    * export proxies if you have any:
        * export {http,https}_proxy=http://proxy_ip:proxy_port
        * pip3 install -r requirements.txt
        
  > This process will install Ansible Runner and other required libraries.

CONFIGURATION
-------------
 
 * Configure Ansible Runner:

   - private_data_dir: this is the project root which should contain the dir 
   structure required for Ansible Runner to identify playbooks, vars, templates,
   roles etc.
   - Follow [this](https://cdn.swapps.com/uploads/2019/10/image-6.png) dir structure to use this playbook.
   - Add private ssh key to env/ssh_key file.
   - Add extra vars to env/extravars file.
   - Add all playbooks to project/ folder.
   - This project folder will be treated as root of your playbooks.
   - So for templates you can create a template folder in there and keep your templates there.
   - Add env variable to env/envvars file.
   - Add commandline flags to env/cmdline file.
   - Add inventory to inventory/hosts file.

USAGE
-----

   source venv/bin/activate.sh
   >(venv) python3 run.py


TASKS AND SOLUTIONS
------------------- 
 Write the Ansible playbook which can cover following pointers:
 
 > mentioning plabook names followed by how I have done tasks.

* Have python Custom Environment and use the python in custom environment to run Ansible(not in Host, minions)
    * created with:
         * python3 venv -m ex-venv
         
* Check File Status.
* Pass the status variable to another playbook.
    * registerVarRemoteHost.yaml
        * used [**stat**](https://docs.ansible.com/ansible/latest/modules/stat_module.html) module to check status of the file.
        * register result to output variable.
        * added that variable to a dummy host variable play1var with [**add_host**](https://docs.ansible.com/ansible/latest/modules/add_host_module.html).
    * useVarRemoteHost.yaml
        * used the resulted output variable with "{{ hostvars['dummyhost']['play1var'] }}"
        
* Upload something to URL(using POST)
    * uploadContent.yaml
        * used [uri](https://docs.ansible.com/ansible/latest/modules/uri_module.html) module to create a post request 
        * lookup to add the file to the body of the request.
        
* Check the version of Operating System and display.
    * In registerVarRemoteHost.yaml used "{{ ansible_distribution }}" env variable to get remotes OS version.
    
* Create a List and add variables dynamically to the list(variables needs to be passed as extra variables)  
    * extraVarList.yaml
    * wrote all extra variables in env/extravars.
    * created one empty list dynamiclist in the playbook.
    * used [set_fact](https://docs.ansible.com/ansible/latest/modules/set_fact_module.html) module 
    to append extra vars to the dynamiclist.
* Imported all playbooks in main.yaml.
* Triggered main.yaml with run.py, ansible_runner.run(playbook='ansible_runner',private_data_dir='/location/of/this/dir')

    
TROUBLESHOOTING
---------------

* If the Ansible Runner can't find the location of the playbooks, ssh_key, vars etc?
    - Check the value of  private_data_dir which must be set to the folder structure root.

* If ansible_runner module is not installed:
    - Check pip3 list.
    - Install requirements.txt after activating the venv.
    
* If playbook takes longer than usual:
    
    - Check env/settings, which if not present will take defaults of idle_timeout, job_timeout etc.


MAINTAINERS
-----------

Current maintainer:
    _Ravindra Singh - https://www.linkedin.com/in/ravindra-singh-aa1b2282/_





 
