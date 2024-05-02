
def remove_non_digits_from(line: str) -> str:
    """Removes All non-digit characters from a string"""
    return ''.join(filter(str.isdigit, line)).strip()

def clean_non_digits_file_from(file: str, output: str) -> None:
    """Effectively Removes all non-digit characters from a file"""
    # Open the input and output files
    output_file = open(output, 'w')
    input_file = open(file, 'r')
    
    # Iterate through the file and write the cleaned lines to the output file
    for line in input_file:
        output_file.write(remove_non_digits_from(line) + '\n')
    
    # Close files to not have memory leaks
    output_file.close()
    input_file.close()
