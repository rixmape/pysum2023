def show_count(count, word):
    """Returns a string representation of the count and a singular or plural
    word, depending on the count.

    Args:
        count (int): The count to be included in the string.
        word (str): The word to be used, singular or plural, based on the count.

    Returns:
        str: The resulting string representation of the count and word.

    Example:
        >>> show_count(1, 'part')
        '1 part'
        >>> show_count(2, 'part')
        '2 parts'
        >>> show_count(0, 'part')
        'no parts'
    """
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'


def format_duration(seconds: int):
    """Returns a formatted string representing a duration in hours, minutes,
    and seconds.

    Args:
        seconds (int): The duration in seconds.

    Returns:
        str: The formatted string representation of the duration.

    Example:
        >>> format_duration(3661)
        '1 hour, 1 minute, 1 second'
        >>> format_duration(120)
        '2 minutes'
        >>> format_duration(7200)
        '2 hours'
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    parts = []
    if hours > 0:
        parts.append(f'{hours} {"hour" if hours == 1 else "hours"}')
    if minutes > 0:
        parts.append(f'{minutes} {"minute" if minutes == 1 else "minutes"}')
    if remaining_seconds > 0:
        parts.append(
            f'{remaining_seconds} {"second" if remaining_seconds == 1 else "seconds"}'
        )

    return ', '.join(parts)
