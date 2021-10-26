from flask import Flask, request
import pdfkit
from pyvirtualdisplay import Display

app = Flask(__name__)

@app.route("/pdf", methods=["POST"])
def generate_pdf():
    #Handle request coming in
    if request.method == "POST":
        dataJSON = request.get_json()

    #Configuration of the binary path
    config = pdfkit.configuration(wkhtmltopdf=bytes('/usr/bin/wkhtmltopdf', 'utf-8'))

    with Display():
      pdf_file = pdfkit.from_string(dataJSON['html'], False,configuration=config, options=dataJSON['options'])
    
    return(pdf_file)

