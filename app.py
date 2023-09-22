from music21 import *

from scanner import scanner

def get_transposition_interval(input_instrument, output_instrument):
    # Define the transposition intervals in semitones for specific instruments
    transposition_intervals = {
        'Clarinet': -2,  # Bb instruments are transposed down a whole step (2 semitones)
        'A Clarinet': -3,  # A instruments are transposed down a minor third (3 semitones)
        'F Horn': -7,  # F instruments are transposed down a perfect fifth (7 semitones)
        'Flute' : 0
        # Add more instruments as needed
    }

    input_transposition = transposition_intervals.get(input_instrument, 0)
    output_transposition = transposition_intervals.get(output_instrument, 0)

    # Calculate the transposition interval between input and output instruments
    transposition_interval = output_transposition - input_transposition
    return transposition_interval


def transpose_musicxml(file_path, input_instrument, output_instrument):
    # Load the MusicXML file
    score = converter.parse(file_path)

    # Get the transposition interval between the specified input and output instruments
    transposition_interval = get_transposition_interval(input_instrument, output_instrument)

    # Transpose the score
    transposed_score = score.transpose(transposition_interval)

    return transposed_score


if __name__ == '__main__':
    # Get the MusicXML file path and instrument names
    file_path = input("Enter the path of the pdf file: ").strip()
    input_instrument = input("Enter the input instrument name: ").strip()
    output_instrument = input("Enter the output instrument name: ").strip()

    scanner("./temp", file_path)
    file_name = file_path.split("/")[-1].split(".")[0]
    mxl_file_path = "./temp/" + file_path.split("/")[-1].split(".")[0] + ".mxl"
    print(mxl_file_path)
    #exit()


    # Transpose the MusicXML file
    transposed_score = transpose_musicxml(mxl_file_path, input_instrument, output_instrument)

    # Save the transposed score to a new MusicXML file
    transposed_file_path = "./" + file_name + "_transposed.mxl"
    print(transposed_file_path)
    transposed_score.write('musicxml', transposed_file_path)
    print(f'Transposed MusicXML file saved to {transposed_file_path}')
