import pygame as pg
import pygamebg

(sirina, visina) = (300, 300); # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Kucica");

BELA = pg.Color("white")
ZUTA = pg.Color("yellow")
CRVENA = pg.Color("red")
PLAVA = pg.Color("skyblue")
CRNA = pg.Color("black")
BRAON = pg.Color("brown")

prozor.fill(BELA)

margina_y = 20

# osnova kuće
osnova_x = 60
osnova_y = 120
osnova_sirina = 180
osnova_visina = 160
pg.draw.rect(prozor, ZUTA, (osnova_x, osnova_y, osnova_sirina, osnova_visina))

# krov
pg.draw.polygon(prozor, CRVENA, [(60, 120), (150, 20), (240, 120)])

def prozor_linije(x, y, sirina, visina):
	# horizontalna linija
	pg.draw.line(prozor, CRNA, (x, y + visina / 2), (x + sirina, y + visina / 2))
	# print("Horizontalna linija: (" + str(x) + ", " + str(y + visina / 2) + "), (" + str(x + sirina) + ", " + str(y + visina / 2) + ")")
	# vertikalna linija
	pg.draw.line(prozor, CRNA, (x + sirina / 2, y), (x + sirina / 2, y + visina))
	# print("Vertikalna linija: (" + str(x + sirina / 2) + ", " + str(y) + "), (" + str(x + sirina / 2) + ", " + str(y + visina) + ")")

prozor_sirina = 50
prozor_visina = 50

# levi prozor
prozor_levi_x = 80
prozor_levi_y = 140
pg.draw.rect(prozor, PLAVA, (prozor_levi_x, prozor_levi_y, prozor_sirina, prozor_visina))
# print("Levi prozor")
prozor_linije(prozor_levi_x, prozor_levi_y, prozor_sirina, prozor_visina)

# desni prozor
prozor_desni_x = 170
prozor_desni_y = 140
pg.draw.rect(prozor, PLAVA, (prozor_desni_x, prozor_desni_y, prozor_sirina, prozor_visina))
# print("Desni prozor")
prozor_linije(prozor_desni_x, prozor_desni_y, prozor_sirina, prozor_visina)

# vrata
vrata_sirina = 60
vrata_visina = 80
vrata_x = sirina / 2 - vrata_sirina / 2
vrata_y = visina - margina_y - vrata_visina
pg.draw.rect(prozor, BRAON, (vrata_x, vrata_y, vrata_sirina, vrata_visina))

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
