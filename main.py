#!/usr/bin/python3

import paramiko
import sshtunnel
import time
import threading

def open_sshtunnel(thread):
	with sshtunnel.open_tunnel(
		("proxy-vm.ddns.net", 22),
		ssh_username="ubuntu",
		ssh_pkey="Public_Key.pem",
		remote_bind_address=("0.0.0.0", 8000),
		local_bind_address=('127.0.0.1', 54321)
    ) as tunnel:
		client = paramiko.SSHClient()
		client.load_system_host_keys()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		#client.connect('127.0.0.1', 4444)
		#do some operations with client session
		#client.close()
		#source: https://pypi.org/project/sshtunnel/
		thread.join()

def game_thread():
	time.sleep(10)


def main():
	t1 = threading.Thread(target=game_thread)
	t2 = threading.Thread(target=open_sshtunnel, args=(t1,))
	t1.start()
	t2.start()

if __name__ == '__main__':
	main()