import datetime
'''
Created on 10/08/2015

Módulo responsável pelos processos de criptografia e adaptação de uma data informada, 
para que possa ser gerado o conteúdo padrão do QRCode. 
A partir desses processos, será possível adicionar o conteúdo em uma imagem de QRCode.
   
@author: Leonardo Braz
@contact: lhleonardo@hotmail.com
'''

def criptografa(self, data):
        '''
            Método responsável por criptografar uma data recebida como parâmetro e transforma-la em 
            hexadecimal, no formato mDDyyyy
            
            @param data: Data que deverá ser convertida para hexadecimal
            @return: Data convertida para hexadecimal.

            Exemplo de utilização: 
            data_criptografada = ControleDatas.criptografa(datetime.date(2014,2,23))
            
        '''
        dia = data.day
        mes = data.month
        ano = data.year
        
        hexa_dia = self.zero_a_esquerda_hexadecimal(dia, 2)
        hexa_mes = self.zero_a_esquerda_hexadecimal(mes, 2)   
        hexa_ano = self.zero_a_esquerda_hexadecimal(ano, 3) 
        
        resultado = str(hexa_mes) + "" + str(hexa_dia) + "" + str(hexa_ano)
        
        return resultado.upper()

def zero_a_esquerda_hexadecimal(self, valor, menor_que):
        '''
            Método responsável por adicionar 'zeros' no numero, 
            sendo ele menor do que um número informado.
            
            @param valor: valor a ser preenchido;
            @param menor_que: tamanho mínimo para realizar a comparação;
            @return numero com determinados zeros a esquerda.
            
            
        '''
        if len(self.dec_para_hex(valor)) < menor_que:
            return '0' + self.dec_para_hex(valor)
        else:
            return self.dec_para_hex(valor)
        
def descriptografa(self, data):
        '''
            Método responsável por descriptografar uma data já criptografada. 

            @param data: Data que será descriptografada
            @return data já descriptografada


            #############################################################################
                                    Exemplo de utilização: 

            data_criptografada = ControleDatas.criptografa(datetime.date(2014,2,23))
            data_descriptografada = ControleDatas.descriptografa(data_criptografada)

        '''
        mes = data[0:2]
        dia = data[2:4]
        ano = data[4:7]
        
        dec_mes = int(mes, 16)
        dec_dia = int(dia, 16)
        dec_ano = int(ano, 16)
        
        resultado = str(dec_ano) + "/" + str(dec_mes) + "/" + str(dec_dia)    
        return resultado 
        
def hex_para_dec(self, valor):
        '''
            Método responsável por realizar a conversão de um numero hexadecimal para decimal.
           
            @param valor: número hexadecimal
            @return valor hexadecimal convertido para decimal

            ############################################################################          
                                        Exemplo de utilização
            
            num_hexadecimal = 3F
            num_decimal = hex_para_dec(num_hexadecimal)
        '''
        return int(valor, 16)

def dec_para_hex(self, valor):
        '''
            Método responsável por realizar a conversão de um numero decimal para hexadecimal.
           
            @param valor: número decimal
            @return valor decimal convertido para hexadecimal

            ############################################################################          
                                        Exemplo de utilização
            
            num_decimal = 18
            num_hexadecimal = hex_para_dec(num_decimal)
        '''
        return hex(valor)[2:]    

def str_to_date(self, date_str):
        '''
            Método responsável por realizar a conversão de uma cadeia de caracteres (string) para 
            uma data. Essa data será formatada no estilo YYYYMMDD.
            @param date_str: data em string que será convertida
            @return data convertida para o formato YYYYMMDD
            @except ValueError: caso o valor contido em date_str não seja válido 
        '''
        
        try:
            result = datetime.datetime.strptime(date_str, '%Y, %m, %d')
        except ValueError:
            result = "Formato inválido"

        return result       
