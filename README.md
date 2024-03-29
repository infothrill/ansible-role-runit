# Ansible role runit

![Build status](https://github.com/infothrill/ansible-role-runit/actions/workflows/tests.yml/badge.svg)
[![Ansible Role](https://img.shields.io/ansible/role/27484.svg)](https://galaxy.ansible.com/infothrill/runit/)


An [Ansible](http://www.ansible.com) role to install
[runit](http://smarden.org/runit/), a UNIX init scheme with service supervision

## Quick howto

requirements.yml:

	- src: infothrill.runit
	  version: v1.2.0

Install:

	ansible-galaxy install -r requirements.yml -p ./roles/

Playbook:

    - hosts: servers
        roles:
		    - role: infothrill.runit

## Role variables

n/a

## Dependencies

n/a

## License

MIT

## Author Information

This role was created in 2018 by Paul Kremer.


## Changes

### v1.2.0

* Switch to Github actions CI
* Drop ansible older than 4 and add ansible 5, 6 support
* upgrade to molecule 3
* add support for Debian 10 'Buster'
* add support for python 3.8+
* drop support for python 2 and python 3.7
* ensure apt cache is up-to-date when installing

### v1.1.0

* add support for Ubuntu 20.04 (focal)
* drop support for Ubuntu 14.04 (trusty)
* add support for ansible 2.9
* drop support for ansible 2.4

### v1.0.1

* upgrades of test dependencies, maintenance only

### v1.0.0

* initial release
