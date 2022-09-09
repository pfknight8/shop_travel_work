from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Abstract base user model in order to have a more flexible user type that still utilizes Django's admin.

class UserManager(BaseUserManager):
  def get_by_natural_key(self, username):
    return self.get(username__iexact=username)
    
  def create_user(self, username, email, password, **extra_fields):
    if not email:
      raise ValueError("Must have an email address!")
    elif not username:
      raise ValueError("Must choose a valid username!")
    
    user = self.model(
      username=username,
      email=self.normalize_email(email),
      **extra_fields
    )
    user.set_password(password)
    user.save(using=self.db)
    return user
    
  def create_staffuser(self, username, email, password, **extra_fields):
    user = self.create_user(username, email, password=password, **extra_fields)
    user.staff = True
    user.admin = False
    user.save(using=self._db)
    return user

  def create_superuser(self, username, email, password, **extra_fields):
    user = self.create_user(username, email, password=password, **extra_fields)
    user.staff = True
    user.admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(verbose_name='email address', max_length=100, unique=True)
  active = models.BooleanField(default=True)
  staff = models.BooleanField(default=False)
  admin = models.BooleanField(default=False)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  # passwold is built in, so no need to include here.

  objects = UserManager()

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

  def __str__(self):
    return self.username

  def has_perm(self, perm, obj=None):
    return True

  def has_perms(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True

  def clean(self):
    super().clean()
    self.email=self.__class__.objects.normalize_email(self.email)
    self.username=self.username.lower()

  @property
  def is_staff(self):
    return self.staff

  @property
  def is_admin(self):
    return self.admin

  @property
  def is_active(self):
    return self.active