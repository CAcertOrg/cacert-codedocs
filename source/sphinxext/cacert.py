# -*- python -*-
# This module provides the following project specific sphinx directives
#
# sourcefile

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx import addnodes, roles
from sphinx.util.nodes import make_refnode, set_source_info

_SOURCEFILES = 'cacert_sourcefiles'

__version__ = '0.1.0'


# noinspection PyPep8Naming
class sourcefile_node(nodes.Structural, nodes.Element):
    pass


def file_list(argument):
    if argument is None:
        return []
    else:
        file_names = [s.strip() for s in argument.splitlines()]
        return file_names


class SourceFileRole(roles.XRefRole):
    def __init__(self, fix_parens=False, lowercase=False, nodeclass=None,
                 warn_dangling=True):
        super().__init__(fix_parens, lowercase, nodeclass, nodes.literal,
                         warn_dangling)

    def process_link(self, env, refnode, has_explicit_title, title, target):
        return title, 'sourcefile-{}'.format(nodes.make_id(target))

    def result_nodes(self, document, env, node, is_ref):
        try:
            indexnode = addnodes.index()
            targetid = 'index-%s' % env.new_serialno('index')
            targetnode = nodes.target('', '', ids=[targetid])
            doctitle = list(document.traverse(nodes.title))[0].astext()
            idxtext = "%s; %s" % (node.astext(), doctitle)
            idxtext2 = "%s; %s" % ('sourcefile', node.astext())
            indexnode['entries'] = [
                ('single', idxtext, targetid, '', None),
                ('single', idxtext2, targetid, '', None),
            ]
            return [indexnode, targetnode, node], []
        except KeyError as e:
            return [node], [e.args[0]]


def _source_file_info(env):
    if not hasattr(env, _SOURCEFILES):
        env.cacert_sourcefiles = {}
    return env.cacert_sourcefiles


class SourceFile(Directive):
    """
    A sourcefile entry in the form of an admonition.
    """

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'uses': file_list,
        'links': file_list,
    }

    def run(self):
        env = self.state.document.settings.env

        file_name = self.arguments[0]

        target_id = 'sourcefile-{}'.format(nodes.make_id(file_name))
        section = nodes.section(ids=[target_id])

        section += nodes.title(text=file_name)

        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)

        node = sourcefile_node()
        node.attributes['file_name'] = file_name
        node += section

        _source_file_info(env)[file_name] = {
            'docname': env.docname,
            'lineno': self.lineno,
            'target_id': target_id,
            'uses': self.options.get('uses', []),
            'links': self.options.get('links', [])
        }

        node += par
        set_source_info(self, node)

        return [node]


def _get_sourcefile_index_text(place_info):
    return "Source file; {}".format(place_info['filename'])


def by_filename(item):
    return item[2].lower()


def _add_reference_list(node, title, target_list, fromdocname, app):
    if target_list:
        para = nodes.paragraph()
        para += nodes.emphasis(text=title)
        items = nodes.bullet_list()
        para += items
        for item in sorted(target_list, key=by_filename):
            list_item = nodes.list_item()
            items += list_item
            refnode = nodes.reference('', '')
            innernode = nodes.literal(text=item[2])
            refnode['refdocname'] = item[0]
            refnode['refuri'] = "{}#{}".format(
                app.builder.get_relative_uri(fromdocname, item[0]),
                item[1])
            refnode += innernode
            refpara = nodes.paragraph()
            refpara += refnode
            list_item += refpara
        node.insert(-1, para)


def process_sourcefiles(app, doctree):
    env = app.builder.env

    source_file_info = _source_file_info(env)
    for node in doctree.traverse(sourcefile_node):
        file_name = node.attributes['file_name']
        info = source_file_info[file_name]
        outgoing_uses = [
            (item['docname'], item['target_id'], use)
            for item, use in [
                (source_file_info[use], use)
                for use in source_file_info[file_name]['uses']
                if use in source_file_info]]
        outgoing_links = [
            (item['docname'], item['target_id'], link)
            for item, link in [
                (source_file_info[link], link)
                for link in source_file_info[file_name]['links']
                if link in source_file_info]]
        incoming_uses = [
            (value['docname'], value['target_id'], key)
            for key, value in source_file_info.items()
            if file_name in value['uses']]
        incoming_links = [
            (value['docname'], value['target_id'], key)
            for key, value in source_file_info.items()
            if file_name in value['links']]
        _add_reference_list(
            node, 'Uses', outgoing_uses, env.docname, app) 
        _add_reference_list(
            node, 'Links to', outgoing_links, env.docname, app)
        _add_reference_list(
            node, 'Used by', incoming_uses, env.docname, app)
        _add_reference_list(
            node, 'Linked from', incoming_links, env.docname, app)


def resolve_missing_references(app, env, node, contnode):
    if node['reftype'] == 'sourcefile':
        target = [
            value for value in _source_file_info(env).values()
            if value['target_id'] == node['reftarget']]
        if len(target) == 1:
            return make_refnode(
                app.builder, node['refdoc'], target[0]['docname'],
                node['reftarget'], contnode)


def purge_sourcefiles(app, env, docname):
    if not hasattr(env, 'cacert_sourcefiles'):
        return
    env.cacert_sourcefiles = dict([
        (key, value) for key, value in env.cacert_sourcefiles.items()
        if value['docname'] != docname])


def visit_sourcefile_node(self, node):
    self.visit_admonition(node)


def depart_sourcefile_node(self, node):
    self.depart_admonition(node)


def setup(app):
    app.add_node(
        sourcefile_node,
        html=(visit_sourcefile_node, depart_sourcefile_node))

    app.add_role('sourcefile', SourceFileRole())

    app.add_directive('sourcefile', SourceFile)

    app.connect('doctree-read', process_sourcefiles)
    app.connect('missing-reference', resolve_missing_references)
    app.connect('env-purge-doc', purge_sourcefiles)

    return {'version': __version__}
