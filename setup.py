from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mashood-neural-snr",
    version="0.1.4",
    author="Muhammad Mashood Awan",
    author_email="mashoodawan27@gmail.com",
    description="Blind SNR estimation using DeepFilterNet. Includes bundled model weights.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mashoodAwan/mashood-neural-snr",
    
    # This automatically finds packages
    packages=find_packages(),
    
    # CRITICAL FIX: Explicitly include the model data
    include_package_data=True,
    
    # CRITICAL FIX: Modern License Definition
    license="MIT",
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
    ],
    python_requires='>=3.8',
    install_requires=[
        "torch==2.0.1",
        "torchaudio==2.0.2",
        "numpy",
        "scipy",
        "pandas",
        "deepfilternet",
        "soundfile",
        "tqdm",
        "loguru",
    ],
)