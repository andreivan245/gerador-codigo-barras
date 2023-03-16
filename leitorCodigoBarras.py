from PIL import Image
from pyzbar.pyzbar import decode


def lerCodigo(nomeProduto):

    img = Image.open("produtos/"+nomeProduto+".png")
    decoded_list = decode(img)

    codigoBarra = decoded_list[0].data
    print(int(codigoBarra))
