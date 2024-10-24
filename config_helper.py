import os
import configparser 

DEF_LOCATION = ""
DEF_TEMPLATE = './config_template.conf'
class config_helper:
    def __init__(self, config_location = ''):
        self.config_location =config_location
        if config_location == '':
            config_location = DEF_LOCATION
        if not os.path.isfile(config_location):
            self.create_conf()
        self._config = configparser.ConfigParser()
        self._config.read(config_location)
    
    def create_conf(self):
        new_config = configparser.ConfigParser()
        if not os.path.isfile(DEF_TEMPLATE):
            print("Template not found exiting")
        else:
            new_config.read(DEF_TEMPLATE)
            with open(self.config_location, 'w') as configfile:
                new_config.write(configfile)
                configfile.close()

    def print_config(self):
        #  data in self.data:?
        for section in self._config.sections():
            print('[',section,']')
            for config in self._config[section]:
                print(config, "=", self._config[section][config],'(',type(self._config[section][config]),')')
        # print(self._config.sections())
    
    