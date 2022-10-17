from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
pdf.add_page()

pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')


pdf.output(name = 'main.pdf')