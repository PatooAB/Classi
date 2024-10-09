class Libro:
    def __init__(self, titolo, anno, autore):
        self._titolo = titolo
        self._anno = anno
        self._autore = autore

    # Metodi get
    def get_titolo(self):
        return self._titolo

    def get_anno(self):
        return self._anno

    def get_autore(self):
        return self._autore

    # Metodi set
    def set_titolo(self, titolo):
        self._titolo = titolo

    def set_anno(self, anno):
        self._anno = anno

    def set_autore(self, autore):
        self._autore = autore

    # Metodo ToString
    def __str__(self):
        return f"Libro: '{self._titolo}', Anno: {self._anno}, Autore: {self._autore}"

es_libro = Libro("Esercizio Libro", 2024, "Alessio Barabash")
print(es_libro)
