from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass(frozen = True)
class ResultNeko:
  data : Dict[str, Any] = field(repr=False)
  """Return JSON"""
  @property
  def content(self):
    return self.data['data']

@dataclass(frozen = True)
class RandomNeko:
  data : Dict[str, Any] = field(repr=False)
  """Return JSON"""
  tag : Optional[str] = field(repr=True, compare=True, default=None)
  """Return Tag"""
  @property
  def content(self):
    """Return URL"""
    return self.data['data']
