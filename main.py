import pandas as pd
from fpdf import FPDF
import datetime
import  numpy as np
import string
filename = './IOK.csv'
df = pd.read_csv(filename)
with open("CopanyInfoIOK.txt") as f:
    contents = f.readlines()
info1="THIS IS MPORTANT TAX INFORMATION AND IS BEING FURNISHED TO THE INTERNAL REVENUE SERVICE. IF YOU ARE REQUIRED TO FILE A RETURN, A NEGLIGENCE PENALTY OR OTHER SANCTION MAY BE IMPOSED ON YOU IF THIS INCOME IS TAXABLE AND IRS DETERMINES THAT IT HAS NOT BEEN REPORTED"
info2="Shows nonemployee compensation. If the amount in this box is SE income, report it on Schedule C or F (Form 1040) if a sole proprietor, or on Form 1065 and Schedule K-1 (Form 1065) if a partnership, and the recipient/partner completes Schedule SE (Form 1040)."
info3="Shows backup withholding. A payer must backup withhold on certain payments if you did not give your TIN to the payer. See Form W-9, Request for Taxpayer Identification Number and Certification, for information on backup withholding. Include this amount on your income tax return as tax withheld."
info="You received this form instead of Form W-2 because the payer did not consider you an employee and did not withhold income tax or social security and Medicare tax."
class PdfReport(FPDF):
    def __init__(self, filename):
        FPDF.__init__(self) #initializes parent class
        self.filename = filename

    def generate(self, first_name,last_name, address_lane,city,zip_code, amount,ss_number, state, company):

        pdf.add_page()
        #pdf.image('image.jpg', w=50, h=50)

        pdf.set_font(family="Times", size=18, style='B')
        pdf.cell(w=0, h=3, txt="", border=0, ln=1)
        pdf.set_fill_color(192, 192, 192)
        pdf.cell(w=0, h=7, txt="FORM 1099-NEC  ", border=1, align="C", ln=1, fill=True)

        pdf.set_font(family="Times", size=14)
        pdf.cell(w=0, h=5, txt="", border=0, align="C", ln=1)
        for i in contents[0:3]:

            pdf.cell(w=0, h=5, txt=str(i), border=0, align="L", ln=1)
        pdf.cell(w=0, h=27, txt="", border=0,ln=1)

        if len(company) > 1:
            pdf.cell(w=0, h=5, txt=company, border=0, ln=1)
        pdf.cell(w=0, h=5, txt= first_name, border=0, ln=1)
        pdf.cell(w=0, h=5, txt=address_lane, border=0, ln=1)
        pdf.cell(w=12, h=5, txt=city+", "+state+" "+ str(zip_code), border=0,ln=1)



        pdf.cell(w=0, h=19, txt="", border=0, ln=1)
        pdf.set_font(family="Times", size=15, style='B')
        pdf.cell(w=0, h=15, txt= str(contents[4])+"  1099-NEC Miscellaneous Income Statement (Recipient's Copy B)" , border=1, align="C", ln=1,fill=True)
        pdf.set_font(family="Times", size=14, style='B')


        pdf.cell(w=0, h=8, txt="", border=0, ln=1)
        pdf.set_font(family="Times", size=14, style='B')
        pdf.set_fill_color(192, 192, 192)
        pdf.cell(w=70, h=10, txt="Payers Federal ID: ", border=1, fill=True)
        pdf.set_font(family="Times", size=16)
        pdf.cell(w=0, h=10, txt=str(contents[3]), border=1, ln=1)
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=70, h=10, txt="Recipient ID: ", border=1,  fill=True )
        pdf.set_font(family="Times", size=16)
        pdf.cell(w=0, h=10, txt=ss_number, border=1, ln=1)
        pdf.set_font(family="Times", size=12, style='B')

        pdf.cell(w=70, h=5, txt="",ln=1  )
        pdf.cell(w=70, h=5, txt="Payer's Name address", border=1, fill=True)
        pdf.cell(w=0, h=5, txt="Recipient's Name address", border=1, fill=True, ln=1)
        pdf.multi_cell(0, 3, "")
        pdf.set_font(family="Times", size=12)
        if len(company) > 1:
            pdf.cell(w=70, h=5, txt="", border=0, )
            pdf.cell(w=40, h=5, txt=company, border=0,ln=1)
        else:
            pass
        pdf.cell(w=70, h=5, txt=str(contents[0]), border=0, )
        pdf.cell(w=0, h=5, txt=first_name, border=0, ln=1 )
        pdf.cell(w=70, h=5, txt=str(contents[1]), border=0, )
        pdf.cell(w=0, h=5, txt=address_lane, border=0, ln=1)
        pdf.cell(w=70, h=5, txt=str(contents[3]), border=0, )
        pdf.cell(w=0, h=5, txt=city+", "+state+" "+ str(zip_code), border=0, ln=1)
        formatted = str(format(amount, '.2f'))
        pdf.set_font(family="Times", size=10, style='B')
        pdf.cell(w=70, h=5, txt="", ln=1)
        pdf.cell(w=0, h=6, txt="Box 1 - Nonemployee Compensation", border=1, align="L", ln=1, fill=True)
        pdf.set_font(family="Times", size=14, )
        pdf.cell(w=0, h=10, txt="    "+str(formatted), border=1, align="L",ln=1)
        pdf.set_font(family="Times", size=10, style='B')
        pdf.cell(w=0, h=6, txt="Box 4 - Federal Tax Withelded", border=1, align="L", ln=1, fill=True)
        pdf.set_font(family="Times", size=14,)
        pdf.cell(w=0, h=10, txt="     0.00 ", border=1, align="L",ln=1)
        pdf.set_font('Arial', 'B', 8)
        pdf.multi_cell(0, 3, "")
        pdf.multi_cell(0, 3, info1)
        pdf.multi_cell(0, 3, "")
        pdf.multi_cell(0, 3, info)
        pdf.multi_cell(0, 3, "")
        pdf.set_font('Arial', 'B', 10)
        pdf.multi_cell(0, 4, txt="Instruction for Recipient:")
        pdf.set_font(family="Times", size=8, style='B')
        pdf.multi_cell(0, 3, txt="Box 4:")
        pdf.set_font(family="Times", size=8,)
        pdf.multi_cell(0, 3, info2)
        pdf.multi_cell(0, 3, "")
        pdf.set_font(family="Times", size=8, style='B')
        pdf.multi_cell(0, 3, txt= "Box 4:")
        pdf.set_font(family="Times", size=8, )
        pdf.multi_cell(0, 3, info3)

        if company != np.nan:
            # Do something
            print(company)


pdf = PdfReport(filename)
pdf.alias_nb_pages()

for ind in df.index:
    pdf.generate(df['first_name'][ind], df['last_name'][ind], df['address_lane'][ind], df['city'][ind], df['zip_code'][ind], df['amount'][ind], df['ss_number'][ind],df['state'][ind],df['company'][ind])
now = datetime.datetime.now()
date_time_str = now.strftime("%b_%d_%Y_%I%p_%M_%S")
#text_without_spaces = "".join(contents[0].split())
text_without_spaces = contents[0].replace(" ", "_").replace(",", "_")
text_without_spaces = text_without_spaces[:10]
pdf.output(f'{text_without_spaces}_{date_time_str}.pdf', 'F')


#for ind in df.index:
