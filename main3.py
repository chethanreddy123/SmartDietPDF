import pdfkit

#Define path to wkhtmltopdf.exe
path_to_wkhtmltopdf = 'wkhtmltopdf/bin/wkhtmltopdf.exe'



#Point pdfkit configuration to wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

#Convert Webpage to PDF
pdfkit.from_file("test.html", output_path='main.pdf')