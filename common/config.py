import ConfigParser

class CloudConfig(object):
    def __init__(self, config='config.ini'):
        self.cfg = ConfigParser.ConfigParser()
        with open('config.ini', 'r') as f:
            self.cfg.readfp(f)

    def get(self, section, option):
        return self.cfg.get(section, option)

if __name__ == '__main__':
    config = CloudConfig()
    print config.get('CloudDB', 'user')