import pandas as pd
from fpdf import FPDF
filename = './alley.csv'
df = pd.read_csv(filename)
with open("CopanyInfo.txt") as f:
    contents = f.readlines()

class PdfReport(FPDF):
    def __init__(self, filename):
        FPDF.__init__(self) #initializes parent class
        self.filename = filename

    def generate(self, first_name,last_name, address_lane,city,zip_code, amount):

        pdf.add_page()
        pdf.image('image.jpg', w=50, h=50)
        pdf.set_font(family="Times", size=12, style='B')

        pdf.cell(w=0, h=5, txt="1099 NEC  "+str(contents[3]), border=1, align="C", ln=1)

        pdf.cell(w=0, h=5, txt="", border=0, align="C", ln=1)
        for i in contents[0:3]:

            pdf.cell(w=0, h=5, txt=str(i), border=0, align="L", ln=1)
        pdf.cell(w=0, h=20, txt="", border=0,ln=1)


        pdf.cell(w=0, h=5, txt=last_name+" "+first_name, border=0, ln=1)
        pdf.cell(w=0, h=5, txt=address_lane, border=0, ln=1)
        pdf.cell(w=20, h=5, txt=city, border=0)
        pdf.cell(w=0, h=5, txt=str(zip_code), border=0, ln=1)


        pdf.cell(w=0, h=20, txt="", border=0, ln=1)
        pdf.set_font(family="Times", size=18, style='B')
        pdf.cell(w=0, h=15, txt="1099 NEC " + str(contents[4]), border=1, align="C", ln=1)
        pdf.set_font(family="Times", size=12, style='B')


        pdf.cell(w=0, h=20, txt="", border=0, ln=1)
        pdf.cell(w=40, h=10, txt=first_name, border=1)
        pdf.cell(w=0, h=10, txt=last_name, border=1, ln=1)
        pdf.cell(w=0, h=10, txt=address_lane, border=1, ln=1)
        pdf.cell(w=40, h=10, txt=city, border=1 )
        pdf.cell(w=0, h=10, txt=str(zip_code), border=1, ln=1)
        pdf.cell(w=0, h=10, txt="Total Compensation: "+str(amount), border=1, ln=1)

pdf = PdfReport(filename)
pdf.alias_nb_pages()

for ind in df.index:
    pdf.generate(df['first_name'][ind], df['last_name'][ind], df['address_lane'][ind], df['city'][ind], df['zip_code'][ind],df['amount'][ind])

pdf.output('PDF_TEST.pdf','F')


#for ind in df.index:
