# **All In One**
### Video Demo: https://youtu.be/PTMG-o3Yedc
## Description:
> This projects is multiple projects together because I couldn't decide which one I should choose so I just made everything. <br />
> Below you will find the **[table of contents](#table-of-contents)** and a **[tabular view](#tabular-view)** of the project.
> In addition there is a **[checklist](#checklist)** for an overview of the achievements. <br />
> You can find the explanation to the program under **[explanations](#explanations)** if you're interested.
> and of course there will also be **[code documentation](#code-documentation)** with it's own **[table of contents](#table-of-code-contents)**. <br />
> And lastly, if you want to learn more about the **[tests](#tests)**, there is extra documentation for that too.
---

## Table of contents
> 1. **Passwords & security**
>     1. [Password generator](#password-generator)
>     2. [Password strength checker](#password-strength-checker)
>     3. [String comparision](#string-comparison)
>     4. [Word encryption](#word-en--and-decryption)
>     5. [Word decryption](#word-en--and-decryption)
> 2. **Links**
>     1. [Link shortener](#link-shortener)
>     2. [QR code generator](#qr-code-generator)
>     3. [Link checker](#link-checker)
> 3. **Time killers**
>     1. [Typewriter (+ time)](#typewriter)
>     2. [Number guesser (+ highscore)](#number-guesser)
>     3. [Rock, Paper, Scissors (+ tracker)](#rock-paper-scissors)
---

## Tabular view
> | Passwords & Security                                        | Links                                         | Time Killers                                                  |
> |:-----------------------------                               |:----------------------------------------------|:--------------------------------------------------------------|
> | 1. [Password generator](#password-generator)                | 1. [Link shortener](#link-shortener)          | 1. [Typewriter (+ time)](#typewriter)                         |
> | 2. [Password strength checker](#password-strength-checker)  | 2. [QR code generator](#qr-code-generator)    | 2. [Number guesser (+ highscore)](#number-guesser)            |
> | 3. [String comparision](#string-comparison)                 | 3. [Link checker](#link-checker)              | 3. [Rock, Paper, Scissors (+ tracker)](#rock-paper-scissors)  |
> | 4. [Word encryption](#word-en--and-decryption)              |                                               |                                                               |
> | 5. [Word decryption](#word-en--and-decryption)              |                                               |                                                               |
---

## Checklist
> - [x] Markdown
> - [x] Error checking
> - [x] Libraries
> - [x] API's
> - [x] Unit tests
> - [x] File I/O
> - [x] Images
> - [x] Regular Expression
> - [x] Object-Oriented Programming
> - [x] Structured code
---

## Explanations
### Password generator
> The password generator takes 1 argument, the length of the password. <br />
> A password will be created and returned using the python built-in module "secrets"
---
### Password strength checker
> The password strength checker takes 1 argument, the password and returns the strength.  <br />
> There are 4 different strength levels: "weak", "moderate", "strong", "very strong" <br />
> The strength is calculated by adding the characters used like lowercase, uppercase, numbers and special characters. <br />
> Then the log2 of the characters to the power of the length equals the bits (Bits = log2(characters ** length)). <br />
> The levels are then summarised as follows: weak = 0-39, moderate = 40-59, strong = 60-79, very strong = 80+.
---
### String comparison
> The string comparison takes 2 strings and arguments and return wheter they are the same or not. <br />
> This function was implemented to secure users from suspicious websites with wrong URL's. <br />
> An example is: http://www.example.com, http://www.examp1e.com where the second one is from a scammer.
---
### Word en- and decryption
> In this funciton the ASCII value of the word is multiplied with the given key. <br />
> Then it outputs the list, each number representing a character. <br />
> Of course the decryption proccess is the same just with division of the word. <br />
> It might be a simple algorithms but in the early days these worken.  <br />
---
### Link shortener
> This is a funciton using Regular Expression and checking if it's a valid email.  <br />
> If it is the start and the end will be left alone but the website stays the same.
---
### QR code generator
> This is a really simple program for me because I used the "segno" framework.  <br />
> You may pass in a valid link and it generates an image for you.  <br />
> In addition you can change the coulours and the thickness but I chose not to because for other users this would be overwhelming.  <br />
> All I wanted to do is generate a working QR code and it does that by itself.  <br />
> Here is an example of a generated QR code:  <br />
> ![QR Code](example.png)

---
### Link checker
> This was the part that made the most part to code. Not only because I didn't know how to but also everything worked just fine.  <br />
> You pass in a link, it will be sent to the Google Safe Search algorithm and check if it is marked as dangerous.  <br />
> Keep in mind that for this to work you need a valid Safe Search token which you can request on the **[website](https://console.cloud.google.com/apis/)**.  <br />
> In addition, if you want to post your code to GitHub you better make a .gitignore file and in it an .env file.  <br />
> In those files you can store you're own token without it being used for unwanted purposees.
---
### Typewriter
> Here I just wanted to check if I still knew how to read and write a floating point value to a csv file.  <br />
> You are given a random string of characters (as long as you like) and have to type it.  <br />
> The best seconds/characters ratio is kept in a file called "results.csv" and also printed at the end.
---
### Number guesser
> This is a similar program to the rock, paper, scissors and the typewriter.  <br />
> The best score for every digit is kept in the "results.csv" file and will be updated if a new highscore occurs.  <br />
> Here the get_file and write_file function are important, as they allow a smooth reading/writing.
---
### Rock, paper, scissors
> This is just an addition I made because I was bored. You can play the game against a computer and the score is being tracked.  <br />
> Altough this was easy it was still funny and hopefully it can entertain you.  <br />
> Hint: You may change this first value of the third line and therefore chaning your score!
---

## Code documentation
### Table of code contents
> 1. **Classes**
>    1. [Password](#password-class)
>    2. [Link](#link-class)
> 2. **Functions**
>    1. [Main](#main-function)
>    2. [get_file](#get_file-function)
>    3. [write_file](#write_file-function)
>    4. [clear_terminal](#clear_terminal-function)
> 3. **Images**
>    1. [CQ code](#qr-code-image)
> 4. **Imports**
>    1. [Imports](#imports)
> 5. **Tests**
>    1. [Classes](#class-tests)
>    2. [Functions](#function-tests)
---

### Password class
#### Description
> The Password class is a class only containing *classmethods*. <br />
> There is no specific reasons to use OOP in this case but I figuered it would help my understanding of OOP. <br />
> In total there are 6 *classmethods* and 1 *class variable*.

#### Code
```python
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
```
#### Methods
> The methods are like mentioned classmethods and help the reader understand the code faster. <br />
> Therefore the code is more readable and more expandable for fellow programmers
---

### Link class
#### Description
> In this class there are gain mostly *staticmethods* because I wanted to train my OOP. <br />
> The class is used to check links with the **[Google Safe Searching API](https://console.cloud.google.com/apis/)**. <br />
> Another usage would be to shorten the link, which is also possible.

#### Code
```python
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
```

#### Methods
> The methods are used to shorten URL's and check URL's. <br />
> Keep in mind that to use the check method you need to get your own Google API key like mentioned above.
---

### Main function
#### Description
> The main function is mainly used for an infinite loop for the user and to exit when wanted. <br />
> In addition the main funciton takes care of small stuff while the classes have a direct purpose.

#### Code
```python
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
```
---

### get_file function
#### Description
> This function, like the name implies, reads an intire file and returns a lists in a list as lines. <br />
> You may enter the name of the file if you want to use it for yourself but in the name function the filename is hardcoded.

#### Code
```python
def get_file(file_name):
    # variables
    lines = []

    # read the entire file
    with open(file_name) as file:
        read = reader(file)
        for row in read:
            lines.append(row)
    return lines
```
---

### write_file function
#### Description
> This function is like the get_file function, however it takes one more arguments. <br />
> The argument needed is the list of lits to write to. <br />
> This is combined with reding the function, changing one value and writing it. <br />
> It was very useful for the file I/O in the games.

#### Code
```python
def write_file(lines, file_name):
    with open(file_name, "w") as file:
        write = writer(file)
        for i in range(len(lines)):
            write.writerow(lines[i])
```
---

### clear_terminal function
#### Description
> This funtion takes no arguments and, like the name implies, clears the terminal. <br />
> This is done by checking the os system and then sending the correct command.

#### Code
```python
def clear_terminal():
    # Check the OS
    if platform_system() == "Windows":
        os_system('cls')  # Clear command for Windows
    else:
        os_system('clear')  # Clear command for Unix/Linux/Mac
```
---

### QR code Image
#### Description
> This is an image of a QR code and it will send you to the *ASCII table* as an example. <br />
> Here's the image: <br />
![QR Code](example.png)

#### Code
```python
from segno      import make_qr
print("Attention! The link is neither checked nor changed!")
qrcode = make_qr(input("Enter the link of the QR code: "))
qrcode.save("qrcode.png")
```
---

### Imports
#### Description
> With the imports a lot of my own work has been done and I'm gratefule for these frameworks. <br />
> Example usecases: generating QR code, checking suspisious links, reading a token from a secret file, etc. <br />
> Please have a look at the listed below. <br />
> PS: If you are wondering why I always import so specific it's because I don't want any confusion with names. <br />
> Another reason is the storage space, which is also minimalized.

#### Code
```python
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
```
---

### Class tests
#### Description
> In these functions mostly all important functions are tested and this actually helped me a lot. <br />
> Not only did I find some errors but it made me believe more in my code after seeing the tests pass.

#### Code
```python
# check the random function
def test_random():
    for i in range(8, 99):
        assert len(Password.random(i)) == i

# test the strength checker
def test_strength():
    assert Password.strength("weak")                == ("weak", "seconds")
    assert Password.strength("m0derAte")            == ("moderate", "hours")
    assert Password.strength("aA0.aA0.oOl")         == ("strong", "weeks")
    assert Password.strength("tH1sI5Ap@ssw0rD!")    == ("very strong", "years")

# test the link shortener
def test_shortener():
    URL1 = "https://www.deepl.com/en/translator"
    URL2 = "https://obscure-tribble-r46p66g446vcx55r.github.dev/?autoStart=true&folder=%2Fworkspaces%2F149601399&vscodeChannel=stable"
    assert Link.shorten(URL1) == "deepl.com"
    assert Link.shorten(URL2) == "obscure-tribble-r46p66g446vcx55r.github.dev"

# test the link checker
def test_check():
    load_dotenv()
    TOKEN = getenv("TOKEN")
    URL1 = "https://www.deepl.com/en/translator"
    URL2 = "https://www.codecademy.com/resources/docs/python/requests-module"
    URL3 = "https://obscure-tribble-r46p66g446vcx55r.github.dev/?autoStart=true&folder=%2Fworkspaces%2F149601399&vscodeChannel=stable"
    assert Link.check(TOKEN, URL1).json() == {}
    assert Link.check(TOKEN, URL2).json() == {}
    assert Link.check(TOKEN, URL3).json() == {}
```
---

### Function tests
#### Description
> In this function the most important regualar functions are tested. <br />
> Altough I could have made a class I decided not to to not further complicate things <br />
> In this example the "test_resuslts.csv" file is read & written multiple times to insure the functions are working properly.

#### Code
```python
# test the file reader & writer
def test_csv():
    # 1st test - reading
    file_name = "test_results.csv"
    file_lines = [['0', '.', '6', '4', '6', '5', '5', '0', '4', '1', '3', '7', '4', '9', '9', '9', '2'],
                  ['4', '7', '13', '17', '23', '34'],
                  ['8', '6']]
    assert get_file(file_name) == file_lines

    # 2nd test - write & read
    file_lines = [['1', '.', '6', '4', '6', '5', '5', '9', '4', '1', '3', '7', '4', '9', '9', '9', '2'],
                  ['1', '4', '13', '17', '45', '34'],
                  ['8', '9']]
    write_file(file_lines, file_name)
    assert get_file(file_name) == file_lines

    # 3rd test - reverse write & read
    file_lines = [['0', '.', '6', '4', '6', '5', '5', '0', '4', '1', '3', '7', '4', '9', '9', '9', '2'],
                  ['4', '7', '13', '17', '23', '34'],
                  ['8', '6']]
    write_file(file_lines, file_name)
    assert get_file(file_name) == file_lines
```
---
