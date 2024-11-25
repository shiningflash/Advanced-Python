from abc import ABC, abstractmethod
from typing import List

class Smoothie(ABC):
    @abstractmethod
    def ingredients(self) -> List[str]:
        """Ingrediants for specific type smoothie"""
        pass
    
    @abstractmethod
    def prepare(self) -> str:
        """Preparing a specific type smoothie"""
        pass

class MangoSmoothie(Smoothie):
    def ingredients(self) -> List[str]:
        return ['Mango', 'Milk', 'Sugar']
    
    def prepare(self) -> str:
        return f'Blending: {', '.join(self.ingredients())}'

class ChocolateSmoothie(Smoothie):
    def ingredients(self) -> List[str]:
        return ['Chocolate', 'Almond Milk', 'Honey']
    
    def prepare(self) -> str:
        return f'Blending: {', '.join(self.ingredients())}'

class SmoothieFactory(ABC):
    @abstractmethod
    def create_smoothie(self) -> Smoothie:
        """Create a specific type smoothie"""
        pass

class MangoSmoothieFactory(SmoothieFactory):
    def create_smoothie(self) -> Smoothie:
        return MangoSmoothie()

class ChocolateSmoothieFactory(SmoothieFactory):
    def create_smoothie(self) -> Smoothie:
        return ChocolateSmoothie()

class SmoothieMachine:
    def __init__(self) -> None:
        self.factory = {
            "mango": MangoSmoothieFactory(),
            "chocolate": ChocolateSmoothieFactory()
        }
    
    def prepare_smoothie(self, smoothie_type: str) -> str:
        factory = self.factory.get(smoothie_type.lower())
        if not factory:
            return f'Error! {smoothie_type} smoothie is not available!'
        smoothie = factory.create_smoothie()
        return smoothie.prepare()

if __name__ == "__main__":
    smoothie_machine = SmoothieMachine()
    
    print(smoothie_machine.prepare_smoothie("mango"))
    print(smoothie_machine.prepare_smoothie("chocolate"))
    print(smoothie_machine.prepare_smoothie("banana"))
