# Helios - one bash command to start the day

> inspired by Doaa Mahely [dev.to/dmahely] but different 

## Whats it all about
I do pretty much all of my work in google chrome/browser. Since I do work on multiple projects at the same time, I usually do have many many tabs open synchronically. But of course I do use other applications like VSCode.

This sometimes results in a messy working environment, thus I do have different "workspaces" open at a time.

This project focuses on having some kind of structurized workspaces which I can open/close/modify by only one command.

This has pretty much the same functionality as using multiple desktops - but I don't like them.

## Functionality
Helios is a python script which can be accessed by command line. It does open different (workspace-specific) browser-tab, and additionally executes shell commands.

## Commands
```helios help``` prints some information

```helios open``` opens "main" workspace

```helios open <workspace>``` opens workspace

```helios edit <workspace> new``` creates new workspace

```helios edit <workspace> remove``` removes workspace

```helios edit <workspace> add-web <URL>``` adds URL to workspace

```helios edit <workspace> add-cmd <CMD>``` adds CMD to workspace

```helios print <workspace>``` prints workspace and its assets. if workspace is not defined, all assets will be printed.
