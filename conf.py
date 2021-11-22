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
    'furo',
    'breathe',
    "myst_parser",
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
html_theme = 'furo'

# ----------------------------
# 添加自定义 CSS 或 JavaScript
# ----------------------------
# 相对于这个目录，添加任何包含自定义静态文件（如样式表）的路径，。
## 它们被复制到内置的静态文件之后，
## 所以一个名为 ``default.css`` 的文件将覆盖内置的 ``default.css``。
breathe_projects = {'Cyber RT Documents': 'cyber/doxy-docs/xml'}
templates_path = ['_templates', 'cyber/doxy-docs/_templates']
html_static_path = ['_static']
html_css_files = ['cyber/doxy-docs/source/main_stylesheet.css']

# ==============================
# 自定义
# ==============================
# root_doc = 'README'

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
    'python': ('https://daobook.github.io/cpython', None),
    'sphinx': ('https://daobook.github.io/sphinx/', None)
}

# Sphinx document translation with sphinx gettext feature uses these settings:
locale_dirs = ['locales/']
gettext_compact = False

# 缩短链接
extlinks = {
    'daobook': ('https://daobook.github.io', 'daobook'),
    'xinetzone': ('https://xinetzone.github.io', 'xinetzone'),
    'apollo': ('http://apollo.auto', 'apollo'),
    'images': ('http://apollo.auto', 'images'),
    'params': ('http://apollo.auto', 'params'),
}

highlight_language = 'c++'
pygments_style = 'sphinx'
todo_include_todos = False
htmlhelp_basename = 'CyberRTdoc'
