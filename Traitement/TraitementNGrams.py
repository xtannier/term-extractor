# -*- coding: utf-8 -*-
from Traitement import Traitement
from TraitementSimple import TraitementSimple
import re
from nltk import ngrams

class TraitementNGrams(Traitement):
    def __init__(self, n, lang):
        self.n = n
        self.lang=lang

    def preprocessing(self,texte):
        """
        param texte : le texte non traité
        param lang : la langue dans laquelle le texte est écrit

        Renvoie une liste des mots traités

        Le traitement consiste à mettre tout les mots en minuscule,
        retirer les mots vides et la ponctuation.
        """
        if self.n < 1:
            raise AttributeError("n must be >= 1")
        if (self.n == 1):
            t = TraitementSimple(self.lang)
            return t.preprocessing(texte)
        
        texte = texte.replace("\xa0", " ").replace("\u2009", " ").replace("\u202f", " ").replace("\xad", " ")
        texte = texte.replace("\n--", " ").replace("\n-", " ").replace("\n", " ").replace("--", " ").replace("––", "")
        texte = texte.replace(".", " ").replace(",", " ").replace(";", " ").replace(")", " ").replace("(", " ")
        texte = re.sub(r"\s+"," ",texte)
        #on met tout en minuscule
        txt = texte.lower()
        #retire les mots vides
        #words = utils.removeStopWords(words, self.lang)
        words = ngrams(txt.split(), self.n)
        return [gram for gram in words]