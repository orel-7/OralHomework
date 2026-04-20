total_tickets=0
game_code=int(input("אנא הזן קוד משחק  "))

while game_code != 0:
    num_tickets=int(input("כמה כרטיסים תרצה להזמין? "))
    print("כרטיסים למשחק מספר",game_code)
    print("הוזמנו", num_tickets,)
    total_tickets=total_tickets+num_tickets
    game_code=int(input("אנא הזן קוד משחק  "))

print(total_tickets,"כרטיסים לשני המשחקים")