# System imports 
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import easygui
from easygui import*

# File imports
def combine_pdf() -> bool: 
    arr_of_input_pdfs: List[PdfFileReader] = []
    state: bool = False
    while 1:
        if state == False: 
            user_response: str = easygui.buttonbox(msg='Select a PDF to merge', title='PDF Merger', choices=('Select PDF', 'Cancel'))
            if user_response == 'Select PDF':
                f: str = easygui.fileopenbox()
                if (f is None): 
                    sys.exit(1) 
                if (f[-4:] != ".pdf"): 
                    print("Error: File selected is not a PDF. Please select a PDF.")
                    continue
                arr_of_input_pdfs.append(PdfFileReader(open(f, 'rb'))) 
                state = True
            else:
                sys.exit(1)
        elif state:
            user_response: str = easygui.buttonbox(msg='Select another PDF to merge', title='PDF Merger', choices=('Select another PDF', 'Finish'))
            if user_response == 'Select another PDF':
                f: str = easygui.fileopenbox()
                if (f is None): 
                    sys.exit(1) 
                if (f[-4:] != ".pdf"): 
                    print("Error: File selected is not a PDF. Please select a PDF.")
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
        print("Success")

if __name__ == "__main__":
    main()
