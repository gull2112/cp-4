menu = ["냉면", "볶음밥", "피자", "짜장면"]

def get_menu_choice():
    while True:
        try:
            choice = int(input("메뉴를 선택하세요 (1. 냉면, 2. 볶음밥, 3. 피자, 4. 짜장면): "))
            if choice < 1 or choice > 4:
                raise ValueError("해당 번호의 메뉴가 없습니다. 다시 선택하세요.")
            return menu[choice - 1]
        except ValueError as e:
            print(e)
        except Exception:
            print("잘못된 입력입니다. 숫자를 입력하세요.")

selected_menu = get_menu_choice()
print(f"선택한 메뉴는 {selected_menu}입니다.")
