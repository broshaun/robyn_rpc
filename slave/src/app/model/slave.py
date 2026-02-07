from utils.middle import JWT
import config


class MGSuper():

    def __init__(self,collection_name):
        self.uid = JWT.get_user('uid')
        self.session = config.Session()
        self._hpmgo = config.MongoDB('slave').open(collection_name)
        self._hpmgo.uid = self.uid

    @property
    def hpmgo(self):
        return self._hpmgo
  