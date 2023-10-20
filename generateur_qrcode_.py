from CreateurdeQRcode import QRCodeGenerator

def generate_qrcode_interface():
    qrcode_generator = QRCodeGenerator()
    qrcode_generator.generate_qrcode() 

if __name__ == '__main__':
    generate_qrcode_interface()
