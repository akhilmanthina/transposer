import os
import re
import subprocess



def mxl_to_pdf(mxl_file_path, input_instrument, output_instrument):
    mxl_to_ly_path = os.getcwd() + "/Lilypond/bin/musicxml2ly"
    ly_file = './temp/output.ly'

    #Convert the MusicXML file to a Lilypond file
    subprocess.run([mxl_to_ly_path, "-o", ly_file, mxl_file_path])

    modify_ly(ly_file, input_instrument, output_instrument)
    ly_to_pdf(ly_file)


def ly_to_pdf(ly_file):
    lilypond_path = os.getcwd() + "/Lilypond/bin/lilypond"

    #Convert the Lilypond file to a pdf
    subprocess.run([lilypond_path, '--pdf', '-o', './temp', ly_file])

    pdf_file = os.path.splitext(ly_file)[0] + '.pdf'
    
    
def modify_ly(ly_file, input_instrument, output_instrument):
    with open(ly_file, 'r') as file:
        content = file.read()

    title = f"Transposed Piece for {output_instrument}, (Originally for {input_instrument})"
    composer = "Transposed by AkhilM"

    #Change the title
    content = re.sub(r'(title\s*=\s*)"([^"]*)"', rf'\1"{title}"', content)

    #Change composer
    content = re.sub(r'(composer\s*=\s*)"([^"]*)"', rf'\1"{composer}"', content)

    #Remove the instrument naming
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

    #Write the modified content back to the file
    with open(ly_file, 'w') as file:
        file.write(content)
