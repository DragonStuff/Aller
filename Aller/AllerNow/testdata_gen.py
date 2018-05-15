import factory
from . import models

class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = 'John'
    last_name = 'Doe'
    admin = False

class LocationFactory(factory.Factory):
    class Meta:
        model = models.Location

    first_name = 'John'
    last_name = 'Doe'
    admin = False

# Another, different, factory for the same object
class PersonFactory(factory.Factory):
    class Meta:
        model = models.Person

    first_name = 'Admin'
    last_name = 'User'
    
    email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))

    author = factory.SubFactory(UserFactory)

class RandomUserFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
