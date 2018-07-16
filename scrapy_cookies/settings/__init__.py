from contextlib import contextmanager


@contextmanager
def unfreeze_settings(settings):
    original_status = settings.frozen
    settings.frozen = False
    try:
        yield settings
    finally:
        settings.frozen = original_status
