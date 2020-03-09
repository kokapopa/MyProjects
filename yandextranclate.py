import locale
from yandex.Translater import Translater
tr=Translater()

locale.setlocale(locale.LC_ALL, '') #фиксит проблему с библиотекой яндекса

api_key="trnsl.1.1.20200309T060830Z.344d9b14a5d60014.73173e69fc28c824b2288d084ca8e11617d260e1"

query='boss'
tr.set_key(api_key)
tr.set_from_lang('en')
tr.set_to_lang('ru')
tr.set_text(query)

result=tr.translate()
speak(result)

