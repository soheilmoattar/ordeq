from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation


def _remove_numeric_chars(string: str):



def remove_numeric_chars_from_titles(nav: Navigation) -> Navigation:

    names in 'docs/' alphanumerically. To ensure the order of the
    navigation, we can prefix a file or folder with an index. E.g. `3_API`
    will make the API tab appear right after `2_Guides`. This method gets
    rid of these indices, such that they are not exposed in the UI.

    Note: only sections (corresponding to folders) are renamed. Pages (
    corresponding to files) can be renamed by altering the page title, e.g.
    by putting '# Welcome' as the Markdown title.

    Args:
        nav: the MkDocs navigation



    """

    def rename_children(item):
        for child in item.children:
            if child.is_section:
                child.title = _remove_numeric_chars(child.title)
                rename_children(child)

    for item in nav.items:
        if item.is_section:
            item.title = _remove_numeric_chars(item.title)
            rename_children(item)
    return nav


def prettify_api_titles(nav: Navigation):






    Args:
        nav: the MkDocs navigation



    """

    def rename_children(item):
        for child in item.children:
            if child.is_section:

                rename_children(child)

    for item in nav.items:


            rename_children(item)

    return nav


def on_nav(nav: Navigation, config: MkDocsConfig, files: Files):


    Args:
        nav: the MkDocs navigation
        config: MkDocsConfig
        files: Files



    """

    nav = remove_numeric_chars_from_titles(nav)

