'''
Created on 10/08/2015

Módulo  responsável pelos processos de criação das imagens QRCode. 

@author: Leonardo Braz
@contact: lhleonardo@hotmail.com
'''
import os
import qrcode
import string
import random

default_locale = os.path.expanduser('~/')

def gera_qrcode(self, conteudo, nome_imagem):
    '''
        Método responsável por gerar o QRCode de um determinado conteúdo, criando uma imagem no 
        formato JPEG.

        @param conteudo - O que será adicionado como o conteúdo do QRCode
        @param nome_imagem - Nome do arquivo após gerado. 
        @return imagem com o conteúdo já adicionado ao QRCode. O local padrão que será salva a imagem
        será na pasta raiz do usuário. EX: (/home/lhleonardo)
    '''
    qr = qrcode.QRCode(version=1, box_size=4, border=2)
    qr.add_data(conteudo)
    qr.make(fit=True)
    x = qr.make_image()
     
    qr_file = os.path.join(self.default_locale, nome_imagem + ".jpg")
    img_file = open(qr_file, 'wb')
    x.save(img_file, 'JPEG')
    img_file.close()    
    
def gera_hexadecimal_aleatorio(tamanho_da_chave):
    '''
    Método responsável por gerar o QRCode de um determinado conteúdo, criando uma imagem no 
    formato JPEG.

    @param conteudo - O que será adicionado como o conteúdo do QRCode
    @param nome_imagem - Nome do arquivo após gerado. 

    @return imagem com o conteúdo já adicionado ao QRCode. O local padrão que será salva a imagem
            será na pasta raiz do usuário. EX: (/home/lhleonardo)
    '''
    charDisponivel = string.hexdigits[:16]
    return ''.join(random.choice(charDisponivel) 
                for dummy in range(tamanho_da_chave)).upper()
