# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.body import Body
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Problem(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, version: int=None, body: Body=None):
        """
        Problem - a model defined in Swagger

        :param version: The version of this Problem.
        :type version: int
        :param body: The body of this Problem.
        :type body: Body
        """
        self.swagger_types = {
            'version': int,
            'body': Body
        }

        self.attribute_map = {
            'version': 'version',
            'body': 'body'
        }

        self._version = version
        self._body = body

    @classmethod
    def from_dict(cls, dikt) -> 'Problem':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Problem of this Problem.
        :rtype: Problem
        """
        return deserialize_model(dikt, cls)

    @property
    def version(self) -> int:
        """
        Gets the version of this Problem.

        :return: The version of this Problem.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int):
        """
        Sets the version of this Problem.

        :param version: The version of this Problem.
        :type version: int
        """

        self._version = version

    @property
    def body(self) -> Body:
        """
        Gets the body of this Problem.

        :return: The body of this Problem.
        :rtype: Body
        """
        return self._body

    @body.setter
    def body(self, body: Body):
        """
        Sets the body of this Problem.

        :param body: The body of this Problem.
        :type body: Body
        """

        self._body = body

