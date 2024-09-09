from datetime import date
from typing import List, Dict, Tuple, Set


tars: List[Dict] = []
cates: Dict[str, List[Dict]] = {}
etiqs: Set[str] = set()



def AgreTar():
    nom = input("Ingresar el nombre de una tarea: ")
    cate = input("Ingresar la categoría de una tarea: ")
    FechVenc = tuple(map(int, input("Ingresar una fecha de vencimiento (AAAA MM DD): ").split()))
    EtiqTar = set(input("Ingresar las etiquetas (Que esten separadas por comas): ").split(","))

    tar = {
        'nombre': nom,
        'categoria': cate,
        'fecha_vencimiento': date(*FechVenc),
        'etiquetas': EtiqTar
    }
    tars.append(tar)
    if cate not in cates:
        cates[cate] = []
    cates[cate].append(tar)
    etiqs.update(EtiqTar)

def ElimTar():
    if not HayTars():
        print("Se Debe agregar una tarea primero")
        return
    nom = input("Ingresar el nombre de la tarea que se desea eliminar: ")
    if not TarExist(nom):
        print("No existe ninguna tarea con este nombre")
        return
    global tars
    tars = [tar for tar in tars if tar['nombre'] != nom]
    for cate in cates.values():
        cate[:] = [tar for tar in cate if tar['nombre'] != nom]

def ModTar():
    if not HayTars():
        print("Se Debe agregar una tarea primero")
        return
    nom = input("Ingresar el nombre de la tarea que se desea modificar: ")
    if not TarExist(nom):
        print("No existe ninguna tarea con este nombre")
        return
    NuevNom = input("Ingresar el nuevo nombre de la tarea (dejar en blanco para mantener igual): ")
    NuevCate = input("Ingresar la nueva categoría de la tarea (dejar en blanco para mantener igual): ")
    NuevFechVenc = input("Ingresar la nueva fecha de vencimiento (AAAA MM DD, dejar en blanco para mantener igual): ")
    NuevEtiqs = input("Ingresar las nuevas etiquetas (Que esten separadas por comas, dejar en blanco para mantener igual): ")
    for tar in tars:
        if tar['nombre'] == nom:
            if NuevNom:
                tar['nombre'] = NuevNom
            if NuevCate:
                CateAnt = tar['categoria']
                tar['categoria'] = NuevCate
                cates[CateAnt].remove(tar)
                if NuevCate not in cates:
                    cates[NuevCate] = []
                cates[NuevCate].append(tar)
            if NuevFechVenc:
                tar['fecha_vencimiento'] = date(map(int, NuevFechVenc.split()))
            if NuevEtiqs:
                tar['etiquetas'] = set(NuevEtiqs.split(","))
                etiqs.update(tar['etiquetas'])

def MostTar():
    if not HayTars():
        print("Se debe agregar una tarea primero")
        return
    for tar in tars:
        print(f"Nombre: {tar['nombre']}, Categoría: {tar['categoria']}, Fecha de Vencimiento: {tar['fecha_vencimiento']}, Etiquetas: {tar['etiquetas']}")

def TarExist(nom: str) -> bool:
    return any(tar['nombre'] == nom for tar in tars)

def HayTars() -> bool:
    return len(tars) > 0


class Tar:
    def init(self, nom: str, cate: str, FechVenc: Tuple[int, int, int], EtiqsTar: Set[str]):
        self.nom = nom
        self.cate = cate
        self.FechVenc = date()
        self.Etiqs = EtiqsTar

    def str(self):
        return f"Nombre: {self.nom}, Categoría: {self.cate}, Fecha de Vencimiento: {self.FechVenc}, Etiquetas: {self.Etiqs}"

class TarConFechLim(Tar):
    def init(self, nom: str, cate: str, FechVenc: Tuple[int, int, int], EtiqsTar: Set[str], FechLim: Tuple[int, int, int]):
        super().init(nom, cate, FechVenc, EtiqsTar)
        self.FechLim = date(*FechLim)

    def str(self):
        return super().str() + f", Fecha Límite: {self.FechLim}"