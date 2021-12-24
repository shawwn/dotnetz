from __future__ import annotations
import unittest
from dotnetz import *
from dotnetz.System.EventHandler import *
import time

class SomeResource(System.Disposable):
  def __init__(self):
    super().__init__()
    self.dispose_count = 0

  def dispose(self):
    if not self.disposed:
      self.dispose_count += 1
    super().dispose()

class ImproperResource(System.Disposable):
  def dispose(self):
    pass

# https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/events/how-to-publish-events-that-conform-to-net-framework-guidelines#example

class CustomEventArgs(System.EventArgs):
  def __init__(self, message: str):
    self.message = message

class Publisher:
  # raise_custom_event: EventHandler[CustomEventArgs, Callable[Publisher, CustomEventArgs]]

  def __init__(self):
    self.raise_custom_event: EventHandler[CustomEventArgs] = EventHandler()

  def do_something(self):
    # Write some code that does something useful here
    # then raise the event. You can also raise an event
    # before you execute a block of code.
    self.on_raise_custom_event(CustomEventArgs("Event triggered"))

  # Wrap event invocations inside a protected virtual method
  # to allow derived classes to override the event invocation behavior
  def on_raise_custom_event(self, e: CustomEventArgs):
    # Make a temporary copy of the event to avoid possibility of
    # a race condition if the last subscriber unsubscribes
    # immediately after the null check and before the event is raised.
    raise_event = self.raise_custom_event.clone()

    # Event will be null if there are no subscribers
    if raise_event:
      # Format the string to send inside the CustomEventArgs parameter
      # e.Message += $" at {DateTime.Now}";
      e.message += f" at {time.time()}"

      # Call to raise the event.
      raise_event(self, e)

class Subscriber:
  def __init__(self, id: str, pub: Publisher):
    self._id = id
    self.received: Optional[str] = None

    # Subscribe to the event
    pub.raise_custom_event.add(self.handle_custom_event)

  # Define what actions to take when the event is raised.
  def handle_custom_event(self, sender: Publisher, e: CustomEventArgs):
    assert isinstance(sender, Publisher)
    self.received = f"{self._id} received this message: {e.message}"

class Tests(unittest.TestCase):
  def test_disposable(self):
    with SomeResource() as resource:
      self.assertFalse(resource.disposed)
    self.assertTrue(resource.disposed)
    self.assertEquals(resource.dispose_count, 1)
    resource.dispose()  # verify it's ok to dispose multiple times
    self.assertTrue(resource.disposed)
    self.assertEquals(resource.dispose_count, 1)
    with self.assertRaises(RuntimeError):
      with ImproperResource() as resource:
        self.assertFalse(resource.disposed)

  def test_events(self):
    pub = Publisher()
    sub1 = Subscriber("sub1", pub)
    sub2 = Subscriber("sub2", pub)

    # Call the method that raises the event.
    pub.do_something()

    # verify that our subscribers saw it.
    self.assertTrue(sub1.received.startswith("sub1 received this message: Event triggered at "))
    self.assertTrue(sub2.received.startswith("sub2 received this message: Event triggered at "))

if __name__ == '__main__':
  unittest.main()
