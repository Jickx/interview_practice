from abc import ABC, abstractmethod


class CallDevice(ABC):
    @abstractmethod
    def call(self):
        pass


class SearchDevice(ABC):
    @abstractmethod
    def search(self):
        pass


class SMSDevice(ABC):
    @abstractmethod
    def SMS(self):
        pass


class MobilePhone(CallDevice, SearchDevice, SMSDevice):
    def call(self):
        print('Calling')

    def SMS(self):
        print('Making SMS')

    def search(self):
        print('Searching')


class BabushkaPhone(CallDevice):
    def call(self):
        print('Calling')


device1 = MobilePhone()

device1.call()
device1.search()

device2 = BabushkaPhone()
device2.call()
