# imports
from project    import *
from os         import getenv
from dotenv     import load_dotenv

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
