import subprocess
import signal
import time
import os

p = subprocess.Popen('npm start', shell=True, preexec_fn=os.setsid) 

print('Command: npm start!')

# O tempo de coleta vai depender do número de reviews coletado. Por
# segurança, calculei 1 hora de coleta. Se achar muito ou pouco, é só alterar.
time.sleep(3600)

os.killpg(os.getpgid(p.pid), signal.SIGINT)
print('Keyboard Interrupt!')

p.wait()
print('Finish Google Play API')