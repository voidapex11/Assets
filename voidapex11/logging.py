import logging as logger
from Assets.voidapex11.setting import *
import time


def timess():
  return time.asctime


class log:
  import logging as logger
  from logging import StreamHandler
  from logging import Formatter
  import sys
  import time
  
  def __init__(self, level, clear=True):
    '''
    logging is a program made by voidapex11 that logs mesages not just to console but also to a file
    '''
    try:
      with open('Assets/app.log', 'r') as appLog:
        if clear and len(appLog.readlines()) >= 500:  
          open('Assets/app.log', 'w').close()
          with open('Assets/app.log', 'a') as file:
            
            file.write(f'\n\n{timess()}\n\n\n **** START **** \n\n\n\n')
            file.close()
        else:
          with open('Assets/app.log', 'a') as file:
            file.write(f'\n\n{timess()}\n\n **** START **** \n\n\n\n')
            file.close()
    except:
      with open('Assets/app.log', 'x+') as appLog:
        if len(appLog.readlines()) >= 500:
          open('Assets/app.log', 'w').close()

        with open('Assets/app.log', 'a') as file:
          file.write('\n\n\n\n **** START **** \n\n\n\n')
          file.close()
      # setup a log formatter
    formatter = self.logger.Formatter('\n%(asctime)s:  %(name)s: %(levelname)s: \n%(message)s')

    # setup a StreamHandler for console logging
    console_handler = self.StreamHandler(self.sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # add the StreamHandler to the logs logger
    self.logger.getLogger('').addHandler(console_handler)

    # setup a FileHandler for app.log file logging
    file_handler = self.logger.FileHandler('Assets/app.log')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # add the FileHandler to the logs logger
    self.logger.getLogger('').addHandler(file_handler)

    # set the overall logging level for the logs logger
    self.logger.getLogger('').setLevel(level)


      
  
  def DEBUG(self, message):
    self.logger.debug(message)
    return
  
  def debug(self, message):
    self.logger.debug(message)
    return

  def INFO(self, message):
    self.logger.info(message)
    return
  
  def info(self, message):

    self.logger.info(message)
    return

  def WARNING(self, message):
    self.logger.warning(message)
    return

  def warning(self, message):
    self.logger.warning(message)
    return

  def ERROR(self, message):
    self.logger.error(message)
    return

  def error(self, message):
    self.logger.error(message)
    return

  def CRITICAL(self, message):
    self.logger.critical(message)
    return

  def critical(self, message):
    self.logger.critical(message)
    return


logging = log(logger.INFO)
logSetting = setting.get('loggingLvl', defaltData='INFO')
try:
  exec(f'logging = log(logger.{logSetting})')
except:
  pass