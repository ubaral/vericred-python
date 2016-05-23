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


class County(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        County - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'fips_code': 'str',
            'name': 'str',
            'state_code': 'str',
            'state_id': 'int',
            'state_live': 'bool',
            'state_live_for_business': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'fips_code': 'fips_code',
            'name': 'name',
            'state_code': 'state_code',
            'state_id': 'state_id',
            'state_live': 'state_live',
            'state_live_for_business': 'state_live_for_business'
        }

        self._id = None
        self._fips_code = None
        self._name = None
        self._state_code = None
        self._state_id = None
        self._state_live = None
        self._state_live_for_business = None

    @property
    def id(self):
        """
        Gets the id of this County.
        Primary key

        :return: The id of this County.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this County.
        Primary key

        :param id: The id of this County.
        :type: int
        """
        self._id = id

    @property
    def fips_code(self):
        """
        Gets the fips_code of this County.
        State FIPS code

        :return: The fips_code of this County.
        :rtype: str
        """
        return self._fips_code

    @fips_code.setter
    def fips_code(self, fips_code):
        """
        Sets the fips_code of this County.
        State FIPS code

        :param fips_code: The fips_code of this County.
        :type: str
        """
        self._fips_code = fips_code

    @property
    def name(self):
        """
        Gets the name of this County.
        Human-readable name

        :return: The name of this County.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this County.
        Human-readable name

        :param name: The name of this County.
        :type: str
        """
        self._name = name

    @property
    def state_code(self):
        """
        Gets the state_code of this County.
        Two-character state code

        :return: The state_code of this County.
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """
        Sets the state_code of this County.
        Two-character state code

        :param state_code: The state_code of this County.
        :type: str
        """
        self._state_code = state_code

    @property
    def state_id(self):
        """
        Gets the state_id of this County.
        state relationship

        :return: The state_id of this County.
        :rtype: int
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """
        Sets the state_id of this County.
        state relationship

        :param state_id: The state_id of this County.
        :type: int
        """
        self._state_id = state_id

    @property
    def state_live(self):
        """
        Gets the state_live of this County.
        Is the state containing this county active for consumers?(deprecated in favor of last_date_for_individual)

        :return: The state_live of this County.
        :rtype: bool
        """
        return self._state_live

    @state_live.setter
    def state_live(self, state_live):
        """
        Sets the state_live of this County.
        Is the state containing this county active for consumers?(deprecated in favor of last_date_for_individual)

        :param state_live: The state_live of this County.
        :type: bool
        """
        self._state_live = state_live

    @property
    def state_live_for_business(self):
        """
        Gets the state_live_for_business of this County.
        Is the state containing this county active for business?(deprecated in favor of last_date_for_shop)

        :return: The state_live_for_business of this County.
        :rtype: bool
        """
        return self._state_live_for_business

    @state_live_for_business.setter
    def state_live_for_business(self, state_live_for_business):
        """
        Sets the state_live_for_business of this County.
        Is the state containing this county active for business?(deprecated in favor of last_date_for_shop)

        :param state_live_for_business: The state_live_for_business of this County.
        :type: bool
        """
        self._state_live_for_business = state_live_for_business

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

