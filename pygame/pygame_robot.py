import pygame as pg
import pygamebg

(sirina, visina) = (400, 400); # otvaramo prozor
prozor = pygamebg.open_window(sirina, visina, "Robotica Mica");

# definisemo boje koje cemo koristiti
SIVA = (250, 250, 250)
CRVENA = (255, 0, 0)
PLAVA = (0, 0, 255)

# debljina linije
debljina = 3

prozor.fill(SIVA)

# koordinata sredine prozora
(cx, cy) = (sirina / 2, visina / 2)

# telo
telo = 120
telo_x = cx - telo / 2
telo_y = cy - telo / 2
pg.draw.rect(prozor, PLAVA, (telo_x, telo_y, telo, telo), debljina)

# haljina
haljina_x = telo_x
haljina_visina = telo / 8
haljina_y = telo_y + telo - telo / 8
pg.draw.rect(prozor, CRVENA, (haljina_x, haljina_y, telo, haljina_visina))

# glava
glava = 3 * telo / 4
glava_x = cx - glava / 2
glava_y = cy - telo / 2 - glava
pg.draw.rect(prozor, PLAVA, (glava_x, glava_y, glava, glava), debljina)

# oci
oko = glava / 5
zenica = oko / 3
oko_y = cy - telo / 2 - glava * 3 / 4
levo_oko_x = cx - oko / 2 * 3
desno_oko_x = cx + oko / 2
pg.draw.rect(prozor, CRVENA, (levo_oko_x, oko_y, oko, zenica), 1)
pg.draw.rect(prozor, CRVENA, (desno_oko_x, oko_y, oko, zenica), 1)

# zenice
pg.draw.rect(prozor, CRVENA, (levo_oko_x + zenica, oko_y, zenica, zenica))
pg.draw.rect(prozor, CRVENA, (desno_oko_x + zenica, oko_y, zenica, zenica))

# usta
usta_sirina = glava / 3
usta_visina = usta_sirina / 3
usta_y = cy - telo / 2 - glava / 2 + usta_visina
pg.draw.rect(prozor, CRVENA, (glava_x + usta_sirina, usta_y, usta_sirina, usta_visina))

# noge
noga_sirina = telo / 4
noga_duzina = noga_sirina * 3
leva_noga_x = cx - noga_sirina
leva_noga_y = telo_y + telo
desna_noga_x = cx
desna_noga_y = telo_y + telo
pg.draw.rect(prozor, PLAVA, (leva_noga_x, leva_noga_y, noga_sirina, noga_duzina), debljina)
pg.draw.rect(prozor, PLAVA, (desna_noga_x, desna_noga_y, noga_sirina, noga_duzina), debljina)

# ruke
ruka_sirina = telo / 6
ruka_duzina = ruka_sirina * 4
ruka_y = cy - telo / 3
leva_ruka_x = cx - telo / 2 - ruka_duzina
desna_ruka_x = cx + telo / 2
pg.draw.rect(prozor, PLAVA, (leva_ruka_x, ruka_y, ruka_duzina, ruka_sirina), debljina)
pg.draw.rect(prozor, PLAVA, (desna_ruka_x, ruka_y, ruka_duzina, ruka_sirina), debljina)


# prikazujemo prozor i čekamo da ga korisnik isključi
pygamebg.wait_loop()
