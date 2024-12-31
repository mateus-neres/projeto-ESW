import fitz  # PyMuPDF

class PdfImg:
    def __init__(self, pdf):
        self.pdf = pdf

    def convert(self):
        # Abrir o PDF
        doc = fitz.open("extrato.pdf")
        # Loop pelas páginas
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            pix = page.get_pixmap()  # Renderizar a página como uma imagem
            pix.save(f"page_{page_number + 1}.png")  # Salvar como imagem




