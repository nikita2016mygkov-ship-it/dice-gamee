python
import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice():
    return random.randint(1, 6)

def roll_two_dice():
    dice1 = roll_dice()
    dice2 = roll_dice()
    return dice1, dice2, dice1 + dice2

def show_dice_art(value):
    arts = {
        1: ["┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"],
        2: ["┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"],
        3: ["┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"],
        4: ["┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"],
        5: ["┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"],
        6: ["┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"]
    }
    return arts[value]

def show_both_dice(dice1, dice2):
    art1 = show_dice_art(dice1)
    art2 = show_dice_art(dice2)
    for i in range(5):
        print(art1[i] + "  " + art2[i])

def show_menu():
    print("=" * 50)
    print("        🎲 ИГРА В КОСТИ 🎲")
    print("=" * 50)
    print("1️⃣  Новая игра")
    print("2️⃣  Статистика")
    print("3️⃣  Правила")
    print("0️⃣  Выход")
    print("-" * 50)

def show_rules():
    clear_screen()
    print("📖 ПРАВИЛА ИГРЫ:")
    print("-" * 40)
    print("• Игрок и компьютер бросают по два кубика")
    print("• Побеждает тот, у кого сумма очков больше")
    print("• Игра идет до 3 побед")
    print("• Можно остановить игру в любой момент")
    print("-" * 40)
    input("\nНажмите Enter для возврата...")

def load_stats():
    if os.path.exists("dice_stats.txt"):
        with open("dice_stats.txt", "r") as f:
            data = f.read().split(",")
            return int(data[0]), int(data[1]), int(data[2])
    return 0, 0, 0

def save_stats(wins, losses, total_games):
    with open("dice_stats.txt", "w") as f:
        f.write(f"{wins},{losses},{total_games}")

def play_round():
    clear_screen()
    print("🎲 РАУНД НАЧАЛСЯ! 🎲")
    print("-" * 40)
    
    input("Нажмите Enter, чтобы бросить кости...")
    
    print("\n🎲 ВАШ БРОСОК:")
    player_dice1, player_dice2, player_sum = roll_two_dice()
    show_both_dice(player_dice1, player_dice2)
    print(f"Сумма: {player_sum}")
    
    time.sleep(1)
    
    print("\n🤖 БРОСОК КОМПЬЮТЕРА:")
    computer_dice1, computer_dice2, computer_sum = roll_two_dice()
    show_both_dice(computer_dice1, computer_dice2)
    print(f"Сумма: {computer_sum}")
    
    time.sleep(1)
    
    print("\n" + "=" * 40)
    if player_sum > computer_sum:
        print("✅ ВЫ ВЫИГРАЛИ РАУНД!")
        return "player"
    elif computer_sum > player_sum:
        print("❌ КОМПЬЮТЕР ВЫИГРАЛ РАУНД!")
        return "computer"
    else:
        print("🤝 НИЧЬЯ!")
        return "tie"

def play_game():
    clear_screen()
    
    player_wins = 0
    computer_wins = 0
    target_score = 3
    
    print("🎲 НОВАЯ ИГРА! 🎲")


print(f"Кто первым одержит {target_score} победы — победитель!")
    print("-" * 40)
    
    while player_wins < target_score and computer_wins < target_score:
        print(f"\n📊 СЧЁТ: Вы {player_wins} : {computer_wins} Компьютер")
        print("-" * 30)
        
        choice = input("\nНажмите Enter для броска или '0' для выхода: ")
        if choice == "0":
            print("\nИгра прервана!")
            return None
        
        result = play_round()
        
        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1
        
        if result != "tie":
            input("\nНажмите Enter для следующего раунда...")
    
    clear_screen()
    print("=" * 50)
    print("🏆 ИГРА ОКОНЧЕНА! 🏆")
    print("=" * 50)
    print(f"ФИНАЛЬНЫЙ СЧЁТ: {player_wins} : {computer_wins}")
    
    if player_wins > computer_wins:
        print("\n🎉 ПОЗДРАВЛЯЮ! ВЫ ПОБЕДИЛИ В ИГРЕ! 🎉")
        return "player"
    else:
        print("\n💻 ПОБЕДИЛ КОМПЬЮТЕР! В СЛЕДУЮЩИЙ РАЗ ПОВЕЗЁТ! 💻")
        return "computer"

def main():
    wins, losses, total = load_stats()
    
    while True:
        clear_screen()
        show_menu()
        
        if total > 0:
            win_rate = (wins / total) * 100
            print(f"📊 Статистика: {wins} побед / {losses} поражений")
            print(f"🎯 Процент побед: {win_rate:.1f}%")
            print("-" * 50)
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            result = play_game()
            if result:
                wins += 1 if result == "player" else 0
                losses += 1 if result == "computer" else 0
                total += 1
                save_stats(wins, losses, total)
            input("\nНажмите Enter для продолжения...")
            
        elif choice == "2":
            clear_screen()
            print("📊 СТАТИСТИКА ИГР:")
            print("-" * 40)
            print(f"Сыграно игр: {total}")
            print(f"Побед: {wins}")
            print(f"Поражений: {losses}")
            if total > 0:
                print(f"Процент побед: {(wins/total)*100:.1f}%")
            print("-" * 40)
            input("\nНажмите Enter для возврата...")
            
        elif choice == "3":
            show_rules()
            
        elif choice == "0":
            print("\n👋 Спасибо за игру! До свидания!")
            break
            
        else:
            print("❌ Неверный выбор!")
            time.sleep(1)

if __name__ == "__main__":
    main()

#авп
#хэштег
