from django.db import models



class User(models.Model):
    username=models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True,blank=True)
    uid = models.UUIDField(primary_key=True, unique=True,editable=False)
    password = models.CharField(max_length=8)
    usertype_choices = (('ADMIN', 'ADMIN'), ('USER', 'USER'))
    usertype = models.CharField(
        max_length=10, choices=usertype_choices, default='USER')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table='users'



class LoginLogs(models.Model):
    user_logged=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    user_type=models.CharField(max_length=10)
    logged_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='login_logs'