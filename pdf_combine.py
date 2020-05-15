# System imports 
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
from easygui import *

# File imports
def combine_pdf() -> bool: 
    arr_of_input_pdfs: List[PdfFileReader] = []
    state: bool = False
    default_path: str = 'C:\\'
    while 1:
        if state == False:
            user_response: str = buttonbox(msg='Select a PDF to merge', title='PDF Merger', choices=('Select PDF', 'Cancel'))
            if user_response == 'Select PDF':
                f: str = fileopenbox(default=default_path)
                if (f is None):
                    # @Note:
                    # Depending on your defintion of what
                    # should happen when you exit file explorer
                    # without selecting a file, either cancel the entire
                    # process or let the user have another opportunity to
                    # select another PDF or Finish, currently I do the latter
                    # sys.exit(1)
                    continue
                default_path =  "\\".join(f.split('\\')[:-1]) + "\\"
                if (f[-4:] != ".pdf"):
                    ccbox(msg="Error: File selected is not a PDF. Please select a PDF.", title="Error")
                    # print("Error: File selected is not a PDF. Please select a PDF.")
                    continue
                arr_of_input_pdfs.append(PdfFileReader(open(f, 'rb')))
                state = True
            else:
                sys.exit(1)
        # @Copy n' Paste from above
        elif state:
            user_response: str = buttonbox(msg='Select another PDF to merge', title='PDF Merger', choices=('Select another PDF', 'Finish'))
            if user_response == 'Select another PDF':
                f: str = fileopenbox(default=default_path)
                if (f is None): 
                    continue
                    # See @Note above
                    # sys.exit(1) 
                default_path =  "\\".join(f.split('\\')[:-1]) + "\\"
                if (f[-4:] != ".pdf"): 
                    ccbox(msg="Error: File selected is not a PDF. Please select a PDF.", title="Error")
                    continue
                arr_of_input_pdfs.append(PdfFileReader(open(f, 'rb'))) 
            elif user_response == 'Finish': 
                break
            else: 
                sys.exit(1) 
            
    output_pdf: PdfFileWriter = PdfFileWriter()

    for pdf in arr_of_input_pdfs: 
        for page in range(pdf.getNumPages()): 
            output_pdf.addPage(pdf.getPage(page))
            
    output_filename: str = input("\nNote: .pdf is not necessary\nName the output file: ")
    outputStream: fileObj = open(output_filename + ".pdf", "wb")
    output_pdf.write(outputStream)
    outputStream.close()
    return True

def main() -> None:
    if(combine_pdf()): 
        print("Success, Goodbye!")

if __name__ == "__main__":
    main()
