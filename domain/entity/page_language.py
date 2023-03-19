from graphene import ObjectType, String, JSONString, Int

from domain.main.exceptions.page.empty_title_exception import EmptyTitleException


class PageLanguage(ObjectType):
    pk = Int()
    title = String()
    description = String()
    metadata = JSONString()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__validate_fields()

    def __validate_fields(self):
        self.__is_empty_title()

    def __is_empty_title(self):
        if not self.title:
            raise EmptyTitleException()
