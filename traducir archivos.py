#%% IMPORTAR
import detectlanguage
from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

# %% TRADUCIR UN ARCHIVO
translated = GoogleTranslator(source='fr', target='es').translate_file("C:/Users/redk8/OneDrive/Documentos/prueba en francés.txt")

# %% MYMEMORY
path = "C:/Users/redk8/OneDrive/Documentos/prueba en francés.txt"
translated2 = MyMemoryTranslator(source='fr', target='es').translate_file(path)

# %% GUARDAR ARCHIVO
with open("C:/Users/redk8/OneDrive/Documentos/prueba en francés_es.txt", "w") as f:
    f.write(translated2)


# %% DETECTAR LENGUAJE
import detectlanguage
detectapi = detectlanguage.configuration.api_key = "74d394297bfc4ff6c4fdd2f1e255aee6"
detectlanguage.detect("Buenos dias señor")

# la api funciona bien pero no sé por qué no funciona en la siguiente
lang = single_detection('bonjour la vie', api_key=detectapi)
print(lang)