# setup.py

from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages() + ['features'],
    version='0.1.0',
    description='В рамках исследования "Russia Real Estate2021" мы планируем анализировать динамику цен на недвижимость, факторы влияния на спрос и предложение, а также выявлять перспективные регионы для инвестирования. Будем рассматривать ключевые тренды и изменения в структуре рынка, а также оценивать влияние социоэкономических факторов на его развитие.',
    author='Bobojonov Bahram',
    license='MIT',
    install_requires=[
        'pandas',
    ],
)
