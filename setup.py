from setuptools import setup

setup(
    name='fasta-merge',
    version='0.2.0',
    description='FASTA sequence merging tool',
    url='https://github.com/ignasrum/fasta-merge',
    author='Ignas Rumbavicius',
    license='MIT',
    packages=['fasta_merge'],
    python_requires='>=3.8',
    install_requires=['argparse',
                      'pysam'],
    entry_points = {
        'console_scripts': ['fasta-merge=fasta_merge.fasta_merge:main'],
    }
)
