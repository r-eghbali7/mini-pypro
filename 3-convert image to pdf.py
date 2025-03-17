# website: https://rohallaheghbali.ir/  |  instagram: eghbaliit  | youtube: rohallaheghbali

import img2pdf

with open('img.png', 'rb') as iamge :
    byte_pdf = img2pdf.convert(iamge.read())
    
with open('img.pdf', 'wb') as pdf:
    pdf.write(byte_pdf)
    
print("convert Done!!!!!")