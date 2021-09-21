from unittest import main
import unittest
from abc import ABCMeta, abstractmethod

class Calculadora (object):

    def calcular(self, valor1, valor2, operador):
        operacaoFab = OperacaoFab()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0
        else: 
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFab (object):

    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif (operador == 'divisao'):
            return Divisao()      
        elif (operador == 'multiplicacao'):
             return Multiplicacao()

class Operacao(metaclass=ABCMeta):

    @abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao): 
      def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado
    
class Divisao(Operacao): 
      def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

class Multiplicacao(Operacao): 
      def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado  


class Testes(unittest.TestCase):
    def teste_somar(self):
        calculador = Calculadora()
        result = calculador.calcular(5,5, 'soma')
        self.assertEqual(result, 10) 

    def teste_subtracao(self):
        calculador01 = Calculadora()
        result = calculador.calcular(5,5, 'subtracao')
        self.assertEqual(result, 0)     

    def teste_divisao(self):
        calculador02 = Calculadora()
        result = calculador.calcular(5,5, 'divisao')
        self.assertEqual(result, 1)
        
    def teste_multiplicacao(self):
        calculador03 = Calculadora()
        result = calculador.calcular(5,5, 'multiplicacao')
        self.assertEqual(result, 25)        

if __name__ == '__main__':
    main()
