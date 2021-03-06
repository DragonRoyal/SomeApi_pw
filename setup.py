from distutils.core import setup
setup(
  name = 'someapi_wrapper',         # How you named your package folder (MyLib)
  packages = ['someapi_wrapper'],   # Chose the same as "name"
  version = '0.45',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Light weight official wrapper of SomeApi in python',   # Give a short description about your library
  author = 'DragonRoyal',                   # Type in your name
  author_email = 'aarav.singhania50@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/DragonRoyal/SomeApi_pw',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/DragonRoyal/SomeApi_pw/archive/refs/tags/V_0.45.tar.gz',    # I explain this later on
  keywords = ['SomeApi', 'Api', 'Image Api'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'aiohttp',
       
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
