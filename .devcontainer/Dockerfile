FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
# Garante compatibilidade de escrita entre o Windows e o Container
ENV UV_LINK_MODE=copy

# Instala o uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Dependências básicas: git para controle de versão e ssh para o DevPod/GitHub
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates git curl build-essential ssh \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash dev
USER dev
WORKDIR /workspaces
