from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    """
        custom user . each website may have its functionality and field required for this part so we do this
    """
    pass


