import configparser

par = configparser.ConfigParser()

par.read("grabify.cfg")

webhook = par.get("discord", "webhook")
