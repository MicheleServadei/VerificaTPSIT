from pannello import PannelloFotovoltaico
from impianto import ImpiantoSolare

if __name__ == "__main__":
    impiantoSolare = ImpiantoSolare()

    impiantoSolare.aggiungi_pannello( "codice", "modello", 16)
    impiantoSolare.aggiungi_pannello( "aiuto", "bt7274", 18)
    impiantoSolare.aggiungi_pannello( "sabato","Masterchief", 20)
    impiantoSolare.aggiungi_pannello( "domenica", "Masterchief", 20)
    impiantoSolare.riepilogo_impianti("rocketry", ListaImpianti)
    
    
    
ListaImpianti = [impiantoSolare]
def registra_impianto(self, impianti: list[ImpiantoSolare], impianto: ImpiantoSolare) ->None :
    if impianto is in impianti:
        raise ValueError("è già presente")
    self.impianti.append(self.impianto)

def cerca_impianto(self,impianti: list[ImpiantoSolare], codice: str) -> ImpiantoSolare:
    for impiantoSolare in impianti:
        if self.impiantoSolare.Codice == codice:
            return self.impiantoSolare
            
def riepilogo_impianti(self, nome_azienda: str, impianti: list[ImpiantoSolare]) -> None:
    for impiantoSolare in impianti:
        print(f"{impiantoSolare}, Modello : {impiantoSolare.Modello}, Stato:  {impiantoSolare.Stato}, Somma Potenze : {sum(impiantoSolare.Potenza_massima_kw)}")
            
    
