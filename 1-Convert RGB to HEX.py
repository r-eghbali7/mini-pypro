# website: https://rohallaheghbali.ir/  |  instagram: eghbaliit  | youtube: rohallaheghbali

from webcolors import name_to_hex

def color_name_to_code(colername):
    try:
        colore_code = name_to_hex(colername)
        return colore_code
    except ValueError:
        return "its not coler"
    
coler_name = input("Enter your color: ")
resulte_colore = color_name_to_code(coler_name)
print(resulte_colore)
