from unidecode import unidecode
import subprocess

class Usuari:

    # arrel d'Active Directori i Unitat organitzativa
    __arrel = "OU=CB Smart Security,DC=bernat,DC=nom,DC=es"

    # grup al què pertany tota l'empresa
    __grupGlobal = "CN=cbss," + __arrel

    # correspondència entre departaments i el seu grup
    # podria ser un mètode que llegeix un JSON
    deptsGrups = {
        "Comptabilitat":"CN=comptabilitat," + __arrel,
        "Vendes":"CN=vendes," + __arrel,
        "Administració":"CN=administracio," + __arrel,
        "Tècnics":"CN=tecnics," + __arrel,
        "Informàtica":"CN=informatica," + __arrel,
        "Direcció":"CN=direccio," + __arrel,
        "Caps d'Àrea":"CN=caps," + __arrel
    }

    @staticmethod
    def __genUsuariContra(llinatges, nom):
        # es lleven accents
        llinatges = unidecode(llinatges).lower()
        nom = unidecode(nom).lower()
        # primera lletra nom + primer llinatge
        usuari = nom[0] + llinatges.split()[0]
        # primer llinatge + nom (amb primera lletra de cada en majúscula)
        contra = llinatges.split()[0].title() + nom.title()
        contra += "12345678"
        return usuari, contra

    def __init__(self, llinatges, nom, dept):
        self.__llinatges = llinatges
        self.__nom = nom
        usuariContra = self.__genUsuariContra(self.__llinatges, self.__nom)
        self._usuari = usuariContra[0]
        # contrasenya per defecte
        self.__contrasenya = usuariContra[1]
        self.grups = [self.__grupGlobal]
        if "Cap" in dept:
            # pertany al grup "caps" i al del dept. que dirigeix
            self.dept = "Caps d'Àrea"
            grupDept = self.deptsGrups[dept.replace("Cap de ", "")]
            self.grups.append(grupDept)
        else:
            self.dept = dept
        self.grups.append(self.deptsGrups[self.dept])

    def crearUsuari(self):
        ordre = f"dsadd user \"CN={self._usuari},OU={self.dept},{self.__arrel}\""
        ordre += f" -pwd {self.__contrasenya} -mustchpwd yes"
        ordre += " -memberof"
        for grup in self.grups:
            ordre += f" \"{grup}\""
        ordre += f" -fn \"{self.__nom}\""
        ordre += f" -ln \"{self.__llinatges}\""
        ordre += f" -dept \"{self.dept}\""
        ordre += " -company \"CB Smart Security\""
        subprocess.run(ordre, shell=True, check=True)

    # def modificarUsuari, eliminarUsuari, etc.