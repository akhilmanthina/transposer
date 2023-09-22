import os
import re
import subprocess



def mxl_to_pdf(mxl_file_path):
    mxl_to_ly_path = os.getcwd() + "/Lilypond/bin/musicxml2ly"
    ly_file = './temp/output.ly'

    subprocess.run([mxl_to_ly_path, "-o", ly_file, mxl_file_path])
    
    modify_ly(ly_file)
    ly_to_pdf(ly_file)


def ly_to_pdf(ly_file):
    lilypond_path = os.getcwd() + "/Lilypond/bin/lilypond"
    subprocess.run([lilypond_path, '--pdf', ly_file])

    pdf_file = os.path.splitext(ly_file)[0] + '.pdf'
    
    
def modify_ly(ly_file):
    with open(ly_file, 'r') as file:
        content = file.read()

    # Change the title
    content = re.sub(r'(title\s*=\s*)"([^"]*)"', r'\1"Transposed Piece"', content)

    # Remove the instrument naming
    content = re.sub(
        r'\\set Staff.instrumentName = "[^"]*"', 
        '', 
        content
    )

    content = re.sub(
        r'\\set Staff.shortInstrumentName = "[^"]*"', 
        '', 
        content
    )

    # Write the modified content back to the file
    with open(ly_file, 'w') as file:
        file.write(content)
