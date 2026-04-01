from pypdf import PdfReader

def extractpdf(pdf_doc): # module to load and extract text from the PDF
    try:
        pdf=PdfReader(pdf_doc) # Load pdf_doc
        
        raw_text=''
        for index,page in enumerate(pdf.pages): # by taking the number of pages which is index and data in the pages from the loaded doc
            text=page.extract_text() # from page it will extract text 
            if text:
                raw_text+=text # append the text 
        return raw_text
    
    except:
        return f'Error in reading the pdf'
        