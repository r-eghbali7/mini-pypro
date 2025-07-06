# import random
# import string

# def generate_random_word(min_length=3, max_length=10):
#     # تعیین طول تصادفی کلمه
#     word_length = random.randint(min_length, max_length)
    
#     # ایجاد یک لیست از حروف الفبا
#     letters = string.ascii_letters.lower()
    
#     # تولید کلمه تصادفی با طول مشخص شده
#     word = ''.join(random.choice(letters) for _ in range(word_length))
    
#     print(word)

# word = "python" # اگر کلمه به صورت پیش فرض باشد
# # word =  generate_random_word() # اگر کلمه به صورت رندوم  توسط کامپوتر تولید شود

# word_found = list("-" * len(word)) # کلمه یافیت شده 


# # حلقه جهت دفعات تکرار که 6 با تکرار میشه
# def guess_word():   
#     username = input("please enter your name: ")
#     print(f"welcome {username} in a game!")
#     counter = 0 # شمارنده تعداد تکرار لحقه جهت محدود سازی 
#     while counter < 6:
#         print("".join(word_found)) # کلمات یافت شده تکی
#         guess_word = input("Enter your guess: ") # دریافت کلمه ها توسط کاربر

#         # شرط اینکه اگر کاربر کل کلمات را به درستی نویشت
#         if guess_word == word:
#             print(f"You guessed '{guess_word}' it right!")
#             break

#         # شمارنده تعداد دور جهت محدود سازی
#         counter += 1 # counter = counter + 1

#         # برسی جهت یافت شدن کلمه درست و قرار گیری در محل مناسب ان
#         for i, char in enumerate(word):
#             if char in guess_word:
#                 word_found[i] = char

#         if "".join(word_found) == word:
#             print(f"You guessed it right!")
#             break
#         else:
#             print("You guessed it wrong!")

# guess_word()


import random
import string

# def generate_random_word(min_length=3, max_length=10):
#     # تعیین طول تصادفی کلمه
#     word_length = random.randint(min_length, max_length)
    
#     # ایجاد یک لیست از حروف الفبا
#     letters = string.ascii_letters.lower()
    
#     # تولید کلمه تصادفی با طول مشخص شده
#     word = ''.join(random.choice(letters) for _ in range(word_length))
    
#     return word

word = "python" # اگر کلمه به صورت پیش فرض باشد
# word = generate_random_word() # اگر کلمه به صورت رندوم توسط کامپیوتر تولید شود

word_found = list("-" * len(word)) # کلمه یافت شده 

# حلقه جهت دفعات تکرار که 6 بار تکرار می‌شود
def guess_word():   
    username = input("please enter your name: ")
    print(f"welcome {username} in a game!")
    counter = 0 # شمارنده تعداد تکرار حلقه جهت محدود سازی 
    while counter < 6:
        print("".join(word_found)) # کلمات یافت شده تکی
        guess_word = input("Enter your guess: ") # دریافت کلمه‌ها توسط کاربر

        # برسی جهت یافت شدن کلمه درست و قرار گیری در محل مناسب آن
        for i, char in enumerate(word):
            if char in guess_word:
                word_found[i] = char

        if "".join(word_found) == word:
            print(f"You guessed '{word}' it right!")
            break

        # شرط اینکه اگر کاربر کل کلمات را به درستی نوشت
        if guess_word == word:
            print(f"You guessed '{guess_word}' it right!")
            break

        # شمارنده تعداد دور جهت محدود سازی
        counter += 1 # counter = counter + 1
        
        if counter == 6:
            print(f"You failed to guess the word '{word}'")

    else:
        print("You guessed it wrong!")

guess_word()
