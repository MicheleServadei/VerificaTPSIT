from pannello import PannelloFotovoltaico

listaPanelli = [PannelloFotovoltaico]

class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        self.Codice = codice
        self.Modello = modello
        self.Localita = localita
        self.Potenza_massima_kw = potenza_massima_kw
        self.Stato = stato
        
        
        def aggiungi_pannello(self, pannello : PannelloFotovoltaico)->None:
            if self._pannello in listaPanelli:
                raise ValueError("esista già all'interno della lista")
            self.listaPannelli.append(self._pannello)
            
        def potenza_pannelli(self)->float:
            return sum(listaPanelli(self._pannello.Potenza))
        
        def cerca_pannello(self, codice : str) -> PannelloFotovoltaico:
            if not codice:
                raise ValueError("il codice non può essere vuoto")
            
            for self._pannello in listaPanelli :
                if self._pannello.Codice == codice:
                    return self._pannello
                return None
            
        def rimuovi_pannello(self, codice : str) ->PannelloFotovoltaico:
            if not codice:
                raise ValueError("il codice non può essere vuoto")
            
            for self._pannello in listaPanelli :
                if self._pannello.Codice == codice:
                    listaPanelli.remove(self._pannello)
                    return self.pannello
                return None
            
        def pannelli_sotto_potenza(self, potenza_massima : float) -> list[PannelloFotovoltaico]:
            PannelliSottoPotenza = []
            if not potenza_massima:
                raise ValueError("potenza_masima non può essere vuota")
            for self._pannello in listaPanelli:
                if(self._pannello.Potenza_kw <= potenza_massima)
                    PannelliSottoPotenza.append(self._pannello)
        
        
        
        
        
        
        