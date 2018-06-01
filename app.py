import os

from tgdeleter.app import start

config_file = os.environ.get('TGDELETER_CONFIG', 'local_config.LocalConfig')
print('Start using {}'.format(config_file))

if __name__ == '__main__':
    start(config_file)
