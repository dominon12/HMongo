from distutils.core import setup


setup(
  name = 'HMongo',       
  packages = ['HMongo'],   
  version = '0.1',    
  license='cc0-1.0',       
  description = 'Library to easy work with NoSQL database MongoDB',   
  author = 'Dominon12',               
  author_email = 'youneedmax@gmail.com',  
  url = 'https://github.com/dominon12/HMongo',   
  download_url = 'https://github.com/dominon12/HMongo/archive/v_01.tar.gz',    
  keywords = ['database', 'mongo', 'mongodb', 'easy'],   
  install_requires=['pymongo'],
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: Developers',   
    'Topic :: Software Development :: Build Tools',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',  
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)