# coding: utf-8

"""
AnalyticscontrollerApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


__version__ = "1.0.0"


class AnalyticscontrollerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def feed_using_post(self, x_real_ip, event_data, **kwargs):
        """
        feed
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.feed_using_post(x_real_ip, event_data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_real_ip: X-Real-IP (required)
        :param RestEvent event_data: eventData (required)
        :param str authorization: Authorization
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_real_ip', 'event_data', 'authorization']
        all_params += ['callback', 'binary_data', 'binary_filename', 'binary_range', 'binary_permissions', 'headers_handler']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method feed_using_post" % key
                )
            if val is not None:
                params[key] = val
        del params['kwargs']

        # verify the required parameter 'x_real_ip' is set
        if ('x_real_ip' not in params) or (params['x_real_ip'] is None):
            raise ValueError("Missing the required parameter `x_real_ip` when calling `feed_using_post`")
        # verify the required parameter 'event_data' is set
        if ('event_data' not in params) or (params['event_data'] is None):
            raise ValueError("Missing the required parameter `event_data` when calling `feed_using_post`")


        resource_path = '/event'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_real_ip' in params:
            header_params['X-Real-IP'] = params['x_real_ip']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'event_data' in params:
            body_params = params['event_data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        if 'binary_data' in kwargs:
            header_params['Content-Type'] = 'application/octet-stream'
            if 'binary_filename' in kwargs:
                header_params['Content-Filename'] = kwargs['binary_filename']
            if 'binary_range' in kwargs:
                header_params['Range'] = kwargs['binary_range']
            if 'binary_permissions' in kwargs:
                header_params['X-File-Permissions'] = kwargs['binary_permissions']
            form_params = kwargs['binary_data']

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            headers_handler=params.get('headers_handler'))
        return response

    def sync_using_post(self, authorization, users, **kwargs):
        """
        sync
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sync_using_post(authorization, users, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str authorization: Authorization (required)
        :param Users users: users (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'users']
        all_params += ['callback', 'binary_data', 'binary_filename', 'binary_range', 'binary_permissions', 'headers_handler']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sync_using_post" % key
                )
            if val is not None:
                params[key] = val
        del params['kwargs']

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params) or (params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `sync_using_post`")
        # verify the required parameter 'users' is set
        if ('users' not in params) or (params['users'] is None):
            raise ValueError("Missing the required parameter `users` when calling `sync_using_post`")


        resource_path = '/sync'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'users' in params:
            body_params = params['users']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        if 'binary_data' in kwargs:
            header_params['Content-Type'] = 'application/octet-stream'
            if 'binary_filename' in kwargs:
                header_params['Content-Filename'] = kwargs['binary_filename']
            if 'binary_range' in kwargs:
                header_params['Range'] = kwargs['binary_range']
            if 'binary_permissions' in kwargs:
                header_params['X-File-Permissions'] = kwargs['binary_permissions']
            form_params = kwargs['binary_data']

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            headers_handler=params.get('headers_handler'))
        return response
