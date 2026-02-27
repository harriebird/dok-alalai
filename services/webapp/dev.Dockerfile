FROM ghcr.io/astral-sh/uv:python3.14-trixie

ENV PYTHONBUFFERED=1
ENV PYTHONDONTREWRITEBYTECODE=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /code

RUN mkdir -p /etc/sudoers.d/

RUN groupadd --gid 1000 devuser \
    && useradd --uid 1000 --gid devuser --shell /bin/bash --create-home devuser \
    && echo devuser ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/devuser \
    && chmod 0440 /etc/sudoers.d/devuser

COPY . .

RUN uv pip install -r pyproject.toml --system

RUN chmod +x entrypoint.sh

USER devuser

ENTRYPOINT ["./entrypoint.sh"]

ENTRYPOINT ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0"]
