"""


"""


def validate_user_input(url, count):
    """

    :param url:
    :param count:
    :return:
    """
    err_msg = ''
    if 'www.youtube.com/' not in url:
        err_msg = "URL provided in not valid!"
        return False, err_msg
    elif count > 50:
        err_msg = "View count exceeding the limit!"
        return False, err_msg
    else:
        return True, err_msg
