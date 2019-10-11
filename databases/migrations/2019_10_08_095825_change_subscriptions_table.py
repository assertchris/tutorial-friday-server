from orator.migrations import Migration


class ChangeSubscriptionsTable(Migration):
    def up(self):
        with self.schema.table('subscriptions') as table:
            table.string('title', 200).change()

    def down(self):
        with self.schema.table('subscriptions') as table:
            table.string('title').change()
