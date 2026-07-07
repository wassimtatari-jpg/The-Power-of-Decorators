def required_authentication(func):
    def wrapper(*arges,**kwarges):
        if not arges[0].is_authenticaited:
            raise PermissionError("program blocked by owner wassim")
        return func(*arges,**kwarges)
    return wrapper
class user:
    def __init__(self,is_authenticaited):
        self.is_authenticaited=is_authenticaited
    @required_authentication
    def view_profile(self):
        print("you are authenticaiteid")
user1=user(is_authenticaited=True)
user1.view_profile()
user2=user(is_authenticaited=False)
user2.view_profile()


        