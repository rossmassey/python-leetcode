from docutils import nodes
from docutils.parsers.rst import Directive


class HorizontalLineDirective(Directive):
    has_content = False

    def run(self):
        # Create a node in the document that will be converted to <hr/> in HTML
        node = nodes.raw('', '<hr />', format='html')
        return [node]


def setup(app):
    app.add_directive('line', HorizontalLineDirective)