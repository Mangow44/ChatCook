from googletrans import Translator

translator = Translator()
t = translator.translate("I don't know your recipe", dest='fr')
print(t)