from flask import Flask, request
import pdfkit
from pyvirtualdisplay import Display

app = Flask(__name__)

@app.route("/pdf", methods=["POST"])
def generate_pdf():
    #Handle request coming in
    if request.method == "POST":
        print(request)
        dataJSON = request.get_json()
        print(dataJSON)

    for key,value in dataJSON['options'].items():
      if value == "None":
        dataJSON['options'][key] = None
     
    print(dataJSON['options'])

    #Configuration of the binary path
    config = pdfkit.configuration(wkhtmltopdf=bytes('/usr/bin/wkhtmltopdf', 'utf-8'))

    with Display():
      pdf_file = pdfkit.from_string(dataJSON['html'], False,configuration=config, options=dataJSON['options'])
    
    return(pdf_file)

