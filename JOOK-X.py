import os
try:
	import requests
except:
	os.system("pip install requests")
	import requests
version="2.2.9"
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
logo=red+str("""
   
  888888  .d88888b.   .d88888b.  888    d8P      Y88b   d88P 
    "88b d88P" "Y88b d88P" "Y88b 888   d8P        Y88b d88P  
     888 888     888 888     888 888  d8P          Y88o88P   
     888 888     888 888     888 888d88K            Y888P    
     888 888     888 888     888 8888888b           d888b    
     888 888     888 888     888 888  Y88b  888888 d88888b   
     88P Y88b. .d88P Y88b. .d88P 888   Y88b       d88P Y88b  
     888  "Y88888P"   "Y88888P"  888    Y88b     d88P   Y88b 
   .d88P                                                     
 .d88P"                                                      
888P"                                                        
""")   
slogan2="                 βββ πππππ ππ ππ π₯πππ£ ππ¦ππππ£ βββ                      "
header=logo+cyan+"\n\n\n\t\tDeveloped By : πΏπ-πΏππππ\n\n"+green+"\t\t     Version : "+str(version)+" \n\n"+end+line+"\n"+end
\x1b[92;1m===========================================>\x1b[92;1m
\x1b[93;1m ~πΌπππππ       \x1b[92;1m=>      \x1b[93;1m ππ·π-ππΏπ΄π π΅ππ π
\x1b[93;1m ~πππΌπππΌπ   \x1b[92;1m=>      \x1b[93;1m+8801979526394
\x1b[93;1m ~ππΌπΎππ½πππ       \x1b[92;1m=>      \x1b[93;1mγ¬γ€γγ³γγ¬γ€γγΌγ€
\x1b[92;1m===========================================>\x1b[92;1m
"""%(h))

print_check=requests.get("https://www.facebook.com/profile.php?id=100072883587040").text

if print_check=="header":
	print(header)
elif print_check=="logo":
	print(logo)
elif print_check=="slogan2":
	print(slogan2)
