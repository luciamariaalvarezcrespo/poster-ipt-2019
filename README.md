![logo](https://dl1.cbsistatic.com/i/r/2018/06/11/226a1c00-6ce2-4986-aa05-4f275fdb8e69/thumbnail/64x64/220c0e478df6797cf12198ea696fb074/imgingest-873298016181467337.png) Easy TensorFlow CNN
===========
Poster for the [IPT event](https://ipt.acm.org/) March 2019 held by the [ACM-W](https://women.acm.org/) at [FIC-UDC (A Coruña)](https://www.fic.udc.es/)

## What's this?
A simple and easy CNN implementation which classifies between dogs and cats through Deep Learning techniques.

## What do we use?
* Python
* TensorFlow
* Keras

## Useful commands (Ubuntu only)
1. Install [Python](https://www.python.org/)
```
sudo apt-get install python3
```
2. Install the TensorFlow Python dependencies
```
sudo apt install python3-dev python3-pip 
```
3. Make sure you're running the latest version of pip
```
python -m pip install --upgrade pip
```
4. Install the TensorFlow *pip* dependencies
```
pip install -U --user pip six numpy wheel mock
pip install -U --user keras_applications==1.0.6 --no-deps
pip install -U --user keras_preprocessing==1.0.5 --no-deps
```
5. Install [Bazel](https://docs.bazel.build/versions/master/install-ubuntu.html) dependencies
```
sudo apt-get install pkg-config zip g++ zlib1g-dev unzip
```
6. Download Bazel from [here](https://github.com/bazelbuild/bazel/releases/download/0.23.1/bazel-0.23.1-installer-linux-x86_64.sh)
7. Run the installer
```
chmod +x bazel-0.23.1-installer-linux-x86_64.sh
./bazel-0.23.1-installer-linux-x86_64.sh --user
```
8. Set up your environment
```
export PATH="$PATH:$HOME/bin"
```
9. Install the JDK
```
sudo apt-get install openjdk-8-jdk
```
10. Add Bazel distribution URI as a package source
```
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
```
11. Install and update Bazel
```
sudo apt-get update && sudo apt-get install bazel
sudo apt-get install --only-upgrade bazel
```
12. Download the TensorFlow source code
```
git clone https://github.com/tensorflow/tensorflow.git
cd tensorflow
```
13. Configure the build
```
./configure
```
14. Bazel build
```
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package
```
15. Build the package
```
./bazel-bin/tensorflow/tools/pip_package/build_pip_package --nightly_flag /tmp/tensorflow_pkg
```
16. Install the package
The filename of the generated ```.whl``` file depends on the TensorFlow version and your platform. Use ```pip install``` to install the package, for example:
```
pip install /tmp/tensorflow_pkg/tensorflow-version-tags.whl
```

## Developers
* [Lucía María Álvarez Crespo](https://github.com/luciamariaalvarezcrespo)
* [Icia Carro Barallobre](https://github.com/IciaCarroBarallobre)

## Licensing
This project is licensed under the MIT License. See [LICENSE](https://github.com/luciamariaalvarezcrespo/poster-ipt-2019/blob/master/LICENSE) for the full license text.

<br>
