import subprocess

def scanner(output_folder, input_file):
    print("Scanning pdf...")
    #print(os.getcwd())
    subprocess.run(['./Audiveris/bin/Audiveris', '-batch', '-export', '-output', output_folder, input_file])
    print("Done scanning")


