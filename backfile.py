import os
from fpdf import FPDF
from PIL import Image



img = Image.new('RGB', (210,297), "#4f88e3" )
img.save('blue_colored.png')

# adding image to pdf page that e created using fpdf



pdf = FPDF()
pdf.add_page()
pdf.image('blue_colored.png', x = 0, y = 0, w = 210, h = 297, type = '', link = '')
pdf.set_font('helvetica', '', 13.0)
pdf.set_xy(105.0, 8.0)
pdf.cell(ln=0, h=22.0, align='C', w=75.0, txt='Dear Sarthak', border=0)


pdf.set_xy(105.0, 15.0)
pdf.cell(ln=0, h=22.0, align='C', w=75.0, txt='Here is suggested diet plan for you', border=0)
pdf.set_line_width(0.0)
pdf.rect(15.0, 15.0, 170.0, 245.0)
pdf.set_line_width(0.0)

pdf.image('logo.jpeg', 20.0, 17.0, link='', type='', w=20.0, h=20.0)
pdf.set_font('arial', 'B', 16.0)
pdf.set_xy(95.0, 18.0)



pdf.set_line_width(0.0)
pdf.line(100.0, 15.0, 100.0, 57.0)
pdf.set_font('arial', 'B', 14.0)
pdf.set_xy(145.0, 28.5)
pdf.cell(ln=0, h=9.5, align='L', w=60.0, txt='00000001', border=0)
pdf.set_xy(115.0, 30.5)
pdf.cell(ln=0, h=5.5, align='L', w=10.0, txt='Booking ID:', border=0)
pdf.set_font('arial', 'B', 12.0)
pdf.set_xy(17.0, 37.5)

pdf.cell(ln=0, h=5.0, align='L', w=98.0, txt='Smart Diet Planner', border=0)

pdf.set_xy(17.0, 42.5)
pdf.cell(ln=0, h=5.0, align='L', w=98.0, txt='Unleash the Power of Nutrition !', border=0)

pdf.set_font('arial', '', 12.0)
pdf.set_xy(115.0, 36.0)
pdf.cell(ln=0, h=7.0, align='L', w=60.0, txt='Date:', border=0)
pdf.set_xy(135.0, 36.0)
pdf.cell(ln=0, h=7.0, align='L', w=40.0, txt='19/02/2009', border=0)

pdf.set_line_width(0.0)
pdf.line(15.0, 57.0, 185, 57.0)



# Remember to always put one of these at least once.
pdf.set_font('Times','',10.0) 
 
# Effective page width, or just epw
epw = pdf.w - 2*pdf.l_margin
 
# Set column width to 1/4 of effective page width to distribute content 
# evenly across table and page
col_width = epw/4
 
# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.
 
data = [
    ["6:30AM" , "1 Glass-250 ml Dhaniya Seeds Water/ Coriander Seeds Water "],
    ["7:30AM" , "1 Glass-250 ml Green Vegetable Juice, 10 pieces Raisins "],
    ["10:00AM" , "2 pc - 50g Moonglet Chila, 1 cup- 200ml Toned Milk"]
]

pdf.set_xy(150.0, 55.0)


th = pdf.font_size
 

pdf.ln(4*th)
pdf.set_fill_color(r=255,g=0,b=0)
 
pdf.set_xy(35.0, 70.0)
pdf.set_font('Times','B',14.0) 
pdf.multi_cell(60, 5, border=1, txt = 'Morning Diet Schedule', ln = 1, fill = 1, align='C')
pdf.set_font('Times','',10.0) 
pdf.ln(5)


line_height = pdf.font_size * 2.5
col_width = pdf.epw / 4  # distribute content evenly

step = 0

for row in data:
    pdf.set_xy(30.0 , 80.0 + step)
    for datum in row:
        pdf.multi_cell(col_width, line_height, str(datum), border=1,
                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
    pdf.ln(line_height)
    step += line_height




# Remember to always put one of these at least once.
pdf.set_font('Times','',10.0) 
 
# Effective page width, or just epw
epw = pdf.w - 2*pdf.l_margin
 
# Set column width to 1/4 of effective page width to distribute content 
# evenly across table and page
col_width = epw/4
 
# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.
 
data = [
    ["6:30AM" , "1 Glass-250 ml Dhaniya Seeds Water/ Coriander Seeds Water "],
    ["7:30AM" , "1 Glass-250 ml Green Vegetable Juice, 10 pieces Raisins "],
    ["10:00AM" , "2 pc - 50g Moonglet Chila, 1 cup- 200ml Toned Milk"]
]

pdf.set_xy(150.0, 105.0)


th = pdf.font_size
 

pdf.ln(4*th)
 
pdf.set_font('Times','B',14.0) 
pdf.cell(epw, 0.0, 'Lunch Diet Schedule', align='C')
pdf.set_font('Times','',10.0) 
pdf.ln(5)


line_height = pdf.font_size * 2.5
col_width = pdf.epw / 4  # distribute content evenly

step = 0

for row in data:
    pdf.set_xy(30.0 , 130.0 + step)
    for datum in row:
        pdf.multi_cell(col_width, line_height, str(datum), border=1,
                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
    pdf.ln(line_height)
    step += line_height


pdf.output('main.pdf', 'F')
