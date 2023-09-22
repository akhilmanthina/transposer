import os

def scanner(output_folder, input_file):
    print("Scanning pdf...")
    #print(os.getcwd())
    command = f'./Audiveris/bin/Audiveris -batch -export -output {output_folder} {input_file}'
    print(command)
    os.system(command)
    print("Done scanning")


    
if __name__ == '__main__':
    scanner("./temp", "./carolflutecpy.pdf")
