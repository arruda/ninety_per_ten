# Ninety Per Ten

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

### Building app
**OBS:** Might be necessary to start adb server as root before, ex:
`sudo /home/myuser/.buildozer/android/platform/android-sdk-20/platform-tools/adb start-server`

`buildozer android debug deploy`

## Publishing
`buildozer android release`

# LICENSE
Software under MIT license. See LICENSE file for more details.
