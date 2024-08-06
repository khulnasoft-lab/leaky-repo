#!/usr/bin/env bash

if ! type "pip" > /dev/null
then
    echo "Pip and Python are required for installing detect-secrets and truffleHog, but pip was not found!"
    exit 1
fi

mkdir -p ~/.local/bin
if ! type "gitleaks" > /dev/null && ! type "$HOME/.local/bin/gitleaks" > /dev/null; then
    latest=$(curl -L -s https://api.github.com/repos/zricethezav/gitleaks/releases/latest |grep "browser_download_url.*linux_x64" |cut -d : -f 2,3 | tr -d '"')
    mkdir -p gitleaks-install && cd gitleaks-install
    # This custom config no longer seems to make a difference (even when modified to extend the base config),
    # however there's been a severe drop in detection rates for some reason.
    # curl https://raw.githubusercontent.com/gitleaks/gitleaks/e74e6292ee3233a7167e7a1a4502fb0553c0d8c0/examples/leaky-repo.toml -O../leaky-repo.toml
    curl $latest -Ogitleaks.tar.gz
    tar xf gitleaks.tar.gz
    # We will intentionally leave the license here <3
    rm -f ./gitleaks.tar.gz ./README.md
    mv gitleaks ~/.local/bin/gitleaks
    cd ..
    chmod +x ~/.local/bin/gitleaks
fi

pip install detect-secrets truffleHog
