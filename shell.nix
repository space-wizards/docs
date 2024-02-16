{ pkgs ? import (builtins.fetchTarball {
  url =
    "https://github.com/nixos/nixpkgs/archive/66559cae054c9abe9f6f997c3c9720fbad8d5443.tar.gz";
  sha256 = "sha256-2u/2oCSFH4QCVKeL/GHnse/S+rZ7aOMQeFJOIwCdBYU=";
}) { } }:

with pkgs;
mkShell {
  buildInputs = [
    mdbook
    mdbook-mermaid
    mdbook-linkcheck
    mdbook-admonish
    mdbook-emojicodes
  ];
}
