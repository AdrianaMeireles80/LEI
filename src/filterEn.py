import pandas as pd 
import googletrans
from googletrans import Translator

translator = Translator()

df_port = pd.read_csv('rumores.csv',encoding="utf8")

df_en = df_port.copy()

translations = {}
unique_elements = df_en['tweet'].unique()

for element in unique_elements:

   	# add translation to the dictionary
	translations[element] = translator.translate(element).text

df_en.replace(translations, inplace = True)

df_en.to_csv('rumoresIngles.csv',encoding="utf8", index=False)
