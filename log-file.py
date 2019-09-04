import logging

# to store in a log file
logging.basicConfig(filename="C:/Users/user/Downloads/test.log" ,
                    # for formate
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt= '%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
# by second parameter we will be able to store debug and info msg in file also

####################
# this will print in console but not upper two
logging.debug("Debug msg")
logging.info("Info msg")
logging.error("Error msg")
logging.critical("Critical msg")
logging.warning("Warning msg")