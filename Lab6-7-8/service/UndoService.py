
class UndoService:
    def __init__(self):
        self._history = []
        self._index = -1

    @property
    def index(self):
        return self._index

    @property
    def history(self):
        return self._history

    def record(self, operation):
        self._history = self._history[0:self._index + 1]

        self._history.append(operation)
        self._index += 1

    def undo(self):

        self._history[self._index].undo()
        self._index -= 1

    def redo(self):

        self._index += 1
        self._history[self._index].redo()


class CascadedOperation:

    def __init__(self, *operations):
        self._operations = operations

    def undo(self):
        for oper in self._operations:
            oper.undo()

    def redo(self):
        for oper in self._operations:
            oper.redo()


class Operation:

    def __init__(self, undo_function, redo_function):
        self._undo_function = undo_function
        self._redo_function = redo_function

    def undo(self):
        self._undo_function()

    def redo(self):
        self._redo_function()


class MultipleOperations:

    def __init__(self, undo_function1, undo_function2, redo_function1, redo_function2):
        self._undo_function1 = undo_function1
        self._undo_function2 = undo_function2
        self._redo_function1 = redo_function1
        self._redo_function2 = redo_function2

    def undo(self):
        self._undo_function1()
        self._undo_function2()

    def redo(self):
        self._redo_function1()
        self._redo_function2()


class FunctionCall:

    def __init__(self, function_ref, *function_params):
        self._function_ref = function_ref
        self._function_params = function_params

    def call(self):
        return self._function_ref(*self._function_params)

    def __call__(self):
        return self.call()
