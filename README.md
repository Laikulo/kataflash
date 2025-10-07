# Kataflash

## Synopsis
Kataflash is a repackaging of the flashtool included in [Katapult](https://github.com/Arksine/katapult).

This is intended for power-users to leverage devices with katapult already installed w/o needing to clone the entire repo.

## Status
Work in progres: Pre-alpha.

## Installation

### With pip

It is reccomended to do this in a virtual environment.
```
pip install kataflash
```

### With pipx automatic environment management
```
pipx install kataflash
```

## Usage
Kataflash provides two commands:

### `kataflash`
This is kataflash's main entrypoint. It provides a few quality-of-life improvements over the basic flashtool.

`kataflash` has a number of subcommands:

#### `kataflash version`

Prints the version of kataflash, and the git hash of the embedded katapult flashtook

NOTE: Printing the version of kataflash is not supported yet, and always prints 0.0.0

#### Following __NOT YET IMPLEMENTED__

* `kataflash status` - Print the status of a given device
* `kataflash flash`  - Flash a given device (or devices) with a given firmware bundle.
* `kataflash verify` - Verify that a given device contains a given firmware bundle.
* `kataflash reboot` - Reboot a device into katapult.
* `kataflash exit`   - Exit the katapult bootloader on a device.

### `kataflashtool`
This is a transparent wrapper around the vendored flashtool.py, it see [Upstream Docs](https://github.com/Arksine/katapult?tab=readme-ov-file#flash-tool-usage) for usage information.

```
kataflashtool -i can1 -u asdffdsa -f ../path/to/klipper.bin
```


## Building
The vendored script is not part of this repo, and is downloaded by the `Makefile`.

At this early stage of development, it is nessacary to download and package this before building an sdist or wheel


