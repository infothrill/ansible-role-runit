# Ansible role runit

[![Build Status](https://img.shields.io/travis/infothrill/ansible-role-runit/master.svg?label=travis_master)](https://travis-ci.org/infothrill/ansible-role-runit)
[![Build Status](https://img.shields.io/travis/infothrill/ansible-role-runit/develop.svg?label=travis_develop)](https://travis-ci.org/infothrill/ansible-role-runit)
[![Updates](https://pyup.io/repos/github/infothrill/ansible-role-runit/shield.svg)](https://pyup.io/repos/github/infothrill/ansible-role-runit/)
[![Ansible Role](https://img.shields.io/ansible/role/27484.svg)](https://galaxy.ansible.com/infothrill/runit/)


An [Ansible](http://www.ansible.com) role to install
[runit](http://smarden.org/runit/), a UNIX init scheme with service supervision

## Quick howto

requirements.yml:

	- src: infothrill.runit
	  version: v1.1.0

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

### vx

* Drop ansible <= 2.7 and add ansible 2.10 support
* upgrade to molecule 3
* add support for Debian 10 'Buster'
* drop support for python 2
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
