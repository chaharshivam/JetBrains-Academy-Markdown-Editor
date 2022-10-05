import sys

available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line',
                        'ordered-list', 'unordered-list']
special_commands = ['!help', '!done']
complete_text = ""


def display_help():
    print("Available formatters: ", end="")
    for formatter in available_formatters:
        print(formatter, end=" ")
    print()
    print("Special commands: ", end="")
    for commands in special_commands:
        print(commands, end=" ")
    print()


def done_exit():
    return True


# All formatters

def plain():
    text = input("Text: ")
    return text


def bold():
    text = input("Text: ")
    modified_text = "**" + text + "**"
    return modified_text


def italic():
    text = input("Text: ")
    modified_text = "*" + text + "*"
    return modified_text


def inline_code():
    text = input("Text: ")
    modified_text = "`" + text + "`"
    return modified_text


def link():
    label = input("Label: ")
    url = input("URL: ")
    modified_text = "[{}]({})".format(label, url)
    return modified_text


def header():
    while True:
        level = int(input("Level: "))
        if 1 <= level <= 6:
            text = input("Text: ")
            num_of_hashtags = "#" * level
            modified_text = "{} {}\n".format(num_of_hashtags, text)
            return modified_text
        else:
            print("The level should be within the range of 1 to 6")


def new_line():
    return "\n"


def ordered_list():
    while True:
        num_rows = int(input("Number of rows: "))
        if num_rows > 0:
            modified_text = ""
            for i in range(1, num_rows+1):
                text = input("Row #{}: ".format(i))
                modified_text += "{}. {}\n".format(i, text)
            return modified_text
        else:
            print("The number of rows should be greater than zero")
            continue


def unordered_list():
    while True:
        num_rows = int(input("Number of rows: "))
        if num_rows > 0:
            modified_text = ""
            for i in range(1, num_rows + 1):
                text = input("Row #{}: ".format(i))
                modified_text += "* {}\n".format(text)
            return modified_text
        else:
            print("The number of rows should be greater than zero")
            continue


while True:
    user_formatter = input("Choose a formatter: ")
    if user_formatter not in available_formatters and user_formatter not in special_commands:
        print("Unknown formatting type or command")
        continue
    elif user_formatter == "!help":
        display_help()
    elif user_formatter == "!done":
        done_exit_called = done_exit()
        if done_exit_called:
            break
    elif user_formatter == "plain":
        complete_text += plain()
    elif user_formatter == "bold":
        complete_text += bold()
    elif user_formatter == "italic":
        complete_text += italic()
    elif user_formatter == "inline-code":
        complete_text += inline_code()
    elif user_formatter == "link":
        complete_text += link()
    elif user_formatter == "header":
        complete_text += header()
    elif user_formatter == "new-line":
        complete_text += new_line()
    elif user_formatter == "ordered-list":
        complete_text += ordered_list()
    elif user_formatter == "unordered-list":
        complete_text += unordered_list()
    print(complete_text)

