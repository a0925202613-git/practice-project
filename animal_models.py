# animal_models.py

from art_data import PET_ART

# --- 父類別 Animal：定義通用屬性和行為 ---
class Animal:
    """所有寵物的基礎類別。"""

    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"✅ 成功領養一隻 {self.species}，取名為 {self.name}！")

    def make_sound(self):
        """通用方法：發出基本聲音。子類別應該覆寫這個方法。"""
        print(f"[{self.name}] 發出了一般動物的聲音。")

    def display_art(self):
        """顯示寵物的 ASCII Art。"""
        return PET_ART.get(self.species, PET_ART["Default"])

    def get_info(self):
        """回傳寵物的基本資訊。"""
        #### [任務] 實作 get_info ####
        # 預期輸出範例: "🐾 小花 (Cat)"
        return f"🐾{self.name}({self.species})"
    
my_pet=Animal("小花","Cat")
print(my_pet.get_info())




# --- 子類別 1: Cat (繼承自 Animal) ---
class Cat(Animal):
    def __init__(self, name, favorite_food="魚"):
        #### [任務] 呼叫父類別建構式，物種設為 "Cat" ####
        super().__init__(name,"Cat")
        self.favorite_food = favorite_food

    def make_sound(self):
        """【多型】覆寫父類別方法。"""
        #### [任務] 讓貓發出聲音 ####
        # 預期輸出範例: "[小花] 喵喵～ 想吃魚！"
        print(f"{self.name}喵喵～ 想吃{self.favorite_food}！")

    def climb_tree(self):
        """貓咪特有行為。"""
        print(f"[{self.name}] 爬上樹了！ (貓咪專屬動作)")


# --- 子類別 2: Dog (繼承自 Animal) ---
class Dog(Animal):
    def __init__(self, name, breed="米克斯"):
        #### [任務] 呼叫父類別建構式，物種設為 "Dog" ####
        super().__init__(name,"Dog")
        self.breed = breed
        
    def make_sound(self):
        """【多型】覆寫父類別方法。"""
        #### [任務] 讓狗發出聲音 ####
        # 預期輸出範例: "[旺財] 汪汪！我是一隻柴犬！"
        print(f"{self.name}汪汪！我是一隻{self.breed}！")

    def fetch(self):
        """狗狗特有行為。"""
        print(f"[{self.name}] 開心地去撿球了！ (狗狗專屬動作)")


# --- 子類別 3: Turtle (繼承自 Animal) ---
class Turtle(Animal):
    def __init__(self, name):
        #### [任務] 呼叫父類別建構式，物種設為 "Turtle" ####
        super().__init__(name,"Turtle")
        
    def make_sound(self):
        """【多型】覆寫父類別方法。"""
        #### [任務] 讓烏龜發出聲音 ####
        # 預期輸出範例: "[龜龜] ...（緩慢地眨眼）..."
        print(f"{self.name}...(緩慢地眨眼）...")
        
    def hide_in_shell(self):
        """烏龜特有行為。"""
        print(f"[{self.name}] 感覺不安全，躲進殼裡了。 (烏龜專屬動作)")


# =========================================
#        【多型示範函式】
# =========================================

def let_animal_speak(animal):
    """
    【多型的核心概念】
    不管傳入 Cat、Dog 還是 Turtle，都用同樣方式呼叫 make_sound()。
    """
    print(f"\n🎤 讓 {animal.name} 發出聲音：")
    animal.make_sound()


def introduce_all_animals(animal_list):
    """【多型應用】讓所有動物自我介紹。"""
    print("\n📢 全體寵物自我介紹時間！")
    print("-" * 30)
    
    #### [任務] 用 for 迴圈讓每隻動物呼叫 make_sound() ####
    # 預期輸出（假設有貓、狗、烏龜各一隻）:
    # [小花] 喵喵～ 想吃魚！
    # [旺財] 汪汪！我是一隻柴犬！
    # [龜龜] ...（緩慢地眨眼）...
    for animal in animal_list:
        animal.make_sound()

pets = [
    Cat("小花", "魚"),
    Dog("旺財", "柴犬"),
    Turtle("龜龜")
]

let_animal_speak(pets[0])

introduce_all_animals(pets)