import pdfkit

#Define path to wkhtmltopdf.exe
path_to_wkhtmltopdf = ""

#Define path to HTML file
path_to_file = 'sample.html'

#Point pdfkit configuration to wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Convert HTML file to PDF:

pdfkit.from_file(path_to_file, output_path='main.pdf', configuration=config)