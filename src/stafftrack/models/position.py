"""Модель должности."""

from dataclasses import dataclass


@dataclass
class Position:
    position_id: int
    title: str
    salary: float
    staff_units: int
