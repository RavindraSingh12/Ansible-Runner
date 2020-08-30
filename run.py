import ansible_runner
r = ansible_runner.run(playbook='main.yaml',private_data_dir='/userdata/theVerizonTask/')
# successful: 0
print("Final status:")
print(r.stats)

