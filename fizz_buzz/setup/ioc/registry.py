import inspect
import logging
import pkgutil
from importlib import import_module
from pathlib import Path

from dishka import Provider

_log = logging.getLogger(__name__)


def get_all_providers_from_package(package_path: str) -> list[type[Provider]]:
    """
    Finds all Dishka providers in a package.

    Args:
        package_path: Package path (ex: 'vif_ai_scp.setup.ioc.dishka_providers')

    Returns:
        List of found Provider classes
    """
    providers: list[type[Provider]] = []

    try:
        package = import_module(package_path)
        package_dir = Path(package.__file__).parent if package.__file__ else None

        if package_dir is None:
            _log.error(f"Could not find package directory for {package_path}")
            return providers

        for finder, module_name, is_pkg in pkgutil.walk_packages([str(package_dir)], prefix=f"{package_path}."):
            try:
                module = import_module(module_name)

                for name, obj in inspect.getmembers(module):
                    if (
                        inspect.isclass(obj)
                        and issubclass(obj, Provider)
                        and obj is not Provider
                        and obj.__module__ == module_name
                    ):
                        providers.append(obj)

            except Exception as e:
                _log.warning(f"Failed to import module {module_name}: {str(e)}")
                continue

    except Exception as e:
        _log.error(f"Failed to import package {package_path}: {str(e)}")

    return providers


def instantiate_all_providers(package_path: str) -> list[Provider]:
    """
    Instantiates all providers found in a package.

    Args:
        package_path: Package path (ex: 'document_extractor.setup.ioc.dishka_providers')

    Returns:
        List of Provider instances
    """
    provider_classes = get_all_providers_from_package(package_path)
    return [provider_class() for provider_class in provider_classes]


def get_providers() -> list[Provider]:
    """
    Automatically loads all providers from dishka_providers package.

    Returns:
        List of all found provider instances
    """
    providers = instantiate_all_providers("document_extractor.setup.ioc.dishka_providers")
    _log.info(f"Loaded {len(providers)} providers")

    return providers
