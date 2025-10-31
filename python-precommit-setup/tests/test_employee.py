"""Tests for the employee module."""

from src.employee import Employee


def test_annual_salary():
    """Test the annual salary calculation."""
    emp = Employee(name="Alice", role="Developer", base_salary=5000)
    assert emp.annual_salary() == 60000


def test_apply_raise():
    """Test the apply_raise function."""
    emp = Employee(name="Bob", role="Manager", base_salary=10000)
    emp.apply_raise(10)
    assert emp.base_salary == 11000
