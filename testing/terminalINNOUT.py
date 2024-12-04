import subprocess
import os



while True:
    
    cmd = input(f"{os.getcwd()}$ ")
    cmd = cmd.split(" ")
    try:
        if(cmd[0] == "cd"):
                os.chdir(cmd[1])     
                continue
        test = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output = test.communicate()[0].decode("utf-8")
        print(output)
    except NotADirectoryError:
        print(f"{cmd[1]} Is not a directory")
        
   

    
    
    
    