def get_profile(username):
    return {
        "username": username,
        "status": "active"
    }
def update_status(username, new_status):
    return f"Статус {username} изменён на {new_status}"
