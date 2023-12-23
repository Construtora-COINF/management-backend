from fastapi import APIRouter, Request, status
from app.modules.notifications import schema, usecase

router = APIRouter()


@router.post(
    "/email/first-contact/",
    status_code=status.HTTP_200_OK,
    # response_model=schema.GetNotificationSchema,
    description="This router is to login user",
)
async def send_welcome_email(
    payload: schema.SendEmailFirstContactSchema, request: Request
):
    return await usecase.SendEmailFirstContactUseCase(payload, request).execute()
