![logo](https://dl1.cbsistatic.com/i/r/2018/06/11/226a1c00-6ce2-4986-aa05-4f275fdb8e69/thumbnail/64x64/220c0e478df6797cf12198ea696fb074/imgingest-873298016181467337.png) Easy TensorFlow CNN
===========
Poster for the [IPT event](https://ipt.acm.org/) March 2019 held by the [ACM-W](https://women.acm.org/) at [FIC-UDC (A Coruña)](https://www.fic.udc.es/)

## What's this?
A simple and easy CNN implementation which classifies between dogs and cats through Deep Learning techniques.

## What do we use?
* Python
* TensorFlow
* Keras

## Useful commands (Windows only)
1. Download [Python](https://www.python.org/downloads/windows/) and install it adding *pip* to your ```%PATH%``` environmental variable
2. Make sure you're running the latest version of pip
```
python -m pip install --upgrade pip
```
3. Install the TensorFlow *pip* dependencies
```
pip3 install six numpy wheel
pip3 install keras_applications==1.0.6 --no-deps
pip3 install keras_preprocessing==1.0.5 --no-deps
```
4. Install [Bazel](https://docs.bazel.build/versions/master/install-windows.html) and set it up to build C++
5. Then run this on the MSYS2 shell
```
pacman -Syu
pacman -Su
pacman -S git patch unzip
```
6. Install [Visual C++ Build Tools 2015](https://visualstudio.microsoft.com/es/vs/older-downloads/?rr=https%3A%2F%2Fwww.tensorflow.org%2Finstall%2Fsource_windows)
* Microsoft Visual C++ 2015 Redistributable Update 3
* Microsoft Build Tools 2015 Update 3

## Developers
* [Lucía María Álvarez Crespo](https://github.com/luciamariaalvarezcrespo)
* [Icia Carro Barallobre](https://github.com/IciaCarroBarallobre)

## Licensing
This project is licensed under the MIT License. See [LICENSE](https://github.com/luciamariaalvarezcrespo/poster-ipt-2019/blob/master/LICENSE) for the full license text.

<br>
