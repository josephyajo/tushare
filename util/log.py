#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import logging.config
import configuration as config

class Log:
    logger = None
     
    def __init__(self):
        logging.config.fileConfig(config.logging_conf_dir)
        self.logger = logging.getLogger("logger01")
     
    def debug(self, msg):
        self.logger.debug(msg)
     
    def info(self, msg):
        self.logger.info(msg)
        
    def warning(self, msg):
        self.logger.warning(msg)
         
    def warn(self, msg):
        self.logger.warn(msg)
        
    def error(self, msg):
        self.logger.error(msg)
    
    def critical(self, msg):
        self.logger.critical(msg)
 
 
Log().logger.info("configuration")
