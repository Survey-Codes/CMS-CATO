from domain.entity.page import Page as PageDomain
from domain.repository.page_repository import PageRepository
from infrastucture.dataaccess.contents.acl.page_acl import PageAcl
from infrastucture.dataaccess.contents.acl.page_language_acl import PageLanguageAcl
from infrastucture.dataaccess.contents.models import Page as PageModel


class PageRepositoryImpl(PageRepository):
    __page_acl = PageAcl()
    __page_language_acl = PageLanguageAcl()

    def select(self, lang: str, slug: str) -> [PageDomain]:
        pages_model = PageModel.objects.filter(slug=slug)
        assert pages_model, "No se encontraron páginas, por favor intenta nuevamente"
        return self.__page_acl.from_models_to_domains(pages_model)

    def select_children_by_pk(self, pk: property) -> [int]:
        children = PageModel.objects.filter(parent__pk=pk)
        return map(lambda child: child.pk, children)
