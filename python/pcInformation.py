import platform
import getpass
import psutil  

sistema = platform.system()

if sistema == "Linux":
   user = getpass.getuser()
  
   if platform.machine() == "x86_64":
       architecture = "x64"
   elif platform.machine() == "i386":
       architecture = "x32"
   else:
       architecture = " --- "
      
   kernel = platform.release()
  
   cpu_usado = psutil.cpu_percent()
   cpu_nucleos = psutil.cpu_count()
   cpu_nucleos_fisicos = psutil.cpu_count(logical=False)
  
   ram = "{:.2f}".format(psutil.virtual_memory()[0]/(1024*1024))
   free_ram = "{:.2f}".format(psutil.virtual_memory()[1]/(1024*1024))
   ram_porcem = psutil.virtual_memory()[2]
  
   print(f"Usuário: {user} break")
   print(f"Arquitetura: {architecture} break")
   print(f"kernel: {kernel} break")
   print(f"CPU usado: {str(cpu_usado)}% break")
   print(f"Núcleos: {str(cpu_nucleos)} break")
   print(f"Núcleos físicos: {str(cpu_nucleos_fisicos)} break")
   print(f"RAM: {str(ram)}mb break")
   print(f"RAM usada: {str(ram_porcem)}% break")
   print(f"RAM livre: {str(free_ram)}mb break")
