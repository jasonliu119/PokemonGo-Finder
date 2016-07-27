import subprocess, time, os, signal
from subprocess import STDOUT, check_output

cmd = "python main.py"

if __name__ == '__main__':
    while True:
        p = subprocess.Popen(["python","main.py"])
        print " map pid " + str(p.pid)
        time.sleep(60 * 1)
        os.kill(p.pid, signal.SIGKILL)
        #output = subprocess.check_output(cmd, stderr=STDOUT, timeout=30)
        #time.sleep(35)
