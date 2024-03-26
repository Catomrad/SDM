from dataclasses import dataclass

@dataclass(frozen=True)
class Material:
    name:str

# m1=Material("Дуб")
# m2=Material("Дуб")

# print(m1 == m2)