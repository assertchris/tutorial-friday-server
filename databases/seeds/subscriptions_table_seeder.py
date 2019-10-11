from config.database import DB
from faker import Faker
from orator.seeds import Seeder


class SubscriptionsTableSeeder(Seeder):
    def run(self):
        fake = Faker()

        DB.table('subscriptions').insert({
            'url': fake.uri(),
            'title': fake.sentence(),
        })
