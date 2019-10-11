from orator.migrations import Migration


class AddFavoriteToSubscriptionsTable(Migration):
    def up(self):
        with self.schema.table('subscriptions') as table:
            table.boolean('favorite').index()

    def down(self):
        with self.schema.table('subscriptions') as table:
            table.drop_column('favorite')
