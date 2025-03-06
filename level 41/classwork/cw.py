def print_word_from_list():
    # 5 სიტყვიანი სიის შექმნა
    word_list = ["milk", "bread", "meat", "chinkali", "mwvadi"]
    
    # მომხმარებლისგან რიცხვის მიღება
    try:
        index = int(input(" 1 2 3 4 "))
        
        # დარწმუნდებით, რომ რიცხვი 0-დან 4-მდეა
        if 0 <= index < len(word_list):
            print(f"თქვენი შესავალი: {word_list[index]}")
        else:
            print("1 2 3 4.")
    except ValueError:
        print("5800")

# ფუნქციის გაშვება
print_word_from_list()
