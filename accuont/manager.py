from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, full_name, date_of_birth, adress, user_name, phone, password=None):
        user = self.model(
            full_name=full_name,
            date_of_birth=date_of_birth,
            adress=adress,
            user_name=user_name,
            phone=phone,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, full_name, adress, user_name, phone, password=None):
        user = self.create_user(
            full_name=full_name,
            date_of_birth=None,
            adress=adress,
            user_name=user_name,
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user