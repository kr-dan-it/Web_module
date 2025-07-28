import functools
import time
import datetime
import random

# def greet(name):
#     return f"Hello, {name}"
#
# def say_bye(name):
#     return f"Goodbye, {name}"
#
# my_function = greet
#
# def call_function(func, arg):
#     return func(arg)
#
# # print(call_function(my_function, "Ann"))
# # print(call_function(say_bye, "Ann"))
#
# def get_func(name_func):
#     if name_func == "sum":
#         return sum
#     elif name_func == "len":
#         return len
#
# # print(get_func("len")("cinema"))
#
# list_func = [sum, len, range]
#
# # print(list(list_func[2](5)))
#
# dict_funct = {
#     "sum": sum,
#     "len": len,
#     "range": range
# }
#
# def outer_function(message):
#     def inner_function():
#         print(message)
#     return inner_function
#
# hello_func = outer_function("Hello world")
# bye_func = outer_function("Bye world")
# karolinas_function = outer_function("My day was great!")
#
# hello_func()
# bye_func()
# karolinas_function()

# @decorators
# def func():
#     pass

# def my_decorator(func):
#     def wrapper():
#         print("Wrapper before function.")
#         func()
#         print("Wrapper after function.")
#     return wrapper
#
# def say_hello():
#     print("Hello world")
#
# # # manually
# # say_hello = my_decorator(say_hello)
# # say_hello()
#
# # auto
# @my_decorator
# def say_hello():
#     print("Hello world")
#
# say_hello()

# def decorator_with_arg(command):
#     """Dec params"""
#     init_dict = {}
#     def actual_decorator(func):
#         """Actual decorator"""
#         @functools.wraps(func)
#         def wrapper():
#             """Wrapper"""
#             # print(f"Decorator take arguments: {arg1}, {arg2}")
#             init_dict[command] = func
#             # func()
#         return wrapper
#     return actual_decorator
#
# @decorator_with_arg(command="start")
# def my_func():
#     """Main func"""
#     print("Function is done!")
#     # print(args)
#     # print(kwargs)
#
# # my_func()
#
# print(my_func.__name__)
# print(my_func.__doc__)
#
# def simple_logger_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Call function: {func.__name__}.")
#         result = func(*args, **kwargs)
#         print(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Function: {func.__name__} ended.")
#         return result
#     return wrapper
#
# @simple_logger_decorator
# def add_number(digit1, digit2):
#     print(f"Add two digits: {digit1} + {digit2}")
#     return digit1 + digit2
#
# @simple_logger_decorator
# def sub_number(digit1, digit2):
#     print(f"Subtract two digits: {digit1} - {digit2}")
#     return digit1 - digit2
#
# print(add_number(37, 73))
# print(30 * "-")
# print(sub_number(102, 45))

# user_roles = ["admin", "user"]
# current_role = ["user"]
#
# def role_required(role):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if role in current_role:
#                 result = func(*args, **kwargs)
#                 print(f"Access approved for {func.__name__}. Role: {role}")
#                 return result
#             else:
#                 print(f"Access denied for {func.__name__}. Needs role: {role}")
#                 return None
#         return wrapper
#     return decorator
#
# @role_required("admin")
# def delete_user(user_id):
#     """Deletes user from userbase"""
#     print(f"User [{user_id}] was deleted successfully.")
#     return True
#
# @role_required("user")
# def view_profile(user_id):
#     """Views profile of user"""
#     print(f"Current user look on profile: {user_id}")
#     return True
#
# delete_user(777)
# view_profile(13)
# current_role.append("admin")
# delete_user(876)
# view_profile(111)
#

class TelegramBot:
    _BOT_COMMANDS = {}

    def command(self, command_name):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[{datetime.datetime.now().strftime("%H:%M:%S")}] Call command: /{command_name}")
                return func(*args, **kwargs)

            self._BOT_COMMANDS[command_name] = wrapper
            print(f"Command is registered /{command_name}")
            return wrapper

        return decorator

    def is_command(self, message):
        return message.startswith("/")

    def process_messages(self, message):

        if self.is_command(message):
            command = message.split(" ")[0][1:]

            if command in self._BOT_COMMANDS:
                message_text = " ".join(message.split(" ")[1:])
                print(f"Command processing [{command}]")
                return self._BOT_COMMANDS[command](message_text)
            else:
                print(f"Not cached command {command}")
                return "Command not defined"
        else:
            print("Not a command")
            return message

bot = TelegramBot()

@bot.command("start")
def handle_start(message):
    return "Hello, it's message from start"

@bot.command("help")
def handle_help(message):
    return "Commands: /help, /start"

print(bot.process_messages("/help Help me"))
print(bot.process_messages("/start Init message"))
print(bot.process_messages("Random message for echo"))