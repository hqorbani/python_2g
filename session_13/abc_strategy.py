from abc import ABC,abstractclassmethod
class abc_strategy(ABC):
    @abstractclassmethod
    def ready_open_buy(self):
        pass
    @abstractclassmethod
    def ready_open_sell(self):
        pass

    # @abstractclassmethod
    # def ready_close_position(self):
    #     pass
