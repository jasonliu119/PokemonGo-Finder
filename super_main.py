import multiprocessing
import time, os
import subprocess, signal

# bar
def show_map():
   print "\n\n-----------------"
   os.system("python main.py");



def do_catch(f, t):
   # Start bar as a process
   p = multiprocessing.Process(target=f)
   p.start()

   time.sleep(t) # sec
   p2 = subprocess.Popen(['sudo', 'lsof', '-i', ':5000'], stdout=subprocess.PIPE)
   out, err = p2.communicate()
   for line in out.splitlines():
       if 'localhost:commplex-main' in line:
           pid = int(line.split(None, 2)[1])
           os.kill(pid, signal.SIGKILL)
           print "kill process " + pid

if __name__ == '__main__':
   while True:
       #print "\n\n--------- restart the bot for transferring evolved pokemons "
       do_catch(show_map, 60)
       time.sleep(3) # wait for clean up
