try:
	from setuptools import setup, Extension
except ImportError:
	from distutils.core import setup, Extension

setup(
	name='leonLPST',
	version='1.0',
	py_modules=['leonLPST'],

	description=(
		'leonLPST'
	),
	author='Leon Wolf',
	author_email='463691529@qq.com'
)