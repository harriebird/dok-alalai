FROM ghcr.io/astral-sh/uv:python3.14-trixie

ENV PYTHONBUFFERED=1
ENV PYTHONDONTREWRITEBYTECODE=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /code

RUN mkdir -p /etc/sudoers.d/

RUN apt update && apt install postgresql-client sudo dos2unix -y

RUN groupadd --gid 1000 devuser \
    && useradd --uid 1000 --gid devuser --shell /bin/bash --create-home devuser \
    && echo devuser ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/devuser \
    && chmod 0440 /etc/sudoers.d/devuser

COPY . .

RUN uv pip install -r pyproject.toml --system

COPY start-dev.sh /start-dev.sh

RUN dos2unix /start-dev.sh
RUN chmod +x /start-dev.sh

USER devuser

CMD ["/start-dev.sh"]
