import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose"
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Dealer won with BlackJack"
    elif user_score == 0:
        return "You won with a BlackJack"
    elif user_score > 21:
        return "You lose"
    elif computer_score > 21:
        return "You win"
    elif user_score > computer_score:
        return "You win"
    elif user_score < computer_score:
        return "You lose"
    
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"You have {user_cards} and score is {user_score}")
        print(f"Computer has {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Y for new card, N to pass: ")
            if user_deal == "Y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand is {user_cards} and score is {user_score}")
    print(f"Dealer's final hand is {computer_cards} and score is {computer_score}")
    print(compare(user_score, computer_score))
    
while input("Y for playing BlackJack, N for not: ") == "Y":
    play_game()
    
    