from setuptools import setup, find_packages

setup(
    name='nikreader',
    version='0.1',
    packages=find_packages(where='./'),
    description='Sebuah modul untuk membaca kode NIK pada KTP dan menjadi beberapa bagian.',
    url='https://github.com/wannazid/NIK-Reader',
    author='wannazid',
    author_email='malastech.id@gmail.com',
    license='MIT',
    data_files=[('nikreader', ['nikreader/database.json'])],
    include_package_data=True,
    package_dir={'nikreader': 'nikreader'},
    keywords=['nikreader', 'NIK Ekstraktor', 'Python'],
)
