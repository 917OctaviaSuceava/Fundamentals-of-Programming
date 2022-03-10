
from dataclasses import dataclass

@dataclass
class UndoOperation:
    target_object: object
    handler: object
    args: tuple


class UndoManager:
    __undo_operations = []
    __redo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *args):
        UndoManager.__undo_operations.append(UndoOperation(target_object, handler, args))

    @staticmethod
    def register_redo(target_object, handler, *args):
        UndoManager.__redo_operations.append(UndoOperation(target_object, handler, args))

    @staticmethod
    def undo():
        undo_operation = UndoManager.__undo_operations.pop()
        # UndoManager.__redo_operations.append(undo_operation)
        undo_operation.handler(undo_operation.target_object, *undo_operation.args)

    @staticmethod
    def get_undo_operations():
        return UndoManager.__undo_operations

    @staticmethod
    def get_redo_operations():
        return UndoManager.__redo_operations

    @staticmethod
    def redo():
        redo_operation = UndoManager.__redo_operations.pop()
        redo_operation.handler(redo_operation.target_object, *redo_operation.args)
        # UndoManager.__undo_operations.append(redo_operation)
