"""Employee module with simple payroll logic."""

from dataclasses import dataclass


@dataclass
class Employee:
    """Represents an employee with a name, role, and salary."""

    name: str
    role: str
    base_salary: float

    def annual_salary(self) -> float:
        """Return the annual salary."""
        return self.base_salary * 12

    def apply_raise(self, percent: float) -> None:
        """Increase the base salary by the given percentage."""
        if percent < 0:
            raise ValueError("Raise percentage must be positive")
        self.base_salary += self.base_salary * (percent / 100)
