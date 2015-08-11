'''
Created on 10/08/2015

M�dulo  respons�vel pelos processos de cria��o das imagens QRCode. 

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
        M�todo respons�vel por gerar o QRCode de um determinado conte�do, criando uma imagem no 
        formato JPEG.

        @param conteudo - O que ser� adicionado como o conte�do do QRCode
        @param nome_imagem - Nome do arquivo ap�s gerado. 
        @return imagem com o conte�do j� adicionado ao QRCode. O local padr�o que ser� salva a imagem
        ser� na pasta raiz do usu�rio. EX: (/home/lhleonardo)
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
    M�todo respons�vel por gerar o QRCode de um determinado conte�do, criando uma imagem no 
    formato JPEG.

    @param conteudo - O que ser� adicionado como o conte�do do QRCode
    @param nome_imagem - Nome do arquivo ap�s gerado. 

    @return imagem com o conte�do j� adicionado ao QRCode. O local padr�o que ser� salva a imagem
            ser� na pasta raiz do usu�rio. EX: (/home/lhleonardo)
    '''
    charDisponivel = string.hexdigits[:16]
    return ''.join(random.choice(charDisponivel) 
                for dummy in range(tamanho_da_chave)).upper()
