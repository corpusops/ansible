#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_firewall
description:
- Each network has its own firewall controlling access to and from the instances.
- All traffic to instances, even from other instances, is blocked by the firewall
  unless firewall rules are created to allow it.
- The default network has automatically created firewall rules that are shown in default
  firewall rules. No manually created network has automatically created firewall rules
  except for a default "allow" rule for outgoing traffic and a default "deny" for
  incoming traffic. For all networks except the default network, you must create any
  firewall rules you need.
short_description: Creates a GCP Firewall
version_added: 2.6
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
  allowed:
    description:
    - The list of ALLOW rules specified by this firewall. Each rule specifies a protocol
      and port-range tuple that describes a permitted connection.
    required: false
    suboptions:
      ip_protocol:
        description:
        - The IP protocol to which this rule applies. The protocol type is required
          when creating a firewall rule. This value can either be one of the following
          well known protocol strings (tcp, udp, icmp, esp, ah, sctp), or the IP protocol
          number.
        required: true
      ports:
        description:
        - An optional list of ports to which this rule applies. This field is only
          applicable for UDP or TCP protocol. Each entry must be either an integer
          or a range. If not specified, this rule applies to connections through any
          port.
        - 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'
        required: false
  denied:
    description:
    - The list of DENY rules specified by this firewall. Each rule specifies a protocol
      and port-range tuple that describes a denied connection.
    required: false
    version_added: 2.8
    suboptions:
      ip_protocol:
        description:
        - The IP protocol to which this rule applies. The protocol type is required
          when creating a firewall rule. This value can either be one of the following
          well known protocol strings (tcp, udp, icmp, esp, ah, sctp), or the IP protocol
          number.
        required: true
      ports:
        description:
        - An optional list of ports to which this rule applies. This field is only
          applicable for UDP or TCP protocol. Each entry must be either an integer
          or a range. If not specified, this rule applies to connections through any
          port.
        - 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'
        required: false
  description:
    description:
    - An optional description of this resource. Provide this property when you create
      the resource.
    required: false
  destination_ranges:
    description:
    - If destination ranges are specified, the firewall will apply only to traffic
      that has destination IP address in these ranges. These ranges must be expressed
      in CIDR format. Only IPv4 is supported.
    required: false
    version_added: 2.8
  direction:
    description:
    - 'Direction of traffic to which this firewall applies; default is INGRESS. Note:
      For INGRESS traffic, it is NOT supported to specify destinationRanges; For EGRESS
      traffic, it is NOT supported to specify sourceRanges OR sourceTags.'
    required: false
    version_added: 2.8
    choices:
    - INGRESS
    - EGRESS
  disabled:
    description:
    - Denotes whether the firewall rule is disabled, i.e not applied to the network
      it is associated with. When set to true, the firewall rule is not enforced and
      the network behaves as if it did not exist. If this is unspecified, the firewall
      rule will be enabled.
    required: false
    type: bool
    version_added: 2.8
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
  network:
    description:
    - 'URL of the network resource for this firewall rule. If not specified when creating
      a firewall rule, the default network is used: global/networks/default If you
      choose to specify this property, you can specify the network as a full or partial
      URL. For example, the following are all valid URLs: U(https://www.googleapis.com/compute/v1/projects/myproject/global/)
      networks/my-network projects/myproject/global/networks/my-network global/networks/default
      .'
    - 'This field represents a link to a Network resource in GCP. It can be specified
      in two ways. First, you can place in the selfLink of the resource here as a
      string Alternatively, you can add `register: name-of-resource` to a gcp_compute_network
      task and then set this network field to "{{ name-of-resource }}"'
    required: false
    default:
      selfLink: global/networks/default
  priority:
    description:
    - Priority for this rule. This is an integer between 0 and 65535, both inclusive.
      When not specified, the value assumed is 1000. Relative priorities determine
      precedence of conflicting rules. Lower value of priority implies higher precedence
      (eg, a rule with priority 0 has higher precedence than a rule with priority
      1). DENY rules take precedence over ALLOW rules having equal priority.
    required: false
    default: '1000'
    version_added: 2.8
  source_ranges:
    description:
    - If source ranges are specified, the firewall will apply only to traffic that
      has source IP address in these ranges. These ranges must be expressed in CIDR
      format. One or both of sourceRanges and sourceTags may be set. If both properties
      are set, the firewall will apply to traffic that has source IP address within
      sourceRanges OR the source IP that belongs to a tag listed in the sourceTags
      property. The connection does not need to match both properties for the firewall
      to apply. Only IPv4 is supported.
    required: false
  source_service_accounts:
    description:
    - If source service accounts are specified, the firewall will apply only to traffic
      originating from an instance with a service account in this list. Source service
      accounts cannot be used to control traffic to an instance's external IP address
      because service accounts are associated with an instance, not an IP address.
      sourceRanges can be set at the same time as sourceServiceAccounts. If both are
      set, the firewall will apply to traffic that has source IP address within sourceRanges
      OR the source IP belongs to an instance with service account listed in sourceServiceAccount.
      The connection does not need to match both properties for the firewall to apply.
      sourceServiceAccounts cannot be used at the same time as sourceTags or targetTags.
    required: false
    version_added: 2.8
  source_tags:
    description:
    - If source tags are specified, the firewall will apply only to traffic with source
      IP that belongs to a tag listed in source tags. Source tags cannot be used to
      control traffic to an instance's external IP address. Because tags are associated
      with an instance, not an IP address. One or both of sourceRanges and sourceTags
      may be set. If both properties are set, the firewall will apply to traffic that
      has source IP address within sourceRanges OR the source IP that belongs to a
      tag listed in the sourceTags property. The connection does not need to match
      both properties for the firewall to apply.
    required: false
  target_service_accounts:
    description:
    - A list of service accounts indicating sets of instances located in the network
      that may make network connections as specified in allowed[].
    - targetServiceAccounts cannot be used at the same time as targetTags or sourceTags.
      If neither targetServiceAccounts nor targetTags are specified, the firewall
      rule applies to all instances on the specified network.
    required: false
    version_added: 2.8
  target_tags:
    description:
    - A list of instance tags indicating sets of instances located in the network
      that may make network connections as specified in allowed[].
    - If no targetTags are specified, the firewall rule applies to all instances on
      the specified network.
    required: false
extends_documentation_fragment: gcp
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/latest/firewalls)'
- 'Official Documentation: U(https://cloud.google.com/vpc/docs/firewalls)'
'''

EXAMPLES = '''
- name: create a firewall
  gcp_compute_firewall:
      name: "test_object"
      allowed:
      - ip_protocol: tcp
        ports:
        - '22'
      target_tags:
      - test-ssh-server
      - staging-ssh-server
      source_tags:
      - test-ssh-clients
      project: "test_project"
      auth_kind: "serviceaccount"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
allowed:
  description:
  - The list of ALLOW rules specified by this firewall. Each rule specifies a protocol
    and port-range tuple that describes a permitted connection.
  returned: success
  type: complex
  contains:
    ip_protocol:
      description:
      - The IP protocol to which this rule applies. The protocol type is required
        when creating a firewall rule. This value can either be one of the following
        well known protocol strings (tcp, udp, icmp, esp, ah, sctp), or the IP protocol
        number.
      returned: success
      type: str
    ports:
      description:
      - An optional list of ports to which this rule applies. This field is only applicable
        for UDP or TCP protocol. Each entry must be either an integer or a range.
        If not specified, this rule applies to connections through any port.
      - 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'
      returned: success
      type: list
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
denied:
  description:
  - The list of DENY rules specified by this firewall. Each rule specifies a protocol
    and port-range tuple that describes a denied connection.
  returned: success
  type: complex
  contains:
    ip_protocol:
      description:
      - The IP protocol to which this rule applies. The protocol type is required
        when creating a firewall rule. This value can either be one of the following
        well known protocol strings (tcp, udp, icmp, esp, ah, sctp), or the IP protocol
        number.
      returned: success
      type: str
    ports:
      description:
      - An optional list of ports to which this rule applies. This field is only applicable
        for UDP or TCP protocol. Each entry must be either an integer or a range.
        If not specified, this rule applies to connections through any port.
      - 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'
      returned: success
      type: list
description:
  description:
  - An optional description of this resource. Provide this property when you create
    the resource.
  returned: success
  type: str
destinationRanges:
  description:
  - If destination ranges are specified, the firewall will apply only to traffic that
    has destination IP address in these ranges. These ranges must be expressed in
    CIDR format. Only IPv4 is supported.
  returned: success
  type: list
direction:
  description:
  - 'Direction of traffic to which this firewall applies; default is INGRESS. Note:
    For INGRESS traffic, it is NOT supported to specify destinationRanges; For EGRESS
    traffic, it is NOT supported to specify sourceRanges OR sourceTags.'
  returned: success
  type: str
disabled:
  description:
  - Denotes whether the firewall rule is disabled, i.e not applied to the network
    it is associated with. When set to true, the firewall rule is not enforced and
    the network behaves as if it did not exist. If this is unspecified, the firewall
    rule will be enabled.
  returned: success
  type: bool
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
network:
  description:
  - 'URL of the network resource for this firewall rule. If not specified when creating
    a firewall rule, the default network is used: global/networks/default If you choose
    to specify this property, you can specify the network as a full or partial URL.
    For example, the following are all valid URLs: U(https://www.googleapis.com/compute/v1/projects/myproject/global/)
    networks/my-network projects/myproject/global/networks/my-network global/networks/default
    .'
  returned: success
  type: str
priority:
  description:
  - Priority for this rule. This is an integer between 0 and 65535, both inclusive.
    When not specified, the value assumed is 1000. Relative priorities determine precedence
    of conflicting rules. Lower value of priority implies higher precedence (eg, a
    rule with priority 0 has higher precedence than a rule with priority 1). DENY
    rules take precedence over ALLOW rules having equal priority.
  returned: success
  type: int
sourceRanges:
  description:
  - If source ranges are specified, the firewall will apply only to traffic that has
    source IP address in these ranges. These ranges must be expressed in CIDR format.
    One or both of sourceRanges and sourceTags may be set. If both properties are
    set, the firewall will apply to traffic that has source IP address within sourceRanges
    OR the source IP that belongs to a tag listed in the sourceTags property. The
    connection does not need to match both properties for the firewall to apply. Only
    IPv4 is supported.
  returned: success
  type: list
sourceServiceAccounts:
  description:
  - If source service accounts are specified, the firewall will apply only to traffic
    originating from an instance with a service account in this list. Source service
    accounts cannot be used to control traffic to an instance's external IP address
    because service accounts are associated with an instance, not an IP address. sourceRanges
    can be set at the same time as sourceServiceAccounts. If both are set, the firewall
    will apply to traffic that has source IP address within sourceRanges OR the source
    IP belongs to an instance with service account listed in sourceServiceAccount.
    The connection does not need to match both properties for the firewall to apply.
    sourceServiceAccounts cannot be used at the same time as sourceTags or targetTags.
  returned: success
  type: list
sourceTags:
  description:
  - If source tags are specified, the firewall will apply only to traffic with source
    IP that belongs to a tag listed in source tags. Source tags cannot be used to
    control traffic to an instance's external IP address. Because tags are associated
    with an instance, not an IP address. One or both of sourceRanges and sourceTags
    may be set. If both properties are set, the firewall will apply to traffic that
    has source IP address within sourceRanges OR the source IP that belongs to a tag
    listed in the sourceTags property. The connection does not need to match both
    properties for the firewall to apply.
  returned: success
  type: list
targetServiceAccounts:
  description:
  - A list of service accounts indicating sets of instances located in the network
    that may make network connections as specified in allowed[].
  - targetServiceAccounts cannot be used at the same time as targetTags or sourceTags.
    If neither targetServiceAccounts nor targetTags are specified, the firewall rule
    applies to all instances on the specified network.
  returned: success
  type: list
targetTags:
  description:
  - A list of instance tags indicating sets of instances located in the network that
    may make network connections as specified in allowed[].
  - If no targetTags are specified, the firewall rule applies to all instances on
    the specified network.
  returned: success
  type: list
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            allowed=dict(type='list', elements='dict', options=dict(ip_protocol=dict(required=True, type='str'), ports=dict(type='list', elements='str'))),
            denied=dict(type='list', elements='dict', options=dict(ip_protocol=dict(required=True, type='str'), ports=dict(type='list', elements='str'))),
            description=dict(type='str'),
            destination_ranges=dict(type='list', elements='str'),
            direction=dict(type='str', choices=['INGRESS', 'EGRESS']),
            disabled=dict(type='bool'),
            name=dict(required=True, type='str'),
            network=dict(default=dict(selfLink='global/networks/default')),
            priority=dict(default=1000, type='int'),
            source_ranges=dict(type='list', elements='str'),
            source_service_accounts=dict(type='list', elements='str'),
            source_tags=dict(type='list', elements='str'),
            target_service_accounts=dict(type='list', elements='str'),
            target_tags=dict(type='list', elements='str'),
        ),
        mutually_exclusive=[
            ['allowed', 'denied'],
            ['destination_ranges', 'source_ranges', 'source_tags'],
            ['destination_ranges', 'source_ranges'],
            ['source_service_accounts', 'source_tags', 'target_tags'],
            ['destination_ranges', 'source_service_accounts', 'source_tags', 'target_service_accounts'],
            ['source_tags', 'target_service_accounts', 'target_tags'],
            ['source_service_accounts', 'target_service_accounts', 'target_tags'],
        ],
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#firewall'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.patch(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#firewall',
        u'allowed': FirewallAllowedArray(module.params.get('allowed', []), module).to_request(),
        u'denied': FirewallDeniedArray(module.params.get('denied', []), module).to_request(),
        u'description': module.params.get('description'),
        u'destinationRanges': module.params.get('destination_ranges'),
        u'direction': module.params.get('direction'),
        u'disabled': module.params.get('disabled'),
        u'name': module.params.get('name'),
        u'network': replace_resource_dict(module.params.get(u'network', {}), 'selfLink'),
        u'priority': module.params.get('priority'),
        u'sourceRanges': module.params.get('source_ranges'),
        u'sourceServiceAccounts': module.params.get('source_service_accounts'),
        u'sourceTags': module.params.get('source_tags'),
        u'targetServiceAccounts': module.params.get('target_service_accounts'),
        u'targetTags': module.params.get('target_tags'),
    }
    request = encode_request(request, module)
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/firewalls/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/firewalls".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'allowed': FirewallAllowedArray(response.get(u'allowed', []), module).from_response(),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'denied': FirewallDeniedArray(response.get(u'denied', []), module).from_response(),
        u'description': response.get(u'description'),
        u'destinationRanges': response.get(u'destinationRanges'),
        u'direction': response.get(u'direction'),
        u'disabled': response.get(u'disabled'),
        u'id': response.get(u'id'),
        u'name': module.params.get('name'),
        u'network': response.get(u'network'),
        u'priority': response.get(u'priority'),
        u'sourceRanges': response.get(u'sourceRanges'),
        u'sourceServiceAccounts': response.get(u'sourceServiceAccounts'),
        u'sourceTags': response.get(u'sourceTags'),
        u'targetServiceAccounts': response.get(u'targetServiceAccounts'),
        u'targetTags': response.get(u'targetTags'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#firewall')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


def encode_request(request, module):
    if 'network' in request and request['network'] is not None:
        if not re.match(r'https://www.googleapis.com/compute/v1/projects/.*', request['network']):
            request['network'] = 'https://www.googleapis.com/compute/v1/projects/{project}/{network}'.format(
                project=module.params['project'], network=request['network']
            )

    return request


class FirewallAllowedArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'IPProtocol': item.get('ip_protocol'), u'ports': item.get('ports')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'IPProtocol': item.get(u'IPProtocol'), u'ports': item.get(u'ports')})


class FirewallDeniedArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'IPProtocol': item.get('ip_protocol'), u'ports': item.get('ports')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'IPProtocol': item.get(u'IPProtocol'), u'ports': item.get(u'ports')})


if __name__ == '__main__':
    main()
