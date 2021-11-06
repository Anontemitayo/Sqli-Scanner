import requests as r
import os,sys
import time


whi = "\033[1;37m"
red = "\033[1;31m"
yel = "\033[1;33m"
cya = "\033[0;36m"
res = "\033[0;37;40m"
gre = "\033[1;32m"

os.system("clear")
def banner():
	print(""" \033[1;34;40m \033[01m
  ______       _  _                          
 / _____)     | |(_)                         
( (____   ____| | _                          
 \____ \ / _  | || |                         
 _____) ) |_| | || |                         
(______/ \__  |\_)_|                         
            |_|                              
  ______                                     
 / _____)                                    
( (____   ____ _____ ____  ____  _____  ____ 
 \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
 _____) | (___/ ___ | | | | | | | ____| |    
(______/ \____)_____|_| |_|_| |_|_____)_|   
 \033[1;36;40m
[✓] Coded by Anontemitayo
[✓] Sqli-Scanner is a python3 script written to scan websites for sql injection vulnerabilities
[✓] Dedicated to Pentesters and bug bounty hunters
[✓] Thanks : Qoyum Opeyemi
[✓] Message : Do not forget to follow me on GitHub                                         """)
banner()    
print("""\033[1;32m \033[01m
  [1] Scan one Website 
  [2] Scan Multiple Websites
  [3] About and Usage of the tool
  [4] Follow and Meet the owner 
  [5] Exit the tool
""") 
check = int(input("\033[1;32m \033[01m Choose an Option >>> "))    
if check == 1:
	  os.system("clear")
	  print(""" \033[1;34;40m \033[01m
  ______       _  _                          
 / _____)     | |(_)                         
( (____   ____| | _                          
 \____ \ / _  | || |                         
 _____) ) |_| | || |                         
(______/ \__  |\_)_|                         
            |_|                              
  ______                                     
 / _____)                                    
( (____   ____ _____ ____  ____  _____  ____ 
 \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
 _____) | (___/ ___ | | | | | | | ____| |    
(______/ \____)_____|_| |_|_| |_|_____)_|   
 \033[1;36;40m
[✓] Coded by Anontemitayo
[✓] Sqli-Scanner is a python3 script written to scan websites for sql injection vulnerabilities
[✓] Dedicated to Pentesters and bug bounty hunters                                    """)
	  print("""\033[1;32m \033[01m
  [1] Scan a Website
  [2] Exit the tool
 """)
	  choice = int(input('\033[1;32m \033[01mChoose an option : '))
	  if choice == 1:
	          os.system("clear")
	          print("""\033[01m \033[1;34;40m 
  ______       _  _                          
 / _____)     | |(_)                         
( (____   ____| | _                          
 \____ \ / _  | || |                         
 _____) ) |_| | || |                         
(______/ \__  |\_)_|                         
            |_|                              
  ______                                     
 / _____)                                    
( (____   ____ _____ ____  ____  _____  ____ 
 \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
 _____) | (___/ ___ | | | | | | | ____| |    
(______/ \____)_____|_| |_|_| |_|_____)_|   
 \033[1;36;40m
[✓] Coded by Anontemitayo
[✓] Note : The link must be with Query and it's parameters e.g http://site.com/gallery.php?id=1
""")
	          site = input("\033[1;33mEnter the link to be scanned [with http/https] : ")
	          if site.endswith("'"):
	          	print("\033[1;31mWrong link : Enter website link without ' ")
	          	sys.exit()
	         
	          if len(site) < 23:
	          	print("\033[1;31mEnter a full website link with query and parameters e.g http://site.com/page.php?id=1 ")
	          	sys.exit()
	          sql = site + "'"
	          code = r.get(site)
	          sitecode = str(code.text)
	          if "DNS" in sitecode:
	           	print("\n \033[1;31mWebsite is down or Website link not available")
	           	sys.exit() 
	          vul = r.get(sql)
	          sqlcode = str(vul.text)
	          
	          print("\n \033[0;37;40m Scanning : ",site)
	          
	          if sitecode != sqlcode or "syntax" in sqlcode or "Warning" in sqlcode or "Not Acceptable!" in sqlcode or "Mod_Security" in sqlcode:
	          	print(gre,"\n [✓]", site,"is vulnerable to SQL injection")
	          elif sitecode == sqlcode:
	          	print(red," \n [+]", site,"is not vulnerable to SQL injection")
	  if choice == 2:
	  	sys.exit()
elif check == 2:
	os.system("clear")
	print(""" \033[1;34;40m \033[01m
  ______       _  _                          
 / _____)     | |(_)                         
( (____   ____| | _                          
 \____ \ / _  | || |                         
 _____) ) |_| | || |                         
(______/ \__  |\_)_|                         
            |_|                              
  ______                                     
 / _____)                                    
( (____   ____ _____ ____  ____  _____  ____ 
 \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
 _____) | (___/ ___ | | | | | | | ____| |    
(______/ \____)_____|_| |_|_| |_|_____)_|   
 \033[1;36;40m
[✓] Coded by Anontemitayo
[✓] Sqli-Scanner is a python3 script written to scan websites for sql injection vulnerabilities
[✓] Dedicated to Pentesters and bug bounty hunters                                    """)
	print("""
 [1] Scan Multiple Sites
 [2] Exit the tool
""")
	muck = int(input('\033[1;32m \033[01mEnter your option : '))
	if muck == 1:
		os.system("clear")
		print("""\033[01m \033[1;34;40m 
  ______       _  _                          
 / _____)     | |(_)                         
( (____   ____| | _                          
 \____ \ / _  | || |                         
 _____) ) |_| | || |                         
(______/ \__  |\_)_|                         
            |_|                              
  ______                                     
 / _____)                                    
( (____   ____ _____ ____  ____  _____  ____ 
 \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
 _____) | (___/ ___ | | | | | | | ____| |    
(______/ \____)_____|_| |_|_| |_|_____)_|   
 \033[1;36;40m
[✓] Coded by Anontemitayo
[✓] Note : Save all links in a text file then input the link to the file 
""")
		print(gre,'[✓] Scan Multiple Sites by saving all the links in a text file ')
		path = input('\033[1;33m \n Enter File path [.txt only] : ')
		file = open(path,'r').readlines()
		os.system("clear")
		print("""\033[01m \033[1;34;40m 
  ______       _  _                          
 / _____)     | |(_)                         
( (____   ____| | _                          
 \____ \ / _  | || |                         
 _____) ) |_| | || |                         
(______/ \__  |\_)_|                         
            |_|                              
  ______                                     
 / _____)                                    
( (____   ____ _____ ____  ____  _____  ____ 
 \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
 _____) | (___/ ___ | | | | | | | ____| |    
(______/ \____)_____|_| |_|_| |_|_____)_|   
 \033[1;36;40m""")
		print(cya," \n             [+] Total number of sites : ",len(file),"\n")
		for password in file:
			
			password = password.strip()
			if password.endswith("'"):
			       
			       print("\033[1;31mWrong link : Enter website link without ' ")
			if len(password) < 23:
			        	
			        	print("\033[1;31mEnter a full website link with query and parameters e.g http://site.com/page.php?id=1 ")
			
			pasr = password + "'"
			cdr = r.get(password)
			passcode = str(cdr.text)
			if "DNS" in passcode:
				print("\n \033[1;31mWebsite is down or Website link not available")
			vuln = r.get(pasr)
			sqlcdr = str(vuln.text)
			if passcode != sqlcdr or "syntax" in sqlcdr or "Warning" in sqlcdr or "Not Acceptable!" in sqlcdr or "Mod_Security" in sqlcdr:
			        	   
			        	   print(gre,"[✓]",password,"<==> Vulnerable")
			elif passcode == sqlcdr:
			   
			   print(red,"[+]",password,"<==> Not Vulnerable")  
elif check == 3:
	  	
	  	os.system("clear")
	  	time.sleep(0.5)
	  	print(""" \033[1;34;40m \033[01m
  ______       _  _                          
 / _____)     | |(_)                         
( (____   ____| | _                          
 \____ \ / _  | || |                         
 _____) ) |_| | || |                         
(______/ \__  |\_)_|                         
            |_|                              
  ______                                     
 / _____)                                    
( (____   ____ _____ ____  ____  _____  ____ 
 \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
 _____) | (___/ ___ | | | | | | | ____| |    
(______/ \____)_____|_| |_|_| |_|_____)_|   
 \033[1;36;40m
[✓] Coded by Anontemitayo
[✓] Note : The link must be with Query and it's parameters e.g http://site.com/gallery.php?id=1
""")
	  	print("""\033[1;32m
	[✓]About:
SqliScanner is a tool to Scan websites for SQL injection vulnerability 

	[✓]Usage:
Provide the tool the full link (with query and parameters e.g http://site.com/gallery.php?id=1) of the website you want to scan then wait for the tool to scan (+_+) """)
elif check == 4:
	os.system("clear")
	print(""" \033[1;34;40m \033[01m
  ______       _  _                          
 / _____)     | |(_)                         
( (____   ____| | _                          
 \____ \ / _  | || |                         
 _____) ) |_| | || |                         
(______/ \__  |\_)_|                         
            |_|                              
  ______                                     
 / _____)                                    
( (____   ____ _____ ____  ____  _____  ____ 
 \____ \ / ___|____ |  _ \|  _ \| ___ |/ ___)
 _____) | (___/ ___ | | | | | | | ____| |    
(______/ \____)_____|_| |_|_| |_|_____)_|   
 \033[1;36;40m
[✓] Coded by Anontemitayo
[✓] Note : The link must be with Query and it's parameters e.g http://site.com/gallery.php?id=1
""")
	print("""
[1] Message on Facebook
[2] Follow on GitHub 
	""")
	pick = int(input('Choose an option : '))
	if pick == 1:
	 os.system("xdg-open https://www.facebook.com/Anon.temitayo")
	elif pick == 2:
	   	os.system("xdg-open https://github.com/Anontemitayo")
elif check == 5:
	sys.exit()
else:
	print("choose from the option")  			 