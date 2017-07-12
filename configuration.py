import json, os

default_config_file_addr = 'config.json'
def get_config():
    with open(default_config_file_addr, 'r') as config_file:
        config = json.loads(config_file.read())
    return config

def install_template(temp_addr):
    config = get_config()
    template_dir = config['template-dir']
    with open(temp_addr, 'r') as new_temp:
        new_template = new_temp.read()

    with open(os.path.join(template_dir, os.path.split(temp_addr)[1]),'w') as new_temp:
        new_temp.write(new_template)
    return True
