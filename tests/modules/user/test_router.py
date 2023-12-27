from fastapi import status

END_POINT = "/users/"


def test_router_get_users_should_be_return_200_when_get_all_users(
    test_app_with_db, access_token, registered_user_db
):
    response = test_app_with_db.get(END_POINT, headers=access_token)
    assert response.status_code == status.HTTP_200_OK


def test_router_user_create_should_be_return_201_when_post_user(
    test_app_with_db, user_post_fake_dict, access_token
):
    response = test_app_with_db.post(
        END_POINT, json=user_post_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_router_user_create_should_be_return_400_when_post_user(
    test_app_with_db, user_post_fake_dict, access_token
):
    response_new_user = test_app_with_db.post(
        END_POINT, json=user_post_fake_dict, headers=access_token
    )
    assert response_new_user.status_code == status.HTTP_201_CREATED

    response = test_app_with_db.post(
        END_POINT, json=user_post_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_login_user_should_be_return_400_when_payload_invalid(
    test_app_with_db, user_login_fake_dict, access_token
):
    response = test_app_with_db.post(
        f"{END_POINT}login", json=user_login_fake_dict, headers=access_token
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
