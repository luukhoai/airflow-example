import airflow
from airflow import models, settings

from airflow.contrib.auth.backends.password_auth import PasswordUser

user = PasswordUser(models.User())
user.username = 'silverlight'
user.email = 'silverlight@gmail.com'
user.password = 'k1h2o3a4i5'

session = settings.Session()
session.add(user)
session.commit()
session.close()
