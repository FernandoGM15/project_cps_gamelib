from abc import abstractmethod, ABCMeta
@abstractmethod
class API_request(metaclass=ABCMeta):
  def get_juego(self):
    pass

  def search_juego(self,nombre):
    pass
