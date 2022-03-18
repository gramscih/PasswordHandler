import random

LENGTH = 8

char_candidates = {
    "lower": lambda: chr(random.choice(range(97, 123))), 
    "upper": lambda: chr(random.choice(range(65, 91))), 
    "number": lambda: chr(random.choice(range(48, 58)))
}

def generate_psw():
    result = ""
    for _ in range(0, LENGTH):
        char_key = random.choice([k for k in char_candidates.keys()])
        result = result + char_candidates.get(char_key)()
    return result


# app_name = input("Application: ")
# pwd = generate_psw()
# save_password(app_name, pwd)

