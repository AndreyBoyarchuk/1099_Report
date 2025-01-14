from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Add the 1099-NEC form logo
        self.image('image.jpg', x=10, y=8, w=30)

        # Set the font and font size
        self.set_font('Arial', 'B', 16)

        # Add the title
        self.cell(w=0, h=10, txt="1099-NEC Form", border=0, ln=1, align="C")

    def footer(self):
        # Set the font and font size
        self.set_font('Arial', '', 8)

        # Add the page number
        self.cell(w=0, h=10, txt=f'Page {self.page_no()}', border=0, ln=1, align="C")

    def add_form(self, payer_name, payer_address, payer_ein, recipient_name, recipient_ein, recipient_address,
                 payment_amount):
        # Set the font and font size
        self.set_font('Arial', '', 12)

        # Add the payer information
        self.cell(w=0, h=10, txt="Payer's Name:", border=0, ln=1, align="L")
        self.cell(w=0, h=10, txt=payer_name, border=1, ln=1, align="L")
        self.cell(w=0, h=10, txt="Payer's Address:", border=0, ln=1, align="L")
        self.cell(w=0, h=10, txt=payer_address, border=1, ln=1, align="L")
        self.cell(w=0, h=10, txt="Payer's EIN:", border=0, ln=1, align="L")
        self.cell(w=0, h=10, txt=payer_ein, border=1, ln=1, align="L")

        # Add a line break
        self.ln(10)

        # Add the recipient information
        self.cell(w=0, h=10, txt="Recipient's Name:", border=0, ln=1, align="L")
        self.cell(w=0, h=10, txt=recipient_name, border=1, ln=1, align="L")
        self.cell(w=0, h=10, txt="Recipient's EIN:", border=0, ln=1, align="L")
        self.cell(w=0, h=10, txt=recipient_ein, border=1, ln=1, align="L")
        self.cell(w=0, h=10, txt="Recipient's Address:", border=0, ln=1, align="L")
        self.cell(w=0, h=10, txt=recipient_address, border=1, ln=1, align="L")

        # Add a line break
        self.ln(10)

        # Add the payment amount
        self.cell(w=0, h=10, txt="Payment Amount:", border=0, ln=1, align="L")
        self.cell(w=0, h=10, txt=payment_amount, border=1, ln=1, align="L")

    # Create a new PDF document
    pdf = FPDFPDF()

    # Set the page margins
    pdf.set_margins(20, 20)

    # Set the font and font size
    pdf.set_font('Arial', '', 12)

    # Add a page
    pdf.add_page()

    # Add the 1099-NEC form
    pdf.add_form(payer_name="ABC Company", payer_address="1234 Main St, Anytown, USA", payer_ein="12-3456789",
                 recipient_name="John Doe", recipient_ein="98-7654321", recipient_address="4321 Main St, Anytown, USA",
                 payment_amount="$1,000")

    # Generate the PDF file
    pdf.output('1099-NEC.pdf', 'F')
