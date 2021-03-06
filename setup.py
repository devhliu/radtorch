
from setuptools import setup, find_packages


setup(
      name='radtorch',
      version='2020.06.21',
      version_date='2020.06.21',
      description='RADTorch, The Radiology Machine Learning Framework',
      url='https://radtorch.github.io/radtorch/',
      author='Mohamed Elbanan, MD',
      author_email = "https://www.linkedin.com/in/mohamedelbanan/",
      license='MIT',
      packages=find_packages(),
      install_requires=['torch', 'torchvision', 'torchsummary', 'numpy', 'pandas', 'pydicom', 'matplotlib', 'pillow',
                        'tqdm', 'sklearn','pathlib', 'bokeh', 'xgboost', 'seaborn', 'torchsummary', 'efficientnet_pytorch',
                        'xmltodict',
                        'streamlit',
#                         'detectron2 @ git+https://github.com/facebookresearch/detectron2.git#egg=v0.1.3',
#                         'pyyaml>=5.1'
                       ],

      zip_safe=False,
      classifiers=[
      "License :: OSI Approved :: MIT License",
      "Natural Language :: English",
      "Programming Language :: Python :: 3 :: Only",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ]
      )
