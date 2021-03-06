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


class Applicant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Applicant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'dob': 'date',
            'member_id': 'str',
            'name': 'str',
            'relationship': 'str',
            'smoker': 'bool',
            'ssn': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'dob': 'dob',
            'member_id': 'member_id',
            'name': 'name',
            'relationship': 'relationship',
            'smoker': 'smoker',
            'ssn': 'ssn'
        }

        self._id = None
        self._dob = None
        self._member_id = None
        self._name = None
        self._relationship = None
        self._smoker = None
        self._ssn = None

    @property
    def id(self):
        """
        Gets the id of this Applicant.
        Primary key

        :return: The id of this Applicant.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Applicant.
        Primary key

        :param id: The id of this Applicant.
        :type: int
        """
        self._id = id

    @property
    def dob(self):
        """
        Gets the dob of this Applicant.
        Date of Birth

        :return: The dob of this Applicant.
        :rtype: date
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """
        Sets the dob of this Applicant.
        Date of Birth

        :param dob: The dob of this Applicant.
        :type: date
        """
        self._dob = dob

    @property
    def member_id(self):
        """
        Gets the member_id of this Applicant.
        Member token

        :return: The member_id of this Applicant.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        """
        Sets the member_id of this Applicant.
        Member token

        :param member_id: The member_id of this Applicant.
        :type: str
        """
        self._member_id = member_id

    @property
    def name(self):
        """
        Gets the name of this Applicant.
        Full name of the Applicant

        :return: The name of this Applicant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Applicant.
        Full name of the Applicant

        :param name: The name of this Applicant.
        :type: str
        """
        self._name = name

    @property
    def relationship(self):
        """
        Gets the relationship of this Applicant.
        Relationship of the Applicant to the Member

        :return: The relationship of this Applicant.
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """
        Sets the relationship of this Applicant.
        Relationship of the Applicant to the Member

        :param relationship: The relationship of this Applicant.
        :type: str
        """
        self._relationship = relationship

    @property
    def smoker(self):
        """
        Gets the smoker of this Applicant.
        Does the Applicant smoke?

        :return: The smoker of this Applicant.
        :rtype: bool
        """
        return self._smoker

    @smoker.setter
    def smoker(self, smoker):
        """
        Sets the smoker of this Applicant.
        Does the Applicant smoke?

        :param smoker: The smoker of this Applicant.
        :type: bool
        """
        self._smoker = smoker

    @property
    def ssn(self):
        """
        Gets the ssn of this Applicant.
        Applicant's Social Security Number

        :return: The ssn of this Applicant.
        :rtype: str
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """
        Sets the ssn of this Applicant.
        Applicant's Social Security Number

        :param ssn: The ssn of this Applicant.
        :type: str
        """
        self._ssn = ssn

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

