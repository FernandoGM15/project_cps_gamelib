from abc import abstractmethod, ABCMeta
class API_request(metaclass=ABCMeta):
  @abstractmethod
  def get_juego(self):
    pass

