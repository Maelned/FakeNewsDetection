from setuptools import find_packages, setup

with open('pyproject.toml') as f:
    import toml
    pyproject_data = toml.load(f)
    version = pyproject_data['tool']['poetry']['version']
    description = pyproject_data['tool']['poetry']['description']
    long_description = pyproject_data['tool']['poetry'].get('readme', '')

# Load the dependencies
install_requires = []
for dep in pyproject_data['tool']['poetry']['dependencies']:
    if dep != 'python':
        install_requires.append(dep)

setup(
    name='fakenewsdetection',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'fetch_news=src. news_api:main',
            'train_model=src.train_model:main',
            'predict=src.predict:main',
        ],
    },
    author='Maël Nedellec',
    author_email='mael.nedlc@gmail.com',
    description='Train a ML Model that will classify fake news based on historical news. Fetch news from a news API and classify them as fake or real.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Maelned/FakeNewsDetection',  # Update with your GitHub repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)
