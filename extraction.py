import sys
sys.path.append("./Parser")
sys.path.append("./Traitement")
sys.path.append("./Indexation")
sys.path.append("./Document")
sys.path.append("./Strategy")
import pickle
from Indexation import Indexation
from Document import Document
import utils
import math
from TfIdfStrategy import TfIdfStrategy
from CValueStrategy import CValueStrategy
from CValueTfidfStrategy import CValueTfidfStrategy
from TraitementSimple import TraitementSimple
from TraitementNGrams import TraitementNGrams
from TraitementNGramsSpacy import TraitementNGramsSpacy
import Extractor
from ParserItem import ParserItem
from ParserCorpus import ParserCorpus
from statistics import mean

nomfichierPickle = "indexation5Grams_wikimed"
fichierExtration = "livrePret.txt"
fichierres = 'res/restfidf.csv'
trait = TraitementNGramsSpacy(1,5,'French')

#recup l'indexation
with open(nomfichierPickle, 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    ind = mon_depickler.load()

#recup le doc du quel on extrait les termes
corpus = ParserItem.parse(fichierExtration)
corpusTraite = utils.traiteCorpus(corpus,trait)

#strat = CValueStrategy(ind)
#strat = CValueTfidfStrategy(ind,  lambda tf,idf : (1+math.log(tf))*idf,  lambda iter : max(iter))
strat = TfIdfStrategy(ind,  lambda tf,idf : (1+math.log(tf))*idf,  lambda iter : max(iter))
Extractor.Extractor.extract(corpusTraite,strat,-1,fichierres)