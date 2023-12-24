from fastapi import APIRouter, Request, status
from app.modules.notifications import schema, usecase

router = APIRouter()


@router.post(
    "/email/first-contact/",
    status_code=status.HTTP_200_OK,
    response_model=schema.GetSimpleNotificationSchema,
    description="This router is to send first contact email to Coinf.",
)
async def send_welcome_email(
    payload: schema.SendEmailFirstContactSchema, request: Request
):
    return await usecase.SendEmailFirstContactUseCase(payload, request).execute()
