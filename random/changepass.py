from django.contrib.auth.models import User

from lessonabsentees import settings


settings.configure()
# Replace 'username' with the actual username of the user
user = User.objects.get(username='CB')

# Set the new password
user.set_password('thatone54')

# Save the changes
user.save()
