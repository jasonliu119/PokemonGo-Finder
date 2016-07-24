import multiprocessing
import time, os
import subprocess, signal

# bar
def scan_map():
   os.system("python main.py");


def do_something(f, t):
   # Start bar as a process
   p = multiprocessing.Process(target=f)
   p.start()
   '''
   # Wait for 10 seconds or until process finishes
   p.join(20)

   # If thread is still active
   if p.is_alive():
       print "running... let's kill it..."

       # Terminate
       p.terminate()
       p.join()
   '''
   time.sleep(t) # sec
   p2 = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
   out, err = p2.communicate()
   for line in out.splitlines():
       if 'python2' in line:
           pid = int(line.split(None, 1)[0])
           os.kill(pid, signal.SIGKILL)

if __name__ == '__main__':
   while True:
       print "\n\n--------- scan map "
       do_something(scan_map, 900)
       time.sleep(3) # wait for clean up
