class SuperHero:
    def __init__(self, name="", alias="", special_skill=""):
        self.name = name
        self.alias = alias
        self.special_skill = special_skill  # Corrigido: atribuindo o valor recebido
         
    def __str__(self):
        return f"{self.name}: {self.alias} - {self.special_skill}"  # Corrigido a f-string

# Testando as instâncias
super_hero1 = SuperHero()
super_hero1.name = "Peter Parker"
super_hero1.alias = "Spiderman"
super_hero1.special_skill = "Web Slinging"

super_hero2 = SuperHero("Tony Stark", "Iron man", "Flying")

super_hero3 = SuperHero(
    name="Bruce Banner",
    alias="The Hulk",
    special_skill="Strength"
)

print(f"Hero:{super_hero1.name}:{super_hero1.alias}")
print(f"Hero:{super_hero2.name}:{super_hero2.alias}")
print(f"Hero:{super_hero3.name}:{super_hero3.alias}")


print(super_hero1)
print(super_hero2)
print(super_hero3)

names = [
"Peter Parker"
"Tony Stark"
"Bruce Banner"

]
for item in names:
    print(item)

super_heroes = [super_hero1, super_hero2, super_hero3]
for hero in super_heroes

dc_heroes =  [
    SuperHero("Bruce","Batman","Technology"),
    SuperHero("Clark","Superman", "Flyng"),
    SuperHero("Diana Prince","Wonder Woman", "Speed")
]

for hero in dc_heroes:
    print (hero)