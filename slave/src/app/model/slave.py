from utils.middle import JWT
import config


class MGSuper():

    def __init__(self,collection_name):
        usr = JWT.get_user()
        self.uid = usr.get('uid',0)
        self.sub = usr.get('sub','...')
        self.alias = f'{self.sub}:{self.uid}'
        self.session = config.Session()
        self._hpmgo = config.MongoDB('slave').open(collection_name)
        self._hpmgo.uid = self.uid

    @property
    def hpmgo(self):
        return self._hpmgo
  