from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser



class SuperUserCreationTests(TestCase):
    def test_create_superuser_test(self):
        User = get_user_model()

        email = "amama@gmail.com"
        password = "alizamani!123"
        admin_user = User.objects.create_superuser(
            email = email,
            password = password
        )


        self.assertEqual(admin_user.email,email)
        self.assertTrue(admin_user.check_password(password))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


    def test_create_superuser_without_is_staff(self):
            User =  get_user_model()
            with self.assertRaises(ValueError):
                User.objects.create_superuser(
                email='admin_fail@example.com',
                password='password123',
                is_staff=False # Intentional Error
            )
