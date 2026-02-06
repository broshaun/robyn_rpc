from .mgops import Mongo
from .hpmgo import CRUD


class DBOpen(Mongo):
    def open(self,collection_name):
        return CRUD(self,collection_name=collection_name)

