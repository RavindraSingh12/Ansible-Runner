import ansible_runner
r = ansible_runner.run(playbook='main.yaml',private_data_dir='/Ansible-Runner/')
# successful: 0
print("Final status:")
print(r.stats)

