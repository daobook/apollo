# Configuration file for the Sphinx documentation builder.
#  Sphinx 文档生成器的配置文件。
# 这个文件只包含一些最常用的选项。完整的清单见文档：
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# --  Path 设置  --------------------------------------------------------------

# 如果插件（或用 autodoc 记录的模块）在另一个目录下，
# 在这里将这些目录加入 ``sys.path``。如果目录是相对于文档根目录的，
# 使用 ``os.path.abspath`` 使其成为绝对目录，就像这里所示。
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- 项目信息 -----------------------------------------------------

project = 'Apollo Auto'
copyright = '2021, xinetzone'
author = 'xinetzone'

# 完整版本，包括 alpha/beta/rc 标签
release = 'alpha'

# -- 通用配置 ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#  在这里添加任何 Sphinx 插件模块的名字，以字符串的形式。
# 它们可以是 Sphinx 自带的插件（命名为 ``'sphinx.ext.*'``）或你自定义的。
extensions = [
    'sphinx_rtd_theme',
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinx_inline_tabs",
    'sphinx.ext.autodoc', 
    'sphinx.ext.doctest', 
    'sphinx.ext.todo',
    'sphinx.ext.autosummary', 
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx', 
    'sphinx.ext.viewcode', 
    'sphinx.ext.inheritance_diagram'
]

# 在这里添加任何包含模板的路径，相对于这个目录。
templates_path = ['_templates']

# 由 Sphinx 自动生成的内容的语言。支持的语言列表请参考文档。
#
# 如果你通过 ``gettext`` 目录做内容翻译，也会用到这个。
# 通常你在这些情况下从命令行设置 ``language``。
language = 'zh_CN'

# 相对于源目录的模式列表，在寻找源文件时，匹配的文件和目录会被忽略。
# 这个模式也会影响 html_static_path 和 html_extra_path。
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# --  HTML 输出的选项  -------------------------------------------------

# 用于 HTML 和 HTML 帮助页面的主题。参见文档中的内置主题的列表。
#
html_theme = 'sphinx_rtd_theme'
# =========================
#  主题选项
# =========================
html_theme_options = {
    # 如果指定，Google Analytics 的 `gtag.js`_ 就会包含在你的页面中。
    ## 将该值设置为谷歌提供给你的 ID（如 UA-XXXXXXX 或 G-XXXXXXXXXX）。
    # 'analytics_id': 'G-XXXXXXXXXX',  #  由谷歌在你的仪表板上提供
    # 在谷歌分析中对访问者的 IP 地址进行匿名处理。
    # 'analytics_anonymize_ip': False,
    # 显示 :guilabel:`Next` 和 :guilabel:`Previous` 按钮的位置。
    ## 这可以是 ``bottom``，``top``，``both``，或 ``None``。
    'prev_next_buttons_location': 'bottom',
    'navigation_depth': 1, # 目录深度
    # 在外部链接旁边添加一个图标。
    'style_external_links': False,
    # "改变了使用 ``display_github``, ``display_gitlab`` 等文件时的查看方式。
    ## 当使用 GitHub 或 GitLab 时，这可以是：``blob`` （默认），``edit`` 或 ``raw``。
    ## 在 Bitbucket 上，这可以是 ``view`` （默认）或 ``edit``。
    'vcs_pageview_mode': 'view',
    # 改变导航栏中搜索区域的背景。
    ## 该值可以是任何在 CSS background 属性中有效的东西。
    ## 默认 ``#2980B9``。
    'style_nav_header_background': 'skyblue',
    # 指定导航是否包括隐藏的内容目录
    ##（任何被标记为 ``:hidden:`` 选项的 :rst:dir:`sphinx:toctree` 指令。）。
    'includehidden': False, 
    # 启用后，页面小标题不包括在导航中。
    'titles_only': False
}

# ======================================
# 文件范围的元数据
# ======================================
# 强制 :guilabel:`Edit on GitHub` 按钮使用配置的 URL。
github_url = '' 
# 强制 :guilabel:`Edit on Bitbucket` 按钮使用配置的 URL。
bitbucket_url = '' 
# 强制 :guilabel:`Edit on GitLab` 按钮使用配置的 URL。
gitlab_url = ''

# ----------------------------
# 添加自定义 CSS 或 JavaScript
# ----------------------------
# 相对于这个目录，添加任何包含自定义静态文件（如样式表）的路径，。
## 它们被复制到内置的静态文件之后，
## 所以一个名为 ``default.css`` 的文件将覆盖内置的 ``default.css``。
breathe_projects = {'Cyber RT Documents': 'cyber/doxy-docs/xml'}
templates_path = ['_templates', 'cyber/doxy-docs/_templates']
html_static_path = ['_static']

# ==============================
# 自定义
# ==============================
# root_doc = 'README'
import re

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "substitution",
    "tasklist",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://daobook.github.io/sphinx-locale/', None)
}

# Sphinx document translation with sphinx gettext feature uses these settings:
locale_dirs = ['locale/']
gettext_compact = False

# -- Extension interface -------------------------------------------------------
from sphinx import addnodes  # noqa

event_sig_re = re.compile(r'([a-zA-Z-]+)\s*\((.*)\)')


def parse_event(env, sig, signode):
    m = event_sig_re.match(sig)
    if not m:
        signode += addnodes.desc_name(sig, sig)
        return sig
    name, args = m.groups()
    signode += addnodes.desc_name(name, name)
    plist = addnodes.desc_parameterlist()
    for arg in args.split(','):
        arg = arg.strip()
        plist += addnodes.desc_parameter(arg, arg)
    signode += plist
    return name


def setup(app):
    from sphinx.ext.autodoc import cut_lines
    from sphinx.util.docfields import GroupedField
    app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
    app.add_css_file("cyber/doxy-docs/source/main_stylesheet.css")
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    app.add_object_type('setuptools-confval', 'setuptools-confval',
                        objname='setuptools configuration value',
                        indextemplate='pair: %s; setuptools configuration value')
    fdesc = GroupedField('parameter', label='Parameters',
                         names=['param'], can_collapse=True)
    app.add_object_type('event', 'event', 'pair: %s; event', parse_event,
                        doc_field_types=[fdesc])

    # workaround for RTD
    from sphinx.util import logging
    logger = logging.getLogger(__name__)
    app.info = lambda *args, **kwargs: logger.info(*args, **kwargs)
    app.warn = lambda *args, **kwargs: logger.warning(*args, **kwargs)
    app.debug = lambda *args, **kwargs: logger.debug(*args, **kwargs)

# 缩短链接
extlinks = {
    'daobook': ('https://daobook.github.io', 'daobook'),
    'xinetzone': ('https://xinetzone.github.io', 'xinetzone'),
    'apollo': ('http://apollo.auto', 'apollo'),
    'images': ('http://apollo.auto', 'images'),
    'params': ('http://apollo.auto', 'params'),
}

