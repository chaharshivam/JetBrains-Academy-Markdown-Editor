#TODO Git commit after completing this question
import sys

available_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code',
                         'ordered-list', 'unordered-list', 'new-line']
special_commands = ['!help', '!done']


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