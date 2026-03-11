# ==============================================================================
# Stage 1: Base Image
# ==============================================================================
ARG PYTHON_VERSION=3.12.8

FROM python:$PYTHON_VERSION-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_COMPILE_BYTECODE=1 \
    VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# ==============================================================================
# Stage 2: Builder
# ==============================================================================
FROM base AS builder

COPY --from=ghcr.io/astral-sh/uv:alpine3.22 /usr/local/bin/uv /usr/local/bin/uvx /bin/

WORKDIR /app

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --locked --no-install-project

# ==============================================================================
# Stage 3: Runtime
# ==============================================================================
FROM base AS runtime

ENV PYTHONPATH="/app/:$PYTHONPATH"

RUN apt-get update
RUN apt-get install -y ffmpeg

RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

WORKDIR /app

COPY --chown=appuser:appuser --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --chown=appuser:appuser fizz_buzz/ ./fizz_buzz/

USER appuser
EXPOSE 8000

ENTRYPOINT ["python", "fizz_buzz"]
