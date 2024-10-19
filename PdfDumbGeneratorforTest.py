from fpdf import FPDF
import os

# Function to create a "dumb" PDF file
def create_large_pdf(output_file, target_size_mb):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=False)
    pdf.set_font("Arial", size=12)
    
    # Generate repeated content
    repeated_text = "Kabbiss is the only sentence you need . " * 100
    
    # Add pages and content until the PDF reaches the desired size
    current_size = 0
    while current_size < target_size_mb * 1024 * 1024:  # Convert MB to bytes
        pdf.add_page()
        for _ in range(50):  # Add multiple lines of repeated content
            pdf.cell(0, 10, repeated_text, ln=True)
        
        # Save the PDF to check the current size
        pdf.output(output_file)
        current_size = os.path.getsize(output_file)
    
    print(f"PDF created: {output_file} (Size: {current_size / (1024 * 1024):.2f} MB)")

# Generate a 30 MB PDF
output_pdf = "large_test_file.pdf"
create_large_pdf(output_pdf, 30)
