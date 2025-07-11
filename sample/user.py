class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.logged_in = False

    def login(self) -> None:
        self.logged_in = True

    def logout(self) -> None:
        self.logged_in = False

    def is_logged_in(self) -> bool:
        return self.logged_in

    def update_email(self, new_email: str) -> None:
        if "@" not in new_email:
            raise ValueError("Invalid email address")
        self.email = new_email


# class User:
#     def __init__(self, username: str, email: str):
#         self.username = username
#         self.email = email
#         self.logged_in = False
# 
#     def login(self) -> None:
#         self.logged_in = True
# 
#     def logout(self) -> None:
#         self.logged_in = False
# 
#     def is_logged_in(self) -> bool:
#         return self.logged_in
# 
#     def update_email(self, new_email: str) -> None:
#         if "@" not in new_email:
#             raise ValueError("Invalid email address")
#         self.email = new_email

