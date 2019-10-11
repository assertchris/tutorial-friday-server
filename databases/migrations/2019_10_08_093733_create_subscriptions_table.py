from orator.migrations import Migration


class CreateSubscriptionsTable(Migration):
    def up(self):
        with self.schema.create('subscriptions') as table:
            table.increments('id')
            table.string('url')
            table.string('title')
            table.timestamps()

    def down(self):
        self.schema.drop('subscriptions')
