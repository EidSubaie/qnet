from setuptools import setup, find_packages

setup(
    name="qnet",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "networkx",
        "matplotlib",
        "cython",
        "pytest",
    ],
    include_package_data=True,
    description="Quantum Network Simulation Framework",
    url="https://github.com/qbits/qnet",  # Update with the correct URL if necessary
    author="Qbits",
    author_email="contact@qbitsest.com",
    license="MIT",
)
