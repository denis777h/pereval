def get_level_list():

    level_list = [
        ('1a', '1A'),
        ('1b', '1Б'),
        ('2a', '2А'),
        ('2b', '2Б'),
        ('3a', '3А'),
        ('3b', '3Б'),
        ('4a', '4А'),
        ('4b', '4Б'),
        ('5a', '5А'),
        ('5b', '5Б'),
    ]

    return level_list


def get_status_list():

    status_list = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    return status_list


def get_new_status():
    new_status = (
        ('Active', 'Active'),
        ('Deactivated', 'Deactivated')
    )

    return new_status