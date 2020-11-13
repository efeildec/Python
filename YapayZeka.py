import pyglet
def toplama():
  toplama1 = int( input("1. sayı:"))
  toplama2 = int( input("2. sayı:"))
  print(toplama1 + toplama2 , "sonuç")
def carpma():
  carpma1 = int( input("1. sayı:"))
  carpma2 = int( input("2. sayı:"))
  print(carpma1 * carpma2 , "sonuç")
def bolme():
  bolme1 = int( input("1. sayı:"))
  bolme2 = int( input("2. sayı:"))
  print(bolme1 / bolme2 , "sonuç")
def cikarma():
  cikarma1 = int( input("1. sayı:"))
  cikarma2 = int( input("2. sayı:"))
  print(cikarma1 - cikarma2 , "sonuç")
def factorial(num):
  factorial = 1
  if (num == 0 or num == 1):
    print("factorial")
  else:
    while(num>=1):
      factorial = factorial * num
      num = num - 1
    print("factorial:", factorial)

sonuc = input("Ne İstersin? > ")
if sonuc == ("müzik"):
  sonuc = input("hangi şarkı? > ")
  if sonuc == ("believer"):
    sound = pyglet.media.load('Imagine Dragons Believer.mp3', streaming=False)
    sound.play()
    pyglet.app.run()
if sonuc == ("kim programladı?"):
  print("Efe İldeç - Yapımcı")

if sonuc == ("topla"):
  toplama()
if sonuc == ("çarp"):
  carpma()
if sonuc == ("böl"):
  bolme()
if sonuc == ("çıkar"):
  cikarma()
