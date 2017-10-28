# Ninety Per Ten
Project requested by [@annanda](https://github.com/annanda) to help keep track of her food habits.

# Install
You need to have pipenv installed. To install run (outside of any virtual environment)
```
pip install pipenv
```

Prepare venv (only Python 2 is supported):
```shell
$ pipenv --two
```

Cython has to be installed before any other requirement, or else installation will break.

```shell
$ pipenv install Cython==0.25.2
```

Then, install everything:
```shell
$ pipenv install
```

You can verify if Buildozer is really installed inside the virtualenv, running:
```
pipenv run pip freeze
```

# You need to put your android device in developer mode and USB debugging mode (google it to know how to do it).

# Building app
**PS:** Might be necessary to start adb server as root before, BUT it not be necessary!! Don't try this step if you didn't face this error.

```shell
$ sudo /home/$USER/.buildozer/android/platform/android-sdk-20/platform-tools/adb start-server
```
Run:

```shell
$ buildozer android debug deploy
```

One dialog window will appear in you android device, you need to accept it.

# Publishing
Run:
```shell
$ buildozer android release
```

# LICENSE
Software under MIT license. See LICENSE file for more details.
