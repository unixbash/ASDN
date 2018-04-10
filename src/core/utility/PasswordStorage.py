import bcrypt
import configparser

raw_password = "ASDN2018"
from getpass import getpass
master_secret_key = getpass('')
salt = bcrypt.gensalt()
combo_password = raw_password + salt + master_secret_key
hashed_password = bcrypt.hashpw(combo_password, salt)

config = configparser.ConfigParser()
config.read("/etc/settings.txt")
pawd = config.get("configuration","password")
