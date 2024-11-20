from setuptools import setup, find_packages

setup(
    name='git-fusion',  # Replace with your tool's name
    version='1.0.0',
    packages=find_packages(),
    install_requires=["typer"],  # Add dependencies if needed
    entry_points={
        'console_scripts': [
            'git-fusion=package.app:app',  # 'command=module:function'
        ],
    },
    author="MinasFakhori",
    author_email="minas.dev0@gmail.com",
    description="A tool to manage multiple git repositories.",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)