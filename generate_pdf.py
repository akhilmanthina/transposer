import os
import subprocess


def mxl_to_pdf(mxl_file_path):
    mxl_to_ly_path = os.getcwd() + "/Lilypond/bin/musicxml2ly"


    ly_file = './temp/output.ly'

    subprocess.run([mxl_to_ly_path, "-o", ly_file, mxl_file_path])
    

    ly_to_pdf(ly_file)
    os.remove(ly_file)



def ly_to_pdf(ly_file):
    lilypond_path = os.getcwd() + "/Lilypond/bin/lilypond"
    subprocess.run([lilypond_path, '--pdf', ly_file])

    pdf_file = os.path.splitext(ly_file)[0] + '.pdf'
    
    
    
