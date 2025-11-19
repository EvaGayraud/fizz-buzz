from fastapi import APIRouter

from via_report_generator.infrastructure.api.v1 import version
from via_report_generator.infrastructure.api.v1.report import (
    create_report,
    delete_report,
    list_reports,
    retrieve_report,
    update_report,
)
from via_report_generator.infrastructure.api.v1.transcription import create_transcription
from via_report_generator.infrastructure.api.v1.user import retrieve_user

router = APIRouter()

router.include_router(version.router, tags=["version"], prefix="/version")
router.include_router(list_reports.router, tags=["reports"], prefix="/reports")
router.include_router(create_report.router, tags=["reports"], prefix="/reports")
router.include_router(retrieve_report.router, tags=["reports"], prefix="/reports")
router.include_router(delete_report.router, tags=["reports"], prefix="/reports")
router.include_router(update_report.router, tags=["reports"], prefix="/reports")
router.include_router(retrieve_user.router, tags=["users"], prefix="/users")
router.include_router(create_transcription.router, tags=["transcriptions"], prefix="/transcriptions")
