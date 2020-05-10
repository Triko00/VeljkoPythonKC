import pygame as pg
import pygamebg

(sirina, visina) = (400, 400); # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Oblaci");

# bojimo pozadinu u plavo
prozor.fill(pg.Color("skyblue"))

# crtamo sunce
pg.draw.circle(prozor, pg.Color("yellow"), (100, 100), 80)

# procedura koja crta oblak na datoj poziciji, date velicine u datoj
# nijansi sive boje
def oblak(x, y, r, siva):
	# nijansa sive boje
	boja = [ siva, siva, siva ]
	# crtamo oblak od tri kruga
	# centralni veliki krug oblaka
	pg.draw.circle(prozor, boja, (x, y), r)
	# poluprecnik levog i desnog, manjeg kruga oblaka
	r_malo = round(5 * r / 8)
	# levi manji krug oblaka
	pg.draw.circle(prozor, boja, (x - r, y), r_malo)
	# desni manji krug oblaka
	pg.draw.circle(prozor, boja, (x + r, y), r_malo)

# crtamo nekoliko oblika razlicite velicine i nijanse
oblak(240, 200, 40, 180)
oblak(270, 250, 50, 210)
oblak(230, 100, 50, 230)
oblak(80, 80, 30, 150)
oblak(110, 320, 60, 255)

# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
