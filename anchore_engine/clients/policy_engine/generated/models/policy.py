# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from anchore_engine.clients.policy_engine.generated.models.policy_rule import PolicyRule  # noqa: F401,E501


class Policy(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'comment': 'str',
        'version': 'str',
        'rules': 'list[PolicyRule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'comment': 'comment',
        'version': 'version',
        'rules': 'rules'
    }

    def __init__(self, id=None, name=None, comment=None, version=None, rules=None):  # noqa: E501
        """Policy - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._comment = None
        self._version = None
        self._rules = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if comment is not None:
            self.comment = comment
        self.version = version
        if rules is not None:
            self.rules = rules

    @property
    def id(self):
        """Gets the id of this Policy.  # noqa: E501


        :return: The id of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Policy.


        :param id: The id of this Policy.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Policy.  # noqa: E501


        :return: The name of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Policy.


        :param name: The name of this Policy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this Policy.  # noqa: E501


        :return: The comment of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Policy.


        :param comment: The comment of this Policy.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def version(self):
        """Gets the version of this Policy.  # noqa: E501


        :return: The version of this Policy.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Policy.


        :param version: The version of this Policy.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def rules(self):
        """Gets the rules of this Policy.  # noqa: E501


        :return: The rules of this Policy.  # noqa: E501
        :rtype: list[PolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this Policy.


        :param rules: The rules of this Policy.  # noqa: E501
        :type: list[PolicyRule]
        """

        self._rules = rules

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other