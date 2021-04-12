from celery import current_app
from celery.task import task
from celery.utils.log import get_logger

from domain.contents import models


logger = get_logger(__name__)


@task(name='update_page_jsonfield', ignore_result=True)
def update_page_jsonfield(translation_id):
    """

    """
    try:
        page_translation = models.PageLanguage.objects.get(pk=translation_id)
        logger.debug(f'Found translation {page_translation}')
        page_translation.metadata = {
            'test': 'SUCCESS'
        }
        page_translation.save(run_tasks=False, update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving translation: \n{e}')

