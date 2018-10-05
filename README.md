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
	  version: v1.0

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

### v1.0.0

* initial release
