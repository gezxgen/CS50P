# imports
from requests   import post
from os         import getenv
from re         import search
from segno      import make_qr
from random     import randint, choice
from math       import log2, ceil
from dotenv     import load_dotenv
from secrets    import token_urlsafe
from csv        import reader, writer
from timeit     import default_timer    as timer
from os         import system           as os_system
from platform   import system           as platform_system


# classes
class Password:
    _password = ""

    @classmethod
    def password(cls):
        return cls._password

    @classmethod
    def password(cls, new_password):
        cls._password = new_password

    @staticmethod
    def random(length):
        i = 0
        password = ""
        random_word = token_urlsafe(Password.char_to_bytes(length))
        while len(password) != length:
            password += random_word[i]
            i += 1
        Password.password = password
        return Password.password

    @staticmethod
    def strength(str):
        # calculating the entropy in the password
        entropy = log2(Password.get_size(str) ** len(str))

        if entropy < 40:
            return "weak", "seconds"
        elif entropy < 60:
            return "moderate", "hours"
        elif entropy < 80:
            return "strong", "weeks"
        else:
            return "very strong", "years"

    @staticmethod
    def get_size(str):
        charset_size = 0
        if any(c.islower() for c in str):
            charset_size += 26
        if any(c.isupper() for c in str):
            charset_size += 26
        if any(c.isdigit() for c in str):
            charset_size += 10
        if any(c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for c in str):
            charset_size += 32
        return charset_size

    @staticmethod
    def char_to_bytes(char):
        return ceil(((char * 3) / 4))

    @classmethod
    def __str__(cls):
        return f"The password is: {cls.password}"


class Link:
    _Link = ""

    @classmethod
    def link(cls):
        return cls._link

    @classmethod
    def link(cls, link):
        cls._link = link

    @staticmethod
    def shorten(link):
        if matches := search(r"^(?:https?://)?(?:www\.)?([^/]+)(?:/.+)*$", link):
            Link.link = matches.group(1)
            return Link.link
        else:
            return "The link could not be found."

    @staticmethod
    def check(TOKEN, URL):
        SAFE_BROWSING_URL = 'https://safebrowsing.googleapis.com/v4/threatMatches:find'
        payload = {
            'client': {
                'clientId': "yourClientID",
                'clientVersion': "0.1"
            },
            'threatInfo': {
                'threatTypes': ["MALWARE", "SOCIAL_ENGINEERING"],
                'platformTypes': ["WINDOWS"],
                'threatEntryTypes': ["URL"],
                'threatEntries': [
                    {'url': URL},
                ]
            }
        }
        params = {'key': TOKEN}
        return post(SAFE_BROWSING_URL, params=params, json=payload)

    @classmethod
    def __str__(cls):
        return Link._link


def main():
    # variables & startup
    load_dotenv()
    best = ""
    round = True
    results = []
    file_lines = []
    file_name = "results.csv"

    # infinite loop
    while round:
        match print_table():
            # Password generator
            case 11:
                print(f"Your new password is: {Password.random(get_length())}\n")

            # Password strength checker
            case 12:
                results = Password.strength(input("What's your password? "))
                print(f'The strength level of your password is: "{results[0]}"', end="")
                print(f", it would take {results[1]} to crack.")

            # String camparison
            case 13:
                str1 = input("String 1: ")
                str2 = input("String 2: ")
                if str1 == str2:
                    print("The strings are equal.")
                else:
                    print("The strings are not equal.")

            # Encrypt words
            case 14:
                # variables
                output = []
                word = input("Which word would you want to encrypt? ")
                key = get_key()

                for char in word:
                    output.append(int(ord(char) * key))
                print("The encrypted word is: ", end="")
                for i, number in enumerate(output):
                    print(f"{number}", end="")
                    if i != len(output) - 1:
                        print(", ", end="")
                print("")

            # Decrypt words
            case 15:
                # variables
                output = input("Which word would you like to decrypt? ").split(", ")
                key = get_key()
                word = ""
                try:
                    for number in output:
                        word += chr(int(int(number) / key))
                    print(f"The decrypted word is: {word}")
                except ValueError:
                    print("There has been a prblem with the value.")
                except TypeError:
                    print("There has been a problem with the type.")
                except ZeroDivisionError:
                    print("There has been a problem with the divison 0.")

            # link shortener
            case 21:
                print(Link.shorten(input("Which link would you like to shorten? ")))

            # QR code generator
            case 22:
                print("Attention! The link is neither checked nor changed!")
                qrcode = make_qr(input("Enter the link of the QR code: "))
                qrcode.save("qrcode.png")

            # link checker
            case 23:
                # get token and link
                print("Attention! The link is neither checked nor changed!")
                response = Link.check(getenv("TOKEN"), input("Enter the link you would like to check: "))

                # Interpret the response
                if response.json():
                    print("Threats found:")
                    print(response.json())
                else:
                    print("No threats found.")

            # typewriter
            case 31:
                # generate a random string
                errors = 0
                best = ""
                string = get_string()
                print("Type the following string (per wrong character +3s): ")
                string = Password.random(string)
                print(string)

                # measure the time it took
                start = timer()
                result = input("")
                end = timer()
                difference = float(end - start)
                while len(result) < len(string):
                    result += "`"

                # review
                for i in range(len(string)):
                    if string[i] != result[i]:
                        errors += 1
                        difference += 3

                # get results
                now = float (difference / len(string))
                print(f"The string {string} had {errors} erros and finished with a time of {difference}!")
                print(f"Your score now was {now}s/char!")

                # read file and personal best
                file_lines = get_file(file_name)
                for digit in file_lines[0]:
                    best += digit
                best = float(best.strip())

                # if new highscore, write entire file
                if best > now:
                    file_lines[0] = str(now)
                    write_file(file_lines, file_name)
                    print(f"Your personal best is {now}s/char!")
                else:
                    print(f"Your personal best is {best}s/char!")

            # number guesser
            case 32:
                # variables
                number = 0
                guess = -1
                index = 0
                guesses = 0
                digits = ""
                file_lines = get_file(file_name)
                correct_digits = set(["1", "2", "3", "4", "5", "6"])

                # get random number
                while digits not in correct_digits:
                    digits = input("How many digits do you wnat to guess (1-6)? ")
                match int(digits):
                    case 1:
                        best = int(file_lines[1][0].strip())
                        index = 0
                        number = randint(0, 10)
                    case 2:
                        best = int(file_lines[1][1].strip())
                        index = 1
                        number = randint(0, 100)
                    case 3:
                        best = int(file_lines[1][2].strip())
                        index = 2
                        number = randint(0, 1000)
                    case 4:
                        best = int(file_lines[1][3].strip())
                        index = 3
                        number = randint(0, 10000)
                    case 5:
                        best = int(file_lines[1][4].strip())
                        index = 4
                        number = randint(0, 100000)
                    case 6:
                        best = int(file_lines[1][5].strip())
                        index = 5
                        number = randint(0, 1000000)

                # guess random number
                while guess != number:
                    guess = int(input("Next guess: "))
                    guesses += 1
                    if number > guess:
                        print("higher")
                    elif number < guess:
                        print("lower")
                    else:
                        print("Just right!")

                # compare the score to highscore
                print(f"You had {guesses} tries for a number with {digits} digit(s).")
                if guesses < best:
                    file_lines[1][index] = str(guesses)
                    best = guesses
                    write_file(file_lines, file_name)
                print(f"You have {best} tries as a highscore for a number with {digits} digit(s).")


            # rock, paper, scissors
            case 33:
                # variables
                item = ""
                file_lines = get_file(file_name)
                item_user = get_item()
                item_program = choice(["r", "p", "s"])

                # determine result
                if item_user == item_program:
                    print("It's a tie!")
                elif (item_user == "r" and item_program == "s") or \
                    (item_user == "p" and item_program == "r") or \
                    (item_user == "s" and item_program == "p"):
                    print("You win!")
                    file_lines[2][0] = str(int(file_lines[2][0]) + 1)
                else:
                    print("Computer wins!")
                    file_lines[2][1] = str(int(file_lines[2][1]) + 1)

                # print the result and safe in file
                print(f"The overall score (You:Computer) is {file_lines[2][0]}:{file_lines[2][1]}!")
                write_file(file_lines, file_name)

        round = another_round()


# printing the table of contents and returning the integer
def print_table():
    # variables
    correct_values = set(["11", "12", "13", "14", "15",
                         "21", "22", "23",
                         "31", "32", "33",
                         "99"])
    answer = ""

    print("\n1. Passwords and security:")
    print("\t11. Password generator")
    print("\t12. Password strength checker")
    print("\t13. String camparison")
    print("\t14. Encrypt words")
    print("\t15. Decrypt words")
    print("\n2. Links:")
    print("\t21. Link shortener")
    print("\t22. QR code generator")
    print("\t23. Link checker")
    print("\n3. Time killers:")
    print("\t31. Typewriter")
    print("\t32. Number guesser")
    print("\t33. Rock, Paper, Scissors\n")

    # Getting the target number
    while answer not in correct_values:
        print("Exit possible with number 99!")
        answer = input("Part you would like to acces (0-99): ")
    clear_terminal()

    # if the user chooses to exit the program
    if answer == "99":
        exit()

    return int(answer)


# prompts the user if he wants to play another round
def another_round():
    answer = input("Do you want to play another round (y/n)? ").strip().lower()
    if answer[0] == "n":
        return False
    else:
        return True


# prompts the user for the length of the password
def get_length():
    # variables
    got = True
    length = ""

    while got:
        length = input("How long should the password be (min. 8)? ")
        try:
            length = int(length)
            got = False
        except ValueError:
            print("There has been an error with the input, try again.")

    if length < 8 or length > 100:
        length = 8

    return length


def clear_terminal():
    # Check the OS
    if platform_system() == "Windows":
        os_system('cls')  # Clear command for Windows
    else:
        os_system('clear')  # Clear command for Unix/Linux/Mac


def get_key():
    flag = True
    while flag:
        try:
            str = int(input("Which key would you like to use (0-999)? "))
            flag = False
        except ValueError:
            print("The input was not a correct value.")

    return str

def get_string():
    # variables
    got = True
    length = ""

    while got:
        length = input("How long should the string of the typewriter be (1-99)? ")
        try:
            length = int(length)
            got = False
        except ValueError:
            print("There has been an error with the input, try again.")

    if length < 1 or length > 100:
        length = 10

    return length


def get_file(file_name):
    # variables
    lines = []

    # read the entire file
    with open(file_name) as file:
        read = reader(file)
        for row in read:
            lines.append(row)
    return lines


def write_file(lines, file_name):
    with open(file_name, "w") as file:
        write = writer(file)
        for i in range(len(lines)):
            write.writerow(lines[i])

def get_item():
    correct_items = set(["r", "p", "s"])
    while True:
        item = input("Rock, paper or scissors? ").strip().lower()
        if item[0] in correct_items:
            return item[0]


if __name__ == "__main__":
    main()
