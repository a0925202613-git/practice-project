# shelter_app.py

from animal_models import Cat, Dog, Turtle, Animal, let_animal_speak, introduce_all_animals
import time

# =========================================
#          工具函式區
# =========================================

def show_all_pets(pets_list):
    """顯示所有寵物資訊。"""
    if len(pets_list) == 0:
        print("🏠 收容所目前沒有寵物。")
        return
    
    print("\n📋 目前收容所的寵物清單：")
    
    #### [任務] 用 for 迴圈顯示帶編號的寵物清單 ####
    # 預期輸出:
    #   1. 小花 (Cat)
    #   2. 旺財 (Dog)
    #   3. 龜龜 (Turtle)
    for i, pet in enumerate(pets_list,start=1):
        print(f"{i}.{pet.name}({pet.species})")


def add_pet_interactive(pets_list):
    """互動式新增寵物。"""
    print("\n🐾 新增寵物")
    print("  可選類型: cat / dog / turtle")
    
    #### [任務] 用 input() 取得寵物類型和名字 ####
    pet_type = input("請輸入寵物類型:").lower()
    pet_name = input("請輸入寵物名字:")
    
    #### [任務] 用 if/elif/else 根據類型建立對應物件，並加入 pets_list ####
    # - cat: 建立 Cat 物件
    # - dog: 額外詢問品種，建立 Dog 物件  
    # - turtle: 建立 Turtle 物件
    # - 其他: 印出 "❌ 不支援的寵物類型"
    if pet_type == "cat":
        pets_list.append(Cat(pet_name))
    elif pet_type == "dog":
        breed=input("請輸入狗狗品種:")
        pets_list.addend(Dog(pet_name,breed))
    elif pet_type == "turtle":
        pets_list.addend(Turtle(pet_name))
    else:
        print("❌ 不支援的寵物類型")


def remove_pet_interactive(pets_list):
    """互動式移除寵物（送養出去）。"""
    if len(pets_list) == 0:
        print("🏠 收容所沒有寵物可以送養。")
        return
    
    show_all_pets(pets_list)
    
    #### [任務] 讓用戶輸入編號，移除對應的寵物 ####
    # 預期輸出（假設輸入 1）: "🏡 小花 已經找到新家了！"
    # 注意：用戶輸入的是 1、2、3，但 list 索引是 0、1、2
    idx=int(input("請輸入要送養的寵物編號:"))-1
    if 0 <= idx < len(pets_list):
        pet=pets_list.pop(idx)
        print(f"🏡 {pet.name} 已經找到新家了！")
    else:
        print("❌ 無效編號")


def let_pets_interact(pets_list):
    """讓所有寵物發出聲音並執行特殊動作。"""
    if len(pets_list) == 0:
        print("🏠 收容所沒有寵物。")
        return
    
    print("\n🔊 寵物互動時間！")
    print("=" * 40)
    
    for pet in pets_list:
        time.sleep(0.5)
        print(f"\n--- {pet.name} ({pet.species}) ---")
        print(pet.display_art())
        
        #### [任務] 呼叫 pet.make_sound() ####
        pet.make_sound()
        
        #### [任務] 用 isinstance 判斷寵物類型，呼叫對應的專屬動作 ####
        # Dog -> fetch()
        # Cat -> climb_tree()
        # Turtle -> hide_in_shell()
        if isinstance(pet,Dog):
            pet.fetch()
        elif isinstance(pet,Cat):
            pet.climb_tree()
        elif isinstance(pet,Turtle):
            pet.hide_in_shell()


def count_by_species(pets_list):
    """統計各種類寵物數量。"""
    cat_count = 0
    dog_count = 0
    turtle_count = 0
    
    #### [任務] 用 for 迴圈和 isinstance 統計各類數量 ####
    for pet in pets_list:
        if isinstance(pet,Cat):
            cat_count+=1
        elif isinstance(pet,Dog):
            dog_count+=1
        elif isinstance(pet,Turtle):
            turtle_count+=1
    
    print("\n📊 寵物種類統計：")
    print(f"  🐱 貓咪: {cat_count} 隻")
    print(f"  🐶 狗狗: {dog_count} 隻")
    print(f"  🐢 烏龜: {turtle_count} 隻")
    print(f"  📝 總計: {len(pets_list)} 隻")


# =========================================
#             互動式主選單
# =========================================

def interactive_menu(pets_list):
    """互動式選單。"""
    
    while True:
        print("\n=========================================")
        print("           🏠 收容所主選單")
        print("=========================================")
        print("  1. 📋 查看所有寵物")
        print("  2. ➕ 新增寵物")
        print("  3. ➖ 送養寵物")
        print("  4. 🔊 寵物互動時間")
        print("  5. 🎤 多型示範 (全體發聲)")
        print("  6. 📊 種類統計")
        print("  0. 👋 離開系統")
        print("-----------------------------------------")
        
        #### [任務] 用 input() 取得用戶選擇 ####
        choice = input("請選擇功能:")
        
        #### [任務] 用 if/elif/else 處理各選項 ####
        # 1 -> show_all_pets(pets_list)
        # 2 -> add_pet_interactive(pets_list)
        # 3 -> remove_pet_interactive(pets_list)
        # 4 -> let_pets_interact(pets_list)
        # 5 -> introduce_all_animals(pets_list)
        # 6 -> count_by_species(pets_list)
        # 0 -> 印出告別訊息，用 break 離開迴圈
        # 其他 -> 印出 "❌ 無效選項"
        if choice == "1":
            show_all_pets(pets_list)
        elif choice == "2":
            add_pet_interactive(pets_list)
        elif choice == "3":
            remove_pet_interactive(pets_list)
        elif choice == "4":
            let_pets_interact(pets_list)
        elif choice == "5":
            introduce_all_animals(pets_list)
        elif choice == "6":
            count_by_species(pets_list)
        elif choice == "0":
            print("👋 感謝使用，再見！")
            break
        else:
            print("❌ 無效選項")
        


# =========================================
#               程式入口
# =========================================

def run_shelter():
    print("=========================================")
    print("====== 歡迎來到虛擬寵物收容所系統 =======")
    print("=========================================\n")
    
    #### [任務] 建立初始寵物列表，放入幾隻你喜歡的寵物 ####
    pets_in_shelter = [
        Cat("小花"),
        Dog("旺財", "柴犬"),
        Turtle("龜龜")
    ]
    
    interactive_menu(pets_in_shelter)


if __name__ == "__main__":
    run_shelter()
