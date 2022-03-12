# Tipo de texto:      str
# Tipos numéricos:    int, float, complex
# Tipos de sequência: list, tuple, range
# Tipo de mapeamento: dict
# Tipos de conjuntos: set, frozenset
# Tipo booleano:      bool
# Tipos binários:     bytes, bytearray, memoryview

#### Definir o tipo de dados ####

x = "Hello World" # str
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = range(6) # range
x = {"name" : "Jhon", "age" : 36} # dict
x = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True # bool
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview

#### Configurando o Tipo de Dados Espesífico ####

x = str("Hello Wolrd") # str
x = int(20) # int
x = float(20.5) # float
x = complex(1j) # complex
x = list(["apple", "banana", "cherry"]) # list
x = tuple(("apple", "banana", "cherry")) # tuple
x = range(6) # range
x = dict({"name" : "Jhon", "age" : 36}) # dict
x = set({"apple", "banana", "cherry"}) # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = bool(5) # bool
x = bytes(5) # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview

x = "20"
print(x)
print(type(x))

x = int("20")
print(type(x))
