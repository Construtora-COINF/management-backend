from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "notification" (
            "id" SERIAL NOT NULL PRIMARY KEY,
            "uuid" VARCHAR(32) NOT NULL,
            "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
            "type" VARCHAR(100) NOT NULL,
            "ip_address" VARCHAR(100) NOT NULL,
            "payload" JSONB
        );"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "notification";"""
