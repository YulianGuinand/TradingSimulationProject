import yfinance as yf
import datetime
import pandas as pd
from time import sleep

class Data:
    
    def __init__(self, symbol):
        """
        Constructeur de la classe Data.
        :param symbol: Symbole de l'action.
        """
        self.symbol = symbol
        self.currentprice = self.get_current_price()
        self.previousClose = yf.Ticker(self.symbol).info['previousClose'] # Permmant d'avoir accès au prix de clôture le plus récent
        self.change = self.calculate_change()

    def get_current_price(self):
        """
        Récupère le prix de clôture le plus récent pour un symbole donné.
        
        :param symbol: Symbole de l'action (par exemple, 'META' pour Meta Platforms Inc.).
        :return: Prix de clôture le plus récent de l'action.
        """
        pass

    def get_current_volume(self):
        """
        Récupère le volume de trading actuel pour un symbole donné.
        
        :param symbol: Symbole de l'action.
        :return: Volume de trading actuel formaté avec des séparateurs de milliers.
        """
        pass

    def calculate_change(self):
        """
        Calcule le changement absolu et en pourcentage par rapport à un prix de référence donné.
        
        :param current_price: Prix actuel.
        :param reference_price: Prix de référence.
        :return: Tuple contenant le changement absolu et le changement en pourcentage.
        """
        
        pass

    def get_info(self, mode = 0):
        """
        Récupère les informations importantes pour un symbole d'action donné.
        
        :param symbol: Symbole de l'action.
        :param new_current_price: Prix de clôture le plus récent.
        :return: Tuple contenant le prix actuel, le changement, le volume et l'objectif sur un an.
        """
        pass
def data_main(symbole):
    """
    Fonction principal pour récupérer et stocker les informations.
    """
    pass

        
        
        

# Boucle principale pour récupérer et stocker les informations

if __name__ == '__main__':
    symbole = 'meta'
    data_main(symbole)