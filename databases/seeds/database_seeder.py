from orator.seeds import Seeder
# from .user_table_seeder import UserTableSeeder
from .subscriptions_table_seeder import SubscriptionsTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        # self.call(UserTableSeeder)
        self.call(SubscriptionsTableSeeder)
