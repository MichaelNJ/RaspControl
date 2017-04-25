import os


for dirpath, dir, files in os.walk("./home/mc_mickey/Rasp/RaspControl/"):
    os.system('python raspController.py')
            