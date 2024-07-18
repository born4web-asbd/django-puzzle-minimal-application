"""
Pydantic models for Django Puzzle Application
- define all real application parameters here
- plus base it upon DjangoPuzzleSharedlibraryParameters to be sure implement all global Django Puzzle Parametres
  defined in sharedlibrary module
"""
from sharedlibrary.models import ApplicationParametersConfiguration
from sharedlibrary.pydantic_models import DjangoPuzzleSharedlibraryParameters
from sharedlibrary.utils.export_import.configuration_files import ConfigurationFileMixin


class DjangoPuzzleGlobalParameters(DjangoPuzzleSharedlibraryParameters,
                                   ConfigurationFileMixin):
    """"""
    DEFAULT_HOMEPAGE_URL: str = 'accounts:account-listing'
    USE_ACCOUNT_RIGHTS: bool = False
    USE_ACCOUNT_CONFIGURATION: bool = True
