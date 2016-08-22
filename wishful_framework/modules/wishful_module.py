import uuid
import logging
import inspect
from queue import Queue
from threading import Thread
from functools import partial
import wishful_upis as upis

__author__ = "Piotr Gawlowicz"
__copyright__ = "Copyright (c) 2015, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "gawlowicz@tkn.tu-berlin.de"


def _listify(may_list):
    if may_list is None:
        may_list = []
    if not isinstance(may_list, list):
        may_list = [may_list]
    return may_list


def _is_method(f):
    return inspect.isfunction(f) or inspect.ismethod(f)


def on_event(ev_cls, dispatchers=None):
    def _set_ev_cls_dec(handler):
        if 'callers' not in dir(handler):
            handler.callers = {}
        for e in _listify(ev_cls):
            handler.callers[e] = e.__module__
        return handler
    return _set_ev_cls_dec

on_start = partial(on_event, upis.mgmt.AgentStartEvent)
on_exit = partial(on_event, upis.mgmt.AgentExitEvent)
on_connected = partial(on_event, upis.mgmt.ControllerConnectedEvent)
on_disconnected = partial(on_event, upis.mgmt.ControllerDisconnectedEvent)


def run_in_thread():
    def _set_ev_cls_dec(handler):
        if '_run_in_thread_' not in dir(handler):
            handler._run_in_thread_ = True
        return handler
    return _set_ev_cls_dec


def on_first_call_to_module():
    def _set_ev_cls_dec(handler):
        if '_first_call_' not in dir(handler):
            handler._first_call_ = {}
        return handler
    return _set_ev_cls_dec


def before_call(func):
    def _set_ev_cls_dec(handler):
        if '_before_call_' not in dir(handler):
            handler._before_call_ = func
        return handler
    return _set_ev_cls_dec


def after_call(func):
    def _set_ev_cls_dec(handler):
        if '_after_call_' not in dir(handler):
            handler._after_call_ = func
        return handler
    return _set_ev_cls_dec


def on_function(upiFunc):
    def _set_ev_cls_dec(handler):
        if '_upiFunc_' not in dir(handler):
            handler._upiFunc_ = None
        handler._upiFunc_ = upiFunc.__module__ + "." + upiFunc.__name__
        return handler
    return _set_ev_cls_dec

bind_function = on_function


def event_enable(event):
    def _set_ev_cls_dec(handler):
        if '_event_enable_' not in dir(handler):
            handler._event_enable_ = None
        handler._event_enable_ = event.__module__ + "." + event.__name__
        return handler
    return _set_ev_cls_dec


def event_disable(event):
    def _set_ev_cls_dec(handler):
        if '_event_disable_' not in dir(handler):
            handler._event_disable_ = None
        handler._event_disable_ = event.__module__ + "." + event.__name__
        return handler
    return _set_ev_cls_dec


def service_start(service):
    def _set_ev_cls_dec(handler):
        if '_service_start_' not in dir(handler):
            handler._service_start_ = None
        handler._service_start_ = service.__module__ + "." + service.__name__
        return handler
    return _set_ev_cls_dec


def service_stop(service):
    def _set_ev_cls_dec(handler):
        if '_service_stop_' not in dir(handler):
            handler._service_stop_ = None
        handler._service_stop_ = service.__module__ + "." + service.__name__
        return handler
    return _set_ev_cls_dec


def build_module(module_class):
    original_methods = module_class.__dict__.copy()
    for name, method in original_methods.items():
        if hasattr(method, '_upi_fname'):
            # add UPI alias for the function
            for falias in method._upi_fname - set(original_methods):
                setattr(module_class, falias, method)
    return module_class


class ModuleWorker(Thread):
    def __init__(self, module):
        super().__init__()
        self.log = logging.getLogger("{module}.{name}".format(
            module=self.__class__.__module__, name=self.__class__.__name__))
        self.module = module
        self.taskQueue = Queue()
        self.daemon = True
        self.running = True
        self.start()

    def run(self):
        while self.running:
            (func, args, kargs) = self.taskQueue.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                print(e)
            self.taskQueue.task_done()

    def stop(self):
        self.running = False

    def add_task(self, func, args, kargs):
        self.taskQueue.put((func, args, kargs))


class WishfulModule(object):
    def __init__(self):
        self.log = logging.getLogger("{module}.{name}".format(
            module=self.__class__.__module__, name=self.__class__.__name__))

        self.worker = ModuleWorker(self)
        self.id = None
        self.uuid = str(uuid.uuid4())
        self.name = self.__class__.__name__
        self.agent = None
        self.moduleManager = None

        # TODO: move to AgentModule (DeviceModule)
        self.device = None  # used for filtering of commands
        self.deviceId = None  # used for filtering of commands
        self.attributes = []
        self.functions = []
        self.events = []
        self.services = []
        self.firstCallToModule = False

        # TODO: move to ControllerModule (ControllerApp)
        self.controller = None

    def set_agent(self, agent):
        self.agent = agent

    def set_module_manager(self, mm):
        self.moduleManager = mm

    def send_event(self, event):
        # stamp event with device
        event.device = self.device
        self.moduleManager.send_event(event)

    # TODO: move to AgentModule (DeviceModule)
    def set_device(self, dev):
        self.device = dev

    def get_device(self):
        return self.device

    def get_attributes(self):
        return self.attributes

    def get_functions(self):
        return self.functions

    def get_events(self):
        return self.events

    def get_services(self):
        return self.services

    # TODO: move to ControllerModule (ControllerApp)
    def set_controller(self, controller):
        self.controller = controller


class ControllerModule(WishfulModule):
    def __init__(self):
        super(ControllerModule, self).__init__()

    def add_rule(self,):
        pass


class AgentModule(WishfulModule):
    def __init__(self):
        super(AgentModule, self).__init__()
