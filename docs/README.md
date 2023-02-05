# Creació automàtica d'usuaris de l'Active Directory de Windows

Tots els fitxers d'aquest projecte són publicats sota els termes de la Llicència Pública General Menor de GNU versió 3 (LGPLv3).

Una còpia de la llicència s'inclou en el fitxer "[LICENSE](/docs/LICENSE)".

Copyright © 2023 Bernat Mas Quetglas

## Funcionament

Principalment, l'*script* llegeix d'un CSV on cada fila és un empleat de l'empresa i cada columna representa els llinatges, nom i departament al qual pertany. El nom d'usuari per defecte és `<primera lletra del nom>llinatge`. També estableix una contrasenya per defecte de la forma `Llinatge1Nom12345678`, que s'haurà de canviar el primer pic que s'iniciï sessió.

## Estructura de l'empresa i l'AD

L'Active Directory conté la unitat organitzativa *CB Smart Security* (nom de l'empresa fictícia) amb les sub-unitats corresponents a cada departament:
- Comptabilitat
- Vendes
- Administració
- Tècnics
- Informàtica
- Direcció
- Caps d'Àrea

Cada depertament té el seu grup corresponent, incloent el grup *cbss* global a tota l'empresa. L'*script* també fica cada cap d'Àrea dins el grup del departament que dirigeix.

Per tant, i com a exemples, un empleat del departament de Comptabilitat pertany als grups *cbss* i *comptabilitat*; mentre que el cap de comptabilitat pertany a aquests i al de *caps*.