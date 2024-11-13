import asyncpg

class Database:
    def __init__(self):
        self.connection = None

    async def connect(self):
        self.connection = await asyncpg.connect(
            user='postgres',
            password='postgres',
            database='postgres',
            host='localhost'
        )
        await self._create_table()

    async def _create_table(self):
        await self.connection.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL
            )
        ''')

    async def create_record(self, content):
        record_id = await self.connection.execute('''
            INSERT INTO records (content) VALUES ($1) RETURNING id
        ''', content)
        return record_id

    async def read_record(self, record_id):
        record = await self.connection.fetchrow('SELECT * FROM records WHERE id = $1', record_id)
        return record

    async def update_record(self, record_id, new_content):
        await self.connection.execute('UPDATE records SET content = $1 WHERE id = $2', new_content, record_id)

    async def delete_record(self, record_id):
        await self.connection.execute('DELETE FROM records WHERE id = $1', record_id)

    async def close(self):
        await self.connection.close()

        
     