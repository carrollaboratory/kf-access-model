"""Data model package for kf-access-model."""

from pathlib import Path
from .kf_access_model import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "kf_access_model.yaml"
