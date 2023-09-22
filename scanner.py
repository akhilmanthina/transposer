import subprocess

def scanner(output_folder, input_file):
    print("Scanning pdf...")
    #print(os.getcwd())
    #Execute Audiveris shell script (which calls jar files) with the input file and output folder
    subprocess.run(['./Audiveris/bin/Audiveris', '-batch', '-export', '-output', output_folder, input_file])
    print("Done scanning")


