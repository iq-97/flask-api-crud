from app.migrations.db_migration import meta
from app.config.connection import engine


try:
    meta.create_all(engine)
    print('Migrado correctamente')
except Exception as e:
    print(f"Se dio el siguiente error: {e!r}")