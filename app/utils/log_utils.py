import logging
from typing import Callable
from functools import wraps
from .time_utils import current_time
from inspect import iscoroutinefunction

logger = logging.getLogger(__name__)


# logging decorator
def detailed_logging(logging_path: str):
    def internal_logger(func: Callable):
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            logger.info(
                f"{current_time()} {logging_path} call against {func.__name__} with:"
                f"Argument:{args} "
                f"Keyword argument:{kwargs}"
            )
            try:
                result = func(*args, **kwargs)
                logger.info(
                    f"{current_time()} {logging_path} call against {func.__name__} with:"
                    f"Result:{result}"
                )
                return result
            except Exception as e:
                logger.error(
                    f"{current_time()} {logging_path} Exception raised in {func.__name__}. exception {str(e)}"
                )
                raise e

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            logger.info(
                f"{current_time()} {logging_path} call against {func.__name__} with:"
                f"Argument:{args} "
                f"Keyword argument:{kwargs}"
            )
            try:
                result = func(*args, **kwargs)
                logger.info(
                    f"{current_time()} {logging_path} call against {func.__name__} with:"
                    f"Result:{result}"
                )
                return result
            except Exception as e:
                logger.error(
                    f"{current_time()} {logging_path} Exception raised in {func.__name__}. exception {str(e)}"
                )
                raise e

        if iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return internal_logger
