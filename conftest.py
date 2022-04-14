# The conftest.py file serves as a means of providing fixtures for an entire directory
import pytest

pytest_plugins = [
  "ecommerce.tests.fixtures",
  "ecommerce.tests.selenium",
]