import datetime
import locale

def numdnia(x):
    if x==1:
        dzien="poniedzialek"
    if x==2:
        dzien="wtorek"
    if x==3:
        dzien="sroda"
    if x==4:
        dzien="czwartek"
    if x==5:
        dzien="piatek"
    if x==6:
        dzien="sobota"
    if x==7:
        dzien="niedziela"
    return dzien

def short(nazwa):
    if nazwa=='poniedziałek':
        return 'pon'
    if nazwa=='wtorek':
        return 'wto'
    if nazwa=='środa':
        return 'śro'
    if nazwa=='czwartek':
        return 'czw'
    if nazwa=='piątek':
        return 'pią'
    if nazwa=='sobota':
        return 'sob'
    if nazwa=='niedziela':
        return 'nie'