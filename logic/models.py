import uuid
from dataclasses import dataclass, field


@dataclass
class Song:
    title: str
    artist: str
    duration: float
    album: str = ""
    genre: str = ""
    year: int = 0
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        if self.duration < 0:
            raise ValueError("Duration must be a non-negative number")

    def __str__(self) -> str:
        duration_minutes = int(self.duration)
        duration_seconds = int((self.duration - duration_minutes) * 60)
        return f"{self.title} by {self.artist} [{duration_minutes}:{duration_seconds:02d}]"
