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


class RequestPlanFind(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RequestPlanFind - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'applicants': 'list[RequestPlanFindApplicant]',
            'enrollment_date': 'str',
            'drug_packages': 'list[DrugPackage]',
            'fips_code': 'str',
            'household_income': 'int',
            'household_size': 'int',
            'market': 'str',
            'providers': 'list[RequestPlanFindProvider]',
            'zip_code': 'str'
        }

        self.attribute_map = {
            'applicants': 'applicants',
            'enrollment_date': 'enrollment_date',
            'drug_packages': 'drug_packages',
            'fips_code': 'fips_code',
            'household_income': 'household_income',
            'household_size': 'household_size',
            'market': 'market',
            'providers': 'providers',
            'zip_code': 'zip_code'
        }

        self._applicants = None
        self._enrollment_date = None
        self._drug_packages = None
        self._fips_code = None
        self._household_income = None
        self._household_size = None
        self._market = None
        self._providers = None
        self._zip_code = None

    @property
    def applicants(self):
        """
        Gets the applicants of this RequestPlanFind.
        Applicants for desired plans.

        :return: The applicants of this RequestPlanFind.
        :rtype: list[RequestPlanFindApplicant]
        """
        return self._applicants

    @applicants.setter
    def applicants(self, applicants):
        """
        Sets the applicants of this RequestPlanFind.
        Applicants for desired plans.

        :param applicants: The applicants of this RequestPlanFind.
        :type: list[RequestPlanFindApplicant]
        """
        self._applicants = applicants

    @property
    def enrollment_date(self):
        """
        Gets the enrollment_date of this RequestPlanFind.
        Date of enrollment

        :return: The enrollment_date of this RequestPlanFind.
        :rtype: str
        """
        return self._enrollment_date

    @enrollment_date.setter
    def enrollment_date(self, enrollment_date):
        """
        Sets the enrollment_date of this RequestPlanFind.
        Date of enrollment

        :param enrollment_date: The enrollment_date of this RequestPlanFind.
        :type: str
        """
        self._enrollment_date = enrollment_date

    @property
    def drug_packages(self):
        """
        Gets the drug_packages of this RequestPlanFind.
        National Drug Code Package Id

        :return: The drug_packages of this RequestPlanFind.
        :rtype: list[DrugPackage]
        """
        return self._drug_packages

    @drug_packages.setter
    def drug_packages(self, drug_packages):
        """
        Sets the drug_packages of this RequestPlanFind.
        National Drug Code Package Id

        :param drug_packages: The drug_packages of this RequestPlanFind.
        :type: list[DrugPackage]
        """
        self._drug_packages = drug_packages

    @property
    def fips_code(self):
        """
        Gets the fips_code of this RequestPlanFind.
        County code to determine eligibility

        :return: The fips_code of this RequestPlanFind.
        :rtype: str
        """
        return self._fips_code

    @fips_code.setter
    def fips_code(self, fips_code):
        """
        Sets the fips_code of this RequestPlanFind.
        County code to determine eligibility

        :param fips_code: The fips_code of this RequestPlanFind.
        :type: str
        """
        self._fips_code = fips_code

    @property
    def household_income(self):
        """
        Gets the household_income of this RequestPlanFind.
        Total household income.

        :return: The household_income of this RequestPlanFind.
        :rtype: int
        """
        return self._household_income

    @household_income.setter
    def household_income(self, household_income):
        """
        Sets the household_income of this RequestPlanFind.
        Total household income.

        :param household_income: The household_income of this RequestPlanFind.
        :type: int
        """
        self._household_income = household_income

    @property
    def household_size(self):
        """
        Gets the household_size of this RequestPlanFind.
        Number of people living in household.

        :return: The household_size of this RequestPlanFind.
        :rtype: int
        """
        return self._household_size

    @household_size.setter
    def household_size(self, household_size):
        """
        Sets the household_size of this RequestPlanFind.
        Number of people living in household.

        :param household_size: The household_size of this RequestPlanFind.
        :type: int
        """
        self._household_size = household_size

    @property
    def market(self):
        """
        Gets the market of this RequestPlanFind.
        Type of plan to search for.

        :return: The market of this RequestPlanFind.
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """
        Sets the market of this RequestPlanFind.
        Type of plan to search for.

        :param market: The market of this RequestPlanFind.
        :type: str
        """
        self._market = market

    @property
    def providers(self):
        """
        Gets the providers of this RequestPlanFind.
        List of providers to search for.

        :return: The providers of this RequestPlanFind.
        :rtype: list[RequestPlanFindProvider]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """
        Sets the providers of this RequestPlanFind.
        List of providers to search for.

        :param providers: The providers of this RequestPlanFind.
        :type: list[RequestPlanFindProvider]
        """
        self._providers = providers

    @property
    def zip_code(self):
        """
        Gets the zip_code of this RequestPlanFind.
        5-digit zip code - this helps determine pricing.

        :return: The zip_code of this RequestPlanFind.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this RequestPlanFind.
        5-digit zip code - this helps determine pricing.

        :param zip_code: The zip_code of this RequestPlanFind.
        :type: str
        """
        self._zip_code = zip_code

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
