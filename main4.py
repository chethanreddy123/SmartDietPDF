from distutils.log import Log
import os
from fpdf import FPDF
from PIL import Image
from datetime import datetime


import json

f = open('pdf_diet.json', encoding="utf8")
Data = json.load(f)
f.close()


title = 'Smart Diet Planner'
contact = ' WhatsApp Us : +91-9999118595 '
customer = 'Dear Sarthak! Here is your personalised diet plan. '



class PDF(FPDF):
    
    def header(self):

        img = Image.new('RGB', (210,297), "#ccf0e4" )
        img.save('blue_colored.png')
        self.image('blue_colored.png', x = 10, y = 10, w = 190, h = 280, type = '', link = '')

       
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        
        ################################ Main Box
        # Calculate width of title and position
        w = self.get_string_width(title) + 145
        self.set_x((210 - w) / 2)
        
        # Colors of frame, background and text
        self.set_draw_color(242, 242, 242)
        self.set_fill_color(0, 151, 161)
        self.set_text_color(242, 242, 242)
        
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 40, title, 1, 1, 'C', 1)
        # Line break
        
        ################################ Main Name
        w = self.get_string_width(customer) + 15
        #self.set_x((210 - w) / 2)
        
        # Colors of frame, background and text
        self.set_draw_color(242, 242, 242)
        self.set_fill_color(242, 242, 242)
        self.set_text_color(0, 151, 161)
        
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        
        # Arial bold 15
        self.set_font('Arial', 'I', 11)
        self.cell(190, 10, customer, 1, 1, 'C', 1)
        # Line break
        
        
        
        
         # Logo
        self.image('logo_preview_rev_1.jpeg', 10, 12, 33)
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        
        
        # Arial bold 15
        self.set_font('Arial', 'I', 11)
        
        # Calculate width of title and position
        w = self.get_string_width(contact) + 145
        self.set_x((223 - w) / 2)
        
        # Colors of frame, background and text
        self.set_draw_color(242, 242, 242)
        self.set_fill_color(0, 151, 161)
        self.set_text_color(242, 242, 242)
        
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w-13, 14, contact, 10, 1, 'L', 1)
        
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font("Arial", style = 'B', size = 18)
       
        # Title
        self.set_xy(17,70)
        self.set_text_color(0, 151, 161)
        self.cell(0, 6, label )
        # Line break
        self.ln(4)

    def addBox(self,startX : float , startY : float , DataDict : dict, TypeDay : str) :
        Step = None
        Height = None
        LogoPath = ""
        
        if TypeDay == "Morning":
            Height = 3
            LogoPath = "morLogo.png"

        if TypeDay == "Afternoon":
            Height = 3
            LogoPath = "afrLogo.png"

        if TypeDay == "Evening":
            Height = 1.5
            LogoPath = "eveLogo.png"

        if TypeDay == "Night":
            Height = 2.4
            LogoPath = "nigLogo.png"
        
        Step = Height*15

        img = Image.new('RGB', (210,297), "#fff7f7" )
        img.save('white_colored.png')
        self.image('white_colored.png', x =startX, y = startY, w = 160, h = Step, type = '', link = '')
        #self.image('white_colored.png', x = 25, y = 80, w = 160, h = 45, type = '', link = '')



        self.set_font("Arial", style = 'B', size = 11)

        self.set_xy(startX + 20,startY+3)
        self.set_text_color(0, 151, 161)
        self.cell(0, 6, TypeDay)
        self.image(LogoPath, x = startX + 10, y = startY + 2, w = 8, h = 8, type = '', link = '')


        img = Image.new('RGB', (210,297), "#f7990c" )
        img.save('orange_colored.png')

        step = 5

        startY += 7

        print(Height)

        for i in range(int(Height)):
            self.set_font('Helvetica', size = 9)
            self.set_text_color(255, 255, 255)
            self.set_xy(36,startY+step)
            print("Hello")
            self.image('orange_colored.png', x = startX+10, y = startY+step, w = 17, h = 6, type = '', link = '')
            self.set_xy(startX+11,startY +step)
            d = datetime.strptime(DataDict[i]['time'], "%H:%M")
            AcData = str(d.strftime("%I:%M %p"))
            self.cell(0, 6, AcData)
            self.set_font('Helvetica', size = 9)
            self.set_text_color(0,0,0)
            self.set_xy(startX+30, startY+step)
            self.cell(0, 6, DataDict[i]['data'][0]['Food'])
            step += 10


      
        img = Image.new('RGB', (210,297), "#f7990c" )
        img.save('orange_colored.png')

    def chapter_body(self, Data):

        ListData = [
            Data['diets'][0:3],
            Data['diets'][3:6],
            Data['diets'][6:7],
            Data['diets'][7:]
        ]
        

        self.addBox( 25 , 80,ListData[0], "Morning")
        self.addBox( 25, 135, ListData[1] , "Afternoon")
        self.addBox( 25, 190, ListData[2] , "Evening")
        self.addBox( 25, 225, ListData[3], "Night")

    def print_chapter(self, Date, WeekName, Data):

        self.add_page()
        self.chapter_title(Date, WeekName)
        self.chapter_body(Data)

        

pdf = PDF()
pdf.set_title(title)
pdf.set_author('Weekly Diet Plan!')

WeekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']



for i in range(len(WeekDays)):
    pdf.print_chapter('17th October 2022', WeekDays[i] , Data[i])

pdf.output('tuto1.pdf', 'F')