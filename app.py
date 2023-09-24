from music21 import *
import streamlit as st
import os

from scanner import scanner
from generate_pdf import mxl_to_pdf
from get_keys import get_interval


def transpose_musicxml(file_path, input_instrument, output_instrument):
    #Load the MusicXML file
    score = converter.parse(file_path)

    #Get the transposition interval between the specified input and output instruments
    transposition_interval = get_interval(input_instrument, output_instrument)
    print(f"Transposition interval: {transposition_interval}")

    #Transpose the score
    transposed_score = score.transpose(transposition_interval)

    return transposed_score

def clear_temp(temp):
    for filename in os.listdir(temp):
        file_path = os.path.join(temp, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def run_app(file, input_instrument, output_instrument):
    temp = './temp/'
    
    with st.status("Transposing...") as status:
        #Save the pdf to the temp folder
        st.write("Uploading PDF...")

        file_name = file.name.split(".")[0]
        file_path = temp + file.name

        with open(file_path, "wb") as f:
            f.write(file.getvalue())

        #Scan the pdf and convert to MusicXML
        st.write("Scanning to MusicXML...")
        scanner(temp, file_path)
        
        mxl_file_path = temp + file_path.split("/")[-1].split(".")[0] + ".mxl"
        print(mxl_file_path)
        #exit()


        #Transpose the MusicXML file
        st.write("Transposing MusicXML...")
        transposed_score = transpose_musicxml(mxl_file_path, input_instrument, output_instrument)

        #Save the transposed score to a new MusicXML file
        st.write("Saving...")
        transposed_file_path = temp + file_name + "_transposed.mxl"
        print(transposed_file_path)
        print("Writing to mxl...")
        transposed_score.write('musicxml', transposed_file_path)

        #Convert the transposed MusicXML file to pdf
        print("Converting to pdf...")
        mxl_to_pdf(transposed_file_path, input_instrument, output_instrument)

        status.update(label="Download complete!", state="complete", expanded=False)


    print("Done!")

if __name__ == '__main__':

    st.title("Transposer")
    file_path = ""
    input_instrument = ""
    output_instrument = ""
    submitted = False

    #Get the MusicXML file path and instrument names
    with st.form(key='my_form'):
        uploaded_file = st.file_uploader('Upload PDF sheet music', type="pdf")
        input_instrument = st.text_input(label='Input instrument')
        output_instrument = st.text_input(label='Output instrument')
        submitted = st.form_submit_button(label='Submit')
  
    if submitted:
        if input_instrument == "" or output_instrument == "" or uploaded_file == None:
            st.error('Please fill out all fields before submitting.')
        else:
            run_app(uploaded_file, input_instrument, output_instrument)
            
            file_location = "./temp/output.pdf"
            #Make output downloadable
            if os.path.exists(file_location):
  
                with open(file_location, "rb") as file:
                    st.download_button(
                        label="Download Transposed PDF",
                        data=file,
                        file_name="output.pdf",
                        mime="application/pdf",
                    )
            else:
                st.error("The file output.pdf does not exist.")
            
            #Clean up the temp folder
            print("Cleaning up...")
            clear_temp('./temp/')
        






