from googletrans import Translator
text="Sasmitha Akka"
translator=Translator()
translated=translator.translate(text,src='en',dest='ta')
print("Tamil Translation : ",translated.text)