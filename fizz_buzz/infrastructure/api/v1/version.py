from dishka.integrations.fastapi import inject
from fastapi import APIRouter

import via_report_generator
from via_report_generator.domain.shared.value_objects.version_output import VersionOutput

router = APIRouter()


@router.get("")
@inject
async def get_version() -> VersionOutput:
    return VersionOutput(value=via_report_generator.__version__)
