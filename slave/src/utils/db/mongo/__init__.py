from .mgops import MgoDB
from .hpmgo import CRUD


class DBOpen(MgoDB):
    def open(self,collection_name):
        return CRUD(self,collection_name=collection_name)

