from functools import lru_cache

import boto3
from botocore.exceptions import ClientError
from loguru import logger
from app.config.settings import get_settings


@lru_cache()
class AmazonSimpleEmailService:
    __setting = get_settings()
    __aws_access_key_id = __setting.AWS_ACCESS_KEY_ID
    __aws_secret_access_key = __setting.AWS_SECRET_ACCESS_KEY
    _aws_region = __setting.AWS_REGION
    _charset = "UTF-8"
    _config_set = "ConfigSet"

    def __init__(self):
        self._client = self.__init_client_ses()

    def __init_client_ses(self):
        logger.info("Connecting Amazon SES...")
        return boto3.client(
            "ses",
            region_name=self._aws_region,
            aws_access_key_id=self.__aws_access_key_id,
            aws_secret_access_key=self.__aws_secret_access_key,
        )

    async def send_email(
        self,
        from_email: str,
        to_email: str,
        subject: str,
        body_html: bytes,
        body_text: str,
    ):
        try:
            response = self._client.send_email(
                Destination={
                    "ToAddresses": [
                        to_email,
                    ],
                },
                Message={
                    "Subject": {
                        "Charset": self._charset,
                        "Data": subject,
                    },
                    "Body": {
                        "Html": {
                            "Charset": self._charset,
                            "Data": bytes(body_html).decode(self._charset),
                        },
                        "Text": {
                            "Charset": self._charset,
                            "Data": body_text,
                        },
                    },
                },
                Source=from_email,
            )
            logger.info(f"E-mail sent [{response}]")
        except ClientError as e:
            logger.error(f"Error sending e-mail: {e.response['Error']['Message']}")
