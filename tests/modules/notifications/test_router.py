from fastapi import status

END_POINT = "/notifications/"


def test_router_notification_email_first_contact_should_be_return_200(
    test_app_with_db, mock_monkey_patch, send_email_first_contact_fake_dict
):
    response = test_app_with_db.post(
        f"{END_POINT}email/first-contact/",
        json=send_email_first_contact_fake_dict,
    )
    assert response.status_code == status.HTTP_200_OK


def test_router_notification_email_first_contact_should_be_return_400(
    test_app_with_db, mock_monkey_patch, send_email_first_contact_fake_dict
):
    response_send = test_app_with_db.post(
        f"{END_POINT}email/first-contact/",
        json=send_email_first_contact_fake_dict,
    )
    assert response_send.status_code == status.HTTP_200_OK

    response = test_app_with_db.post(
        f"{END_POINT}email/first-contact/",
        json=send_email_first_contact_fake_dict,
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
