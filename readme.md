# srv-inventory_provider

## Description

A simple application that gather inventory data from cloud provider (using api) and send result in a postgresql database. The idea is to gather all server accessible through ssh to generate a dynamic ansible inventory.

This project main goal is to complete data get from [srv-inventory_agent_srv](https://github.com/maraudeurs/srv-inventory_agent_srv).

Current supported cloud services :
- [x] Public cloud services
- [ ] Bare Metal services

Current supported cloud providers :
- [x] [OVH](https://www.ovhcloud.com/)
- [ ] [SCW](https://www.scaleway.com/)
- [ ] [Contabo](https://contabo.com/)