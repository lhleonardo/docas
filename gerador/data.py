import datetime
'''
Created on 10/08/2015

M�dulo respons�vel pelos processos de criptografia e adapta��o de uma data informada, 
para que possa ser gerado o conte�do padr�o do QRCode. 
A partir desses processos, ser� poss�vel adicionar o conte�do em uma imagem de QRCode.
   
@author: Leonardo Braz
@contact: lhleonardo@hotmail.com
'''

def criptografa(self, data):
        '''
            M�todo respons�vel por criptografar uma data recebida como par�metro e transforma-la em 
            hexadecimal, no formato mDDyyyy
            
            @param data: Data que dever� ser convertida para hexadecimal
            @return: Data convertida para hexadecimal.

            Exemplo de utiliza��o: 
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
            M�todo respons�vel por adicionar 'zeros' no numero, 
            sendo ele menor do que um n�mero informado.
            
            @param valor: valor a ser preenchido;
            @param menor_que: tamanho m�nimo para realizar a compara��o;
            @return numero com determinados zeros a esquerda.
            
            
        '''
        if len(self.dec_para_hex(valor)) < menor_que:
            return '0' + self.dec_para_hex(valor)
        else:
            return self.dec_para_hex(valor)
        
def descriptografa(self, data):
        '''
            M�todo respons�vel por descriptografar uma data j� criptografada. 

            @param data: Data que ser� descriptografada
            @return data j� descriptografada


            #############################################################################
                                    Exemplo de utiliza��o: 

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
            M�todo respons�vel por realizar a convers�o de um numero hexadecimal para decimal.
           
            @param valor: n�mero hexadecimal
            @return valor hexadecimal convertido para decimal

            ############################################################################          
                                        Exemplo de utiliza��o
            
            num_hexadecimal = 3F
            num_decimal = hex_para_dec(num_hexadecimal)
        '''
        return int(valor, 16)

def dec_para_hex(self, valor):
        '''
            M�todo respons�vel por realizar a convers�o de um numero decimal para hexadecimal.
           
            @param valor: n�mero decimal
            @return valor decimal convertido para hexadecimal

            ############################################################################          
                                        Exemplo de utiliza��o
            
            num_decimal = 18
            num_hexadecimal = hex_para_dec(num_decimal)
        '''
        return hex(valor)[2:]    

def str_to_date(self, date_str):
        '''
            M�todo respons�vel por realizar a convers�o de uma cadeia de caracteres (string) para 
            uma data. Essa data ser� formatada no estilo YYYYMMDD.
            @param date_str: data em string que ser� convertida
            @return data convertida para o formato YYYYMMDD
            @except ValueError: caso o valor contido em date_str n�o seja v�lido 
        '''
        
        try:
            result = datetime.datetime.strptime(date_str, '%Y, %m, %d')
        except ValueError:
            result = "Formato inv�lido"

        return result       
