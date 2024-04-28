import json
from abc import ABC, abstractmethod

class JsonComponent(ABC):
    """
    Clase abstracta para los componentes JSON.
    """
    @abstractmethod
    def get_data(self):
        pass

class JsonLeaf(JsonComponent):
    """
    Representa un documento JSON individual.
    """
    def __init__(self, json_data):
        self.data = json_data
    
    def get_data(self):
        return self.data

class JsonComposite(JsonComponent):
    """
    Compuesto que puede contener múltiples documentos JSON.
    """
    def __init__(self):
        self.children = []
    
    def add(self, component: JsonComponent):
        self.children.append(component)
    
    def get_data(self):
        combined_data = {}
        for child in self.children:
            self.merge_data(combined_data, child.get_data())
        return combined_data
    
    def merge_data(self, original, new_data):
        """
        Fusiona new_data en original. Este método puede ser extendido para manejar la fusión de maneras específicas.
        """
        for key, value in new_data.items():
            if key in original:
                if isinstance(original[key], dict) and isinstance(value, dict):
                    self.merge_data(original[key], value)
                elif isinstance(original[key], list) and isinstance(value, list):
                    original[key].extend(value)
                else:
                    original[key] = [original[key], value] if not isinstance(original[key], list) else original[key] + [value]
            else:
                original[key] = value
"""
# Uso del patrón Composite
composite = JsonComposite()
composite.add(JsonLeaf({'name': 'Alice', 'age': 25}))
composite.add(JsonLeaf({'name': 'Bob', 'age': 30}))
composite.add(JsonLeaf({'skills': ['Python', 'Data Analysis']}))

combined_json = json.dumps(composite.get_data(), indent=4)
print(combined_json)
"""