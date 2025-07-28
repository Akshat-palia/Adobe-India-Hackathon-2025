from fpdf import FPDF

pdf = FPDF()
for i in range(1, 51):
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Page {i} - Sample Heading", ln=True)
    for j in range(30):
        pdf.cell(200, 10, txt=f"This is a sample line number {j} on page {i}.", ln=True)

pdf.output("test_50_page.pdf")
print("✅ 50-page PDF generated as test_50_page.pdf")
