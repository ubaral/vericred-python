# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ZipCountiesResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ZipCountiesResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'counties': 'list[County]',
            'states': 'list[State]',
            'zip_counties': 'list[ZipCounty]',
            'zip_codes': 'list[ZipCode]'
        }

        self.attribute_map = {
            'counties': 'counties',
            'states': 'states',
            'zip_counties': 'zip_counties',
            'zip_codes': 'zip_codes'
        }

        self._counties = None
        self._states = None
        self._zip_counties = None
        self._zip_codes = None

    @property
    def counties(self):
        """
        Gets the counties of this ZipCountiesResponse.
        Counties that exist in the provided zip prefix.

        :return: The counties of this ZipCountiesResponse.
        :rtype: list[County]
        """
        return self._counties

    @counties.setter
    def counties(self, counties):
        """
        Sets the counties of this ZipCountiesResponse.
        Counties that exist in the provided zip prefix.

        :param counties: The counties of this ZipCountiesResponse.
        :type: list[County]
        """
        self._counties = counties

    @property
    def states(self):
        """
        Gets the states of this ZipCountiesResponse.
        States that exist in the provided zip prefix.

        :return: The states of this ZipCountiesResponse.
        :rtype: list[State]
        """
        return self._states

    @states.setter
    def states(self, states):
        """
        Sets the states of this ZipCountiesResponse.
        States that exist in the provided zip prefix.

        :param states: The states of this ZipCountiesResponse.
        :type: list[State]
        """
        self._states = states

    @property
    def zip_counties(self):
        """
        Gets the zip_counties of this ZipCountiesResponse.
        ZipCounties that exist in the provided zip prefix.

        :return: The zip_counties of this ZipCountiesResponse.
        :rtype: list[ZipCounty]
        """
        return self._zip_counties

    @zip_counties.setter
    def zip_counties(self, zip_counties):
        """
        Sets the zip_counties of this ZipCountiesResponse.
        ZipCounties that exist in the provided zip prefix.

        :param zip_counties: The zip_counties of this ZipCountiesResponse.
        :type: list[ZipCounty]
        """
        self._zip_counties = zip_counties

    @property
    def zip_codes(self):
        """
        Gets the zip_codes of this ZipCountiesResponse.
        ZipCodes that exist in the provided zip prefix.

        :return: The zip_codes of this ZipCountiesResponse.
        :rtype: list[ZipCode]
        """
        return self._zip_codes

    @zip_codes.setter
    def zip_codes(self, zip_codes):
        """
        Sets the zip_codes of this ZipCountiesResponse.
        ZipCodes that exist in the provided zip prefix.

        :param zip_codes: The zip_codes of this ZipCountiesResponse.
        :type: list[ZipCode]
        """
        self._zip_codes = zip_codes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

