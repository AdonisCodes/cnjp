from typing import Iterator

def iterate_file_lines_yield(file: str) -> Iterator[str]:
    """Iterates through a file and yields each line"""
    # Open the input file
    input_file = open(file, 'r')
    
    # Helpful for large files 
    for line in input_file:
        yield line
    
    # Close it to save memory
    input_file.close()
