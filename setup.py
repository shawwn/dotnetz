# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dotnetz', 'dotnetz.System']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.0.1,<5.0.0']

setup_kwargs = {
    'name': 'dotnetz',
    'version': '0.1.4',
    'description': 'An implementation of some .NET patterns in Python',
    'long_description': "# dotnetz\n\n> An implementation of some .NET patterns in Python\n\nWARNING: This repo is in development. It was automatically generated with [mkpylib](https://github.com/shawwn/scrap/blob/master/mkpylib). If you're reading this message, it means that I use this repo for my own purposes right now. It might not do anything at all; the default functionality is `print('TODO')`.\n\nIf you really want to try it out, feel free. I recommend reading through the code and commit history to see if it does what you need, or [ask me](#contact) for status updates.\n\nStay tuned!\n\n## Install\n\n```\npython3 -m pip install -U dotnetz\n```\n\n## Usage\n\n```py\nimport dotnetz\n\nprint('TODO')\n```\n\n## License\n\nMIT\n\n## Contact\n\nA library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!\n\nMy Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.\n\n- Twitter: [@theshawwn](https://twitter.com/theshawwn)\n- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)\n- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)\n- Website: [shawwn.com](https://www.shawwn.com)\n\n",
    'long_description_content_type': 'text/markdown',
    'author': 'Shawn Presser',
    'author_email': 'shawnpresser@gmail.com',
    'url': 'https://github.com/shawwn/dotnetz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
