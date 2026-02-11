"""Type definitions for labels."""

from pydantic import BaseModel


class Label(BaseModel):
    """Label information."""

    id: int
    title: str
    description: str | None = None
    color: str
    show_on_sidebar: bool = False
