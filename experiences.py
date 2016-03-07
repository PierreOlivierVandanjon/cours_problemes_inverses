# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 17:18:46 2016

@author: vandanjon
"""
import numpy as np

def experience1():
    g=9.81 # acceleration de la gravité
    #g=10
    
    M=10000  # masse de 10 tonnes
    rayon = 1.35/2 # rayon des roues
    ZZ = 2*600 # inertie des cylindres
    Fv=100 # frottement sec
    mu=0.01
    Fs = mu*M*g 
    
    #vibration 30 Hz des cylindres
    fc = 30
    
    vitesse_max=6/3.6 # vitesse de 6 km/h
    temps_max=5*60 # rayon de
    acceleration_max = 0.005*g # acceleratmion maximale
    
    vitesse_desire=vitesse_max/2 
    acceleration_desire = acceleration_max /2 
    tech = 0.01
    nech=int(np.floor(temps_max/tech)+1)
    
    temps_montee=vitesse_desire/acceleration_desire
    ntemps_montee= int(np.floor(temps_montee/tech)+1) 
    temps_montee=(ntemps_montee-1)*tech
    
    temps=np.linspace(0,temps_max,num=nech)
    montee=acceleration_desire*temps[0:ntemps_montee]
    descente=montee[::-1]
    palier=montee[-1]*np.ones(nech-2*ntemps_montee)
    profil_vitesse=np.concatenate((montee, palier, descente))
    profil_position=np.cumsum(profil_vitesse)*tech
    montee=acceleration_desire*np.ones(ntemps_montee) 
    palier=np.zeros(nech-2*ntemps_montee)
    descente=-acceleration_desire*np.ones(ntemps_montee)
    profil_acceleration=np.concatenate((montee,palier,descente))
    profil_force = M*profil_acceleration+Fv*profil_vitesse + Fs 
    
    
    #position articulaire sans glissement...
    
    position_articulaire_cylindre=profil_position/rayon
    vitesse_articulaire_cylindre=profil_vitesse/rayon
    acceleration_articulaire_cylindre=profil_acceleration/rayon
    
    #le couple moteur
    profil_couple=profil_force*rayon + ZZ*acceleration_articulaire_cylindre
    
    # signal de position
    ncodeur= 100 # nombre de points par tout
    #ncodeur= 10000000000
    from math import pi
    pas_codeur = (2*pi)/ncodeur
    nb_pas=position_articulaire_cylindre//pas_codeur
    bruit=pas_codeur*np.random.randn(nech)/3 + pas_codeur*np.sin(2*pi*fc*temps);
    #bruit=0 ;
    codeur =nb_pas*pas_codeur+ bruit ;
#    plt.figure(1)
#    plt.plot(temps, position_articulaire_cylindre,temps, codeur)
#    plt.title('Codeur')
    
    #signal de couple
    couple_max=np.amax(profil_couple)
    bruit=couple_max*np.random.randn(nech)/20 + couple_max*np.sin(2*pi*fc*temps)/100;
    #bruit=0;
    couple_mesure=profil_couple + bruit
    
    return couple_mesure, codeur, tech, rayon



def experience2():
    g=9.81 # acceleration de la gravité
    #g=10
    
    M=10000  # masse de 10 tonnes
    rayon = 1.35/2 # rayon des roues
    ZZ = 2*600 # inertie des cylindres
    Fv=100 # frottement sec
    mu=0.01
    Fs = mu*M*g 
    
    #vibration 30 Hz des cylindres
    fc = 30
    
    vitesse_max=14/3.6 # vitesse de 6 km/h
    temps_max=5*60 # temps de l'expérimentation
    acceleration_max = 0.01*g # acceleratmion maximale
    
    vitesse_desire=vitesse_max/2 
    acceleration_desire = acceleration_max /2 
    tech = 0.015
    nech=int(np.floor(temps_max/tech)+1)
    
    temps_montee=vitesse_desire/acceleration_desire
    ntemps_montee= int(np.floor(temps_montee/tech)+1) 
    temps_montee=(ntemps_montee-1)*tech
    
    temps=np.linspace(0,temps_max,num=nech)
    montee=acceleration_desire*temps[0:ntemps_montee]
    descente=montee[::-1]
    palier=montee[-1]*np.ones(nech-2*ntemps_montee)
    profil_vitesse=np.concatenate((montee, palier, descente))
    profil_position=np.cumsum(profil_vitesse)*tech
    montee=acceleration_desire*np.ones(ntemps_montee) 
    palier=np.zeros(nech-2*ntemps_montee)
    descente=-acceleration_desire*np.ones(ntemps_montee)
    profil_acceleration=np.concatenate((montee,palier,descente))
    profil_force = M*profil_acceleration+Fv*profil_vitesse + Fs 
    
    
    #position articulaire sans glissement...
    
    position_articulaire_cylindre=profil_position/rayon
    vitesse_articulaire_cylindre=profil_vitesse/rayon
    acceleration_articulaire_cylindre=profil_acceleration/rayon
    
    #le couple moteur
    profil_couple=profil_force*rayon + ZZ*acceleration_articulaire_cylindre
    
    # signal de position
    ncodeur= 100 # nombre de points par tout
    #ncodeur= 10000000000
    from math import pi
    pas_codeur = (2*pi)/ncodeur
    nb_pas=position_articulaire_cylindre//pas_codeur
    bruit=pas_codeur*np.random.randn(nech)/3 + pas_codeur*np.sin(2*pi*fc*temps);
    #bruit=0 ;
    codeur =nb_pas*pas_codeur+ bruit ;
#    plt.figure(1)
#    plt.plot(temps, position_articulaire_cylindre,temps, codeur)
#    plt.title('Codeur')
    
    #signal de couple
    couple_max=np.amax(profil_couple)
    bruit=couple_max*np.random.randn(nech)/20 + couple_max*np.sin(2*pi*fc*temps)/100;
    #bruit=0;
    couple_mesure=profil_couple + bruit
    
    return couple_mesure, codeur, tech, rayon