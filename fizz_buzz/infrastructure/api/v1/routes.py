from fastapi import APIRouter

from fizz_buzz.infrastructure.api.v1.sequence import create_sequence, sequence_stats

router = APIRouter()

router.include_router(create_sequence.router, tags=["sequences"], prefix="/sequences")
router.include_router(sequence_stats.router, tags=["sequences"], prefix="/stats")
