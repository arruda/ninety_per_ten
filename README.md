# Ninety Per Ten
Project requested by @annanda to help keep track of her food habits.

# Install
Prepare venv:
```shell
$ pipenv --two
```

Cython has to be installed before everything, or else installation will break.

```shell
$ pipenv install Cython==0.25.2
```

Then, install everything:
```shell
$ pipenv install
```

# Building app
**PS:** Might be necessary to start adb server as root before, e.g.:

```shell
$ sudo /home/myuser/.buildozer/android/platform/android-sdk-20/platform-tools/adb start-server
```
Run:

```shell
$ buildozer android debug deploy
```

# Publishing
Run:
```shell
$ buildozer android release
```

# LICENSE
Software under MIT license. See LICENSE file for more details.
