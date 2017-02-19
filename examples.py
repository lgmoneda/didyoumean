from  didYouMean import *
import pandas as pd

### Encoding
df = pd.DataFrame()
df["Português"] = ["paichão", "missanga", "corapão", "cassamba"]
df["Português Corrigido"] = df["Português"].apply(lambda x: didYouMean(x))
print(df)

### Cases
df = pd.DataFrame()
df["Pokemons"] = ["Picachu", "xamander", "boobasar", "skertle"]
df["Pokemons Corrigido"] = df["Pokemons"].apply(lambda x: didYouMean(x))
print(df)

df = pd.DataFrame()
df["Remedios"] = ["catafram", "catafran", "capafran", "kapafran"]
df["Corrigido"] = df["Remedios"].apply(lambda x: didYouMean(x, encrypted=True))
df["Corrigido Contexto"] = df["Remedios"].apply(lambda x: didYouMean(x, context="bula remédio", encrypted=True))
print(df)

df = pd.DataFrame()
df["Remedios"] = ["capafram", "ruvitril", "puscoban", "huyabc", "adivil"]
df["Corrigido"] = df["Remedios"].apply(lambda x: didYouMean(x, context="bula remédio", encrypted=True))
print(df)

import timeit

def test():
    df = pd.DataFrame()
    df["Remedios"] = ["capafram", "ruvitril", "puscoban", "huyabc", "adivil"]
    df["Corrigido"] = df["Remedios"].apply(lambda x: didYouMean(x, context="bula remédio", encrypted=True))

print(timeit.timeit("test()", setup="from __main__ import test", number=5))

