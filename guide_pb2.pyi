from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TaskReply(_message.Message):
    __slots__ = ["task_name", "task_number"]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_NUMBER_FIELD_NUMBER: _ClassVar[int]
    task_name: str
    task_number: str
    def __init__(self, task_name: _Optional[str] = ..., task_number: _Optional[str] = ...) -> None: ...

class TaskRequest(_message.Message):
    __slots__ = ["task_name"]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    task_name: str
    def __init__(self, task_name: _Optional[str] = ...) -> None: ...
