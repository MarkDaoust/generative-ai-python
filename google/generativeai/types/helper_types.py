# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import google.api_core.timeout
import google.api_core.retry

import collections
import dataclasses

from typing_extensions import TypedDict, Union

__all__ = ["RequestOptions", "RequestOptionsType"]


class RequestOptionsDict(TypedDict, total=False):
    retry: google.api_core.retry.Retry
    timeout: int | float | google.api_core.timeout.TimeToDeadlineTimeout


@dataclasses.dataclass
class RequestOptions(collections.abc.Mapping):
    retry: google.api_core.retry.Retry | None
    timeout: int | float | google.api_core.timeout.TimeToDeadlineTimeout | None

    # Inherit from Mapping for **unpacking
    def __getitem__(self, item):
        if item == "retry":
            return self.retry
        elif item == "timeout":
            return self.timeout
        else:
            raise KeyError(f'RequestOptions does not have a "{item}" key')

    def __iter__(self):
        yield "retry"
        yield "timeout"

    def __len__(self):
        return 2


RequestOptionsType = Union[RequestOptions, RequestOptionsDict]