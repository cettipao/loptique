import os
import re

import fitz  # requires fitz, PyMuPDF
import pdfrw
import subprocess
import os.path
import sys

'''
    replace all the constants (the one in caps) with your own lists
'''

class ProcessPdf:

    def __init__(self, temp_directory, output_file):
        print('\n##########| Initiating Pdf Creation Process |#########\n')

        print('\nDirectory for storing all temporary files is: ', temp_directory)
        self.temp_directory = temp_directory
        print("Final Pdf name will be: ", output_file)
        self.output_file = output_file

    def add_data_to_pdf(self, template_path, data):
        print('\nAdding data to pdf...')
        template = pdfrw.PdfReader(template_path)

        for page in template.pages:
            annotations = page['/Annots']
            if annotations is None:
                continue

            for annotation in annotations:
                if annotation['/Subtype'] == '/Widget':
                    if annotation['/T']:
                        key = annotation['/T'][1:-1]
                        if re.search(r'.-[0-9]+', key):
                            key = key[:-2]

                        if key in data:
                            annotation.update(
                                pdfrw.PdfDict(V=self.encode_pdf_string(data[key], "string"))
                            )
                        annotation.update(pdfrw.PdfDict(Ff=1))

        template.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        pdfrw.PdfWriter().write(self.temp_directory + ".pdf", template)
        print('Pdf saved')

        return self.temp_directory + ".pdf"

    def encode_pdf_string(self, value, type):
        if type == 'string':
            if value:
                return pdfrw.objects.pdfstring.PdfString.encode(str(value).upper())
            else:
                return pdfrw.objects.pdfstring.PdfString.encode('')
        elif type == 'checkbox':
            if value == 'True' or value == True:
                return pdfrw.objects.pdfname.BasePdfName('/Yes')
                # return pdfrw.objects.pdfstring.PdfString.encode('Y')
            else:
                return pdfrw.objects.pdfname.BasePdfName('/No')
                # return pdfrw.objects.pdfstring.PdfString.encode('')
        return ''

    def delete_temp_files(self, pdf_list):
        print('\nDeleting Temporary Files...')
        for path in pdf_list:
            try:
                os.remove(path)
            except:
                pass

    def compress_pdf(self, input_file_path, power=3):
        """Function to compress PDF via Ghostscript command line interface"""
        quality = {
            0: '/default',
            1: '/prepress',
            2: '/printer',
            3: '/ebook',
            4: '/screen'
        }

        output_file_path = self.temp_directory + 'compressed.pdf'

        if not os.path.isfile(input_file_path):
            print("\nError: invalid path for input PDF file")
            sys.exit(1)

        if input_file_path.split('.')[-1].lower() != 'pdf':
            print("\nError: input file is not a PDF")
            sys.exit(1)

        print("\nCompressing PDF...")
        initial_size = os.path.getsize(input_file_path)
        subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                        '-dPDFSETTINGS={}'.format(quality[power]),
                        '-dNOPAUSE', '-dQUIET', '-dBATCH',
                        '-sOutputFile={}'.format(output_file_path),
                         input_file_path]
        )
        final_size = os.path.getsize(output_file_path)
        ratio = 1 - (final_size / initial_size)
        print("\nCompression by {0:.0%}.".format(ratio))
        print("Final file size is {0:.1f}MB".format(final_size / 1000000))
        return output_file_path


        

