from setuptools import setup

setup(
    name='gpt2pytorch',
    version='0.1',
    packages=['GPT2'],
    package_data={'GPT2': ['encoder.json', 'vocab.bpe']})
