import subprocess
import os
with open(os.devnull, "wb") as limbo:
                ip=raw_input("Please enter the IP you wish to verify ")
               
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print ip, "inactive"
                else:
                        print ip, "active"
