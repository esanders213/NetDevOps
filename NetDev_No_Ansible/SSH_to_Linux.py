import getpass
from fabric import Connection, Config

password = getpass.getpass("Enter your password: ")

config = Config(overrides={'sudo': {'password': password}})
conn = Connection("192.168.39.248", user="erik", config=config)

# Executes the command on the connected device.
result = conn.run("ping -c 5 192.168.39.1")

