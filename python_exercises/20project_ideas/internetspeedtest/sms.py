"""
Python3 Program to send SMS from WAY2SMS
"""
import requests
from bs4 import BeautifulSoup

class sms:

	def __init__(self,username,password):

		
		'''Takes username and password as parameters for constructors
		and try to log in
		'''

		self.url='http://site24.way2sms.com/Login1.action?'

		self.cred={'username': username, 'password': password}

		self.s=requests.Session()			# Session because we want to maintain the cookies

		
		'''changing s.headers['User-Agent'] to spoof that python is requesting
		'''

		self.s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"

		self.q=self.s.post(self.url,data=self.cred)

		self.loggedIn=False				# a variable of knowing whether logged in or not

		if self.q.status_code!=200:			# http status 200 == OK

			self.loggedIn=False

		else:

			self.loggedIn=True

		self.jsid=self.s.cookies.get_dict()['JSESSIONID'][4:]	    # JSID is the main KEY as JSID are produced every time a session satrts


	def send(self,mobile_no,msg):

		
		'''Sends the message to the given mobile number
		'''

		if len(msg)>139 or len(mobile_no)!=10 or not mobile_no.isdecimal():	#checks whether the given message is of length more than 139

			return False							#or the mobile_no is valid

		self.payload={'ssaction':'ss',
				'Token':self.jsid,					#inorder to visualize how I came to these payload,
			        'mobile':mobile_no,					#must see the NETWORK section in Inspect Element
       				 'message':msg,						#while messagin someone from your browser
			        'msgLen':'129'
       			     }

		self.msg_url='http://site24.way2sms.com/smstoss.action'

		self.q=self.s.post(self.msg_url,data=self.payload)

		if self.q.status_code==200:

			return True

		else:
			return False


	def logout(self):

		self.s.get('http://site24.way2sms.com/entry?ec=0080&id=dwks')

		self.s.close()								# close the Session

		self.loggedIn=False



s=sms("<--Your Way2SMS Username-->","<--Your Way2SMS Password-->") #Object Creation


print("Sending SMS.................")

l=["<--Your receivers list-->"]


for i in l:

    s.send(i,"<--Your message to send-->") #calling methods in the class



print("SMS has been sent:")

s.logout()




