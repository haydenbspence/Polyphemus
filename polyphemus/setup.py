"""
Polyphemus is for use in applications to support observational research.
    Copyright (C) 2023 Hayden Spence

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages

setup(
    name='polyphemus',  # Replace with your package name
    version='0.1.0',  # Your package version
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='A short description of your project',  # Provide a short description
    long_description=open('README.md').read(),  # Long description read from the the readme file
    long_description_content_type='text/markdown',  # Long description content type
    url='https://github.com/haydenbspence/polyphemus',
    packages=find_packages(),  # Automatically find packages in the project directory
    install_requires=[
        'duckdb==0.9.1',
        'fastapi==0.104.1',
        'pydantic==2.4.2',
        'requests==2.31.0',
        'uvicorn==0.24.0.post1'
    ],
    classifiers=[
        # Choose classifiers from https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # Specify the Python version requirements
)
